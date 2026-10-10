import os
from datetime import datetime, timezone
from typing import Optional

import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from kubernetes import client, config
from kubernetes.client.rest import ApiException

app = FastAPI(title="AI-SRE Release Dashboard")

GITHUB_REPOSITORY = os.getenv(
    "GITHUB_REPOSITORY",
    "reytaker101-byte/main_titan_capston_project"
)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "")
GCP_REGION = os.getenv("GCP_REGION", "asia-southeast1")
GAR_REPOSITORY = os.getenv(
    "GAR_REPOSITORY",
    "main-titan-capston-project-artifactory-repo"
)
GHCR_OWNER = os.getenv("GHCR_OWNER", "reytaker101-byte")

COLUMNS = [
    {
        "key": "fleet-green",
        "label": "FLEET-GREEN",
        "namespace": "ai-sre-fleet",
        "deployment": "payment-service-green",
        "color": "green"
    },
    {
        "key": "fleet-blue",
        "label": "FLEET-BLUE",
        "namespace": "ai-sre-fleet",
        "deployment": "payment-service-blue",
        "color": "blue"
    },
    {
        "key": "pilot-green",
        "label": "PILOT-GREEN",
        "namespace": "ai-sre-pilot",
        "deployment": "payment-service-green",
        "color": "green"
    },
    {
        "key": "pilot-blue",
        "label": "PILOT-BLUE",
        "namespace": "ai-sre-pilot",
        "deployment": "payment-service-blue",
        "color": "blue"
    },
    {
        "key": "stage-green",
        "label": "STAGE-GREEN",
        "namespace": "ai-sre-stage",
        "deployment": "payment-service-green",
        "color": "green"
    },
    {
        "key": "stage-blue",
        "label": "STAGE-BLUE",
        "namespace": "ai-sre-stage",
        "deployment": "payment-service-blue",
        "color": "blue"
    },
    {
        "key": "dev",
        "label": "DEV",
        "namespace": "ai-sre-dev",
        "deployment": "payment-service",
        "color": "blue"
    },
]


def now_utc():
    return datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


def k8s_clients():
    try:
        config.load_incluster_config()
    except Exception:
        try:
            config.load_kube_config()
        except Exception:
            return None, None, None

    return (
        client.AppsV1Api(),
        client.CoreV1Api(),
        client.CustomObjectsApi()
    )


def image_info(image: Optional[str]):
    if not image:
        return {
            "image": "NA",
            "tag": "NA",
            "digest": "NA"
        }

    if "@" in image:
        base, digest = image.split("@", 1)
        return {
            "image": base,
            "tag": "digest-pinned",
            "digest": digest
        }

    final = image.rsplit("/", 1)[-1]
    tag = final.rsplit(":", 1)[1] if ":" in final else "untagged"

    image_name = (
        image.rsplit(":", 1)[0]
        if ":" in final
        else image
    )

    return {
        "image": image_name,
        "tag": tag,
        "digest": "Use registry link to view digest"
    }


def deployment_status(apps, core, col):
    namespace = col["namespace"]
    deployment_name = col["deployment"]

    try:
        deployment = apps.read_namespaced_deployment(
            name=deployment_name,
            namespace=namespace
        )

    except ApiException as exc:
        message = (
            "Deployment not found"
            if exc.status == 404
            else f"Kubernetes API error: {exc.status}"
        )

        return {
            "class": "na" if exc.status == 404 else "error",
            "status": (
                "NOT FOUND"
                if exc.status == 404
                else "ERROR"
            ),
            "health": "UNKNOWN",
            "tag": "NA",
            "image": "NA",
            "digest": "NA",
            "ready": 0,
            "desired": 0,
            "restarts": 0,
            "previous_image": "NA",
            "message": message
        }

    except Exception as exc:
        return {
            "class": "error",
            "status": "ERROR",
            "health": "UNKNOWN",
            "tag": "NA",
            "image": "NA",
            "digest": "NA",
            "ready": 0,
            "desired": 0,
            "restarts": 0,
            "previous_image": "NA",
            "message": str(exc)[:120]
        }

    desired = deployment.spec.replicas or 0
    ready = deployment.status.ready_replicas or 0

    containers = (
        deployment.spec.template.spec.containers
        if deployment.spec.template
        and deployment.spec.template.spec
        else []
    )

    current_image = containers[0].image if containers else None
    info = image_info(current_image)

    restarts = 0
    previous_image = "NA"

    try:
        selector = deployment.spec.selector.match_labels or {}

        label_selector = ",".join(
            f"{key}={value}"
            for key, value in selector.items()
        )

        pods = core.list_namespaced_pod(
            namespace,
            label_selector=label_selector
        ).items

        restarts = sum(
            container_status.restart_count or 0
            for pod in pods
            for container_status in (
                pod.status.container_statuses or []
            )
        )

        replica_sets = apps.list_namespaced_replica_set(
            namespace,
            label_selector=label_selector
        ).items

        previous_candidates = []

        for replica_set in replica_sets:
            owners = replica_set.metadata.owner_references or []

            belongs_to_deployment = any(
                owner.kind == "Deployment"
                and owner.name == deployment_name
                for owner in owners
            )

            if not belongs_to_deployment:
                continue

            old_containers = (
                replica_set.spec.template.spec.containers
                if replica_set.spec.template
                and replica_set.spec.template.spec
                else []
            )

            old_image = (
                old_containers[0].image
                if old_containers
                else None
            )

            if old_image and old_image != current_image:
                previous_candidates.append(
                    (
                        replica_set.metadata.creation_timestamp,
                        old_image
                    )
                )

        if previous_candidates:
            previous_candidates.sort(
                key=lambda item: (
                    item[0]
                    or datetime.min.replace(tzinfo=timezone.utc)
                ),
                reverse=True
            )

            previous_image = previous_candidates[0][1]

    except Exception:
        pass

    if desired == 0:
        status = "SCALED TO ZERO"
        health = "INACTIVE"
        status_class = "inactive"

    elif ready == desired:
        status = "HEALTHY"
        health = "UP"
        status_class = "healthy"

    elif ready > 0:
        status = "DEGRADED"
        health = "DEGRADED"
        status_class = "warning"

    else:
        status = "UNAVAILABLE"
        health = "DOWN"
        status_class = "error"

    return {
        **info,
        "class": status_class,
        "status": status,
        "health": health,
        "ready": ready,
        "desired": desired,
        "restarts": restarts,
        "previous_image": previous_image,
        "message": "Kubernetes Deployment status"
    }


