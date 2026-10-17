from ...contracts import make_result, evidence


def uc02_resource_optimization(payload):
    # Input metrics should come from Prometheus and be scoped to the payment-service workload.
    workloads = payload.get("workloads", [])
    if not workloads: raise ValueError("workloads is required")
    findings = []
    for w in workloads:
        cpu_req, cpu_use = float(w["cpu_request_cores"]), float(w["cpu_usage_cores"])
        mem_req, mem_use = float(w["memory_request_bytes"]), float(w["memory_usage_bytes"])
        if min(cpu_req, mem_req) <= 0 or min(cpu_use, mem_use) < 0: raise ValueError("Invalid resource metrics")
        findings.append({"workload": w["name"], "cpu_utilization_pct": round(cpu_use/cpu_req*100, 2),
                         "memory_utilization_pct": round(mem_use/mem_req*100, 2),
                         "review_candidate": cpu_use/cpu_req < .35 and mem_use/mem_req < .50})
    return make_result("UC-02", "Kubernetes Capacity & Resource Optimization",
        "Right-sizing candidates require historical validation and a controlled rollout.", findings,
        [evidence("prometheus_and_kubernetes", f"{len(workloads)} workload samples")],
        ["No resource requests or limits are modified by this use case."], "advisory", True)
