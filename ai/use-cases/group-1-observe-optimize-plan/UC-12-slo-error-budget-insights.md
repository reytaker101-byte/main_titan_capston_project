# UC-12 — SLO & Error-Budget Insights

**Group:** Group 1 — Observe, Optimize & Plan

**Python implementation:** `ai/sre_guardian/use_cases/group1_observe_optimize_plan.py` → `uc12_slo_error_budget`

## Purpose
Implement slo & error-budget insights for the single `payment-service` workload.

## Inputs
SLI aggregate and explicit SLO target.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
