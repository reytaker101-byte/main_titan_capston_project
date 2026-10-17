# UC-20 — SRE Agent Domain Adaptation & Fine-Tuning

**Group:** Group 4 — Knowledge, Tooling & Agent Platform

**Python implementation:** `ai/sre_guardian/use_cases/group4_knowledge_platform.py` → `uc20_domain_adaptation`

## Purpose
Implement sre agent domain adaptation & fine-tuning for the single `payment-service` workload.

## Inputs
Offline baseline and candidate predictions on held-out labels.

## Safety and reliability
- Input values must come from approved, timestamped sources.
- Missing data must be surfaced, not silently fabricated.
- This use case produces analysis or recommendations; production writes require a separately authorized executor.
- Validate thresholds and assumptions against actual service history before using this result as an operational gate.

## Validation
Unit tests live in `ai/tests/`. Run them from the repository root with `pytest -q ai/tests`.
