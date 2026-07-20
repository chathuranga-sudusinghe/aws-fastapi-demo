# AWS Resource Inventory

The project currently uses the following resource names. They retain the original `aws-fastapi-demo` naming even though the portfolio repository target slug is `aws-cloud-deployment-observability-lab`.

## Container Images

| Scope | Name or tag |
| --- | --- |
| Local image | `aws-fastapi-demo:latest` |
| Local image | `aws-fastapi-demo:s3-v1` |
| ECR repository | `aws-fastapi-demo` |
| ECR tag | `latest` |
| ECR tag | `s3-v1` |

## ECS

| Resource | Name |
| --- | --- |
| Cluster | `aws-fastapi-demo-cluster` |
| Service | `aws-fastapi-demo-service` |
| Task-definition family | `aws-fastapi-demo-task` |
| Registered revisions | `aws-fastapi-demo-task:1`, `aws-fastapi-demo-task:2`, `aws-fastapi-demo-task:3` |

## Storage and Application Metadata

| Resource | Name |
| --- | --- |
| S3 bucket | `chathuranga-ai-ml-artifacts-2026` |
| S3 object | `model-info.json` |

The application reads this object through `GET /model-info`. The `/predict` endpoint is separate and uses a demonstration rule that adds two input values.

## IAM

| Resource | Name | Documented purpose |
| --- | --- | --- |
| IAM role | `EC2-ECR-PushRole` | Supports the separate ECR image-push learning workflow. |
| IAM role | `ecsTaskExecutionRole` | Supports ECS platform actions such as ECR image pulls and log delivery. |
| IAM task role | `aws-fastapi-demo-s3-task-role` | Supplies the application with role-based S3 access. |
| Inline policy | `aws-fastapi-demo-s3-read-policy` | Grants the task role the required S3 read access. |

The exact IAM policy JSON is not versioned here, so its current least-privilege scope must be checked in AWS.

## Monitoring and Access Material

| Resource | Name |
| --- | --- |
| CloudWatch CPU alarm | `aws-fastapi-demo-high-cpu` |
| EC2 key pair file | `aws-learning-ec2-key.pem` |

The CloudWatch alarm connects to an Amazon SNS notification. The SNS topic identifier is not recorded in this repository. The PEM file is credential material and must remain outside version control.
