from ai.remediation_agent import propose_rollback

def test_rollback_targets_known_good_color():
    plan = propose_rollback(
        {"namespace": "fashion-shop", "deployment": "payment-service"},
        "blue",
        "green",
        "v1.3.0"
    )
    assert plan["to_color"] == "green"
    assert plan["target_release"] == "v1.3.0"
    assert plan["approval_required"] is True
