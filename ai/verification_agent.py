def verification_checks(service, expected_color, expected_tag):
    return [
        f"{service} Service selector == {expected_color}",
        f"{service} active release == {expected_tag}",
        "deployment available replicas == desired replicas",
        "all pods Ready",
        "health endpoint returns 200",
        "5xx rate below incident threshold",
        "p95 latency within SLO",
        "no new CrashLoopBackOff/OOMKilled evidence",
    ]
