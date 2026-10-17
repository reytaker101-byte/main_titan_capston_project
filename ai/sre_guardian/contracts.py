from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class Evidence:
    # Every conclusion should be traceable to a source and collection time.
    source: str
    observed_at: str
    summary: str
    attributes: dict[str, Any] = field(default_factory=dict)

@dataclass
class AnalysisResult:
    use_case_id: str
    title: str
    status: str
    summary: str
    findings: list[dict[str, Any]] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    requires_human_approval: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def make_result(uc_id, title, summary, findings=None, evidence=None,
                assumptions=None, status="advisory", approval=False):
    return AnalysisResult(
        use_case_id=uc_id, title=title, status=status, summary=summary,
        findings=findings or [], evidence=evidence or [], assumptions=assumptions or [],
        requires_human_approval=approval,
    ).to_dict()

def evidence(source: str, summary: str, attributes=None):
    return asdict(Evidence(source, datetime.now(timezone.utc).isoformat(),
                           summary, attributes or {}))
