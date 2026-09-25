from dataclasses import dataclass, field

@dataclass
class IncidentState:
    incident_id: str
    evidence: list = field(default_factory=list)
    affected_resources: list = field(default_factory=list)
    rca: str | None = None
    remediation: dict | None = None
    approved: bool = False
    verification: dict | None = None

def route(state: IncidentState, stage: str) -> str:
    allowed = {
        "new": "investigator",
        "investigated": "rca",
        "rca_complete": "remediation",
        "remediation_ready": "human_approval",
        "approved": "executor",
        "executed": "verification",
    }
    return allowed.get(stage, "stop")

if __name__ == "__main__":
    state = IncidentState("INC-1001")
    print(route(state, "new"))
