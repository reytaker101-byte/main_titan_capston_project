from ...contracts import make_result, evidence


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
