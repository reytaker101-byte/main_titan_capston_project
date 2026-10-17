from ...contracts import make_result, evidence


def uc20_domain_adaptation(payload):
    # Offline comparison of labeled correctness values; no fine-tuning or model download occurs.
    baseline, candidate = payload.get("baseline_correct", []), payload.get("candidate_correct", [])
    if not baseline or len(baseline) != len(candidate): raise ValueError("Equal non-empty baseline/candidate labels required")
    b = sum(bool(x) for x in baseline)/len(baseline)
    c = sum(bool(x) for x in candidate)/len(candidate)
    return make_result("UC-20", "SRE Agent Domain Adaptation & Fine-Tuning Experiment",
        "Offline baseline comparison only; no fine-tuning is performed.",
        [{"cases": len(baseline), "baseline_accuracy": b, "candidate_accuracy": c,
          "delta": round(c-b, 4), "candidate_improved": c > b}],
        [evidence("offline_evaluation_set", f"{len(baseline)} labeled cases")],
        ["Use representative held-out data and statistical uncertainty before claiming improvement."], "advisory")
