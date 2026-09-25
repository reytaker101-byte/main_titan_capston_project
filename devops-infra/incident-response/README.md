# Incident Response

## Severity example

```text
SEV-1 -> PagerDuty + Slack + Email + Ticket
SEV-2 -> Slack + Email + Ticket
SEV-3 -> Slack + Ticket
SEV-4 -> Ticket
```

The exact thresholds should be defined by the target organization.

## RCA format

```text
Incident
Impact
Affected resources
Timeline
Evidence
Root cause
Contributing factors
Remediation
Verification
Rollback
Preventive action
```

## AI rule

RCA claims require evidence.
If evidence is insufficient:

```text
Root cause not established from available evidence.
```
