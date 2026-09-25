# Chaos Engineering — Gremlin

## Scenarios

1. terminate payment pod
2. network latency
3. CPU pressure
4. readiness failure

## Safe process

```text
Experiment definition
   ->
scope validation
   ->
human approval
   ->
execute chaos
   ->
observe
   ->
AI investigation
   ->
verify recovery
   ->
audit
```

Start locally/sandbox first. Never use real production as a learning experiment.

The project is designed so Gremlin can be connected through an adapter rather than embedded directly in the AI reasoning logic.
