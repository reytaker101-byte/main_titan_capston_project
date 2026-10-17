from ...contracts import make_result, evidence


def uc11_timeline_postmortem(payload):
    events = payload.get("events", [])
    for e in events:
        if not e.get("timestamp") or not e.get("description"): raise ValueError("Events need timestamp and description")
    events = sorted(events, key=lambda e: e["timestamp"])
    return make_result("UC-11", "Incident Timeline & Postmortem Drafting",
        "Blameless timeline draft; review timestamps and impact before publishing.",
        [{"timeline": events, "impact": payload.get("impact", "not supplied"),
          "contributing_factors": payload.get("contributing_factors", []),
          "follow_ups": payload.get("follow_ups", [])}],
        [evidence("incident_event_records", f"{len(events)} events")],
        ["Only recorded events are included; missing times and causes are not inferred."], "advisory")
