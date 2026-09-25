# Week 9 — Fine-Tuning + Domain Adaptation

## Decision order

```text
Prompting
  ->
RAG
  ->
tool/state design
  ->
evaluation
  ->
fine-tuning if justified
```

Fine-tuning is not a replacement for live infrastructure tools.

### Useful SRE domain-adaptation goals

- consistent incident classification
- structured RCA output
- organization terminology
- consistent remediation-plan format

### Training example format

JSONL can contain:

```json
{"messages":[
  {"role":"system","content":"You are an SRE RCA assistant."},
  {"role":"user","content":"payment-service is CrashLoopBackOff"},
  {"role":"assistant","content":"Return affected resource, evidence, RCA and safe next step."}
]}
```

### Important

Current Kubernetes state still comes from tools.
Current operational knowledge still comes from retrieval.
