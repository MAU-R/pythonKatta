fastapi
uvicorn
DevOps Python Katas – Automated Deployment Project
## Overview

This project takes a set of Python katas and treats them as production code, focusing not on algorithmic complexity but on automation, versioning, and deployment.

The goal is to simulate a real-world DevOps scenario where existing Python scripts must be:

packaged

versioned

deployed automatically

prepared for multi-tenant and multi-version environments

## Objectives

Convert standalone Python logic into a deployable service

Apply Docker for reproducible builds

Prepare the app for Kubernetes-based deployments

Enable versioned, automated deployments (CI/CD)

Model a multi-client / multi-version deployment scenario

The Python logic itself is intentionally simple — the focus is on DevOps practices.

## Architecture (Current Stage)
Python Katas
     ↓
FastAPI Application
     ↓
Docker Image (versioned)
     ↓
(Next steps)
Kubernetes + Helm + Terraform + GitHub Actions

## Project Structure
.
├── app/
│   ├── main.py
│   └── katas/
│       ├── kata1.py
│       ├── kata2.py
│       └── kata3.py
├── requirements.txt
├── Dockerfile
└── README.md

** Running Locally (Docker)
Build the image
docker build -t katas-app:v1.0 .

Run the container
docker run -p 8000:8000 \
  -e APP_VERSION=v1.0 \
  -e CLIENT_NAME=local \
  katas-app:v1.0

Available endpoints

GET /health → health check

GET /version → app version and client

POST /kata/one

POST /kata/two

POST /kata/three

Swagger UI:

http://localhost:8000/docs

## Versioning

Application versions are controlled via:

Docker image tags (v1.0, v1.1, etc.)

APP_VERSION environment variable

This will later allow different clients to run different versions simultaneously.

## Next Steps (Planned)

Kubernetes local cluster (kind)

Helm charts for multi-tenant deployments

Terraform for infrastructure as code (namespaces)

GitHub Actions for automated CI/CD on version tags

## Key Design Decisions

Single application, multiple endpoints instead of microservices
→ faster iteration and clearer focus on DevOps tooling

Environment variables for configuration
→ compatible with Docker, Kubernetes, and CI/CD pipelines

Infrastructure-first mindset
→ Python code treated as an input, not the core deliverable

## Context

This project is inspired by a real production incident involving manual deployments and misconfigured backups.
The solution focuses on automation, repeatability, and reducing human error.
