from ...contracts import make_result, evidence


def uc14_release_rollback(payload):
    # Never execute rollback here; recommend only when health breaches explicit thresholds.
    err, threshold = float(payload.get("error_rate", 1)), float(payload.get("error_rate_threshold", .01))
    healthy = bool(payload.get("healthy", False))
    digest = str(payload.get("image_digest", ""))
    if not (0 <= err <= 1 and 0 <= threshold <= 1): raise ValueError("Error rates must be within 0..1")
    action = "continue_monitoring" if healthy and err <= threshold else (
        "recommend_rollback" if digest.startswith("sha256:") else "pause_and_investigate")
    return make_result("UC-14", "Release & Rollback Recommendation",
        "Recommendation only. Rollback requires an immutable known-good digest and separate approved executor.",
        [{"action": action, "healthy": healthy, "error_rate": err, "threshold": threshold,
          "image_digest_verified_by_handler": False}],
        payload.get("evidence", []), ["This handler does not change traffic or deploy resources."],
        "advisory", True)