def active_color(core, namespace):
    try:
        service = core.read_namespaced_service(
            "payment-service",
            namespace
        )

        color = (service.spec.selector or {}).get("color")

        return (
            color
            if color in ("blue", "green")
            else None
        )

    except Exception:
        return None


def workflow_history():
    url = (
        f"https://api.github.com/repos/"
        f"{GITHUB_REPOSITORY}/actions/runs"
    )

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"per_page": 30},
            timeout=5
        )

        response.raise_for_status()

        runs = response.json().get("workflow_runs", [])
        items = []

        for run in runs:
            workflow_name = run.get("name", "")

            if any(
                word in workflow_name.lower()
                for word in (
                    "build",
                    "deploy",
                    "promote",
                    "blue green"
                )
            ):
                items.append({
                    "name": workflow_name,
                    "branch": run.get("head_branch", "?"),
                    "sha": (run.get("head_sha") or "")[:12],
                    "status": run.get("status", "?"),
                    "conclusion": (
                        run.get("conclusion") or "running"
                    ),
                    "actor": (
                        run.get("actor") or {}
                    ).get("login", "?"),
                    "created_at": run.get("created_at", ""),
                    "url": run.get("html_url", "")
                })

        return {
            "available": True,
            "items": items[:12],
            "message": "Recent matching GitHub Actions runs"
        }

    except Exception as exc:
        return {
            "available": False,
            "items": [],
            "message": (
                "GitHub Actions history unavailable: "
                f"{str(exc)[:120]}"
            )
        }


def registry_links():
    if GCP_PROJECT_ID:
        base = (
            "https://console.cloud.google.com/artifacts/docker/"
            f"{GCP_PROJECT_ID}/{GCP_REGION}/{GAR_REPOSITORY}"
            f"?project={GCP_PROJECT_ID}"
        )

        payment = (
            "https://console.cloud.google.com/artifacts/docker/"
            f"{GCP_PROJECT_ID}/{GCP_REGION}/{GAR_REPOSITORY}"
            "/images/dev/payment-service"
            f"?project={GCP_PROJECT_ID}"
        )

        dashboard = (
            "https://console.cloud.google.com/artifacts/docker/"
            f"{GCP_PROJECT_ID}/{GCP_REGION}/{GAR_REPOSITORY}"
            "/images/dev/release-dashboard"
            f"?project={GCP_PROJECT_ID}"
        )

    else:
        base = payment = dashboard = (
            "https://console.cloud.google.com/artifacts"
        )

    return {
        "GCP Artifact Registry": base,
        "GCP payment-service": payment,
        "GCP release-dashboard": dashboard,
        "GHCR payment-service": (
            f"https://github.com/users/{GHCR_OWNER}"
            "/packages/container/package/payment-service"
        ),
        "GHCR release-dashboard": (
            f"https://github.com/users/{GHCR_OWNER}"
            "/packages/container/package/release-dashboard"
        ),
        "GitHub Actions": (
            f"https://github.com/{GITHUB_REPOSITORY}/actions"
        ),
        "Source repository": (
            f"https://github.com/{GITHUB_REPOSITORY}"
        )
    }


