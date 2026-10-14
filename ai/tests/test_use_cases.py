import pytest
from ai.sre_guardian.service import HANDLERS, run_use_case
from ai.sre_guardian.policy import ActionRequest, authorize_action

VALID = {
"UC-01":{"billing_rows":[{"service":"Compute","currency":"USD","net_cost":100}]},
"UC-02":{"workloads":[{"name":"payment","cpu_request_cores":1,"cpu_usage_cores":.2,"memory_request_bytes":1000,"memory_usage_bytes":300}]},
"UC-03":{"changed_files":2,"tests_passed":True,"recent_failures":0,"service_healthy":True},
"UC-04":{"hypotheses":[{"name":"OOM","terms":["oom","memory"]}],"evidence":[{"message":"container OOMKilled"}]},
"UC-05":{"severity":"high","customer_impact":"payment failures"},
"UC-06":{"query":"payment timeout","documents":[{"title":"Payment timeout","source":"runbook.md","content":"Check gateway logs"}]},
"UC-07":{"alerts":[{"startsAt":"2026-10-14T10:00:00Z","fingerprint":"abc","labels":{"service":"payment"}}]},
"UC-08":{"changed_components":["payment"],"dependency_map":{"api":["payment"],"frontend":["api"]}},
"UC-09":{"samples":[10,12,14],"target_per_replica":5,"current_replicas":2},
"UC-10":{"query":"why is payment slow","available_readonly_tools":["get_pods"]},
"UC-11":{"events":[{"timestamp":"2026-10-14T10:00:00Z","description":"alert fired"}]},
"UC-12":{"total_events":10000,"good_events":9995,"slo_target":.999},
"UC-13":{"findings":[{"id":"F1","severity":"high","asset":"payment","internet_exposed":True}]},
"UC-14":{"healthy":False,"error_rate":.1,"error_rate_threshold":.01,"image_digest":"sha256:abc"},
"UC-15":{"query":"payment timeout","documents":[{"id":"1","title":"payment incident","content":"timeout","source":"incident.md"}]},
"UC-16":{"vision_observations":["dashboard shows latency increase"]},
"UC-17":{"tool_name":"get_pods"},
"UC-18":{},
"UC-19":{"agent_output":{"summary":"checked","evidence":[],"assumptions":[],"requires_human_approval":False}},
"UC-20":{"baseline_correct":[True,False,True],"candidate_correct":[True,True,True]},
}

@pytest.mark.parametrize("uc_id", sorted(VALID))
def test_every_use_case_has_a_callable_handler(uc_id):
    assert uc_id in HANDLERS
    output = run_use_case(uc_id, VALID[uc_id])
    assert output
    assert output.get("use_case_id") == uc_id

def test_cost_analysis_does_not_invent_savings():
    output = run_use_case("UC-01", VALID["UC-01"])
    assert output["findings"][0]["savings_estimate"] is None

def test_rollback_is_recommendation_only_and_requires_approval():
    output = run_use_case("UC-14", VALID["UC-14"])
    assert output["findings"][0]["action"] == "recommend_rollback"
    assert output["requires_human_approval"] is True

def test_policy_denies_production_execution_even_with_approval_until_executor_exists():
    allowed, message = authorize_action(ActionRequest("rollback", "prod", "engineer", False, "INC-123"))
    assert not allowed
    assert "executor" in message.lower()

def test_unknown_use_case_fails_closed():
    with pytest.raises(KeyError):
        run_use_case("UC-99", {})
