# AI-SRE Guardian folder guide

## Where to find code
- `use_cases/uc01_.../handler.py` through `use_cases/uc20_.../handler.py`: each use case's executable logic.
- `use_cases/ucXX_.../README.md`: purpose and pointers for that use case.
- `adapters/`: reusable connections to external systems such as BigQuery billing, Kubernetes, and Prometheus.
- `contracts.py`: shared output/evidence structure.
- `service.py`: central registry mapping UC IDs to handlers.
- `api.py`: HTTP endpoints (`/health`, `/use-cases`, and `/use-cases/{id}/run`).
- `api_adapters.py`: HTTP endpoints for shared integration adapters.
- `config.py`: environment-based configuration.
- `policy.py`: action/safety policy helpers.
- `../tests/test_use_cases.py`: shared automated tests for use-case registration and behaviour.

## How to explain this in an interview
A use case has its own folder for its business logic. Common infrastructure is not copied into every use-case folder: adapters, API, configuration, output contracts, and the registry are shared to avoid duplication and keep behavior consistent.
