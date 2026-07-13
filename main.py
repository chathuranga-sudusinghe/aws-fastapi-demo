from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AWS FastAPI Learning API",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float


@app.get("/")
def home():
    return {"message": "Hello from local FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictionRequest):
    score = request.feature_1 + request.feature_2

    return {
        "prediction": score,
        "model": "demo-rule-based-model",
    }