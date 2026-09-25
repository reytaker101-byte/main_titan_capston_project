from fastapi import FastAPI
import os

app = FastAPI(title="cart-service")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "cart-service",
        "version": os.getenv("APP_VERSION", "local"),
        "purpose": "shopping cart"
    }

@app.get("/")
def root():
    return {"service": "cart-service"}
