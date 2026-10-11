# AI Use Cases — Payment Service Platform

This folder contains the numbered AI use-case catalogue and implementation guidance for the `payment-service` DevOps/SRE capstone.

## IMPORTANT: Merge with the existing `ai/` directory

Your repository already contains these Python modules:
- `investigator.py`
- `orchestrator.py`
- `policy.py`
- `release_agent.py`
- `remediation_agent.py`
- `state.py`
- `verification_agent.py`

**Do not delete or overwrite these modules just to add this documentation.** This ZIP contains documentation and use-case specifications; it does not include replacement versions of your existing Python modules. Extract/merge the ZIP at the repository root and retain the existing files.

## How the current code maps to the use-case matrix

| Existing module | Likely responsibility | Related use case |
|---|---|---|
| `orchestrator.py` | Coordinates workflow and agents | UC-04, UC-05, UC-14 |
| `investigator.py` | Collects/investigates incident evidence | UC-04 |
| `release_agent.py` | Assesses or handles release-related workflow | UC-03, UC-08, UC-14 |
| `remediation_agent.py` | Proposes/executes remediation workflow | UC-05, UC-14 |
| `verification_agent.py` | Checks whether the service recovered | UC-14 |
| `policy.py` | Enforces safety and action policies | UC-05, UC-14, UC-19 |
| `state.py` | Shared workflow/incident state | UC-04, UC-05, UC-14 |

This mapping is inferred from filenames only. Verify each module's actual implementation before relying on it or claiming a capability is implemented.

## Start here

1. Read `USE_CASE_MATRIX.md` for all numbered use cases.
2. Start with **UC-01 — Agentic Cloud FinOps & Cost Optimization Advisor**.
3. Keep the current incident-agent code until it has been reviewed and mapped to the roadmap.
4. Use `IMPLEMENTATION_ROADMAP.md`, `SAFETY_AND_EVALUATION.md`, and `DATA_CONTRACTS.md` as the design baseline.

## Status vocabulary

- Planned — documented only
- In progress — implementation underway
- Implemented — code exists and tests pass
- Validated — tested with realistic fixtures and recorded results
- Production-ready — security, reliability, cost, and operational controls reviewed

## Project principles

- Business workload: `payment-service` only.
- Use real evidence; never invent metrics, prices, causes, or scan results.
- Keep AI recommendations separate from infrastructure execution.
- Start read-only; require human approval for operational write actions.
- Keep the dashboard's build/release lifecycle independent of `payment-service`.
- Never put secrets, tokens, raw payment payloads, or sensitive customer data into prompts or fixtures.
