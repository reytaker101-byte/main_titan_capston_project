from .use_cases import group1_observe_optimize_plan as g1
from .use_cases import group2_incident_intelligence as g2
from .use_cases import group3_release_risk as g3
from .use_cases import group4_knowledge_platform as g4

# Keep the original UC identifiers stable so docs, API clients, and tests agree.
HANDLERS = {
    "UC-01": ("Cloud Cost Optimization Advisor", g1.uc01_cost_optimization),
    "UC-02": ("Kubernetes Capacity & Resource Optimization", g1.uc02_resource_optimization),
    "UC-03": ("Deployment Risk Analysis", g3.uc03_deployment_risk),
    "UC-04": ("AI Root Cause Analysis", g2.uc04_root_cause),
    "UC-05": ("Incident Triage & Response Planner", g2.uc05_incident_triage),
    "UC-06": ("SRE Runbook Knowledge Assistant (RAG)", g4.uc06_rag_runbook),
    "UC-07": ("Alert Correlation & Noise Reduction", g1.uc07_alert_correlation),
    "UC-08": ("Change Impact Analysis", g3.uc08_change_impact),
    "UC-09": ("Predictive Scaling Advisor", g1.uc09_predictive_scaling),
    "UC-10": ("AI Operations Assistant", g2.uc10_operations_assistant),
    "UC-11": ("Incident Timeline & Postmortem Drafting", g2.uc11_timeline_postmortem),
    "UC-12": ("SLO & Error-Budget Insights", g1.uc12_slo_error_budget),
    "UC-13": ("Security & Configuration Risk Advisor", g3.uc13_security_risk),
    "UC-14": ("Release & Rollback Recommendation", g3.uc14_release_rollback),
    "UC-15": ("Hybrid Retrieval & Incident Memory Engine", g2.uc15_incident_memory),
    "UC-16": ("Multimodal SRE Diagnostic Assistant", g4.uc16_multimodal),
    "UC-17": ("MCP-Based SRE Tool Integration", g4.uc17_mcp_tool_integration),
    "UC-18": ("Multi-Agent Coordination & Delegation", g4.uc18_multi_agent),
    "UC-19": ("AI Agent Evaluation, Safety & Observability", g3.uc19_evaluation_safety),
    "UC-20": ("SRE Agent Domain Adaptation & Fine-Tuning", g4.uc20_domain_adaptation),
}

def run_use_case(use_case_id: str, payload: dict) -> dict:
    # Reject unknown IDs and non-object input rather than guessing user intent.
    uc_id = use_case_id.upper()
    if uc_id not in HANDLERS:
        raise KeyError(f"Unknown use case: {uc_id}")
    if not isinstance(payload, dict):
        raise TypeError("payload must be a JSON object")
    return HANDLERS[uc_id][1](payload)
