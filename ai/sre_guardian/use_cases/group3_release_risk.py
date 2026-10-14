from ..contracts import make_result, evidence

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

def uc08_change_impact(payload):
    # Traverse a supplied dependency graph to identify components affected by a change.
    changed = set(payload.get("changed_components", []))
    graph = payload.get("dependency_map", {})
    if not isinstance(graph, dict): raise ValueError("dependency_map must be an object")
    impacted, changed_flag = set(changed), True
    while changed_flag:
        changed_flag = False
        for component, deps in graph.items():
            if set(deps) & impacted and component not in impacted:
                impacted.add(component); changed_flag = True
    return make_result("UC-08", "Change Impact Analysis",
        "Affected components inferred from the supplied dependency map.",
        [{"changed_components": sorted(changed), "impacted_components": sorted(impacted)}],
        [evidence("git_and_dependency_metadata", f"{len(changed)} changed components")],
        ["Missing or stale dependency edges can under-report impact."], "advisory")

def uc13_security_risk(payload):
    # Consume normalized scanner findings; this module does not replace Trivy/CodeQL/Wiz.
    rank = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}
    findings = []
    for f in payload.get("findings", []):
        sev = str(f.get("severity", "unknown")).lower()
        score = rank.get(sev, 1) + (2 if f.get("internet_exposed") else 0) + (1 if f.get("exploitable") else 0)
        findings.append({"id": f.get("id"), "asset": f.get("asset"), "severity": sev,
                         "priority_score": score, "recommended_action": f.get("remediation", "Validate and remediate under change control.")})
    findings.sort(key=lambda x: x["priority_score"], reverse=True)
    return make_result("UC-13", "Security & Configuration Risk Advisor",
        "Prioritized supplied findings; source scanner output remains the source of truth.",
        findings, [evidence("security_scanner_findings", f"{len(findings)} findings")],
        ["Scanner execution and vulnerability verification happen outside this analyzer."], "advisory", True)

def uc14_release_rollback(payload):
    # Never execute rollback here; recommend only when health breaches explicit thresholds.
    err, threshold = float(payload.get("error_rate", 1)), float(payload.get("error_rate_threshold", .01))
    healthy = bool(payload.get("healthy", False))
    digest = str(payload.get("image_digest", ""))
    if not (0 <= err <= 1 and 0 <= threshold <= 1): raise ValueError("Error rates must be within 0..1")
    action = "continue_monitoring" if healthy and err <= threshold else (
        "recommend_rollback" if digest.startswith("sha256:") else "pause_and_investigate")
    return make_result("UC-14", "Release & Rollback Recommendation",
        "Recommendation only. Rollback requires an immutable known-good digest and separate approved executor.",
        [{"action": action, "healthy": healthy, "error_rate": err, "threshold": threshold,
          "image_digest_verified_by_handler": False}],
        payload.get("evidence", []), ["This handler does not change traffic or deploy resources."],
        "advisory", True)

def uc19_evaluation_safety(payload):
    # These are deterministic contract checks; semantic quality needs a labeled evaluation set.
    output = payload.get("agent_output", {})
    checks = {
        "summary_present": bool(output.get("summary")),
        "evidence_is_list": isinstance(output.get("evidence", []), list),
        "assumptions_is_list": isinstance(output.get("assumptions", []), list),
        "approval_flag_present": "requires_human_approval" in output,
    }
    passed = sum(checks.values())
    return make_result("UC-19", "AI Agent Evaluation, Safety & Observability",
        "Schema and safety-contract checks; not a semantic accuracy score.",
        [{"checks": checks, "passed": passed, "total": len(checks), "pass_fraction": passed/len(checks)}],
        [evidence("agent_output", "Output contract evaluated")],
        ["Add golden datasets, groundedness checks, latency/cost metrics, and regression thresholds."], "advisory")
