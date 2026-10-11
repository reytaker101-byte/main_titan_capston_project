# Shared AI core components

Keep shared cross-agent modules here, separate from individual agents:
- `policy.py` — shared policy, permissions, and safety checks
- `state.py` — shared workflow state and data structures

These locations are recommendations based on filenames; inspect module imports and responsibilities before moving. Update imports and tests, and preserve all behavior. Do not delete, merge, or reduce any agents.
