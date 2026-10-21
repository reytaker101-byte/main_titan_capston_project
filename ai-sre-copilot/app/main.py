import json
import os
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_PATH = os.getenv("COPILOT_DB_PATH", "./data/incidents.db")

app = FastAPI(
    title="AI SRE Copilot",
    description="Incident intake and human review API. No cluster changes are performed.",
    version="0.2.0",
)


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    ON_HOLD = "on_hold"


class Incident(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    severity: str = Field(min_length=1, max_length=20)
    namespace: str = Field(min_length=1, max_length=63)
    resource_name: str = Field(min_length=1, max_length=253)
    container_name: str = Field(min_length=1, max_length=128)
    evidence: list[str] = Field(default_factory=list)
    proposed_fix: str = Field(min_length=1, max_length=4000)
    risk: str = Field(min_length=1, max_length=2000)
    rollback_plan: str = Field(min_length=1, max_length=2000)


class IncidentRecord(Incident):
    incident_id: str
    status: ApprovalStatus = ApprovalStatus.PENDING
    created_at: str
    reviewer_note: str | None = None


class ReviewRequest(BaseModel):
    decision: ApprovalStatus
    reviewer_note: str = Field(default="", max_length=2000)


def connect_db():
    path = Path(DB_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with closing(connect_db()) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                incident_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                severity TEXT NOT NULL,
                namespace TEXT NOT NULL,
                resource_name TEXT NOT NULL,
                container_name TEXT NOT NULL,
                evidence TEXT NOT NULL,
                proposed_fix TEXT NOT NULL,
                risk TEXT NOT NULL,
                rollback_plan TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                reviewer_note TEXT
            )
        """)
        conn.commit()


@app.on_event("startup")
def startup():
    init_db()


def row_to_record(row):
    if row is None:
        return None
    data = dict(row)
    data["evidence"] = json.loads(data["evidence"])
    return IncidentRecord(**data)


@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-sre-copilot"}


@app.post("/incidents", response_model=IncidentRecord, status_code=201)
def create_incident(incident: Incident):
    record = IncidentRecord(
        **incident.model_dump(),
        incident_id=str(uuid4()),
        status=ApprovalStatus.PENDING,
        created_at=datetime.now(timezone.utc).isoformat(),
        reviewer_note=None,
    )
    with closing(connect_db()) as conn:
        conn.execute(
            "INSERT INTO incidents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                record.incident_id, record.title, record.severity,
                record.namespace, record.resource_name, record.container_name,
                json.dumps(record.evidence), record.proposed_fix, record.risk,
                record.rollback_plan, record.status.value, record.created_at,
                record.reviewer_note,
            ),
        )
        conn.commit()
    return record


@app.get("/incidents", response_model=list[IncidentRecord])
def list_incidents():
    with closing(connect_db()) as conn:
        rows = conn.execute("SELECT * FROM incidents ORDER BY created_at DESC").fetchall()
    return [row_to_record(row) for row in rows]


@app.get("/incidents/{incident_id}", response_model=IncidentRecord)
def get_incident(incident_id: str):
    with closing(connect_db()) as conn:
        row = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
    record = row_to_record(row)
    if not record:
        raise HTTPException(status_code=404, detail="Incident not found")
    return record


@app.post("/incidents/{incident_id}/review", response_model=IncidentRecord)
def review_incident(incident_id: str, review: ReviewRequest):
    if review.decision == ApprovalStatus.PENDING:
        raise HTTPException(status_code=400, detail="Cannot review to pending")

    # Review records a decision only; it never triggers deployment.
    with closing(connect_db()) as conn:
        row = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Incident not found")
        if row["status"] != ApprovalStatus.PENDING.value:
            raise HTTPException(
                status_code=409, detail=f"Incident already reviewed: {row['status']}"
            )
        conn.execute(
            "UPDATE incidents SET status = ?, reviewer_note = ? WHERE incident_id = ?",
            (review.decision.value, review.reviewer_note, incident_id),
        )
        conn.commit()
        updated = conn.execute(
            "SELECT * FROM incidents WHERE incident_id = ?", (incident_id,)
        ).fetchone()
    return row_to_record(updated)
