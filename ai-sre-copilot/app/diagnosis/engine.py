from typing import Any


def diagnose(events: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Analyze supplied Kubernetes event samples.
    Only report causes supported by the supplied evidence.
    This function does not connect to or modify a cluster.
    """
    if not events:
        return {
            "diagnosis": "Insufficient evidence",
            "confidence": "low",
            "evidence": [],
            "recommended_action": "Collect pod events, container logs, and resource metrics.",
            "proposed_yaml": None,
            "risk": "Changing resources without evidence may not resolve the incident.",
            "rollback_plan": "No change has been made; no rollback is required.",
        }

    evidence = [str(event.get("message", "")) for event in events]
    combined = " ".join(evidence).lower()

    if any(term in combined for term in ["oomkilled", "out of memory", "reason: oom"]):
        return {
            "diagnosis": "Container likely exceeded its memory limit",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Verify the container's last termination reason and memory usage "
                "before changing its memory limit."
            ),
            "proposed_yaml": None,
            "risk": (
                "Increasing memory limits without checking actual usage may "
                "increase resource consumption and still not fix the cause."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["failedscheduling", "insufficient cpu", "insufficient memory"]):
        return {
            "diagnosis": "Pod scheduling may be blocked by insufficient cluster resources",
            "confidence": "medium",
            "evidence": evidence,
            "recommended_action": (
                "Check node allocatable capacity, pod requests, and scheduler events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Reducing requests without capacity analysis can cause performance "
                "degradation; increasing them may make scheduling harder."
            ),
            "rollback_plan": (
                "If a later approved change causes issues, revert its Git commit "
                "and verify Argo CD sync."
            ),
        }

    if any(term in combined for term in ["back-off restarting failed container", "crashloopbackoff"]):
        return {
            "diagnosis": "Container is repeatedly failing; root cause is not established",
            "confidence": "low",
            "evidence": evidence,
            "recommended_action": (
                "Inspect previous container logs, termination exit code, and pod events."
            ),
            "proposed_yaml": None,
            "risk": (
                "Changing CPU or memory settings without the termination details "
                "may not resolve the failure."
            ),
            "rollback_plan": (
                "No change has been made; if a later approved change is applied, "
                "revert its Git commit and verify Argo CD sync."
            ),
        }

    return {
        "diagnosis": "No supported root cause identified",
        "confidence": "low",
        "evidence": evidence,
        "recommended_action": (
            "Collect relevant pod events, previous container logs, and resource metrics."
        ),
        "proposed_yaml": None,
        "risk": "Evidence is insufficient to recommend a specific configuration change.",
        "rollback_plan": "No change has been made; no rollback is required.",
    }
