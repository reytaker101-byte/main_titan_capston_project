from fastapi import FastAPI
import os

app = FastAPI(title="payment-service")

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
