# UC-18: Multi-Agent Coordination & Delegation

## Purpose
This folder contains the executable Python handler for **Multi-Agent Coordination & Delegation**.

## Main file
- `handler.py` — input validation, analysis logic, and result generation for this use case.

## Shared components used
- `ai/sre_guardian/contracts.py` — common result/evidence format.
- `ai/sre_guardian/service.py` — registers this handler so the API can execute it.
- `ai/sre_guardian/adapters/` — shared external-system adapters where applicable.

## Important
This implementation is an initial baseline. Read the handler's comments and limitations before describing it as production-ready.
