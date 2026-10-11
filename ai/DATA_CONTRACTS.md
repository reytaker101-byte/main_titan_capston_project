# AI Data Contracts

These are logical contracts, not claims that all integrations exist. Implement typed schemas in code when the first use case is built.

## Shared result example
```json
{
  "use_case_id": "UC-01",
  "generated_at": "2026-01-01T00:00:00Z",
  "service": "payment-service",
  "environment": "dev",
  "status": "recommendations_available",
  "summary": "One potential cost optimization was identified.",
  "evidence": [{
    "source_type": "prometheus",
    "source_id": "sample-fixture-001",
    "observed_at": "2026-01-01T00:00:00Z",
    "description": "Illustrative CPU usage",
    "value": 0.18,
    "unit": "cores",
    "is_sample_data": true
  }],
  "recommendations": [{
    "title": "Review CPU request",
    "estimated_monthly_savings": null,
    "currency": null,
    "confidence": "low",
    "risk_level": "medium",
    "requires_human_approval": true
  }],
  "limitations": ["Sample data only; no real savings measured."]
}
```

## UC-01 cost opportunity fields
- `resource_id`, `resource_type`
- `period_start`, `period_end`
- `actual_cost` (observed billing) and `estimated_cost` (calculation with source/assumptions)
- `utilization_summary` (percentile/range and source)
- `proposed_change`
- `estimated_monthly_savings` (nullable), `currency`
- `reliability_risk`, `confidence`
- `validation_plan`, `status` (candidate/reviewed/approved/rejected/applied/verified)

## Evidence quality rules
- Keep timestamps/time zones explicit.
- Attach environment and service to every signal.
- Preserve source references.
- Mark fixtures with `is_sample_data: true`.
- Treat missing data as unknown, not zero.
- Never mix actual billing totals and estimated savings without labels.
- Never include raw payment payloads or sensitive customer data.
