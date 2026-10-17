# UC-13 — Security & Configuration Risk Advisor

**Group:** Group 3 — Release, Change & Risk Controls

**Python implementation:** `ai/sre_guardian/use_cases/group3_release_risk.py` → `uc13_security_risk`

## Purpose
Implement security & configuration risk advisor for the single `payment-service` workload.

## Inputs
Normalized Trivy/CodeQL/Wiz findings.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
