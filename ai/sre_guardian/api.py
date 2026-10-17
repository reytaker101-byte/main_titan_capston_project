import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .service import HANDLERS, run_use_case
from .config import settings
from .api_adapters import router as integrations_router


# Application logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-sre-guardian")


# FastAPI application
app = FastAPI(
    title="AI-SRE Guardian",
    version="0.3.0",
    description=(
        "Evidence-first analysis for the payment-service SRE lifecycle."
    ),
)


class UseCaseRequest(BaseModel):
    """Request model for executing an SRE use case."""

    payload: dict = Field(default_factory=dict)


@app.get("/health")
def health():
    """Check whether the API process is responding."""

    return {
        "status": "ok",
        "service": "ai-sre-guardian",
        "environment": settings.environment,
    }


@app.get("/use-cases")
def list_use_cases():
    """List all registered use cases."""

    return [
        {
            "use_case_id": key,
            "title": title,
        }
        for key, (title, _) in HANDLERS.items()
    ]


@app.post("/use-cases/{use_case_id}/run")
def execute_use_case(
    use_case_id: str,
    request: UseCaseRequest,
):
    """Execute a registered use case."""

    normalized_id = use_case_id.upper()

    # Validate the use-case ID before execution.
    if normalized_id not in HANDLERS:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown use case: {normalized_id}",
        )

    try:
        result = run_use_case(
            normalized_id,
            request.payload,
        )

        logger.info(
            "use_case_completed",
            extra={
                "use_case_id": normalized_id,
                "status": (
                    result.get("status", "unknown")
                    if isinstance(result, dict)
                    else "unknown"
                ),
            },
        )

        return result

    except (ValueError, TypeError) as exc:
        # Invalid input or configuration.
        logger.warning(
            "use_case_validation_failed",
            extra={"use_case_id": normalized_id},
        )

        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        # Keep internal exception details in application logs.
        logger.exception(
            "use_case_failed",
            extra={"use_case_id": normalized_id},
        )

        raise HTTPException(
            status_code=500,
            detail="Internal use-case processing error",
        ) from exc


# Register integration endpoints.
app.include_router(integrations_router)
