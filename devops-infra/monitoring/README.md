# Prometheus + Grafana

## Metrics

Track:

- request rate
- error rate
- p95/p99 latency
- desired vs available replicas
- pod restarts
- CrashLoopBackOff
- OOMKilled
- deployment availability

## SLI

Example:

```text
successful requests / total requests
```

## SLO

Example:

```text
99.9% successful requests
```

## AI usage

The agent queries structured metrics rather than asking an LLM to guess metrics.

Grafana screenshots can be used as multimodal supporting evidence.
