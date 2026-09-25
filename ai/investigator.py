def investigation_plan(alert: dict) -> list[str]:
    return [
        "identify exact environment",
        "identify active color",
        "identify exact deployment/pod/container",
        "inspect rollout status",
        "inspect Kubernetes events",
        "read bounded logs",
        "query Prometheus",
        "check Argo CD sync/health",
        "correlate Git release/tag timing",
        "retrieve relevant runbooks/incidents",
    ]
