def event(incident):
    return {
        "event_action": "trigger",
        "routing_key": "<SECRET>",
        "payload": {
            "summary": f"{incident['service']} incident",
            "severity": incident["severity"],
        }
    }
