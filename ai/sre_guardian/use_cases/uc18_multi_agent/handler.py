from ...contracts import make_result, evidence


def uc18_multi_agent(payload):
    # Explicit bounded delegation; agents must be registered by trusted application code.
    agents = payload.get("_trusted_agents")
    if not isinstance(agents, dict):
        return make_result("UC-18", "Multi-Agent Coordination & Delegation",
            "No trusted agent registry configured; no agents were executed.",
            [], [], ["Do not accept callable agents from client-supplied payloads."], "insufficient_evidence")
    return make_result("UC-18", "Multi-Agent Coordination & Delegation",
        "Trusted agent registry is available but execution requires an application-level workflow.",
        [{"registered_agents": sorted(agents.keys()), "executed": False}],
        [], ["Add bounded workflow state, deadlines, retry budgets, and trace IDs."], "advisory")
