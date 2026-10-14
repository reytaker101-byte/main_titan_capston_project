from ..contracts import make_result, evidence

def uc04_root_cause(payload):
    # Rank hypotheses against actual supplied event/log text; do not claim causal certainty.
    evidence_items = payload.get("evidence", [])
    text = " ".join(str(e.get("message", e.get("summary", ""))).lower() for e in evidence_items)
    hypotheses = []
    for h in payload.get("hypotheses", []):
        terms = [str(t).lower() for t in h.get("terms", [])]
        matched = [t for t in terms if t and t in text]
        hypotheses.append({"hypothesis": h["name"], "matched_terms": matched,
                           "support_score": len(matched)/max(1, len(terms)), "confirmed": False})
    hypotheses.sort(key=lambda h: h["support_score"], reverse=True)
    if not evidence_items: status = "insufficient_evidence"
    else: status = "advisory"
    return make_result("UC-04", "AI Root Cause Analysis",
        "Evidence-ranked hypotheses; verify against metrics, events, logs, and recent changes.",
        hypotheses, [evidence("incident_evidence", f"{len(evidence_items)} evidence items")],
        ["Keyword support is not causal inference; connect a validated LLM/RCA workflow for semantic analysis."], status)

def uc05_incident_triage(payload):
    severity = str(payload.get("severity", "unknown")).lower()
    priority = {"critical": 1, "high": 2, "medium": 3, "low": 4}.get(severity, 5)
    steps = payload.get("runbook_steps", [])
    if not steps: steps = ["Confirm customer impact", "Check payment-service health and recent rollout",
                           "Collect pod events, logs and Prometheus error/latency metrics", "Escalate per on-call policy"]
    return make_result("UC-05", "Incident Triage & Response Planner",
        "Triage plan derived from the supplied incident context.", 
        [{"priority": priority, "severity": severity, "customer_impact": payload.get("customer_impact", "unknown"),
          "recommended_steps": steps, "escalation_recommended": priority <= 2}],
        payload.get("evidence", []), ["This handler does not page or mutate infrastructure."], "advisory", True)

def uc10_operations_assistant(payload):
    # Keep tool execution separate; the assistant returns only the approved read-only choices.
    query = str(payload.get("query", "")).strip()
    tools = payload.get("available_readonly_tools", [])
    if not query: raise ValueError("query is required")
    return make_result("UC-10", "AI Operations Assistant",
        "Choose a read-only tool or retrieve a sourced runbook before answering operational questions.",
        [{"query": query, "available_tools": [t for t in tools if isinstance(t, str)],
          "suggested_next_step": "collect evidence before diagnosis"}],
        [], ["No model provider is called by this deterministic handler."], "advisory")

def uc11_timeline_postmortem(payload):
    events = payload.get("events", [])
    for e in events:
        if not e.get("timestamp") or not e.get("description"): raise ValueError("Events need timestamp and description")
    events = sorted(events, key=lambda e: e["timestamp"])
    return make_result("UC-11", "Incident Timeline & Postmortem Drafting",
        "Blameless timeline draft; review timestamps and impact before publishing.",
        [{"timeline": events, "impact": payload.get("impact", "not supplied"),
          "contributing_factors": payload.get("contributing_factors", []),
          "follow_ups": payload.get("follow_ups", [])}],
        [evidence("incident_event_records", f"{len(events)} events")],
        ["Only recorded events are included; missing times and causes are not inferred."], "advisory")

def uc15_incident_memory(payload):
    # Deterministic lexical retrieval; production hybrid retrieval should combine BM25 and vector search.
    query_terms = set(str(payload.get("query", "")).lower().split())
    docs = payload.get("documents", [])
    ranked = []
    for d in docs:
        body = f"{d.get('title','')} {d.get('content','')}".lower()
        matched = sorted(t for t in query_terms if len(t) > 2 and t in body)
        if matched:
            ranked.append({"id": d.get("id"), "title": d.get("title"), "source": d.get("source"),
                           "score": len(matched)/max(1, len(query_terms)), "matched_terms": matched})
    ranked.sort(key=lambda r: r["score"], reverse=True)
    return make_result("UC-15", "Hybrid Retrieval & Incident Memory Engine",
        "Retrieved matching historical evidence; lexical baseline only.", ranked[:int(payload.get("top_k", 5))],
        [evidence("incident_knowledge_corpus", f"{len(docs)} documents searched")],
        ["For production hybrid retrieval, configure indexed, access-controlled sources and embedding/vector infrastructure."],
        "advisory" if ranked else "insufficient_evidence")
