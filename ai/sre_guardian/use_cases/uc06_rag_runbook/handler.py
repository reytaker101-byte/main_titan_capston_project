from ...contracts import make_result, evidence
from pathlib import Path


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
