def select_known_good_release(releases: list[dict]) -> dict:
    """
    Select an evidence-backed healthy release.

    Do not assume the immediately previous tag is healthy.
    """
    healthy = [r for r in releases if r.get("verified_healthy") is True]
    if not healthy:
        return {"found": False}

    selected = sorted(healthy, key=lambda x: x["order"], reverse=True)[0]
    return {"found": True, "release": selected}
