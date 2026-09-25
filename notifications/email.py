def email_subject(incident):
    return f"[{incident['severity']}] {incident['incident_id']} - {incident['service']}"
