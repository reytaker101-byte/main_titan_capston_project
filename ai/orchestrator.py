from .policy import check_action, require_approval
from .remediation_agent import propose_rollback

def build_incident_response(resource, current_color, known_good_color, known_good_tag):
    plan = propose_rollback(
        resource,
        current_color,
        known_good_color,
        known_good_tag
    )

    policy = check_action({
        "action": plan["action"],
        "namespace": resource["namespace"]
    })

    if not policy["allowed"]:
        return {"status": "blocked", "policy": policy}

    return {
        "status": "awaiting_human_approval",
        "plan": plan,
        "policy": policy
    }

def execute_after_approval(plan, approved: bool):
    require_approval(approved)

    # Real implementation will call the narrow Kubernetes/GitOps write tool.
    return {
        "status": "executed",
        "action": plan["action"],
        "target_color": plan["to_color"],
        "target_release": plan["target_release"]
    }
