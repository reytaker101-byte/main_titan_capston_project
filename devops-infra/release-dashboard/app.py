from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import os
import re
from datetime import datetime, timezone


app = FastAPI(title="AI-SRE Release Dashboard")


# ============================================================
# CONFIGURATION
# ============================================================

REFRESH_SECONDS = 15

ENVIRONMENTS = [
    {
        "name": "DEV",
        "namespace": "ai-sre-dev",
        "mode": "single",
        "blue_deployment": "payment-service",
        "green_deployment": None,
        "color": "blue",
    },
    {
        "name": "STAGE",
        "namespace": "ai-sre-stage",
        "mode": "blue-green",
        "blue_deployment": "payment-service-blue",
        "green_deployment": "payment-service-green",
    },
    {
        "name": "PILOT",
        "namespace": "ai-sre-pilot",
        "mode": "blue-green",
        "blue_deployment": "payment-service-blue",
        "green_deployment": "payment-service-green",
    },
    {
        "name": "FLEET / PROD",
        "namespace": "ai-sre-fleet",
        "mode": "blue-green",
        "blue_deployment": "payment-service-blue",
        "green_deployment": "payment-service-green",
    },
]


# ============================================================
# KUBERNETES CLIENT
# ============================================================

def get_kubernetes_clients():
    """
    Load Kubernetes configuration.

    In Kubernetes:
        load_incluster_config()

    For local development:
        load_kube_config()
    """

    try:
        config.load_incluster_config()
    except Exception:
        try:
            config.load_kube_config()
        except Exception:
            return None, None

    return client.AppsV1Api(), client.CoreV1Api()


# ============================================================
# HELPERS
# ============================================================

def extract_image_tag(image):
    """
    Extract image tag from:

    asia-southeast1-docker.pkg.dev/.../payment-service:v1.1.0

    Returns:
        v1.1.0
    """

    if not image:
        return "—"

    if ":" not in image:
        return image

    return image.rsplit(":", 1)[-1]


def deployment_status(deployment):
    """
    Convert Kubernetes Deployment state into dashboard state.
    """

    if deployment is None:
        return {
            "image": "—",
            "tag": "—",
            "status": "N/A",
            "pods": "0/0",
            "health": "N/A",
            "health_class": "na",
        }

    replicas = deployment.spec.replicas or 0

    ready = deployment.status.ready_replicas or 0

    images = []

    for container in deployment.spec.template.spec.containers or []:
        if container.image:
            images.append(container.image)

    image = images[0] if images else None
    tag = extract_image_tag(image)

    if replicas == 0:
        return {
            "image": image or "—",
            "tag": tag,
            "status": "INACTIVE",
            "pods": f"{ready}/{replicas}",
            "health": "N/A",
            "health_class": "na",
        }

    if ready == replicas:
        return {
            "image": image or "—",
            "tag": tag,
            "status": "ACTIVE",
            "pods": f"{ready}/{replicas}",
            "health": "HEALTHY",
            "health_class": "healthy",
        }

    if ready > 0:
        return {
            "image": image or "—",
            "tag": tag,
            "status": "DEGRADED",
            "pods": f"{ready}/{replicas}",
            "health": "DEGRADED",
            "health_class": "warning",
        }

    return {
        "image": image or "—",
        "tag": tag,
        "status": "FAILED",
        "pods": f"{ready}/{replicas}",
        "health": "FAILED",
        "health_class": "error",
    }


def get_active_color(core_api, namespace):
    """
    Determine active Blue/Green color from the payment-service
    Service selector.

    Example:

    selector:
        app: payment-service
        color: green

    Returns:
        blue / green
    """

    try:
        service = core_api.read_namespaced_service(
            name="payment-service",
            namespace=namespace,
        )

        selector = service.spec.selector or {}

        color = selector.get("color")

        if color in ("blue", "green"):
            return color

        return "blue"

    except ApiException:
        return "blue"

    except Exception:
        return "blue"


