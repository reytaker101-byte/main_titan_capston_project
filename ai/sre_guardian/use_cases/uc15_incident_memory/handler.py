from ...contracts import make_result, evidence
from pathlib import Path


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
