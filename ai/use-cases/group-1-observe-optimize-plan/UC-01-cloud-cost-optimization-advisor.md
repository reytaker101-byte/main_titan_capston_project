# UC-01 — Cloud Cost Optimization Advisor

**Group:** Group 1 — Observe, Optimize & Plan

**Python implementation:** `ai/sre_guardian/use_cases/group1_observe_optimize_plan.py` → `uc01_cost_optimization`

## Purpose
Implement cloud cost optimization advisor for the single `payment-service` workload.

## Inputs
GCP Billing Export / BigQuery adapter; provide billing rows to the analyzer.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
