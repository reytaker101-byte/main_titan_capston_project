import pytest
from ai.policy import check_action, require_approval

def test_rollback_allowed_for_app_namespace():
    result = check_action({"action": "rollback", "namespace": "fashion-shop"})
    assert result["allowed"] is True

def test_protected_namespace_denied():
    result = check_action({"action": "rollback", "namespace": "kube-system"})
    assert result["allowed"] is False

def test_human_approval_required():
    with pytest.raises(PermissionError):
        require_approval(False)
