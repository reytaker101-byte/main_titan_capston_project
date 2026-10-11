# AI Implementation Roadmap

## Phase 0 — Foundations
- Verify data sources and freshness.
- Add sanitized sample fixtures so demos work when GKE is unavailable.
- Define a shared result contract and stable use-case IDs.
- Test missing, stale, conflicting and malformed evidence.
- Keep the dashboard independently versioned from `payment-service`.

## Phase 1 — UC-01 Cost Optimization (first)
1. Identify billing, GKE usage, requests/limits, storage and logging data.
2. Use deterministic calculations for cost and utilization; use an LLM to explain/prioritize, not invent numbers.
3. Rank candidates by estimated monthly savings, confidence, effort, reliability risk and reversibility.
4. Show currency, time window, pricing source and assumptions.
5. Generate recommendations only; no resource deletion, resizing or scale-down.
6. Validate against a reviewed fixture and expected calculations.
7. Demo one opportunity labelled “estimated, not realized”.

**Acceptance:** every recommendation has evidence and a time window; assumptions are visible; missing pricing/metrics yields “insufficient data”; reliability risks and rollback plan are shown.

## Phase 2 — UC-02 Capacity Optimization
Use representative percentiles and peak periods; include throttling, OOMs, restarts and latency. Require staged/load validation before changing resources.

## Phase 3 — UC-04 RCA and observability
Normalize event timestamps and correlate logs, metrics, pod status and deployment history. Return ranked hypotheses with supporting and contradicting evidence; test injected failures.

## Phase 4 — UC-06 RAG
Index approved runbooks, use keyword + semantic search and metadata filters, return citations/revisions, and state when evidence is weak.

## Phase 5 — UC-03, UC-08, UC-13
Analyze release/change risk from real diffs and test/scanner outputs. Unknown checks must not be treated as passed.

## Phase 6 — UC-05, UC-07, UC-10, UC-11, UC-12, UC-14
Add incident planning, alert grouping, read-only operations Q&A, postmortem drafting, SLO analysis and release recommendations. Gate every write behind explicit approval.

## Phase 7 — UC-09 and advanced agents
Add forecasting only with sufficient clean history and compare it to a simple baseline. Add multi-agent orchestration only if it measurably improves results.

## Mapping to a nine-week Agentic AI learning path
| Week | Project application |
|---|---|
| 1 — Agentic foundations / reflex agents | Deterministic rules and UC-01 opportunity detection |
| 2 — RAG foundations | UC-06 runbook assistant |
| 3 — Advanced RAG | Hybrid retrieval, metadata filters and incident-aware context |
| 4 — Multi-agent systems | Coordinated evidence gathering for UC-04/UC-05 |
| 5 — Conversational/multimodal agents | UC-10; optional screenshot/diagram interpretation |
| 6 — Agent communication protocols | Evaluate MCP/A2A only where useful |
| 7 — Hybrid search | Keyword + semantic retrieval and reranking |
| 8 — Safety, evaluation and cost | Guardrails, test dataset, approval gates, token/cost tracking |
| 9 — Fine-tuning/domain adaptation | Optional only after baseline evaluation shows a measurable gap |

Fine-tuning is not a prerequisite.
