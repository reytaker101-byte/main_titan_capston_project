# Week 7 — Hybrid Search & Retrieval

## Why hybrid?

SRE queries contain both meaning and exact identifiers.

```text
semantic search
    +
keyword search
    +
metadata filtering
    +
optional reranking
```

Semantic retrieval can find differently worded incidents.
Keyword retrieval is strong for:

- v1.4.0
- OOMKilled
- HTTP 502
- payment-service
- exact error codes

### Terms

- Dense retrieval
- Sparse retrieval
- BM25-style search
- Hybrid retrieval
- Reranking
- MMR
- Metadata filtering
- Precision@K
- Recall@K
