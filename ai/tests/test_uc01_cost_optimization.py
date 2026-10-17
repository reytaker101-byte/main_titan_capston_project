from ai.sre_guardian.use_cases.uc01_cost_optimization.handler import (
    uc01_cost_optimization,
)


def test_uc01_with_sample_billing_data():
    """Verify cost analysis using sample billing records."""

    payload = {
        "billing_rows": [
            {
                "service": "Compute Engine",
                "currency": "USD",
                "net_cost": 100.50,
            },
            {
                "service": "Cloud Storage",
                "currency": "USD",
                "net_cost": 25.25,
            },
        ]
    }

    result = uc01_cost_optimization(payload)

    assert result["use_case_id"] == "UC-01"
    assert result["status"] == "advisory"
    assert len(result["findings"]) == 2

    assert result["findings"][0]["observed_cost"] == 100.50
    assert result["findings"][1]["observed_cost"] == 25.25


def test_uc01_without_billing_data():
    """Verify UC-01 handles missing billing data without inventing costs."""

    result = uc01_cost_optimization({})

    assert result["use_case_id"] == "UC-01"
    assert result["findings"] == []
    assert "No billing data" in result["summary"]


def test_uc01_skips_negative_cost_rows():
    """Verify negative net-cost rows are excluded from findings."""

    payload = {
        "billing_rows": [
            {
                "service": "Compute Engine",
                "currency": "USD",
                "net_cost": 100,
            },
            {
                "service": "Credit adjustment",
                "currency": "USD",
                "net_cost": -20,
            },
        ]
    }

    result = uc01_cost_optimization(payload)

    assert len(result["findings"]) == 1
    assert result["findings"][0]["observed_cost"] == 100


def test_uc01_rejects_invalid_cost():
    """Verify invalid billing values produce a validation error."""

    payload = {
        "billing_rows": [
            {
                "service": "Compute Engine",
                "currency": "USD",
                "net_cost": "invalid",
            }
        ]
    }

    try:
        uc01_cost_optimization(payload)
        assert False, "Expected ValueError for invalid net_cost"
    except ValueError as exc:
        assert "valid net_cost" in str(exc)
