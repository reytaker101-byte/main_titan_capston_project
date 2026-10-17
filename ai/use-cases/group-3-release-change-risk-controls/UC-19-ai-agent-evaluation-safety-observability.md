# UC-19 — AI Agent Evaluation, Safety & Observability

**Group:** Group 3 — Release, Change & Risk Controls

**Python implementation:** `ai/sre_guardian/use_cases/group3_release_risk.py` → `uc19_evaluation_safety`

## Purpose
Implement ai agent evaluation, safety & observability for the single `payment-service` workload.

## Inputs
Agent output contract and labeled evaluation dataset.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