def get_environment_status(apps_api, core_api, environment):
    """
    Read Deployment + Service information for one environment.
    """

    namespace = environment["namespace"]

    active_color = "blue"

    if environment["mode"] == "blue-green":
        active_color = get_active_color(
            core_api,
            namespace,
        )

    # --------------------------------------------------------
    # BLUE
    # --------------------------------------------------------

    try:
        blue_deployment = apps_api.read_namespaced_deployment(
            name=environment["blue_deployment"],
            namespace=namespace,
        )

        blue = deployment_status(blue_deployment)

    except ApiException as exc:

        if exc.status == 404:
            blue = deployment_status(None)
        else:
            blue = {
                "image": "—",
                "tag": "—",
                "status": "ERROR",
                "pods": "—",
                "health": "ERROR",
                "health_class": "error",
            }

    # --------------------------------------------------------
    # GREEN
    # --------------------------------------------------------

    if environment["green_deployment"]:

        try:
            green_deployment = apps_api.read_namespaced_deployment(
                name=environment["green_deployment"],
                namespace=namespace,
            )

            green = deployment_status(green_deployment)

        except ApiException as exc:

            if exc.status == 404:
                green = deployment_status(None)
            else:
                green = {
                    "image": "—",
                    "tag": "—",
                    "status": "ERROR",
                    "pods": "—",
                    "health": "ERROR",
                    "health_class": "error",
                }

    else:

        green = {
            "image": "—",
            "tag": "—",
            "status": "N/A",
            "pods": "0/0",
            "health": "N/A",
            "health_class": "na",
        }

    # --------------------------------------------------------
    # DEV
    # --------------------------------------------------------

    if environment["mode"] == "single":

        environment_status = "HEALTHY"

        if blue["health"] == "FAILED":
            environment_status = "FAILED"

        elif blue["health"] == "DEGRADED":
            environment_status = "DEGRADED"

        return {
            "name": environment["name"],
            "namespace": namespace,
            "mode": environment["mode"],
            "active_color": "blue",
            "environment_status": environment_status,
            "blue": blue,
            "green": green,
        }

    # --------------------------------------------------------
    # BLUE/GREEN
    # --------------------------------------------------------

    active = blue if active_color == "blue" else green

    if active["health"] == "HEALTHY":
        environment_status = "HEALTHY"

    elif active["health"] == "DEGRADED":
        environment_status = "DEGRADED"

    elif active["health"] == "FAILED":
        environment_status = "FAILED"

    else:
        environment_status = "UNKNOWN"

    return {
        "name": environment["name"],
        "namespace": namespace,
        "mode": environment["mode"],
        "active_color": active_color,
        "environment_status": environment_status,
        "blue": blue,
        "green": green,
    }


def get_dashboard_data():

    apps_api, core_api = get_kubernetes_clients()

    # --------------------------------------------------------
    # Cluster unavailable
    # --------------------------------------------------------

    if not apps_api or not core_api:

        return {
            "cluster_available": False,
            "updated_at": datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            ),
            "environments": [],
        }

    environments = []

    for environment in ENVIRONMENTS:

        try:

            status = get_environment_status(
                apps_api,
                core_api,
                environment,
            )

            environments.append(status)

        except Exception as exc:

            environments.append(
                {
                    "name": environment["name"],
                    "namespace": environment["namespace"],
                    "mode": environment["mode"],
                    "active_color": "blue",
                    "environment_status": "ERROR",
                    "blue": {
                        "image": "—",
                        "tag": "—",
                        "status": "ERROR",
                        "pods": "—",
                        "health": "ERROR",
                        "health_class": "error",
                    },
                    "green": {
                        "image": "—",
                        "tag": "—",
                        "status": "ERROR",
                        "pods": "—",
                        "health": "ERROR",
                        "health_class": "error",
                    },
                }
            )

    return {
        "cluster_available": True,
        "updated_at": datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        ),
        "environments": environments,
    }


# ============================================================
# API
# ============================================================

@app.get("/api/status")
def api_status():

    return get_dashboard_data()


# ============================================================
# HTML DASHBOARD
# ============================================================

