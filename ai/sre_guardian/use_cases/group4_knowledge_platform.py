from pathlib import Path
from ..contracts import make_result, evidence

def uc06_rag_runbook(payload):
    # Retrieve source passages first; answer only from returned evidence in this baseline.
    query = str(payload.get("query", "")).lower().strip()
    documents = payload.get("documents", [])
    if not query: raise ValueError("query is required")
    terms = {t for t in query.split() if len(t) > 2}
    ranked = []
    for doc in documents:
        content = f"{doc.get('title','')} {doc.get('content','')}".lower()
        matched = sorted(t for t in terms if t in content)
        if matched:
            ranked.append({"title": doc.get("title"), "source": doc.get("source"),
                           "matched_terms": matched, "score": len(matched)/max(1, len(terms)),
                           "passage": doc.get("content", "")})
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return make_result("UC-06", "SRE Runbook Knowledge Assistant (RAG)",
        "Retrieved passages for grounded troubleshooting; no unsupported answer is generated.",
        ranked[:int(payload.get("top_k", 5))],
        [evidence("runbook_corpus", f"{len(documents)} documents searched")],
        ["This local retrieval baseline is lexical; embeddings/vector DB and LLM synthesis are not wired yet."],
        "advisory" if ranked else "insufficient_evidence")

def uc16_multimodal(payload):
    # Vision model integration is adapter-based; never claim to inspect a raw image without a model.
    observations = payload.get("vision_observations", [])
    if not observations:
        return make_result("UC-16", "Multimodal SRE Diagnostic Assistant",
            "No structured vision observations provided; configure an approved vision-model adapter.",
            [], [], ["Raw image interpretation is not enabled in this repository baseline."],
            "insufficient_evidence")
    return make_result("UC-16", "Multimodal SRE Diagnostic Assistant",
        "Structured observations received; corroborate them with live telemetry.",
        [{"observation": x} for x in observations],
        [evidence("vision_adapter", f"{len(observations)} observations")],
        ["Observations are not independently verified against the source image."], "advisory")

def uc17_mcp_tool_integration(payload):
    # Deny by default; adapters must be registered in-process after auth and schema validation.
    registry = payload.get("_trusted_tool_registry")
    tool_name = payload.get("tool_name")
    if not isinstance(registry, dict) or tool_name not in registry:
        return make_result("UC-17", "MCP-Based SRE Tool Integration",
            "Tool call denied because no trusted tool adapter is registered.",
            [{"tool_name": tool_name, "executed": False}],
            [], ["Never accept a tool registry from untrusted API request data."], "denied", True)
    # This internal registry must be injected by application wiring, never directly from request JSON.
    return make_result("UC-17", "MCP-Based SRE Tool Integration",
        "Tool adapter is registered; this endpoint remains non-executing by default.",
        [{"tool_name": tool_name, "executed": False}],
        [], ["Wire MCP SDK, authentication, audit logs, timeouts, and server-side allowlists."], "advisory", True)

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

def uc20_domain_adaptation(payload):
    # Offline comparison of labeled correctness values; no fine-tuning or model download occurs.
    baseline, candidate = payload.get("baseline_correct", []), payload.get("candidate_correct", [])
    if not baseline or len(baseline) != len(candidate): raise ValueError("Equal non-empty baseline/candidate labels required")
    b = sum(bool(x) for x in baseline)/len(baseline)
    c = sum(bool(x) for x in candidate)/len(candidate)
    return make_result("UC-20", "SRE Agent Domain Adaptation & Fine-Tuning Experiment",
        "Offline baseline comparison only; no fine-tuning is performed.",
        [{"cases": len(baseline), "baseline_accuracy": b, "candidate_accuracy": c,
          "delta": round(c-b, 4), "candidate_improved": c > b}],
        [evidence("offline_evaluation_set", f"{len(baseline)} labeled cases")],
        ["Use representative held-out data and statistical uncertainty before claiming improvement."], "advisory")
