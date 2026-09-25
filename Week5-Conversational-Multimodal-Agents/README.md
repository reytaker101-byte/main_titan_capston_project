# Week 5 — Conversational + Multimodal Agents

## Conversation

The engineer can ask:

```text
Why is payment failing?
```

Then:

```text
Which pod?
```

Then:

```text
What changed?
```

State preserves the incident context.

## Multimodal

Support evidence such as:

- Grafana screenshot
- Argo CD screenshot
- architecture diagram
- error screenshot

### Production rule

Screenshots are supporting evidence.
Kubernetes/Prometheus APIs are authoritative when available.

### Voice

A voice interface can convert:

```text
"Investigate the payment outage"
```

into the same structured incident request.
