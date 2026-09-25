# Week 2 — RAG Knowledge Agents I

## Goal

Give the agent access to operational knowledge without putting the entire knowledge base inside the prompt.

```text
Incident
   |
Retriever
   |
Relevant runbooks/incidents
   |
LLM
   |
Grounded answer
```

### Topics

- embeddings
- semantic similarity
- chunking
- vector store
- ingestion
- indexing
- retrieval
- generation
- grounding
- hallucination risk

### Project use case

The agent retrieves:

- CrashLoopBackOff runbook
- rollback runbook
- historical payment incident
- release policy

### Rule

Current Kubernetes/Prometheus state is authoritative for current conditions.
RAG provides operational knowledge and historical context.
