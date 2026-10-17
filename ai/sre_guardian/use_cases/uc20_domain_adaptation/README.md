# UC-20: SRE Agent Domain Adaptation & Fine-Tuning

## Purpose
This folder contains the executable Python handler for **SRE Agent Domain Adaptation & Fine-Tuning**.

## Main file
- `handler.py` — input validation, analysis logic, and result generation for this use case.

## Shared components used
- `ai/sre_guardian/contracts.py` — common result/evidence format.
- `ai/sre_guardian/service.py` — registers this handler so the API can execute it.
- `ai/sre_guardian/adapters/` — shared external-system adapters where applicable.

## Important
This implementation is an initial baseline. Read the handler's comments and limitations before describing it as production-ready.
