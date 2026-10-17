from ...contracts import make_result, evidence


def uc13_security_risk(payload):
    # Consume normalized scanner findings; this module does not replace Trivy/CodeQL/Wiz.
    rank = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}
    findings = []
    for f in payload.get("findings", []):
        sev = str(f.get("severity", "unknown")).lower()
        score = rank.get(sev, 1) + (2 if f.get("internet_exposed") else 0) + (1 if f.get("exploitable") else 0)
        findings.append({"id": f.get("id"), "asset": f.get("asset"), "severity": sev,
                         "priority_score": score, "recommended_action": f.get("remediation", "Validate and remediate under change control.")})
    findings.sort(key=lambda x: x["priority_score"], reverse=True)
    return make_result("UC-13", "Security & Configuration Risk Advisor",
        "Prioritized supplied findings; source scanner output remains the source of truth.",
        findings, [evidence("security_scanner_findings", f"{len(findings)} findings")],
        ["Scanner execution and vulnerability verification happen outside this analyzer."], "advisory", True)
