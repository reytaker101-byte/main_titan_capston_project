# UC-03 — Deployment Risk Analysis

**Group:** Group 3 — Release, Change & Risk Controls

**Python implementation:** `ai/sre_guardian/use_cases/group3_release_risk.py` → `uc03_deployment_risk`

## Purpose
Implement deployment risk analysis for the single `payment-service` workload.

## Inputs
CI test results, change size, recent failures and service health.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
