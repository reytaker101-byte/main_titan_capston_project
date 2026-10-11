# Agent modules

Keep all agent implementations separate. Do not merge or remove agents just to simplify the structure.

Place existing modules here:
- `investigator.py`
- `orchestrator.py`
- `release_agent.py`
- `remediation_agent.py`
- `verification_agent.py`

You can add further specialized agents when a use case requires them. The list above is only the set of existing modules visible in the current repository screenshot, not a limit on future agents.

Before moving existing code, update imports and test references, then run the tests. This archive contains documentation only; it does not contain replacements for your Python source files.
