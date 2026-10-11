# Agentic AI SRE Platform — Payment Service

This folder contains numbered use-case specifications and organization guidance for the `payment-service` DevOps/SRE capstone.

## Folder structure

```text
ai/
├── README.md
├── USE_CASE_MATRIX.md
├── IMPLEMENTATION_ROADMAP.md
├── SAFETY_AND_EVALUATION.md
├── DATA_CONTRACTS.md
├── agents/
│   └── README.md
├── core/
│   └── README.md
└── use-cases/
    ├── UC-01-...md
    ├── UC-02-...md
    └── ... UC-20-...md
```

## Preserve all agents

Do not reduce, merge, or delete agents. Keep each agent as a separate module:
- `investigator.py`
- `orchestrator.py`
- `release_agent.py`
- `remediation_agent.py`
- `verification_agent.py`

Shared modules `policy.py` and `state.py` may be placed in `core/` after checking imports and responsibilities. Add more agents when justified by a use case.

**This ZIP is documentation and organization guidance only.** It does not include or replace existing Python source code. Merge the documentation with the current repository; do not use it to overwrite the existing Python modules.

## Start here
1. Review `USE_CASE_MATRIX.md` (UC-01 through UC-20).
2. Implement UC-01 — Agentic Cloud FinOps & Cost Optimization Advisor first.
3. Follow `IMPLEMENTATION_ROADMAP.md`.
4. Apply `SAFETY_AND_EVALUATION.md` before enabling operational actions.

## Status discipline
A documented use case is not an implemented feature. Use `Planned`, `In progress`, `Implemented`, `Validated`, or `Production-ready` accurately.

## Principles
- Business workload: `payment-service` only.
- Use real evidence; never invent metrics, prices, causes, or scanner results.
- Keep recommendations separate from infrastructure execution.
- Start read-only and require human approval for operational write actions.
- Keep dashboard versioning independent of `payment-service`.
- Never include secrets, tokens, raw payment payloads, or sensitive customer data in prompts or fixtures.