def build_data():
    apps, core, custom = k8s_clients()

    history = workflow_history()
    links = registry_links()

    if not apps or not core:
        return {
            "cluster_available": False,
            "updated_at": now_utc(),
            "columns": [],
            "history": history,
            "registry_links": links
        }

    rows = []

    for column in COLUMNS:
        status = deployment_status(
            apps,
            core,
            column
        )

        if column["deployment"] == "payment-service":
            status["traffic"] = "DEV"

        else:
            active = active_color(
                core,
                column["namespace"]
            )

            status["traffic"] = (
                "ACTIVE"
                if active == column["color"]
                else "INACTIVE"
                if active
                else "UNKNOWN"
            )

        rows.append({
            **column,
            "status": status
        })

    return {
        "cluster_available": True,
        "updated_at": now_utc(),
        "columns": rows,
        "history": history,
        "registry_links": links
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "release-dashboard"
    }


@app.get("/api/status")
def api_status():
    return build_data()


@app.get("/api/releases")
def api_releases():
    return workflow_history()


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return HTMLResponse(r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI-SRE Release Dashboard</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f4f7f8;
    color: #172033;
    margin: 0;
    padding: 22px;
}
main {
    max-width: 1800px;
    margin: auto;
}
header {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
}
h1 {
    margin: 0;
    font-size: 27px;
}
.muted {
    color: #667085;
    font-size: 12px;
}
.section {
    margin-top: 22px;
}
h2 {
    font-size: 18px;
}
.links, .summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 10px;
}
.card {
    background: white;
    border: 1px solid #d7dde3;
    border-radius: 8px;
    padding: 13px;
}
.card a {
    overflow-wrap: anywhere;
    font-size: 13px;
}
.tablewrap {
    overflow-x: auto;
    background: white;
    border: 1px solid #d7dde3;
    border-radius: 8px;
}
table {
    width: 100%;
    min-width: 1100px;
    border-collapse: collapse;
}
td, th {
    border: 1px solid #e1e6eb;
    padding: 9px;
    text-align: left;
    font-size: 12px;
}
th {
    background: #eaf0f4;
}
.healthy {
    background: #e1f5e5;
}
.warning {
    background: #fff3cd;
}
.error {
    background: #fee2e2;
}
.inactive {
    background: #edf1f4;
}
.na {
    background: #f3f4f6;
}
.warningbox {
    display: none;
    padding: 10px;
    background: #fff7ed;
    color: #9a3412;
    margin-top: 12px;
}
.small {
    font-size: 11px;
    overflow-wrap: anywhere;
}
footer {
    margin-top: 15px;
    font-size: 11px;
    color: #667085;
}
</style>
</head>
<body>
<main>
<header>
    <div>
        <h1>AI-SRE Release Dashboard</h1>
        <p class="muted">
            payment-service • artifact registry • release history
            • rollback visibility • deployment health
        </p>
    </div>
    <div class="card">
        Auto-refresh: <b>15 seconds</b>
    </div>
</header>

<div id="warning" class="warningbox">
    Kubernetes cluster unavailable. Registry links and GitHub history
    may still be available.
</div>

<section class="section">
    <h2>Artifact Registries and Links</h2>
    <div id="links" class="links"></div>
</section>

<section class="section">
    <h2>Environment Release Matrix</h2>
    <div class="tablewrap">
        <table>
            <thead>
                <tr>
                    <th>Environment</th>
                    <th>Namespace</th>
                    <th>Tag</th>
                    <th>Image</th>
                    <th>Digest</th>
                    <th>Health</th>
                    <th>Ready Pods</th>
                    <th>Restarts</th>
                    <th>Traffic</th>
                </tr>
            </thead>
            <tbody id="matrix"></tbody>
        </table>
    </div>
</section>

<section class="section">
    <h2>Rollback Information</h2>
    <div class="tablewrap">
        <table>
            <thead>
                <tr>
                    <th>Environment</th>
                    <th>Current image</th>
                    <th>Previous image in ReplicaSets</th>
                    <th>Health</th>
                    <th>Guidance</th>
                </tr>
            </thead>
            <tbody id="rollback"></tbody>
        </table>
    </div>
    <p class="muted">
        Read-only information. Rollback is not executed by this dashboard.
    </p>
</section>

<section class="section">
    <h2>Recent Release History</h2>
    <div class="tablewrap">
        <table>
            <thead>
                <tr>
                    <th>Workflow</th>
                    <th>Branch</th>
                    <th>Commit</th>
                    <th>Status</th>
                    <th>Result</th>
                    <th>Actor</th>
                    <th>Started</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody id="history"></tbody>
        </table>
    </div>
    <p id="history-note" class="muted"></p>
</section>

