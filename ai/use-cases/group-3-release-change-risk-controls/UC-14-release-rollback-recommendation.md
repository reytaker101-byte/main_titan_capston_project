# UC-14 — Release & Rollback Recommendation

**Group:** Group 3 — Release, Change & Risk Controls

**Python implementation:** `ai/sre_guardian/use_cases/group3_release_risk.py` → `uc14_release_rollback`

## Purpose
Implement release & rollback recommendation for the single `payment-service` workload.

## Inputs
Release health, error rate, threshold and immutable image digest.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
