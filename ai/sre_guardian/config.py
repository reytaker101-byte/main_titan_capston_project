import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    # Application environment
    environment: str = os.getenv("APP_ENVIRONMENT", "dev")

    # Prometheus monitoring
    prometheus_url: str = os.getenv("PROMETHEUS_URL", "")

    # Kubernetes configuration
    kubernetes_namespace: str = os.getenv(
        "KUBERNETES_NAMESPACE", "default"
    )

    # Payment service
    payment_service_name: str = os.getenv(
        "PAYMENT_SERVICE_NAME", "payment-service"
    )

    # GitHub integration
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    github_repository: str = os.getenv("GITHUB_REPOSITORY", "")

    # GCP BigQuery billing export
    billing_export_table: str = os.getenv(
        "GCP_BILLING_EXPORT_TABLE", ""
    )
    gcp_project_id: str = os.getenv(
        "GOOGLE_CLOUD_PROJECT", ""
    )

    # Runbook knowledge base
    runbook_dir: str = os.getenv(
        "SRE_RUNBOOK_DIR", "ai/runbooks"
    )

    # Safety controls
    require_human_approval: bool = (
        os.getenv("REQUIRE_HUMAN_APPROVAL", "true").lower()
        == "true"
    )


settings = Settings()
