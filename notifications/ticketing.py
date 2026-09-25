def ticket_payload(incident):
    return {
        "title": f"{incident['incident_id']} - {incident['service']}",
        "severity": incident["severity"],
        "description": incident.get("summary", "")
    }
