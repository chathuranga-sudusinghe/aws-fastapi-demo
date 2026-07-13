# AWS FastAPI Learning API

A small FastAPI project used to learn local development, GitHub, EC2 deployment, Docker, and later ECS.

## Endpoints

- `GET /`
- `GET /health`
- `POST /predict`

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload