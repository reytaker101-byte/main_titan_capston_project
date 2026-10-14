# UC-08 — Change Impact Analysis

**Group:** Group 3 — Release, Change & Risk Controls

**Python implementation:** `ai/sre_guardian/use_cases/group3_release_risk.py` → `uc08_change_impact`

## Purpose
Implement change impact analysis for the single `payment-service` workload.

## Inputs
Changed components and a versioned dependency map.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
