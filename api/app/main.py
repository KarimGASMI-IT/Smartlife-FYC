from fastapi import FastAPI

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
