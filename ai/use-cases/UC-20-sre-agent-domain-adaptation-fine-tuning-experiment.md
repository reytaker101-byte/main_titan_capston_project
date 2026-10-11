# UC-20 — SRE Agent Domain Adaptation & Fine-Tuning Experiment

- **Priority:** P3
- **Initial status:** Planned
- **Service scope:** `payment-service` and shared SRE platform capabilities

## Objective
Determine whether fine-tuning or domain adaptation provides measurable improvement over prompting and RAG baselines.

## Inputs
Sanitized domain examples, evaluation set, baseline model outputs, quality/cost/latency metrics and governance approval.

## Proposed workflow
Establish a baseline, identify a repeatable failure mode, prepare a licensed and sanitized dataset, run a bounded experiment, and compare on held-out cases.

## Expected output
Experiment report comparing baseline vs adapted model on quality, grounding, safety, latency and cost.

## Interview Kickstart mapping
Week 9 Fine-Tuning & Domain Adaptation; complements UC-06 and UC-19.

## Safety and design guardrails
Optional experiment only; no fine-tuning before a baseline; prevent leakage; do not claim improvement without held-out evaluation.

## Acceptance criteria
- [ ] The capability has a clearly defined interface and bounded scope.
- [ ] Results include provenance, timestamps and limitations where relevant.
- [ ] Missing or conflicting evidence is explicitly represented.
- [ ] Sanitized test fixtures and repeatable evaluation are available.
- [ ] No unauthorized infrastructure mutation can occur.
- [ ] Benefit is demonstrated against a baseline before calling the capability validated.

## Implementation note
This document describes a planned capability, not an implemented feature. Keep status as `Planned` until working code and repeatable test evidence exist.
