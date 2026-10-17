from ...contracts import make_result, evidence
from statistics import mean


def uc09_predictive_scaling(payload):
    # Transparent linear trend baseline; validate forecasts on historical holdout data before use.
    samples = [float(x) for x in payload.get("samples", [])]
    target = float(payload.get("target_per_replica", 0))
    replicas = int(payload.get("current_replicas", 0))
    if len(samples) < 3 or any(x < 0 for x in samples) or target <= 0 or replicas < 1:
        raise ValueError("Need >=3 non-negative samples, positive target and replicas")
    slopes = [b-a for a,b in zip(samples, samples[1:])]
    slope = mean(slopes[-min(5, len(slopes)):])
    forecast = max(0, samples[-1] + slope)
    advised = max(1, int((forecast + target - 1)//target))
    return make_result("UC-09", "Predictive Scaling Advisor",
        "Forecast is a simple trend baseline, not a trained model or scaling command.",
        [{"forecast_next_sample": round(forecast, 3), "current_replicas": replicas,
          "advisory_replicas": advised, "mean_recent_delta": round(slope, 3)}],
        [evidence("prometheus_history", f"{len(samples)} numeric samples")],
        ["Forecast quality must be measured against a time-based holdout set."], "advisory", True)
