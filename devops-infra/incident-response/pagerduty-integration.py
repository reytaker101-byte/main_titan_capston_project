def build_pagerduty_event(incident):
    return {
        "routing_key": "<FROM_SECRET_MANAGER>",
        "event_action": "trigger",
        "payload": {
            "summary": f"{incident['service']} incident {incident['incident_id']}",
            "severity": incident["severity"],
            "source": "ai-sre-fashion-guardian"
        }
    }
