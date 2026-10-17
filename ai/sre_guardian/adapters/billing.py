from datetime import date, timedelta

class BigQueryBillingReader:
    # GCP billing export is commonly queried from BigQuery; the table must be configured explicitly.
    def __init__(self, table_id: str):
        if not table_id:
            raise RuntimeError("GCP_BILLING_EXPORT_TABLE is not configured")
        # Validate table identifier before interpolating it into SQL.
        import re
        if not re.fullmatch(r"[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_]+", table_id):
            raise ValueError("Billing table must be project.dataset.table")
        self.table_id = table_id

    def monthly_costs(self, project_id: str, start: date | None = None, end: date | None = None) -> list[dict]:
        try:
            from google.cloud import bigquery
        except ImportError as exc:
            raise RuntimeError("Install google-cloud-bigquery for billing export access") from exc
        end = end or date.today()
        start = start or (end - timedelta(days=30))
        client = bigquery.Client(project=project_id or None)
        query = f"""
            SELECT service.description AS service, currency,
                   SUM(cost + IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0)) AS net_cost
            FROM `{self.table_id}`
            WHERE DATE(usage_start_time) >= @start_date
              AND DATE(usage_start_time) < @end_date
            GROUP BY service, currency
            ORDER BY net_cost DESC
        """
        job_config = bigquery.QueryJobConfig(query_parameters=[
            bigquery.ScalarQueryParameter("start_date", "DATE", start),
            bigquery.ScalarQueryParameter("end_date", "DATE", end),
        ])
        return [dict(row.items()) for row in client.query(query, job_config=job_config).result()]
