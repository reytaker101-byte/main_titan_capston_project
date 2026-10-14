# UC-15 — Hybrid Retrieval & Incident Memory Engine

**Group:** Group 2 — Incident Intelligence & Response

**Python implementation:** `ai/sre_guardian/use_cases/group2_incident_intelligence.py` → `uc15_incident_memory`

## Purpose
Implement hybrid retrieval & incident memory engine for the single `payment-service` workload.

## Inputs
Historical incident documents and query.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
