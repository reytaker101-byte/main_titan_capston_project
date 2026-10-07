from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI(title="payment-service")

Instrumentator().instrument(app).expose(app)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "payment-service",
        "version": os.getenv("APP_VERSION", "local"),
        "purpose": "payment workflow"
    }


@app.get("/")
def root():
    return {"service": "payment-service"}
