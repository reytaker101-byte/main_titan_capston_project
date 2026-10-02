from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from datetime import datetime, timezone


app = FastAPI(title="AI-SRE Release Dashboard")


# ============================================================
# DASHBOARD ENVIRONMENT CONFIGURATION
# ============================================================

# Order intentionally follows the reference dashboard:
#
# PRODUCTION:
#   fleet-green | fleet-blue | pilot-green | pilot-blue
#
# PRE-PRODUCTION:
#   stage-green | stage-blue | dev

COLUMNS = [
    {
        "key": "fleet-green",
        "label": "fleet-green",
        "group": "production",
        "namespace": "ai-sre-fleet",
        "deployment": "payment-service-green",
        "color": "green",
    },
    {
        "key": "fleet-blue",
        "label": "fleet-blue",
        "group": "production",
        "namespace": "ai-sre-fleet",
        "deployment": "payment-service-blue",
        "color": "blue",
    },
    {
        "key": "pilot-green",
        "label": "pilot-green",
        "group": "production",
        "namespace": "ai-sre-pilot",
        "deployment": "payment-service-green",
        "color": "green",
    },
    {
        "key": "pilot-blue",
        "label": "pilot-blue",
        "group": "production",
        "namespace": "ai-sre-pilot",
        "deployment": "payment-service-blue",
        "color": "blue",
    },
    {
        "key": "stage-green",
        "label": "stage-green",
        "group": "pre-production",
        "namespace": "ai-sre-stage",
        "deployment": "payment-service-green",
        "color": "green",
    },
    {
        "key": "stage-blue",
        "label": "stage-blue",
        "group": "pre-production",
        "namespace": "ai-sre-stage",
        "deployment": "payment-service-blue",
        "color": "blue",
    },
    {
        "key": "dev",
        "label": "dev",
        "group": "pre-production",
        "namespace": "ai-sre-dev",
        "deployment": "payment-service",
        "color": "blue",
    },
]


# ============================================================
# KUBERNETES CLIENT
# ============================================================

def get_kubernetes_client():

    try:
        # Running inside Kubernetes
        config.load_incluster_config()

    except Exception:

        try:
            # Running locally
            config.load_kube_config()

        except Exception:
            return None, None

    apps_api = client.AppsV1Api()
    core_api = client.CoreV1Api()

    return apps_api, core_api


# ============================================================
# IMAGE TAG
# ============================================================

def get_image_tag(image):

    if not image:
        return "NA"

    if ":" not in image:
        return image

    return image.rsplit(":", 1)[-1]


# ============================================================
# DEPLOYMENT STATUS
# ============================================================

def read_deployment(apps_api, column):

    namespace = column["namespace"]
    deployment_name = column["deployment"]

    try:

        deployment = apps_api.read_namespaced_deployment(
            name=deployment_name,
            namespace=namespace,
        )

    except ApiException as exc:

        if exc.status == 404:

            return {
                "exists": False,
                "tag": "NA",
                "status": "NA",
                "health": "NA",
                "ready": 0,
                "desired": 0,
                "class": "na",
            }

        return {
            "exists": False,
            "tag": "ERROR",
            "status": "ERROR",
            "health": "ERROR",
            "ready": 0,
            "desired": 0,
            "class": "error",
        }

    except Exception:

        return {
            "exists": False,
            "tag": "ERROR",
            "status": "ERROR",
            "health": "ERROR",
            "ready": 0,
            "desired": 0,
            "class": "error",
        }


    desired = deployment.spec.replicas or 0

    ready = deployment.status.ready_replicas or 0


    image = None

    containers = (
        deployment.spec.template.spec.containers
        if deployment.spec.template.spec
        else []
    )

    if containers:

        image = containers[0].image


    tag = get_image_tag(image)


    # --------------------------------------------------------
    # NO REPLICAS
    # --------------------------------------------------------

    if desired == 0:

        return {
            "exists": True,
            "tag": tag,
            "status": "INACTIVE",
            "health": "INACTIVE",
            "ready": ready,
            "desired": desired,
            "class": "inactive",
        }


    # --------------------------------------------------------
    # HEALTHY
    # --------------------------------------------------------

    if ready == desired:

        return {
            "exists": True,
            "tag": tag,
            "status": "ACTIVE",
            "health": "UP",
            "ready": ready,
            "desired": desired,
            "class": "healthy",
        }


    # --------------------------------------------------------
    # PARTIALLY READY
    # --------------------------------------------------------

    if ready > 0:

        return {
            "exists": True,
            "tag": tag,
            "status": "DEGRADED",
            "health": "DEGRADED",
            "ready": ready,
            "desired": desired,
            "class": "warning",
        }


    # --------------------------------------------------------
    # FAILED
    # --------------------------------------------------------

    return {
        "exists": True,
        "tag": tag,
        "status": "ERROR",
        "health": "ERROR",
        "ready": ready,
        "desired": desired,
        "class": "error",
    }


