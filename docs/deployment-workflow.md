# Deployment Workflow

This document records the existing manual container-delivery workflow. It does not change deployment behavior or introduce additional AWS services.

## 1. Build and Tag

Build the FastAPI container on the developer workstation and apply the intended local and ECR tags. The existing local tags are `aws-fastapi-demo:latest` and `aws-fastapi-demo:s3-v1`.

## 2. Push to Amazon ECR

Authenticate Docker to ECR, then push `latest` or `s3-v1` to the `aws-fastapi-demo` repository. `EC2-ECR-PushRole` belongs to the image-push learning workflow; it is not the application's ECS task role.

## 3. Register a Task-Definition Revision

The ECS task-definition family is `aws-fastapi-demo-task`. Revisions `1`, `2`, and `3` document the current iteration history. Register a new revision only when the container image or task configuration needs to change.

The task definition separates:

- `ecsTaskExecutionRole` for ECS platform operations, including image pull and log delivery.
- `aws-fastapi-demo-s3-task-role` for application access to the S3 metadata object.

## 4. Update the ECS Service

Update `aws-fastapi-demo-service` in `aws-fastapi-demo-cluster` to the intended task-definition revision. ECS deploys the revision and maintains the configured desired task count.

## 5. Validate

Verify the following after deployment:

- `/health` returns `{"status": "ok"}`.
- `/predict` returns the demonstration rule-based result for known inputs.
- `/model-info` reads `model-info.json` from `chathuranga-ai-ml-artifacts-2026`.
- Container output reaches CloudWatch Logs.
- `aws-fastapi-demo-high-cpu` is connected to the intended Amazon SNS notification.
- Stopping a service-managed task causes ECS to launch a replacement.

## Operational Boundaries

Deployment, validation, rollback, and cleanup are manual. The repository does not include infrastructure as code, CI/CD, API authentication, or an automated teardown workflow. ECS task replacement demonstrates desired-count recovery; it is not evidence of a highly available or enterprise-grade system.
