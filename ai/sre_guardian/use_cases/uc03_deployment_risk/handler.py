from ...contracts import make_result, evidence


def uc03_deployment_risk(payload):
    # Transparent weighted score; calibrate thresholds with deployment history before gating releases.
    score, factors = 0, []
    if int(payload.get("changed_files", 0)) > 20: score += 2; factors.append("large_change_set")
    if not payload.get("tests_passed", False): score += 4; factors.append("tests_not_confirmed_passing")
    if int(payload.get("recent_failures", 0)) > 0: score += 3; factors.append("recent_release_failures")
    if not payload.get("service_healthy", False): score += 4; factors.append("service_not_confirmed_healthy")
    level = "high" if score >= 6 else "medium" if score >= 3 else "low"
    return make_result("UC-03", "Deployment Risk Analysis",
        "Heuristic risk assessment; do not use as the only release gate.",
        [{"risk_score": score, "risk_level": level, "factors": factors}],
        payload.get("evidence", []), ["Weights require calibration against real release outcomes."], "advisory")
