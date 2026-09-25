# Week 6 — Agent Communication Protocols

## MCP

MCP gives a standard boundary for exposing tools/resources to AI applications.

Read tools:

- get_pod
- get_logs
- get_events
- query_prometheus
- get_release_history
- retrieve_runbook

Write tools remain behind the same policy and approval layer.

## A2A

Use typed contracts when agents communicate.

Example:

```json
{
  "incident_id": "INC-1001",
  "task": "investigate",
  "resource": "payment-service"
}
```

## Google ADK

Keep an adapter boundary so orchestration implementation can change without changing business contracts.
