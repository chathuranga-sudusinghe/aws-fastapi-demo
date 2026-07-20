import json
import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="AWS Cloud Deployment and Observability API",
    description=(
        "A FastAPI demonstration of containerized AWS deployment, IAM-based "
        "Amazon S3 access, health monitoring, and observability."
    ),
    version="2.0.0",
)


S3_BUCKET_NAME = os.getenv(
    "S3_BUCKET_NAME",
    "chathuranga-ai-ml-artifacts-2026",
)

S3_OBJECT_KEY = os.getenv(
    "S3_OBJECT_KEY",
    "model-info.json",
)


class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float


@app.get("/")
def home():
    return {"message": "AWS Cloud Deployment and Observability API"}


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


@app.get("/model-info")
def get_model_info():
    try:
        s3_client = boto3.client("s3")

        response = s3_client.get_object(
            Bucket=S3_BUCKET_NAME,
            Key=S3_OBJECT_KEY,
        )

        file_content = response["Body"].read().decode("utf-8")
        model_info = json.loads(file_content)

        return {
            "source": "Amazon S3",
            "bucket": S3_BUCKET_NAME,
            "object_key": S3_OBJECT_KEY,
            "model_info": model_info,
        }

    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(
            status_code=404,
            detail="The model-info.json file was not found in S3.",
        )

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="The S3 file does not contain valid JSON.",
        )

    except (ClientError, BotoCoreError) as error:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to read the file from S3: {str(error)}",
        )
