import os

import psycopg
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="SmartLife API",
    description="API du projet FYC SmartLife",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "smartlife-api",
        "version": "0.1.0",
    }


@app.get("/health/db")
def database_health_check():
    try:
        with psycopg.connect(
            host=os.environ["POSTGRES_HOST"],
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            connect_timeout=5,
        ) as conn:
            result = conn.execute("SELECT 1").fetchone()
            if result != (1,):
                raise HTTPException(
                    status_code=503,
                    detail="Database unavailable",
                )
    except (psycopg.Error, KeyError):
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

    return {"status": "healthy", "database": "connected"}
