# UC-11 — Incident Timeline & Postmortem Drafting

**Group:** Group 2 — Incident Intelligence & Response

**Python implementation:** `ai/sre_guardian/use_cases/group2_incident_intelligence.py` → `uc11_timeline_postmortem`

## Purpose
Implement incident timeline & postmortem drafting for the single `payment-service` workload.

## Inputs
Timestamped incident events and human-verified impact.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
