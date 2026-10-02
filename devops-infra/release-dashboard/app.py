import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from kubernetes import client, config

app = FastAPI(title="AI-SRE Release Dashboard")

try:
    config.load_incluster_config()
except Exception:
    config.load_kube_config()

apps = client.AppsV1Api()
core = client.CoreV1Api()

ENVIRONMENTS = {
    "DEV": "ai-sre-dev",
    "STAGE": "ai-sre-stage",
    "PILOT": "ai-sre-pilot",
    "FLEET / PROD": "ai-sre-fleet",
}

@app.get("/health")
def health():
    return {"status": "ok", "service": "release-dashboard"}

def deployment_state(namespace, name):
    try:
        d = apps.read_namespaced_deployment(name, namespace)
        desired = d.spec.replicas or 0
        ready = d.status.ready_replicas or 0
        image = d.spec.template.spec.containers[0].image
        return desired, ready, image
    except Exception as exc:
        return 0, 0, f"error: {exc}"

def render_rows():
    rows = []
    for env, namespace in ENVIRONMENTS.items():
        if env == "DEV":
            desired, ready, image = deployment_state(namespace, "payment-service")
            rows.append(
                f"<tr><td>payment-service</td><td>{env}</td>"
                f"<td colspan='2'>Single deployment</td><td>ACTIVE</td>"
                f"<td>{ready}/{desired} Ready<br>{image}</td></tr>"
            )
            continue

        blue = deployment_state(namespace, "payment-service-blue")
        green = deployment_state(namespace, "payment-service-green")

        try:
            svc = core.read_namespaced_service("payment-service", namespace)
            active = svc.spec.selector.get("color", "unknown")
        except Exception:
            active = "unknown"

        rows.append(
            f"<tr><td>payment-service</td><td>{env}</td>"
            f"<td>Blue: {blue[1]}/{blue[0]}<br>{blue[2]}</td>"
            f"<td>Green: {green[1]}/{green[0]}<br>{green[2]}</td>"
            f"<td><b>{active.upper()}</b></td><td>GitOps</td></tr>"
        )
    return "".join(rows)

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return f"""<!doctype html>
<html>
<head>
<title>AI-SRE Release Dashboard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="15">
<style>
body{{font-family:Arial;margin:32px;background:#f4f6f8;color:#222}}
h1{{margin-bottom:4px}} .sub{{color:#666;margin-bottom:24px}}
table{{width:100%;border-collapse:collapse;background:#fff}}
th,td{{padding:14px;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}}
th{{background:#222;color:#fff}}
</style>
</head>
<body>
<h1>AI-SRE Release Dashboard</h1>
<div class="sub">Live Kubernetes Blue / Green GitOps status — refreshes every 15 seconds</div>
<table>
<tr><th>Service</th><th>Environment</th><th>Blue</th><th>Green</th><th>Active</th><th>Status / Image</th></tr>
{render_rows()}
</table>
</body>
</html>"""

