def reflex_route(observation: dict) -> str:
    """Simple reflex policy used before introducing LLM reasoning."""
    status = observation.get("pod_status")
    if status == "CrashLoopBackOff":
        return "collect_logs_and_events"
    if status == "Pending":
        return "inspect_scheduling_and_resources"
    if status == "Running" and observation.get("error_rate", 0) > 0.05:
        return "query_metrics_and_logs"
    return "continue_observation"


if __name__ == "__main__":
    examples = [
        {"pod_status": "CrashLoopBackOff"},
        {"pod_status": "Pending"},
        {"pod_status": "Running", "error_rate": 0.12},
    ]
    for item in examples:
        print(item, "=>", reflex_route(item))
