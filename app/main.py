# app/main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Private Document QA Assistant")

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
