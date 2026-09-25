def propose_rollback(resource, current_color, known_good_color, known_good_tag):
    return {
        "action": "switch_color",
        "resource": resource,
        "from_color": current_color,
        "to_color": known_good_color,
        "target_release": known_good_tag,
        "reason": "Current release has evidence-backed regression and target release is known-good",
        "risk": "Short traffic transition during switch",
        "approval_required": True,
        "verification": [
            "all desired replicas available",
            "readiness checks pass",
            "health endpoint passes",
            "5xx rate recovers",
            "latency returns within SLO"
        ]
    }