@app.get("/", response_class=HTMLResponse)
def dashboard():

    return HTMLResponse(
        """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>AI-SRE Release Dashboard</title>


<style>

/* ============================================================
   GLOBAL
   ============================================================ */

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    padding: 24px;

    background: #f4f7fb;

    color: #172033;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        Arial,
        sans-serif;
}


/* ============================================================
   PAGE
   ============================================================ */

.dashboard {

    max-width: 1700px;

    margin: 0 auto;
}


/* ============================================================
   HEADER
   ============================================================ */

.header {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 20px;

    gap: 20px;
}

.title-area h1 {

    margin: 0;

    font-size: 30px;

    font-weight: 750;

    letter-spacing: -0.5px;
}

.title-area p {

    margin: 6px 0 0;

    color: #667085;

    font-size: 15px;
}


.header-right {

    display: flex;

    align-items: center;

    gap: 10px;
}


.refresh-box {

    background: white;

    border: 1px solid #dbe2ea;

    border-radius: 10px;

    padding: 10px 14px;

    color: #667085;

    font-size: 13px;
}


.refresh-indicator {

    display: inline-block;

    width: 8px;

    height: 8px;

    border-radius: 50%;

    background: #16a34a;

    margin-right: 6px;
}


/* ============================================================
   LEGEND
   ============================================================ */

.legend {

    display: flex;

    align-items: center;

    gap: 18px;

    background: white;

    border: 1px solid #dbe2ea;

    border-radius: 10px;

    padding: 10px 14px;

    margin-bottom: 14px;

    font-size: 13px;

    color: #475467;
}

.legend-item {

    display: flex;

    align-items: center;

    gap: 6px;
}

.legend-dot {

    width: 11px;

    height: 11px;

    border-radius: 3px;
}

.legend-blue {
    background: #2563eb;
}

.legend-green {
    background: #16a34a;
}

.legend-yellow {
    background: #f59e0b;
}

.legend-red {
    background: #dc2626;
}

.legend-grey {
    background: #94a3b8;
}


/* ============================================================
   MATRIX
   ============================================================ */

.matrix-wrapper {

    background: white;

    border: 1px solid #dbe2ea;

    border-radius: 12px;

    overflow-x: auto;

    box-shadow:
        0 2px 8px rgba(15, 23, 42, 0.04);
}


.matrix {

    min-width: 1100px;

    width: 100%;

    border-collapse: collapse;

    table-layout: fixed;
}


/* ============================================================
   TABLE HEADER
   ============================================================ */

.matrix th,
.matrix td {

    border-right: 1px solid #e4e7ec;

    border-bottom: 1px solid #e4e7ec;

    vertical-align: middle;

    text-align: center;
}

.matrix th:last-child,
.matrix td:last-child {

    border-right: none;
}


.matrix thead tr:first-child th {

    height: 50px;
}


.service-header {

    width: 180px;

    background: #172b4d;

    color: white;

    font-size: 14px;

    font-weight: 700;
}


.environment-header {

    width: 130px;

    background: #edf2f7;

    color: #344054;

    font-size: 14px;

    font-weight: 700;
}


.blue-header {

    background: #2563eb;

    color: white;

    font-size: 15px;

    font-weight: 750;

    padding: 12px;
}


.green-header {

    background: #16a34a;

    color: white;

    font-size: 15px;

    font-weight: 750;

    padding: 12px;
}


/* ============================================================
   SUB HEADERS
   ============================================================ */

.sub-header {

    font-size: 12px;

    font-weight: 700;

    padding: 9px 5px;

    color: #475467;
}

.blue-sub-header {

    background: #eff6ff;
}

.green-sub-header {

    background: #f0fdf4;
}


/* ============================================================
   ENVIRONMENT CELL
   ============================================================ */

.environment-cell {

    padding: 14px 10px;

    text-align: left !important;

    font-weight: 700;

    background: #f8fafc;
}


.environment-name {

    font-size: 15px;

    color: #172033;
}


.environment-type {

    margin-top: 5px;

    font-size: 11px;

    color: #667085;

    font-weight: 500;
}


/* ============================================================
   ENVIRONMENT ACCENTS
   ============================================================ */

.env-dev {

    border-left: 5px solid #2563eb;
}

.env-stage {

    border-left: 5px solid #7c3aed;
}

.env-pilot {

    border-left: 5px solid #f59e0b;
}

.env-fleet {

    border-left: 5px solid #dc2626;
}


/* ============================================================
   DATA CELLS
   ============================================================ */

.data-cell {

    padding: 12px 7px;

    min-height: 110px;
}


.image-tag {

    font-size: 13px;

    font-weight: 700;

    color: #344054;

    margin-bottom: 8px;

    word-break: break-word;
}


/* ============================================================
   BADGES
   ============================================================ */

.badge {

    display: inline-block;

    padding: 5px 8px;

    border-radius: 5px;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 0.3px;
}


.badge-active {

    color: #075985;

    background: #dbeafe;

    border: 1px solid #93c5fd;
}


.badge-candidate {

    color: #92400e;

    background: #fef3c7;

    border: 1px solid #fcd34d;
}


.badge-inactive {

    color: #475467;

    background: #f2f4f7;

    border: 1px solid #d0d5dd;
}


.badge-error {

    color: #991b1b;

    background: #fee2e2;

    border: 1px solid #fca5a5;
}


/* ============================================================
   PODS
   ============================================================ */

.pods {

    font-size: 13px;

    font-weight: 650;

    color: #344054;
}


/* ============================================================
   HEALTH
   ============================================================ */

.health {

    display: inline-flex;

    align-items: center;

    gap: 5px;

    margin-top: 7px;

    font-size: 11px;

    font-weight: 750;
}


.health-dot {

    width: 8px;

    height: 8px;

    border-radius: 50%;
}


.health-healthy {

    color: #15803d;
}

.health-healthy .health-dot {

    background: #16a34a;
}


.health-warning {

    color: #b45309;
}

.health-warning .health-dot {

    background: #f59e0b;
}


.health-error {

    color: #b91c1c;
}

.health-error .health-dot {

    background: #dc2626;
}


.health-na {

    color: #667085;
}

.health-na .health-dot {

    background: #94a3b8;
}


/* ============================================================
   ACTIVE CELL
   ============================================================ */

.active-blue {

    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #ffffff
        );
}


.active-green {

    background:
        linear-gradient(
            135deg,
            #f0fdf4,
            #ffffff
        );
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    display: flex;

    justify-content: space-between;

    margin-top: 14px;

    color: #667085;

    font-size: 12px;
}


/* ============================================================
   CLUSTER WARNING
   ============================================================ */

.cluster-warning {

    display: none;

    background: #fff7ed;

    border: 1px solid #fed7aa;

    color: #9a3412;

    padding: 12px 14px;

    border-radius: 9px;

    margin-bottom: 14px;

    font-size: 13px;

    font-weight: 600;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 900px) {

    body {
        padding: 12px;
    }

    .header {
        align-items: flex-start;
        flex-direction: column;
    }

    .title-area h1 {
        font-size: 24px;
    }

    .legend {
        flex-wrap: wrap;
    }
}

</style>

</head>


<body>

<div class="dashboard">


    <!-- =====================================================
         HEADER
         ===================================================== -->

    <div class="header">

        <div class="title-area">

            <h1>
                AI-SRE Release Dashboard
            </h1>

            <p>
                Service: <strong>payment-service</strong>
                &nbsp;•&nbsp;
                GitOps Blue / Green Release Status
            </p>

        </div>


        <div class="header-right">

            <div class="refresh-box">

                <span class="refresh-indicator"></span>

                Auto-refresh:
                <strong>15s</strong>

            </div>

        </div>

    </div>


    <!-- =====================================================
         CLUSTER WARNING
         ===================================================== -->

    <div
        id="cluster-warning"
        class="cluster-warning"
    >

        ⚠ Kubernetes cluster is currently unavailable.
        Dashboard will automatically retry.

    </div>


    <!-- =====================================================
         LEGEND
         ===================================================== -->

    <div class="legend">

        <div class="legend-item">

            <span class="legend-dot legend-blue"></span>

            Blue = Active

        </div>


        <div class="legend-item">

            <span class="legend-dot legend-green"></span>

            Green = Candidate / Ready

        </div>


        <div class="legend-item">

            <span class="legend-dot legend-yellow"></span>

            Candidate / Waiting

        </div>


        <div class="legend-item">

            <span class="legend-dot legend-red"></span>

            Error

        </div>


        <div class="legend-item">

            <span class="legend-dot legend-grey"></span>

            N/A / Not Deployed

        </div>

    </div>


    <!-- =====================================================
         MATRIX
         ===================================================== -->

    <div class="matrix-wrapper">

        <table class="matrix">

            <thead>

                <tr>

                    <th
                        rowspan="2"
                        class="service-header"
                    >
                        SERVICES
                    </th>


                    <th
                        rowspan="2"
                        class="environment-header"
                    >
                        ENVIRONMENT
                    </th>


                    <th
                        colspan="4"
                        class="blue-header"
                    >
                        BLUE DEPLOYMENT
                    </th>


                    <th
                        colspan="4"
                        class="green-header"
                    >
                        GREEN DEPLOYMENT
                    </th>

                </tr>


                <tr>

                    <th class="sub-header blue-sub-header">
                        IMAGE TAG
                    </th>

                    <th class="sub-header blue-sub-header">
                        STATUS
                    </th>

                    <th class="sub-header blue-sub-header">
                        PODS
                    </th>

                    <th class="sub-header blue-sub-header">
                        HEALTH
                    </th>


                    <th class="sub-header green-sub-header">
                        IMAGE TAG
                    </th>

                    <th class="sub-header green-sub-header">
                        STATUS
                    </th>

                    <th class="sub-header green-sub-header">
                        PODS
                    </th>

                    <th class="sub-header green-sub-header">
                        HEALTH
                    </th>

                </tr>

            </thead>


            <tbody id="matrix-body">

                <!-- JavaScript populates this -->

            </tbody>

        </table>

    </div>


    <!-- =====================================================
         FOOTER
         ===================================================== -->

    <div class="footer">

        <div>

            Last updated:
            <strong id="updated-at">—</strong>

        </div>

        <div>

            Source:
            <strong>Kubernetes API / GitOps</strong>

        </div>

    </div>


</div>


<script>

/* ============================================================
   DASHBOARD JAVASCRIPT
   ============================================================ */

function escapeHtml(value) {

    if (value === null || value === undefined) {
        return "";
    }

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* ============================================================
   ENVIRONMENT CLASS
   ============================================================ */

function environmentClass(name) {

    if (name === "DEV") {
        return "env-dev";
    }

    if (name === "STAGE") {
        return "env-stage";
    }

    if (name === "PILOT") {
        return "env-pilot";
    }

    return "env-fleet";
}


/* ============================================================
   HEALTH HTML
   ============================================================ */

function healthHtml(item) {

    const health = item.health || "N/A";

    let healthClass = "health-na";

    if (item.health_class === "healthy") {
        healthClass = "health-healthy";
    }

    if (item.health_class === "warning") {
        healthClass = "health-warning";
    }

    if (item.health_class === "error") {
        healthClass = "health-error";
    }

    return `
        <div class="health ${healthClass}">

            <span class="health-dot"></span>

            ${escapeHtml(health)}

        </div>
    `;
}


/* ============================================================
   STATUS BADGE
   ============================================================ */

function statusBadge(status, color) {

    status = status || "N/A";

    let className = "badge-inactive";

    if (status === "ACTIVE") {

        className =
            color === "blue"
                ? "badge-active"
                : "badge-candidate";
    }

    if (status === "INACTIVE") {
        className = "badge-inactive";
    }

    if (
        status === "FAILED" ||
        status === "ERROR"
    ) {
        className = "badge-error";
    }

    if (status === "DEGRADED") {
        className = "badge-candidate";
    }

    return `
        <span class="badge ${className}">
            ${escapeHtml(status)}
        </span>
    `;
}


/* ============================================================
   DEPLOYMENT CELL
   ============================================================ */

function deploymentCells(item, color, activeColor) {

    if (!item) {

        return `
            <td class="data-cell">
                —
            </td>

            <td class="data-cell">
                —
            </td>

            <td class="data-cell">
                0/0
            </td>

            <td class="data-cell">
                ${healthHtml({
                    health: "N/A",
                    health_class: "na"
                })}
            </td>
        `;
    }


    let activeClass = "";

    if (color === activeColor) {

        activeClass =
            color === "blue"
                ? "active-blue"
                : "active-green";
    }


    return `

        <td class="data-cell ${activeClass}">

            <div class="image-tag">

                ${escapeHtml(item.tag)}

            </div>

        </td>


        <td class="data-cell ${activeClass}">

            ${
                statusBadge(
                    item.status,
                    color
                )
            }

        </td>


        <td class="data-cell ${activeClass}">

            <div class="pods">

                ${escapeHtml(item.pods)}

            </div>

        </td>


        <td class="data-cell ${activeClass}">

            ${healthHtml(item)}

        </td>

    `;
}


/* ============================================================
   RENDER MATRIX
   ============================================================ */

function renderMatrix(data) {

    const body =
        document.getElementById(
            "matrix-body"
        );

    body.innerHTML = "";


    if (
        !data.environments ||
        data.environments.length === 0
    ) {

        body.innerHTML = `

            <tr>

                <td
                    colspan="10"
                    style="
                        padding:40px;
                        color:#667085;
                        text-align:center;
                    "
                >

                    No Kubernetes environment data available.

                </td>

            </tr>

        `;

        return;
    }


    data.environments.forEach(environment => {

        const envClass =
            environmentClass(
                environment.name
            );


        const row = document.createElement("tr");


        row.innerHTML = `

            <!-- SERVICE -->

            <td
                class="environment-cell ${envClass}"
            >

                <div class="environment-name">

                    payment-service

                </div>

                <div class="environment-type">

                    ${escapeHtml(
                        environment.mode === "single"
                            ? "Single Deployment"
                            : "Blue / Green"
                    )}

                </div>

            </td>


            <!-- ENVIRONMENT -->

            <td
                class="environment-cell"
            >

                <div class="environment-name">

                    ${escapeHtml(
                        environment.name
                    )}

                </div>

                <div class="environment-type">

                    ${escapeHtml(
                        environment.namespace
                    )}

                </div>

            </td>


            <!-- BLUE -->

            ${deploymentCells(
                environment.blue,
                "blue",
                environment.active_color
            )}


            <!-- GREEN -->

            ${deploymentCells(
                environment.green,
                "green",
                environment.active_color
            )}

        `;


        body.appendChild(row);

    });
}


/* ============================================================
   FETCH STATUS
   ============================================================ */

async function refreshDashboard() {

    try {

        const response =
            await fetch(
                "/api/status",
                {
                    cache: "no-store"
                }
            );


        if (!response.ok) {

            throw new Error(
                "Dashboard API unavailable"
            );
        }


        const data =
            await response.json();


        renderMatrix(data);


        document.getElementById(
            "updated-at"
        ).textContent =
            data.updated_at || "—";


        const warning =
            document.getElementById(
                "cluster-warning"
            );


        if (data.cluster_available) {

            warning.style.display = "none";

        } else {

            warning.style.display = "block";

        }


    } catch (error) {

        console.error(
            "Dashboard refresh failed:",
            error
        );


        document.getElementById(
            "cluster-warning"
        ).style.display = "block";

    }

}


/* ============================================================
   INITIAL LOAD
   ============================================================ */

refreshDashboard();


/* ============================================================
   AUTO REFRESH
   ============================================================ */

setInterval(
    refreshDashboard,
    15000
);

</script>

</body>

</html>
        """
    )


# ============================================================
# HEALTH ENDPOINT
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "service": "release-dashboard",
        "refresh_seconds": REFRESH_SECONDS,
    }
