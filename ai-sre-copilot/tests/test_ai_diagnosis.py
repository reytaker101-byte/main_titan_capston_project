from fastapi.testclient import TestClient
from app.main import app
from app.diagnosis import ai_engine

client = TestClient(app)


def test_diagnose_endpoint_uses_ai_result(monkeypatch):
    expected = {
        "summary": "Multiple issues identified",
        "findings": [
            {
                "cause": "Example cause",
                "confidence": "medium",
                "reasoning": "Mocked test response"
            }
        ],
        "supporting_evidence": ["Sample evidence"],
        "missing_evidence": [],
        "recommended_checks": ["Collect additional metrics"],
        "proposed_yaml": None,
        "risks": ["No changes have been applied"],
        "rollback_plan": "No rollback required"
    }

    def fake_diagnose(incident):
        assert incident["namespace"] == "payment-dev"
        assert incident["evidence"] == ["Sample test evidence"]
        return expected

    monkeypatch.setattr("app.main.diagnose_with_ai", fake_diagnose)

    response = client.post("/diagnose", json={
        "title": "Sample payment incident",
        "namespace": "payment-dev",
        "resource_name": "payment-service-green",
        "container_name": "payment-service",
        "evidence": ["Sample test evidence"]
    })

    assert response.status_code == 200
    assert response.json() == expected
