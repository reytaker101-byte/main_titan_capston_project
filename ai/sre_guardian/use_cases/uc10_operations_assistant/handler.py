from ...contracts import make_result, evidence


def uc10_operations_assistant(payload):
    # Keep tool execution separate; the assistant returns only the approved read-only choices.
    query = str(payload.get("query", "")).strip()
    tools = payload.get("available_readonly_tools", [])
    if not query: raise ValueError("query is required")
    return make_result("UC-10", "AI Operations Assistant",
        "Choose a read-only tool or retrieve a sourced runbook before answering operational questions.",
        [{"query": query, "available_tools": [t for t in tools if isinstance(t, str)],
          "suggested_next_step": "collect evidence before diagnosis"}],
        [], ["No model provider is called by this deterministic handler."], "advisory")