# ============================================================
# ACTIVE BLUE/GREEN COLOR
# ============================================================

def get_active_color(core_api, namespace):

    try:

        service = core_api.read_namespaced_service(
            name="payment-service",
            namespace=namespace,
        )

        selector = service.spec.selector or {}

        color = selector.get("color")

        if color in ["blue", "green"]:
            return color

    except Exception:
        pass

    return None


# ============================================================
# BUILD DASHBOARD DATA
# ============================================================

def build_dashboard_data():

    apps_api, core_api = get_kubernetes_client()


    if not apps_api or not core_api:

        return {
            "cluster_available": False,
            "updated_at": current_time(),
            "columns": [],
        }


    data = {}

    # --------------------------------------------------------
    # READ DEPLOYMENTS
    # --------------------------------------------------------

    for column in COLUMNS:

        status = read_deployment(
            apps_api,
            column,
        )

        data[column["key"]] = status


    # --------------------------------------------------------
    # READ ACTIVE COLORS
    # --------------------------------------------------------

    active_colors = {}

    namespaces = {
        "ai-sre-stage",
        "ai-sre-pilot",
        "ai-sre-fleet",
    }


    for namespace in namespaces:

        active_colors[namespace] = get_active_color(
            core_api,
            namespace,
        )


    # --------------------------------------------------------
    # ADD ACTIVE / INACTIVE INFORMATION
    # --------------------------------------------------------

    for column in COLUMNS:

        key = column["key"]

        namespace = column["namespace"]

        color = column["color"]

        status = data[key]


        if column["deployment"] == "payment-service":

            # DEV is always treated as the active environment
            status["traffic"] = "ACTIVE"

        else:

            active_color = active_colors.get(namespace)

            if active_color == color:

                status["traffic"] = "ACTIVE"

            else:

                status["traffic"] = "INACTIVE"


    return {
        "cluster_available": True,
        "updated_at": current_time(),
        "columns": [
            {
                **column,
                "status": data[column["key"]],
            }
            for column in COLUMNS
        ],
    }


# ============================================================
# TIME
# ============================================================

def current_time():

    return datetime.now(
        timezone.utc
    ).strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


# ============================================================
# API
# ============================================================

@app.get("/api/status")
def status():

    return build_dashboard_data()


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "service": "release-dashboard",
    }


# ============================================================
# HTML DASHBOARD
# ============================================================

