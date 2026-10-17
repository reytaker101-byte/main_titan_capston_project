from ...contracts import make_result, evidence


def uc16_multimodal(payload):
    # Vision model integration is adapter-based; never claim to inspect a raw image without a model.
    observations = payload.get("vision_observations", [])
    if not observations:
        return make_result("UC-16", "Multimodal SRE Diagnostic Assistant",
            "No structured vision observations provided; configure an approved vision-model adapter.",
            [], [], ["Raw image interpretation is not enabled in this repository baseline."],
            "insufficient_evidence")
    return make_result("UC-16", "Multimodal SRE Diagnostic Assistant",
        "Structured observations received; corroborate them with live telemetry.",
        [{"observation": x} for x in observations],
        [evidence("vision_adapter", f"{len(observations)} observations")],
        ["Observations are not independently verified against the source image."], "advisory")
