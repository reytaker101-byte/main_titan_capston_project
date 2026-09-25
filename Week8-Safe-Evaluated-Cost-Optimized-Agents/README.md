# Week 8 — Safe + Evaluated + Cost-Optimized Agents

## The production safety model

```text
LLM
 |
Structured Action
 |
Policy
 |
Human Approval
 |
Write Tool
 |
Verification
```

### Safety

- allowlist
- RBAC
- least privilege
- protected namespaces
- resource scope
- dry-run
- max retries
- timeout
- audit
- human approval

### Evaluation

Test:

- correct tool selection
- correct resource targeting
- RCA grounding
- rollback correctness
- policy compliance
- verification correctness
- retrieval quality
- latency
- token cost

### Cost optimization

- cheaper model for simple tasks
- bounded investigation loops
- bounded logs
- retrieval instead of huge prompts
- caching
- token tracking
- incident budgets
