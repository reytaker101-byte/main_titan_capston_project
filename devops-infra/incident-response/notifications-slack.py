def build_slack_message(incident):
    return {
        "text": (
            f"[{incident['severity']}] {incident['incident_id']} - "
            f"{incident['service']} - {incident['status']}"
        )
    }

if __name__ == "__main__":
    print(build_slack_message({
        "severity": "SEV-1",
        "incident_id": "INC-1001",
        "service": "payment-service",
        "status": "awaiting human approval"
    }))
