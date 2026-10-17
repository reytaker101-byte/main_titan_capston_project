from datetime import date, timedelta

from ...contracts import make_result, evidence
from ...adapters.billing import BigQueryBillingReader
from ...config import settings


def uc01_cost_optimization(payload):
    """
    UC-01: Cloud Cost Optimization Advisor.

    Fetch billing data from BigQuery when billing_rows
    are not supplied in the request.
    """

    rows = payload.get("billing_rows", [])

    # Use live BigQuery billing data when sample rows are absent.
    if not rows:
        table_id = getattr(settings, "GCP_BILLING_EXPORT_TABLE", None)

        if not table_id:
            raise ValueError(
                "Configure GCP_BILLING_EXPORT_TABLE with "
                "project.dataset.table"
            )

        project_id = payload.get("project_id")

        end_date = date.today()
        start_date = end_date - timedelta(days=30)

        reader = BigQueryBillingReader(table_id)

        rows = reader.monthly_costs(
            project_id=project_id,
            start=start_date,
            end=end_date,
        )

    if not rows:
        raise ValueError(
            "No billing records returned. Verify the BigQuery "
            "export table, date range, and permissions."
        )

    findings = []

    for row in rows:
        cost = float(row["net_cost"])

        if cost < 0:
            continue

        findings.append({
            "service": row.get("service", "unknown"),
            "currency": row.get("currency", "USD"),
            "observed_cost": round(cost, 2),
            "optimization_hypothesis": (
                "Review idle or oversized resources"
            ),
            "savings_estimate": None,
            "savings_status": (
                "not_estimated_without_usage_and_pricing"
            ),
        })

    return make_result(
        "UC-01",
        "Cloud Cost Optimization Advisor",
        (
            "Billing costs summarized. Savings are not invented "
            "without utilization and pricing evidence."
        ),
        findings,
        [
            evidence(
                "gcp_bigquery_billing_export",
                f"{len(rows)} billing rows",
            )
        ],
        [
            "Cost alone is insufficient to claim savings; "
            "correlate with resource usage and pricing."
        ],
        "advisory",
    )
