# Week 3 — RAG Knowledge Agents II

## Goal

Move from basic retrieval to operational/agentic retrieval.

### Production concepts

- metadata filtering
- persistent indexes
- agentic RAG
- retrieval as a tool
- multi-step retrieval
- source attribution
- confidence
- retrieval evaluation
- Precision@K
- Recall@K
- groundedness

### SRE example

Query:

```text
payment-service v1.4.0 CrashLoopBackOff
```

The retriever should prefer documents matching:

```text
service=payment-service
environment=production
release=v1.4.0
incident_type=release-regression
```

rather than unrelated shopping incidents.
