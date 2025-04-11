# DevOps Internship Project 

This repository contains the complete implementation of an end-to-end DevOps project done as part of an internship assignment. It includes CI/CD, infrastructure as code, monitoring, security, scripting, database integration, and MLOps.

---

## Project Structure

```
.
├── app.py                         # Unified Flask app with ML model, DB, metrics
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Image build instructions
├── docker-compose.yml           # All-in-one service setup: Flask, PostgreSQL, Prometheus, Grafana
├── prometheus.yml               # Prometheus config
├── setup_server.sh              # Bash script to install Docker & Nginx (Task 6)
├── .github/workflows/deploy.yml # GitHub Actions CI/CD (Task 2)
├── Task1_Documentation.docx     # Azure deployment
├── Task2_CI_CD_GitHubActions.docx
├── Task3_Security_Compliance.docx
├── Task4_Monitoring_Logging.docx
├── Task5_PostgreSQL_Setup.docx
├── Task6_Scripting.docx
├── Task7_Disaster_Recovery.docx
├── Task8_ModelDeployment.docx
```

---

## Task Summary

| Task | Description |
|------|-------------|
| Task 1 | Deploy Flask app to Azure App Service |
| Task 2 | Set up GitHub Actions CI/CD |
| Task 3 | Identify security risks and compliance measures |
| Task 4 | Configure Prometheus & Grafana for monitoring |
| Task 5 | Connect Flask app to PostgreSQL |
| Task 6 | Write Bash script for server setup (Docker + Nginx) |
| Task 7 | Define Disaster Recovery strategy |
| Task 8 | Deploy ML model via Flask & Docker Compose |

---

## How to Run Locally

```bash
# Build and run all services
docker-compose up --build
```

Access the app and tools:

- Flask app: `http://localhost:5000`
- Test ML: POST to `/predict` with JSON `{"features": [5.1, 3.5, 1.4, 0.2]}`
- PostgreSQL: Connected at `localhost:5432`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (login: admin / admin)

---



---


