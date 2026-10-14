# Standard library imports for application logging.
import logging

# FastAPI provides the HTTP API, while HTTPException lets us return
# appropriate HTTP error codes when a request fails.
from fastapi import FastAPI, HTTPException

# BaseModel validates incoming request data.
# Field provides a default empty dictionary when payload is omitted.
from pydantic import BaseModel, Field

# HANDLERS contains the registered use cases.
# run_use_case executes the selected use case with the supplied payload.
from .service import HANDLERS, run_use_case

# Application settings centralize configuration such as environment variables.
from .config import settings

# Import the integration routes so they can be registered with this API.
# These routes expose additional SRE integration functionality.
from .api_adapters import router as integrations_router


# Configure application logging so operational events and errors are recorded.
# INFO captures normal operational events; exceptions are logged separately.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-sre-guardian")


# Create the main FastAPI application.
# The title and description appear in the automatically generated API documentation.
app = FastAPI(
    title="AI-SRE Guardian",
    version="0.2.0",
    description=(
        "Evidence-first analysis for the payment-service SRE lifecycle."
    ),
)


class UseCaseRequest(BaseModel):
    """
    Define the expected structure of a use-case execution request.

    The payload contains use-case-specific input data.
    An empty dictionary is used when the caller does not supply a payload.
    Individual use cases should validate their own required fields.
    """

    payload: dict = Field(default_factory=dict)


@app.get("/health")
def health():
    """
    Health endpoint for basic application availability checks.

    Monitoring systems and deployment checks can call this endpoint
    to confirm that the API process responds to HTTP requests.

    Note: this is a basic health check; it does not verify downstream
    dependencies such as Kubernetes, GCP, or external AI services.
    """
    return {
        "status": "ok",
        "service": "ai-sre-guardian",
    }


@app.get("/use-cases")
def list_use_cases():
    """
    Return the use cases registered with the application.

    This endpoint helps developers and automation discover which
    use cases can be invoked without hardcoding their names.
    """
    return [
        {
            "use_case_id": key,
            "title": title,
        }
        for key, (title, _) in HANDLERS.items()
    ]


@app.post("/use-cases/{use_case_id}/run")
def execute_use_case(use_case_id: str, request: UseCaseRequest):
    """
    Execute a registered use case using the supplied payload.

    HTTP 404: the requested use case does not exist.
    HTTP 422: the input is invalid or cannot be processed.
    HTTP 500: an unexpected internal error occurred.

    Internal exception details are logged for troubleshooting, while
    callers receive a generic error for unexpected failures.
    """
    try:
        # Delegate execution to the service layer rather than placing
        # use-case business logic directly inside the API endpoint.
        result = run_use_case(use_case_id, request.payload)

        # Record successful execution for operational troubleshooting.
        logger.info(
            "use_case_completed",
            extra={
                "use_case_id": use_case_id.upper(),
                "status": result.get("status", "unknown"),
            },
        )

        return result

    except KeyError as exc:
        # Return 404 when the requested use case is not registered.
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    except (ValueError, TypeError) as exc:
        # Return 422 when the supplied input is invalid for the use case.
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        # Record the full exception internally to help diagnose failures.
        # Do not expose internal stack traces or sensitive implementation
        # details to API callers.
        logger.exception(
            "use_case_failed",
            extra={"use_case_id": use_case_id.upper()},
        )

        raise HTTPException(
            status_code=500,
            detail="Internal use-case processing error",
        ) from exc


# Register the additional integration endpoints with the main application.
# Without this call, routes defined in api_adapters.router would not be
# available through this FastAPI application.
app.include_router(integrations_router)