@app.get("/", response_class=HTMLResponse)
def dashboard():

    return HTMLResponse(
        """
<!DOCTYPE html>

<html>

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

    padding: 22px;

    background: #f4f7f8;

    color: #172033;

    font-family:
        Arial,
        Helvetica,
        sans-serif;
}


.dashboard {

    max-width: 1700px;

    margin: auto;
}


/* ============================================================
   HEADER
   ============================================================ */

.header {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 15px;
}


.title {

    font-size: 29px;

    font-weight: 800;

    margin: 0;
}


.subtitle {

    margin-top: 5px;

    color: #667085;

    font-size: 14px;
}


.refresh {

    background: white;

    border: 1px solid #d0d5dd;

    padding: 10px 15px;

    border-radius: 8px;

    font-size: 12px;
}


.refresh-dot {

    display: inline-block;

    width: 8px;

    height: 8px;

    border-radius: 50%;

    background: #16a34a;

    margin-right: 5px;
}


/* ============================================================
   WARNING
   ============================================================ */

.warning {

    display: none;

    background: #fff7ed;

    border: 1px solid #fed7aa;

    color: #9a3412;

    padding: 10px;

    margin-bottom: 12px;

    border-radius: 6px;

    font-weight: 600;

    font-size: 13px;
}


/* ============================================================
   MATRIX
   ============================================================ */

.matrix-container {

    background: white;

    border: 1px solid #cfd6dd;

    border-radius: 5px;

    overflow-x: auto;

    box-shadow:
        0 2px 6px rgba(0,0,0,0.06);
}


.matrix {

    width: 100%;

    min-width: 1200px;

    border-collapse: separate;

    border-spacing: 3px;

    background: #ffffff;

    table-layout: fixed;
}


/* ============================================================
   TOP LEFT
   ============================================================ */

.services-header {

    width: 210px;

    background: #168fd0;

    color: white;

    font-size: 15px;

    font-weight: 800;

    text-align: center;

    height: 50px;
}


.environment-header {

    width: 115px;

    background: #168fd0;

    color: white;

    font-size: 14px;

    font-weight: 800;

    text-align: center;
}


/* ============================================================
   GROUP HEADERS
   ============================================================ */

.production-header {

    background: #56a83d;

    color: white;

    font-size: 14px;

    font-weight: 800;

    height: 34px;

    text-align: center;

    text-transform: uppercase;
}


.preproduction-header {

    background: #56a83d;

    color: white;

    font-size: 14px;

    font-weight: 800;

    height: 34px;

    text-align: center;

    text-transform: uppercase;
}


/* ============================================================
   COLUMN HEADERS
   ============================================================ */

.column-header {

    height: 42px;

    font-size: 11px;

    font-weight: 800;

    text-align: center;

    text-transform: uppercase;

    color: #263238;
}


.blue-column {

    background: #dbeafe;

    border-top: 4px solid #2563eb;
}


.green-column {

    background: #dcfce7;

    border-top: 4px solid #16a34a;
}


.dev-column {

    background: #dbeafe;

    border-top: 4px solid #2563eb;
}


/* ============================================================
   ACTIVE STATUS HEADER
   ============================================================ */

.status-header {

    height: 25px;

    font-size: 10px;

    font-weight: 800;

    text-align: center;

    text-transform: uppercase;
}


.status-blue {

    background: #eff6ff;

    color: #1d4ed8;
}


.status-green {

    background: #f0fdf4;

    color: #15803d;
}


.status-dev {

    background: #eff6ff;

    color: #1d4ed8;
}


/* ============================================================
   SERVICE CELL
   ============================================================ */

.service-cell {

    background: #eaf2f5;

    min-height: 70px;

    padding: 12px;

    text-align: center;

    font-weight: 800;

    font-size: 14px;

    color: #263238;
}


.service-name {

    font-size: 15px;

    font-weight: 800;
}


.service-type {

    margin-top: 3px;

    font-size: 10px;

    font-weight: 600;

    color: #667085;
}


/* ============================================================
   ENVIRONMENT CELL
   ============================================================ */

.environment-cell {

    background: #eef3f6;

    text-align: center;

    font-size: 12px;

    font-weight: 800;

    color: #344054;

    padding: 8px;
}


/* ============================================================
   STATUS CELLS
   ============================================================ */

.status-cell {

    height: 95px;

    padding: 8px;

    text-align: center;

    vertical-align: middle;

    position: relative;
}


/* BLUE COLUMN */

.cell-blue {

    background: #eaf3ff;

    border-left: 3px solid #2563eb;
}


/* GREEN COLUMN */

.cell-green {

    background: #eaf8ed;

    border-left: 3px solid #16a34a;
}


/* DEV */

.cell-dev {

    background: #eaf3ff;

    border-left: 3px solid #2563eb;
}


/* ============================================================
   HEALTH COLORS
   ============================================================ */

.cell-healthy {

    background: #dff3df;
}


.cell-inactive {

    background: #edf1ee;
}


.cell-warning {

    background: #fff1c7;
}


.cell-error {

    background: #dc2f2f;

    color: white;
}


.cell-na {

    background: #e8eeea;

    color: #5f6b64;
}


/* ============================================================
   CELL CONTENT
   ============================================================ */

.version {

    font-size: 15px;

    font-weight: 800;

    margin-bottom: 5px;
}


.health-line {

    font-size: 11px;

    font-weight: 700;

    margin-bottom: 4px;
}


.traffic-line {

    font-size: 10px;

    font-weight: 800;

    text-transform: uppercase;
}


.pod-line {

    font-size: 10px;

    margin-top: 3px;
}


/* ============================================================
   STATUS BADGE
   ============================================================ */

.badge {

    display: inline-block;

    padding: 3px 7px;

    border-radius: 3px;

    font-size: 9px;

    font-weight: 900;

    margin-top: 4px;
}


.badge-active {

    background: #dcfce7;

    color: #166534;
}


.badge-inactive {

    background: #fef3c7;

    color: #92400e;
}


.badge-error {

    background: #991b1b;

    color: white;
}


.badge-na {

    background: #d1d5db;

    color: #4b5563;
}


/* ============================================================
   LEGEND
   ============================================================ */

.legend {

    display: flex;

    gap: 15px;

    margin-top: 12px;

    font-size: 11px;

    color: #667085;
}


.legend-item {

    display: flex;

    align-items: center;

    gap: 5px;
}


.legend-box {

    width: 13px;

    height: 13px;

    border-radius: 2px;
}


.legend-blue {

    background: #dbeafe;

    border-left: 3px solid #2563eb;
}


.legend-green {

    background: #dcfce7;

    border-left: 3px solid #16a34a;
}


.legend-up {

    background: #dff3df;
}


.legend-error {

    background: #dc2f2f;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    margin-top: 10px;

    color: #667085;

    font-size: 11px;
}


@media (max-width: 900px) {

    body {
        padding: 10px;
    }

    .header {
        align-items: flex-start;
        gap: 10px;
        flex-direction: column;
    }
}

</style>

</head>


<body>


<div class="dashboard">


    <!-- HEADER -->

    <div class="header">

        <div>

            <h1 class="title">
                AI-SRE Release Dashboard
            </h1>

            <div class="subtitle">

                Service:
                <strong>payment-service</strong>

                &nbsp;•&nbsp;

                GitOps Blue / Green Release Status

            </div>

        </div>


        <div class="refresh">

            <span class="refresh-dot"></span>

            Auto-refresh:
            <strong>15s</strong>

        </div>

    </div>


    <!-- WARNING -->

    <div
        id="warning"
        class="warning"
    >

        ⚠ Kubernetes cluster unavailable.
        Waiting for cluster connection...

    </div>


    <!-- MATRIX -->

    <div class="matrix-container">

        <table class="matrix">


            <!-- =================================================
                 HEADER ROW 1
                 ================================================= -->

            <thead>

                <tr>

                    <th
                        rowspan="3"
                        class="services-header"
                    >
                        SERVICES
                    </th>


                    <th
                        rowspan="3"
                        class="environment-header"
                    >
                        ENVIRONMENT
                    </th>


                    <th
                        colspan="4"
                        class="production-header"
                    >
                        PRODUCTION
                    </th>


                    <th
                        colspan="3"
                        class="preproduction-header"
                    >
                        PRE-PRODUCTION
                    </th>

                </tr>


                <!-- =================================================
                     HEADER ROW 2
                     ================================================= -->

                <tr>

                    <th class="column-header green-column">
                        FLEET-GREEN
                    </th>

                    <th class="column-header blue-column">
                        FLEET-BLUE
                    </th>

                    <th class="column-header green-column">
                        PILOT-GREEN
                    </th>

                    <th class="column-header blue-column">
                        PILOT-BLUE
                    </th>

                    <th class="column-header green-column">
                        STAGE-GREEN
                    </th>

                    <th class="column-header blue-column">
                        STAGE-BLUE
                    </th>

                    <th class="column-header dev-column">
                        DEV
                    </th>

                </tr>


                <!-- =================================================
                     HEADER ROW 3
                     ================================================= -->

                <tr>

                    <th class="status-header status-green">
                        INACTIVE
                    </th>

                    <th class="status-header status-blue">
                        ACTIVE
                    </th>

                    <th class="status-header status-green">
                        ACTIVE
                    </th>

                    <th class="status-header status-blue">
                        INACTIVE
                    </th>

                    <th class="status-header status-green">
                        INACTIVE
                    </th>

                    <th class="status-header status-blue">
                        ACTIVE
                    </th>

                    <th class="status-header status-dev">
                        ACTIVE
                    </th>

                </tr>

            </thead>


            <!-- =================================================
                 DATA
                 ================================================= -->

            <tbody id="dashboard-body">

            </tbody>


        </table>

    </div>


    <!-- LEGEND -->

    <div class="legend">

        <div class="legend-item">

            <span class="legend-box legend-blue"></span>

            Blue deployment

        </div>


        <div class="legend-item">

            <span class="legend-box legend-green"></span>

            Green deployment

        </div>


        <div class="legend-item">

            <span class="legend-box legend-up"></span>

            Healthy / UP

        </div>


        <div class="legend-item">

            <span class="legend-box legend-error"></span>

            Error

        </div>

    </div>


    <!-- FOOTER -->

    <div class="footer">

        Last updated:
        <strong id="updated">
            —
        </strong>

        &nbsp; | &nbsp;

        Source:
        Kubernetes API / Argo CD GitOps

    </div>


</div>


<script>

/* ============================================================
   HTML ESCAPE
   ============================================================ */

function escapeHtml(value) {

    if (
        value === null ||
        value === undefined
    ) {

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
   CELL CLASS
   ============================================================ */

function getCellClass(column) {

    const status =
        column.status || {};


    if (status.class === "error") {

        return "cell-error";

    }


    if (status.class === "warning") {

        return "cell-warning";

    }


    if (status.class === "inactive") {

        return "cell-inactive";

    }


    if (status.class === "healthy") {

        return "cell-healthy";

    }


    return "cell-na";
}


/* ============================================================
   BADGE
   ============================================================ */

function getBadge(column) {

    const status =
        column.status || {};


    if (
        status.status === "ACTIVE"
    ) {

        return `
            <span class="badge badge-active">
                UP
            </span>
        `;
    }


    if (
        status.status === "INACTIVE"
    ) {

        return `
            <span class="badge badge-inactive">
                INACTIVE
            </span>
        `;
    }


    if (
        status.status === "ERROR"
    ) {

        return `
            <span class="badge badge-error">
                ERROR
            </span>
        `;
    }


    return `
        <span class="badge badge-na">
            NA
        </span>
    `;
}


/* ============================================================
   CELL
   ============================================================ */

function renderCell(column) {

    const status =
        column.status || {};


    const baseClass =
        column.color === "green"
            ? "cell-green"
            : "cell-blue";


    const stateClass =
        getCellClass(column);


    return `

        <td
            class="status-cell ${baseClass} ${stateClass}"
        >

            <div class="version">

                ${escapeHtml(
                    status.tag || "NA"
                )}

            </div>


            <div class="health-line">

                ${escapeHtml(
                    status.health || "NA"
                )}

            </div>


            <div class="pod-line">

                Pods:
                ${escapeHtml(
                    String(
                        status.ready || 0
                    )
                )}
                /
                ${escapeHtml(
                    String(
                        status.desired || 0
                    )
                )}

            </div>


            <div class="traffic-line">

                ${escapeHtml(
                    status.traffic || "INACTIVE"
                )}

            </div>


            ${getBadge(column)}

        </td>

    `;
}


/* ============================================================
   RENDER DASHBOARD
   ============================================================ */

function renderDashboard(data) {

    const body =
        document.getElementById(
            "dashboard-body"
        );


    body.innerHTML = "";


    if (
        !data.cluster_available
    ) {

        document.getElementById(
            "warning"
        ).style.display = "block";


        body.innerHTML = `

            <tr>

                <td
                    colspan="9"
                    style="
                        height:160px;
                        text-align:center;
                        color:#667085;
                        font-weight:700;
                    "
                >

                    Kubernetes cluster unavailable.

                    <br><br>

                    Dashboard will retry automatically.

                </td>

            </tr>

        `;

        return;
    }


    document.getElementById(
        "warning"
    ).style.display = "none";


    const columns =
        data.columns || [];


    /*
       We currently have ONE service:
       payment-service

       The structure is intentionally generic
       so additional services can be added later.
    */


    const row =
        document.createElement("tr");


    row.innerHTML = `

        <!-- SERVICE -->

        <td class="service-cell">

            <div class="service-name">

                payment-service

            </div>

            <div class="service-type">

                Payment Workflow

            </div>

        </td>


        <!-- ENVIRONMENT -->

        <td class="environment-cell">

            BLUE / GREEN

        </td>


        ${columns.map(
            column => renderCell(column)
        ).join("")}

    `;


    body.appendChild(row);


    document.getElementById(
        "updated"
    ).textContent =
        data.updated_at || "—";
}


/* ============================================================
   REFRESH
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
                "API request failed"
            );

        }


        const data =
            await response.json();


        renderDashboard(data);


    } catch (error) {

        console.error(
            "Dashboard refresh error:",
            error
        );


        document.getElementById(
            "warning"
        ).style.display = "block";

    }
}


/* ============================================================
   INITIAL LOAD
   ============================================================ */

refreshDashboard();


/* ============================================================
   15 SECOND REFRESH
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
