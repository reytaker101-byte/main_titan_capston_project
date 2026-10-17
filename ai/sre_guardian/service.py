"""Central registry for all 20 SRE Guardian use cases.

Each use case's executable handler lives in its own folder under use_cases/.
Shared API, contracts, configuration, policy, and adapters remain centralized.
"""
from .use_cases.uc01_cost_optimization.handler import uc01_cost_optimization
from .use_cases.uc02_resource_optimization.handler import uc02_resource_optimization
from .use_cases.uc03_deployment_risk.handler import uc03_deployment_risk
from .use_cases.uc04_root_cause.handler import uc04_root_cause
from .use_cases.uc05_incident_triage.handler import uc05_incident_triage
from .use_cases.uc06_rag_runbook.handler import uc06_rag_runbook
from .use_cases.uc07_alert_correlation.handler import uc07_alert_correlation
from .use_cases.uc08_change_impact.handler import uc08_change_impact
from .use_cases.uc09_predictive_scaling.handler import uc09_predictive_scaling
from .use_cases.uc10_operations_assistant.handler import uc10_operations_assistant
from .use_cases.uc11_timeline_postmortem.handler import uc11_timeline_postmortem
from .use_cases.uc12_slo_error_budget.handler import uc12_slo_error_budget
from .use_cases.uc13_security_risk.handler import uc13_security_risk
from .use_cases.uc14_release_rollback.handler import uc14_release_rollback
from .use_cases.uc15_incident_memory.handler import uc15_incident_memory
from .use_cases.uc16_multimodal.handler import uc16_multimodal
from .use_cases.uc17_mcp_tool_integration.handler import uc17_mcp_tool_integration
from .use_cases.uc18_multi_agent.handler import uc18_multi_agent
from .use_cases.uc19_evaluation_safety.handler import uc19_evaluation_safety
from .use_cases.uc20_domain_adaptation.handler import uc20_domain_adaptation

# Stable IDs keep API clients, documentation, and tests consistent.
HANDLERS = {
    "UC-01": ("Cloud Cost Optimization Advisor", uc01_cost_optimization),
    "UC-02": ("Kubernetes Capacity & Resource Optimization", uc02_resource_optimization),
    "UC-03": ("Deployment Risk Analysis", uc03_deployment_risk),
    "UC-04": ("AI Root Cause Analysis", uc04_root_cause),
    "UC-05": ("Incident Triage & Response Planner", uc05_incident_triage),
    "UC-06": ("SRE Runbook Knowledge Assistant (RAG)", uc06_rag_runbook),
    "UC-07": ("Alert Correlation & Noise Reduction", uc07_alert_correlation),
    "UC-08": ("Change Impact Analysis", uc08_change_impact),
    "UC-09": ("Predictive Scaling Advisor", uc09_predictive_scaling),
    "UC-10": ("AI Operations Assistant", uc10_operations_assistant),
    "UC-11": ("Incident Timeline & Postmortem Drafting", uc11_timeline_postmortem),
    "UC-12": ("SLO & Error-Budget Insights", uc12_slo_error_budget),
    "UC-13": ("Security & Configuration Risk Advisor", uc13_security_risk),
    "UC-14": ("Release & Rollback Recommendation", uc14_release_rollback),
    "UC-15": ("Hybrid Retrieval & Incident Memory Engine", uc15_incident_memory),
    "UC-16": ("Multimodal SRE Diagnostic Assistant", uc16_multimodal),
    "UC-17": ("MCP-Based SRE Tool Integration", uc17_mcp_tool_integration),
    "UC-18": ("Multi-Agent Coordination & Delegation", uc18_multi_agent),
    "UC-19": ("AI Agent Evaluation, Safety & Observability", uc19_evaluation_safety),
    "UC-20": ("SRE Agent Domain Adaptation & Fine-Tuning", uc20_domain_adaptation),
}

def run_use_case(use_case_id: str, payload: dict) -> dict:
    # Normalize IDs so callers can use UC-01 or uc-01.
    uc_id = use_case_id.upper()
    if uc_id not in HANDLERS:
        raise KeyError(f"Unknown use case: {uc_id}")
    # Every handler expects a JSON object, not a list or scalar.
    if not isinstance(payload, dict):
        raise TypeError("payload must be a JSON object")
    # Keep execution delegated to the selected use-case handler.
    return HANDLERS[uc_id][1](payload)
