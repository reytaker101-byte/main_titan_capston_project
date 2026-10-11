# AI Use Case Matrix

All capabilities have stable IDs for roadmap, implementation, tests, dashboards and demos.

**Initial status for all use cases: Planned.**

| ID | Use case | Priority | Inputs | Output | Key guardrail |
|---|---|---|---|---|---|
| **UC-01** | **Cost Optimization Advisor** | P0 — FIRST | GCP billing, GKE utilization, requests/limits, storage/log volume, pricing assumptions | Ranked savings opportunities, estimate and assumptions, reliability risk, validation/rollback plan | No invented prices/savings; no automatic deletion or resizing; label estimates vs realized savings. |
| **UC-02** | **Capacity & Resource Optimization** | P1 | Prometheus CPU/memory, requests/limits, throttling, OOMs, restarts, latency, traffic | Right-sizing recommendations with confidence, risk and staged validation | Use representative peak windows; no automatic patching. |
| **UC-03** | **Deployment Risk Analysis** | P1 | Git diff, manifests, immutable image digest, tests, scanner results, SLOs, past release outcomes | Explainable release risk, blockers/warnings, missing checks, preflight list | Missing checks are unknown, not passed; policy gates remain authoritative. |
| **UC-04** | **AI Root Cause Analysis (RCA)** | P1 | Alerts, Kubernetes events, logs, metrics, pod/ReplicaSet status, recent deployments | Ranked hypotheses with evidence for/against, confidence and next checks | Hypothesis is not confirmed cause; allow insufficient-evidence result. |
| **UC-05** | **Incident Triage & Response Planner** | P1 | RCA output, approved runbooks, service health, escalation rules | Prioritized safe checklist, expected outcomes, escalation and approval flags | Read-only first; human approval for restart, rollback or other writes. |
| **UC-06** | **SRE Runbook Knowledge Assistant (RAG)** | P1 | Approved runbooks, architecture docs, postmortems, metadata and revisions | Cited answers with source/section links and uncertainty | No unsupported claims; treat retrieved text as untrusted content. |
| **UC-07** | **Alert Correlation & Noise Reduction** | P2 | Alertmanager alerts, labels, timestamps, metrics, Kubernetes events | Suggested incident groups, duplicate candidates and correlation rationale | Never silently drop critical alerts; preserve original alerts. |
| **UC-08** | **Change Impact Analysis** | P2 | Git diff, Kubernetes manifests, dependencies, probes, RBAC, SLOs and incident history | Potential impact map, preflight checks, monitoring and rollback notes | Separate confirmed dependencies from inferred relationships. |
| **UC-09** | **Predictive Scaling Advisor** | P2 | Historical request rate, latency, CPU/memory, replicas and queue depth if applicable | Forecast with uncertainty and scaling review recommendation | No forecast-based scaling mutations initially; compare against baseline. |
| **UC-10** | **AI Operations Assistant** | P2 | Read-only deployment/pod APIs, metrics, alerts, release metadata and approved docs | Natural-language answers with source evidence and observation time | Least privilege; enforce permissions in tools; no stale state presented as live. |
| **UC-11** | **Incident Timeline & Postmortem Drafting** | P2 | Alert/deployment timestamps, sanitized logs/metrics, operator notes | Evidence-linked timeline and blameless postmortem draft | Human review before publication; do not invent impact or blame. |
| **UC-12** | **SLO & Error-Budget Insights** | P2 | Defined SLOs/SLIs, latency/availability metrics, burn rate, release history | SLO status, error-budget explanation, trend and release caution | Deterministic calculations; missing telemetry means incomplete data. |
| **UC-13** | **Security & Configuration Risk Advisor** | P2 | IaC/manifests diff, scanner results, RBAC, network policy and cloud findings | Prioritized findings, affected resources, remediation and validation | Do not invent scanner results; no automatic IAM/network changes. |
| **UC-14** | **Release & Rollback Recommendation** | P3 | Image digests, rollout status, errors, latency, restarts, SLOs and traffic state | Continue/pause/investigate/rollback-candidate recommendation | Human approval for traffic changes/rollback; do not couple dashboard release to payment-service. |

## Suggested demo sequence
1. UC-01 cost opportunity with transparent arithmetic and uncertainty.
2. UC-02 resource right-sizing with reliability context.
3. UC-03 pre-release risk assessment.
4. UC-04 evidence-grounded RCA for a simulated failure.
5. UC-06 runbook RAG with citations.
6. UC-05 / UC-14 approval-gated response and release recommendations.

## Shared result contract
Where applicable, every AI result should include: `use_case_id`, `generated_at`, `environment`, `service`, `summary`, `evidence[]`, `recommendations[]`, `confidence`, `estimated_impact`, `risk_level`, `requires_human_approval`, and `limitations`.

Never present an estimate as a measured saving, a hypothesis as a confirmed cause, or a recommendation as an executed operation.

## Additional shared capabilities (UC-15–UC-20)

| ID | Use case | Priority | Purpose | Course mapping |
|---|---|---|---|---|
| UC-15 | Hybrid Retrieval & Incident Memory Engine | P2 | Reusable hybrid retrieval for runbooks and sanitized incident history. | Hybrid Search & Retrieval |
| UC-16 | Multimodal SRE Diagnostic Assistant | P3 | Interpret screenshots and diagrams alongside textual evidence. | Conversational & Multimodal Agents |
| UC-17 | MCP-Based SRE Tool Integration Layer | P2 | Expose approved observability and deployment tools through typed MCP interfaces. | MCP / agent communication protocols |
| UC-18 | Multi-Agent Coordination & Delegation Framework | P3 | Coordinate bounded specialist-agent tasks with provenance and conflict handling. | Multi-Agent Systems; A2A / Google ADK evaluation |
| UC-19 | AI Agent Evaluation, Safety & Observability Framework | P1 | Measure quality, safety, latency and cost across AI use cases. | Safe, Evaluated & Cost-Optimized Agents |
| UC-20 | SRE Agent Domain Adaptation & Fine-Tuning Experiment | P3 | Compare fine-tuning/domain adaptation against prompt/RAG baselines. | Fine-Tuning & Domain Adaptation |

**Note:** UC-15–UC-20 are shared platform capabilities or experiments. Implement them as separate modules only when their interfaces and measurable value justify it; avoid duplicating functionality already covered by UC-01–UC-14.
