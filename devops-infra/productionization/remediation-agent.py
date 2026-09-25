def build_plan(resource, issue, known_good_color, known_good_tag):
    return {
        "issue": issue,
        "affected_resource": resource,
        "action": "switch_traffic",
        "target_color": known_good_color,
        "target_release": known_good_tag,
        "approval_required": True,
        "verification": [
            "deployment available",
            "pods ready",
            "health endpoint 200",
            "error rate below threshold",
            "latency within SLO"
        ]
    }

if __name__ == "__main__":
    print(build_plan(
        {"namespace": "fashion-shop", "deployment": "payment-service"},
        "release regression",
        "green",
        "v1.3.0"
    ))
