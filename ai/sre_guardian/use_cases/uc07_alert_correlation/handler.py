from ...contracts import make_result, evidence
from datetime import datetime, timezone


def uc07_alert_correlation(payload):
    # Group alert instances by service and a bounded time window; preserve every alert ID.
    alerts = payload.get("alerts", [])
    window = int(payload.get("window_minutes", 5))
    if not 1 <= window <= 60: raise ValueError("window_minutes must be 1..60")
    buckets = {}
    for a in alerts:
        ts = datetime.fromisoformat(a["startsAt"].replace("Z", "+00:00"))
        epoch_bucket = int(ts.timestamp() // (window * 60))
        key = (a.get("labels", {}).get("service", "unknown"), epoch_bucket)
        buckets.setdefault(key, []).append(a)
    findings = [{"service": k[0], "window_bucket": k[1],
                 "alert_ids": [a.get("fingerprint", a.get("labels", {}).get("alertname", "unknown")) for a in v],
                 "alert_count": len(v)} for k, v in buckets.items()]
    return make_result("UC-07", "Alert Correlation & Noise Reduction",
        "Heuristic grouping only; original alerts must remain available to responders.", findings,
        [evidence("alertmanager_payload", f"{len(alerts)} alerts received")],
        ["Correlation uses service and fixed time buckets; topology-based correlation is a future adapter."], "advisory")
