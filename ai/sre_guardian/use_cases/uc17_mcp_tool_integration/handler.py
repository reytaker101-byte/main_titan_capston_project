from ...contracts import make_result, evidence


def uc17_mcp_tool_integration(payload):
    # Deny by default; adapters must be registered in-process after auth and schema validation.
    registry = payload.get("_trusted_tool_registry")
    tool_name = payload.get("tool_name")
    if not isinstance(registry, dict) or tool_name not in registry:
        return make_result("UC-17", "MCP-Based SRE Tool Integration",
            "Tool call denied because no trusted tool adapter is registered.",
            [{"tool_name": tool_name, "executed": False}],
            [], ["Never accept a tool registry from untrusted API request data."], "denied", True)
    # This internal registry must be injected by application wiring, never directly from request JSON.
    return make_result("UC-17", "MCP-Based SRE Tool Integration",
        "Tool adapter is registered; this endpoint remains non-executing by default.",
        [{"tool_name": tool_name, "executed": False}],
        [], ["Wire MCP SDK, authentication, audit logs, timeouts, and server-side allowlists."], "advisory", True)
