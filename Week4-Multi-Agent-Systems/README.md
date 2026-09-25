# Week 4 — Multi-Agent Systems

## Agents

```text
Supervisor
 |
 +-- Investigator Agent
 +-- RCA Agent
 +-- Release Agent
 +-- Remediation Agent
 +-- Verification Agent
```

### Why?

Each agent has a narrow responsibility.

### State

The incident state contains:

- incident ID
- severity
- affected resources
- evidence
- hypotheses
- RCA
- remediation options
- approval
- execution result
- verification
- audit events

### Critical design

No specialist agent gets unrestricted production access.
