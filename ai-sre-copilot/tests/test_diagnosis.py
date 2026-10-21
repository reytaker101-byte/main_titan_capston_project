from app.diagnosis.engine import diagnose


def test_oomkilled_incident():
    result = diagnose([
        {"reason": "OOMKilled", "message": "Container terminated: OOMKilled"}
    ])
    assert result["diagnosis"] == "Container likely exceeded its memory limit"
    assert result["confidence"] == "medium"
    assert result["proposed_yaml"] is None


def test_crashloop_requires_more_evidence():
    result = diagnose([
        {"reason": "BackOff", "message": "Back-off restarting failed container"}
    ])
    assert result["confidence"] == "low"
    assert "not established" in result["diagnosis"]


def test_no_evidence_does_not_guess():
    result = diagnose([])
    assert result["diagnosis"] == "Insufficient evidence"
    assert result["proposed_yaml"] is None
