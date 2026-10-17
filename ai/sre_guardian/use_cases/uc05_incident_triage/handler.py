from ...contracts import make_result, evidence


def uc05_incident_triage(payload):
    severity = str(payload.get("severity", "unknown")).lower()
    priority = {"critical": 1, "high": 2, "medium": 3, "low": 4}.get(severity, 5)
    steps = payload.get("runbook_steps", [])
    if not steps: steps = ["Confirm customer impact", "Check payment-service health and recent rollout",
                           "Collect pod events, logs and Prometheus error/latency metrics", "Escalate per on-call policy"]
    return make_result("UC-05", "Incident Triage & Response Planner",
        "Triage plan derived from the supplied incident context.", 
        [{"priority": priority, "severity": severity, "customer_impact": payload.get("customer_impact", "unknown"),
          "recommended_steps": steps, "escalation_recommended": priority <= 2}],
        payload.get("evidence", []), ["This handler does not page or mutate infrastructure."], "advisory", True)
