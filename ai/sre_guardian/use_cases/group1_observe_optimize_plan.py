from datetime import datetime, timezone
from statistics import mean
from ..contracts import make_result, evidence

def uc01_cost_optimization(payload):
    # Prefer live billing export when requested; otherwise require explicit cost rows.
    rows = payload.get("billing_rows", [])
    if not rows:
        raise ValueError("Provide billing_rows from the configured BigQuery billing adapter.")
    findings = []
    for row in rows:
        cost = float(row["net_cost"])
        if cost < 0:
            continue
        findings.append({"service": row.get("service", "unknown"), "currency": row.get("currency", "USD"),
                         "observed_cost": round(cost, 2), "optimization_hypothesis": "Review idle/oversized resources",
                         "savings_estimate": None, "savings_status": "not_estimated_without_usage_and_pricing"})
    return make_result("UC-01", "Cloud Cost Optimization Advisor",
        "Billing costs summarized; savings are not invented without utilization and pricing evidence.",
        findings, [evidence("gcp_bigquery_billing_export", f"{len(rows)} billing rows")],
        ["Cost alone is insufficient to claim savings; correlate with resource usage and pricing."], "advisory")

def uc02_resource_optimization(payload):
    # Input metrics should come from Prometheus and be scoped to the payment-service workload.
    workloads = payload.get("workloads", [])
    if not workloads: raise ValueError("workloads is required")
    findings = []
    for w in workloads:
        cpu_req, cpu_use = float(w["cpu_request_cores"]), float(w["cpu_usage_cores"])
        mem_req, mem_use = float(w["memory_request_bytes"]), float(w["memory_usage_bytes"])
        if min(cpu_req, mem_req) <= 0 or min(cpu_use, mem_use) < 0: raise ValueError("Invalid resource metrics")
        findings.append({"workload": w["name"], "cpu_utilization_pct": round(cpu_use/cpu_req*100, 2),
                         "memory_utilization_pct": round(mem_use/mem_req*100, 2),
                         "review_candidate": cpu_use/cpu_req < .35 and mem_use/mem_req < .50})
    return make_result("UC-02", "Kubernetes Capacity & Resource Optimization",
        "Right-sizing candidates require historical validation and a controlled rollout.", findings,
        [evidence("prometheus_and_kubernetes", f"{len(workloads)} workload samples")],
        ["No resource requests or limits are modified by this use case."], "advisory", True)

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

def uc09_predictive_scaling(payload):
    # Transparent linear trend baseline; validate forecasts on historical holdout data before use.
    samples = [float(x) for x in payload.get("samples", [])]
    target = float(payload.get("target_per_replica", 0))
    replicas = int(payload.get("current_replicas", 0))
    if len(samples) < 3 or any(x < 0 for x in samples) or target <= 0 or replicas < 1:
        raise ValueError("Need >=3 non-negative samples, positive target and replicas")
    slopes = [b-a for a,b in zip(samples, samples[1:])]
    slope = mean(slopes[-min(5, len(slopes)):])
    forecast = max(0, samples[-1] + slope)
    advised = max(1, int((forecast + target - 1)//target))
    return make_result("UC-09", "Predictive Scaling Advisor",
        "Forecast is a simple trend baseline, not a trained model or scaling command.",
        [{"forecast_next_sample": round(forecast, 3), "current_replicas": replicas,
          "advisory_replicas": advised, "mean_recent_delta": round(slope, 3)}],
        [evidence("prometheus_history", f"{len(samples)} numeric samples")],
        ["Forecast quality must be measured against a time-based holdout set."], "advisory", True)

def uc12_slo_error_budget(payload):
    # This is request-based SLO math; use the service's actual SLI window and objective.
    total, good = int(payload["total_events"]), int(payload["good_events"])
    target = float(payload["slo_target"])
    if total <= 0 or not 0 <= good <= total or not 0 < target < 1: raise ValueError("Invalid SLI/SLO inputs")
    observed = good/total
    allowed_bad = 1-target
    actual_bad = 1-observed
    burn = actual_bad/allowed_bad
    return make_result("UC-12", "SLO & Error-Budget Insights",
        "Calculated from explicit aggregate SLI values and supplied SLO target.",
        [{"observed_success_ratio": observed, "slo_target": target, "slo_met": observed >= target,
          "error_budget_remaining_fraction": max(0, 1 - actual_bad/allowed_bad),
          "error_budget_burn_ratio": burn}],
        [evidence("sli_aggregate", f"{good} good events out of {total}")],
        ["This is a period aggregate, not multi-window burn-rate alerting."], "advisory")
