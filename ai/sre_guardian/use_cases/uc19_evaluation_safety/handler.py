from ...contracts import make_result, evidence


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
