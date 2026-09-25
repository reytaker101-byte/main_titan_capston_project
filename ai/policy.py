ALLOWED_ACTIONS = {"restart", "scale", "rollback", "switch_color"}
PROTECTED_NAMESPACES = {"kube-system", "argocd"}

def check_action(action: dict) -> dict:
    if action.get("action") not in ALLOWED_ACTIONS:
        return {"allowed": False, "reason": "Action is not allowlisted"}

    namespace = action.get("namespace", "")
    if namespace in PROTECTED_NAMESPACES:
        return {"allowed": False, "reason": "Protected namespace"}

    return {
        "allowed": True,
        "reason": "Allowlisted; human approval still required"
    }

def require_approval(approved: bool):
    if not approved:
        raise PermissionError("Human approval required before production mutation")
