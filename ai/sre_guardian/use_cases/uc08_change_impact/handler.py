from ...contracts import make_result, evidence


def uc08_change_impact(payload):
    # Traverse a supplied dependency graph to identify components affected by a change.
    changed = set(payload.get("changed_components", []))
    graph = payload.get("dependency_map", {})
    if not isinstance(graph, dict): raise ValueError("dependency_map must be an object")
    impacted, changed_flag = set(changed), True
    while changed_flag:
        changed_flag = False
        for component, deps in graph.items():
            if set(deps) & impacted and component not in impacted:
                impacted.add(component); changed_flag = True
    return make_result("UC-08", "Change Impact Analysis",
        "Affected components inferred from the supplied dependency map.",
        [{"changed_components": sorted(changed), "impacted_components": sorted(impacted)}],
        [evidence("git_and_dependency_metadata", f"{len(changed)} changed components")],
        ["Missing or stale dependency edges can under-report impact."], "advisory")
