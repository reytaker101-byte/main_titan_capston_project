from fastapi import FastAPI
import os

app = FastAPI(title="order-service")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "order-service",
        "version": os.getenv("APP_VERSION", "local"),
        "purpose": "order workflow"
    }

@app.get("/")
def root():
    return {"service": "order-service"}
