TOOLS = {
    "get_pod": "Read Kubernetes pod state",
    "get_logs": "Read bounded container logs",
    "query_prometheus": "Read metrics",
    "get_release_history": "Read release metadata",
}

if __name__ == "__main__":
    for name, description in TOOLS.items():
        print(f"{name}: {description}")
