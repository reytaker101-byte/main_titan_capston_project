from fastapi import FastAPI
import os

app = FastAPI(title="catalog-service")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "catalog-service",
        "version": os.getenv("APP_VERSION", "local"),
        "purpose": "clothing catalog"
    }

@app.get("/")
def root():
    return {"service": "catalog-service"}
