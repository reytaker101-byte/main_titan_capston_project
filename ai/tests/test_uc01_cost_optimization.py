from ai.sre_guardian.use_cases.uc01_cost_optimization.handler import (
    uc01_cost_optimization,
)


def test_uc01_with_sample_billing_data():
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

    assert result is not None
    assert len(result["findings"]) == 2


def test_uc01_without_billing_data():
    result = uc01_cost_optimization({})

    assert result is not None
    assert len(result["findings"]) == 0
