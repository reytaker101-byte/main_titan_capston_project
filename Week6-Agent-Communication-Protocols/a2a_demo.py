def make_task(incident_id, resource):
    return {
        "task": "investigate_incident",
        "incident_id": incident_id,
        "resource": resource,
    }

if __name__ == "__main__":
    print(make_task("INC-1001", "payment-service"))
