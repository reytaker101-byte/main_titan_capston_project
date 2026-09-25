# Week 1 — Agentic AI Foundations + Reflex Agents

## Goal

Turn the SRE workflow into an agent.

### Beginner idea

Normal automation:

```text
A -> B -> C
```

Agentic workflow:

```text
observe -> decide -> tool -> observe -> decide -> finish
```

### Reflex agent

```text
IF pod == CrashLoopBackOff
THEN collect pod logs
```

### Production extension

The agent will learn to select read-only investigation tools:

- get deployment
- get pod
- get events
- get logs
- query Prometheus
- get Argo/release history

### Terms

- Agent
- LLM
- Tool calling
- State
- Memory
- Reflex agent
- ReAct
- Trace
- Structured output

### Code

See `reflex_agent.py`.

### Interview question

Why is this an agent instead of a normal script?

Answer:

Because the workflow can choose the next investigation action based on the current evidence/state rather than blindly executing one fixed sequence.
