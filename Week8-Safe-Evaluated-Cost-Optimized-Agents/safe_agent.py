ALLOWED = {"restart", "rollback", "scale"}

def policy_check(action: dict) -> dict:
    if action.get("action") not in ALLOWED:
        return {"allowed": False, "reason": "not allowlisted"}

    namespace = action.get("namespace")
    if namespace in {"kube-system", "argocd"}:
        return {"allowed": False, "reason": "protected namespace"}

    return {
        "allowed": True,
        "reason": "allowlisted; human approval still required"
    }

def require_approval(approved: bool):
    if not approved:
        raise PermissionError("Human approval required")

if __name__ == "__main__":
    print(policy_check({
        "action": "rollback",
        "namespace": "fashion-shop"
    }))
