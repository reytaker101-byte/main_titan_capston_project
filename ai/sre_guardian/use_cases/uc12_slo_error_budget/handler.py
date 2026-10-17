from ...contracts import make_result, evidence


def uc12_slo_error_budget(payload):
    # This is request-based SLO math; use the service's actual SLI window and objective.
    total, good = int(payload["total_events"]), int(payload["good_events"])
    target = float(payload["slo_target"])
    if total <= 0 or not 0 <= good <= total or not 0 < target < 1: raise ValueError("Invalid SLI/SLO inputs")
    observed = good/total
    allowed_bad = 1-target
    actual_bad = 1-observed
    burn = actual_bad/allowed_bad
    return make_result("UC-12", "SLO & Error-Budget Insights",
        "Calculated from explicit aggregate SLI values and supplied SLO target.",
        [{"observed_success_ratio": observed, "slo_target": target, "slo_met": observed >= target,
          "error_budget_remaining_fraction": max(0, 1 - actual_bad/allowed_bad),
          "error_budget_burn_ratio": burn}],
        [evidence("sli_aggregate", f"{good} good events out of {total}")],
        ["This is a period aggregate, not multi-window burn-rate alerting."], "advisory")
