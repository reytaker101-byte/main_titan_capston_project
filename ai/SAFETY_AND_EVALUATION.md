# Safety, Evaluation and Operational Guardrails

## Non-negotiable rules
1. Evidence before explanation: claims reference a metric, log, event, configuration, deployment or approved document.
2. No fabricated data: missing/stale evidence must be disclosed.
3. Read-only first: agents inspect and recommend before they mutate.
4. Human approval for writes: rollback, scaling, restart, promotion, IAM changes and deletion require explicit approval.
5. Least privilege: no broad shell or cluster-admin credentials for an LLM.
6. No secrets in prompts; redact credentials, payment data and personal/customer information.
7. Separate recommendation from execution; a recommendation is not proof an action ran.
8. Audit use-case ID, evidence references, model/template version, decision, approver and action result.
9. Set timeouts, token limits, caching, rate limits and model budgets.
10. Preserve deterministic health checks and runbooks as fallback.

## Evaluation dimensions
- Grounding: do citations support the answer?
- Correctness: does output match labelled test cases?
- Calibration: is confidence reduced when evidence is incomplete?
- Safety: are unauthorized/destructive actions prevented?
- Usefulness: can an SRE take the next step?
- Latency and cost per analysis.
- Robustness to stale, conflicting or malformed evidence.
- Traceability: can the decision be reconstructed?

## Minimum test cases
- Healthy service; no action required.
- Pod crash/restarts; ImagePullBackOff; failed readiness probe.
- CPU throttling or memory pressure.
- Recent release followed by elevated latency.
- Missing/stale metrics or billing export.
- Conflicting evidence.
- Prompt injection embedded in a log/document.
- Destructive request without approval.

## Production readiness checklist
- [ ] Unit/integration tests pass.
- [ ] Sanitized evaluation dataset and baseline results are recorded.
- [ ] Logs and AI output are redacted.
- [ ] Kubernetes RBAC and cloud IAM are least-privilege.
- [ ] Human approval gates are tested for all writes.
- [ ] Timeout/failure fallback is tested.
- [ ] Cost and latency are measured.
- [ ] Rollback path is documented and tested.
- [ ] Estimates, hypotheses, confidence and limitations are labelled.
- [ ] Operational owner and runbook are identified.
