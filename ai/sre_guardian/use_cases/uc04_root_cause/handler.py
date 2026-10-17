from ...contracts import make_result, evidence


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
