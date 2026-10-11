# UC-16 — Multimodal SRE Diagnostic Assistant

- **Priority:** P3
- **Initial status:** Planned
- **Service scope:** `payment-service` and shared SRE platform capabilities

## Objective
Help engineers interpret screenshots, dashboards, architecture diagrams and sanitized error captures alongside textual evidence.

## Inputs
User-provided screenshots/diagrams, OCR or image extraction, related metrics and incident context.

## Proposed workflow
Extract visible signals, identify uncertainty, connect observations to known service context, and request confirmation when details are ambiguous.

## Expected output
Image observations, extracted labels/text, likely interpretations, missing context and linked next checks.

## Interview Kickstart mapping
UC-10 Operations Assistant; Week 5 Conversational & Multimodal Agents.

## Safety and design guardrails
Do not infer hidden telemetry from an image; redact secrets/customer data; keep visual interpretations as hypotheses.

## Acceptance criteria
- [ ] The capability has a clearly defined interface and bounded scope.
- [ ] Results include provenance, timestamps and limitations where relevant.
- [ ] Missing or conflicting evidence is explicitly represented.
- [ ] Sanitized test fixtures and repeatable evaluation are available.
- [ ] No unauthorized infrastructure mutation can occur.
- [ ] Benefit is demonstrated against a baseline before calling the capability validated.

## Implementation note
This document describes a planned capability, not an implemented feature. Keep status as `Planned` until working code and repeatable test evidence exist.
