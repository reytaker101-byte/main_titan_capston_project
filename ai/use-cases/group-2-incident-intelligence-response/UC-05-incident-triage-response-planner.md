# UC-05 — Incident Triage & Response Planner

**Group:** Group 2 — Incident Intelligence & Response

**Python implementation:** `ai/sre_guardian/use_cases/group2_incident_intelligence.py` → `uc05_incident_triage`

## Purpose
Implement incident triage & response planner for the single `payment-service` workload.

## Inputs
Incident severity, impact, runbook steps and evidence.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
