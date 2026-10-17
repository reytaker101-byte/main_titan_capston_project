from datetime import date, timedelta

from ...contracts import make_result, evidence


def uc01_cost_optimization(payload):
    """
    UC-01: Cloud Cost Optimization Advisor.

    Supports:
    1. Sample billing data for development and testing.
    2. Future BigQuery billing integration.
    3. Future Kubernetes utilization correlation.

    Does not invent cost or savings figures.
    """

    billing_rows = payload.get("billing_rows", [])

    # Optional date window for future billing integrations.
    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    findings = []

    for row in billing_rows:
        try:
            cost = float(row["net_cost"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(
                "Each billing row must contain a valid net_cost."
            ) from exc

        if cost < 0:
            continue

        service = row.get("service", "unknown")
        currency = row.get("currency", "USD")

        findings.append({
            "service": service,
            "currency": currency,
            "observed_cost": round(cost, 2),
            "optimization_hypothesis": (
                "Review resource utilization, idle capacity, "
                "and oversized workloads."
            ),
            "savings_estimate": None,
            "savings_status": (
                "pending_usage_and_pricing_evidence"
            ),
        })

    if not billing_rows:
        message = (
            "UC-01 is ready for development. No billing data is "
            "available yet. Connect BigQuery billing export when "
            "the GCP environment is provisioned."
        )
        evidence_items = [
            evidence(
                "billing_data",
                "No billing records supplied; no live cost analysis performed.",
            )
        ]
    else:
        message = (
            "Billing costs summarized. Savings estimates require "
            "resource utilization and pricing evidence."
        )
        evidence_items = [
            evidence(
                "sample_or_supplied_billing_data",
                f"{len(billing_rows)} billing rows supplied.",
            )
        ]

    return make_result(
        "UC-01",
        "Cloud Cost Optimization Advisor",
        message,
        findings,
        evidence_items,
        [
            "Cost alone cannot establish achievable savings.",
            "Correlate billing data with resource utilization.",
            "Verify pricing and workload requirements before "
            "recommending resource changes.",
        ],
        "advisory",
    )