<section class="section">
    <h2>Deployment Health Summary</h2>
    <div id="summary" class="summary"></div>
</section>

<footer>
    Last updated: <b id="updated">—</b>
    • Sources: Kubernetes API and GitHub Actions API.
</footer>
</main>

<script>
const esc = value =>
    String(value ?? "NA")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

const cls = status =>
    status.class === "healthy" ? "healthy" :
    status.class === "warning" ? "warning" :
    status.class === "error" ? "error" :
    status.class === "inactive" ? "inactive" : "na";

function render(data) {
    document.getElementById("warning").style.display =
        data.cluster_available ? "none" : "block";

    document.getElementById("links").innerHTML =
        Object.entries(data.registry_links || {})
            .map(([name, url]) => `
                <div class="card">
                    <b>${esc(name)}</b>
                    <p>
                        <a
                            target="_blank"
                            rel="noopener noreferrer"
                            href="${esc(url)}"
                        >
                            Open ${esc(name)} ↗
                        </a>
                    </p>
                </div>
            `).join("");

    document.getElementById("matrix").innerHTML =
        (data.columns || []).map(column => {
            const status = column.status || {};

            return `
                <tr class="${cls(status)}">
                    <td><b>${esc(column.label)}</b></td>
                    <td>${esc(column.namespace)}</td>
                    <td>${esc(status.tag)}</td>
                    <td class="small">${esc(status.image)}</td>
                    <td class="small">${esc(status.digest)}</td>
                    <td>
                        ${esc(status.health)} /
                        ${esc(status.status)}
                        <div class="small">
                            ${esc(status.message)}
                        </div>
                    </td>
                    <td>
                        ${esc(status.ready)} /
                        ${esc(status.desired)}
                    </td>
                    <td>${esc(status.restarts)}</td>
                    <td>${esc(status.traffic)}</td>
                </tr>
            `;
        }).join("") ||
        '<tr><td colspan="9">No Kubernetes data.</td></tr>';

    document.getElementById("rollback").innerHTML =
        (data.columns || []).map(column => {
            const status = column.status || {};

            return `
                <tr class="${cls(status)}">
                    <td>
                        ${esc(column.label)}
                        <div class="small">
                            ${esc(column.namespace)}
                        </div>
                    </td>
                    <td class="small">
                        ${esc(status.image)}:${esc(status.tag)}
                    </td>
                    <td class="small">
                        ${esc(status.previous_image)}
                    </td>
                    <td>${esc(status.health)}</td>
                    <td>
                        ${
                            status.previous_image &&
                            status.previous_image !== "NA"
                            ? "Previous image found; verify before rollback."
                            : "No previous image found in retained ReplicaSets."
                        }
                    </td>
                </tr>
            `;
        }).join("") ||
        '<tr><td colspan="5">No rollback data.</td></tr>';

    const history = data.history || {};

    document.getElementById("history").innerHTML =
        (history.items || []).map(run => `
            <tr>
                <td>${esc(run.name)}</td>
                <td>${esc(run.branch)}</td>
                <td>${esc(run.sha)}</td>
                <td>${esc(run.status)}</td>
                <td>${esc(run.conclusion)}</td>
                <td>${esc(run.actor)}</td>
                <td>${esc(run.created_at)}</td>
                <td>
                    <a
                        target="_blank"
                        rel="noopener noreferrer"
                        href="${esc(run.url)}"
                    >
                        Open run ↗
                    </a>
                </td>
            </tr>
        `).join("") ||
        '<tr><td colspan="8">No matching workflow runs available.</td></tr>';

    document.getElementById("history-note").textContent =
        history.message || "";

    const columns = data.columns || [];

    const count = statusClass =>
        columns.filter(
            column => column.status?.class === statusClass
        ).length;

    const restarts = columns.reduce(
        (total, column) =>
            total + (Number(column.status?.restarts) || 0),
        0
    );

    const summaryItems = [
        ["Environments / deployments", columns.length],
        ["Healthy", count("healthy")],
        ["Degraded", count("warning")],
        ["Unavailable", count("error")],
        ["Observed pod restarts", restarts]
    ];

    document.getElementById("summary").innerHTML =
        summaryItems.map(([label, value]) => `
            <div class="card">
                <div class="muted">${esc(label)}</div>
                <h2>${esc(value)}</h2>
            </div>
        `).join("");

    document.getElementById("updated").textContent =
        data.updated_at || "—";
}

async function refresh() {
    try {
        const response = await fetch(
            "/api/status",
            { cache: "no-store" }
        );

        if (!response.ok) {
            throw new Error("API failed");
        }

        render(await response.json());

    } catch (error) {
        console.error(error);

        document.getElementById("warning").style.display =
            "block";
    }
}

refresh();
setInterval(refresh, 15000);
</script>
</body>
</html>
""")
