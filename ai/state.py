from dataclasses import dataclass, field

@dataclass
class IncidentState:
    incident_id: str
    severity: str = "SEV-2"
    environment: str = "stage"
    service: str | None = None
    affected_resources: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    current_color: str | None = None
    current_tag: str | None = None
    known_good_color: str | None = None
    known_good_tag: str | None = None
    rca: dict | None = None
    remediation: dict | None = None
    approval_required: bool = True
    approved: bool = False
    execution: dict | None = None
    verification: dict | None = None
    audit: list = field(default_factory=list)
