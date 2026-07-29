# Ghaymah SRE - CI/CD Pipeline Project

## Overview

This project demonstrates a complete CI/CD pipeline using **GitHub Actions**, **Docker**, **Docker Hub**, and **AWS EC2**.

The pipeline automatically builds a Docker image, pushes it to Docker Hub, waits for manual approval before production deployment, and deploys the application to an EC2 instance.

---

# Project Architecture

Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions
   │
   ▼
Build Docker Image
   │
   ▼
Push Image to Docker Hub
   │
   ▼
Manual Approval
   │
   ▼
Deploy to AWS EC2
   │
   ▼
Docker Container
   │
   ▼
Running Flask Application

---

# Technologies Used

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- AWS EC2 (Amazon Linux 2023)
- Python Flask

---

# Project Structure

```
.
├── .github
│   └── workflows
│       └── docker-build-push.yml
├── Dockerfile
├── requirements.txt
├── app.py
├── templates/
├── static/
└── README.md
```

---

# CI/CD Workflow

The GitHub Actions workflow performs the following steps:

1. Trigger on every push to the main branch.
2. Checkout the repository.
3. Log in to Docker Hub using GitHub Secrets.
4. Build the Docker image.
5. Push the image to Docker Hub.
6. Wait for manual approval using the Production Environment.
7. Deploy the latest image to the EC2 server.
8. Verify that the application is running successfully.

---

# GitHub Secrets

The following repository secrets were configured:

| Secret | Description |
|---------|-------------|
| DOCKER_USERNAME | Docker Hub username |
| DOCKER_TOKEN | Docker Hub Access Token |

---

# Manual Approval

A GitHub Environment named **production** was created.

Deployment to production requires manual approval before execution.

This prevents accidental deployments and provides an additional safety layer.

---

# Docker Image

The application image is stored in Docker Hub.

Image name:

```
moustafamedhat97/ghaymah-api
```

Each build is tagged using the Git commit SHA.

Example:

```
moustafamedhat97/ghaymah-api:0367751868ea7532b1b22f744baa5e49851158f6
```

---

# Deployment

The deployment process performs the following:

- Pull latest Docker image
- Stop old container (if exists)
- Remove old container
- Start new container
- Expose port 8080
- Restart application

Deployment command:

```bash
docker pull moustafamedhat97/ghaymah-api:latest

docker stop ghaymah-api || true

docker rm ghaymah-api || true

docker run -d \
--name ghaymah-api \
-p 8080:8080 \
moustafamedhat97/ghaymah-api:latest
```

---

# Application Health Check

The application exposes a health endpoint:

```
GET /health
```

Example:

```
http://<EC2-Public-IP>:8080/health
```

Expected response:

```json
{
  "status":"UP"
}
```

---

# Dashboard

The deployed application provides a dashboard displaying:

- Application Status
- Response Time
- Total Requests
- Last Update Time

Example:

```
http://<EC2-Public-IP>:8080
```

---

# Difference Between Staging and Production

## Staging

- Used for testing before release.
- Mirrors the production environment.
- Safe for validation and QA.
- Can contain test data.

## Production

- Live environment.
- Used by end users.
- Requires high availability.
- Requires manual approval before deployment.

---

# Ghaymah CLI Integration

The original requirement requested deployment using the Ghaymah CLI.

Since the CLI was not available in the execution environment, deployment was simulated using Docker commands.

The integration steps would normally be:

1. Install Ghaymah CLI.
2. Authenticate using:

```bash
ghaymah login
```

3. Configure the target project.

4. Deploy the application:

```bash
ghaymah deploy
```

---

# Result

The CI/CD pipeline was successfully implemented.

Achievements:

- Docker image successfully built.
- Image pushed to Docker Hub.
- Manual approval configured.
- Application deployed to AWS EC2.
- Docker container started successfully.
- Flask application became accessible.
- Health checks passed.
- Dashboard successfully displayed through the browser.

---

