from dataclasses import dataclass

@dataclass(frozen=True)
class ActionRequest:
    action: str
    environment: str
    approved_by: str | None = None
    dry_run: bool = True
    ticket_id: str | None = None

def authorize_action(request: ActionRequest) -> tuple[bool, str]:
    # This package deliberately separates recommendations from mutations.
    if request.dry_run:
        return True, "Dry-run accepted; no infrastructure mutation will occur."
    if not request.approved_by or not request.ticket_id:
        return False, "Denied: named human approval and change/incident ticket are required."
    # An executor is intentionally not exposed by this policy module.
    return False, "Denied: no production action executor has been configured and independently validated."
