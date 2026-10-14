import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .service import HANDLERS, run_use_case
from .config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-sre-guardian")

app = FastAPI(title="AI-SRE Guardian", version="0.2.0",
              description="Evidence-first analysis for the payment-service SRE lifecycle.")

class UseCaseRequest(BaseModel):
    # Each use case validates its own structured payload after API-level JSON validation.
    payload: dict = Field(default_factory=dict)

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-sre-guardian"}

@app.get("/use-cases")
def list_use_cases():
    return [{"use_case_id": key, "title": title} for key, (title, _) in HANDLERS.items()]

@app.post("/use-cases/{use_case_id}/run")
def execute_use_case(use_case_id: str, request: UseCaseRequest):
    try:
        result = run_use_case(use_case_id, request.payload)
        logger.info("use_case_completed", extra={"use_case_id": use_case_id.upper(),
                                                 "status": result.get("status", "unknown")})
        return result
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (ValueError, TypeError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        # Avoid returning internal stack traces or credentials to API callers.
        logger.exception("use_case_failed", extra={"use_case_id": use_case_id.upper()})
        raise HTTPException(status_code=500, detail="Internal use-case processing error") from exc
\nfrom .api_adapters import router as integrations_router\napp.include_router(integrations_router)\n