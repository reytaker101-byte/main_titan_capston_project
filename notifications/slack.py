def message(incident):
    return {
        "text": (
            f"[{incident['severity']}] {incident['incident_id']} "
            f"{incident['service']} status={incident['status']}"
        )
    }
