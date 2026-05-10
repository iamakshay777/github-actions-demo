# github-actions-demo

This repo demonstrates CI/CD with GitHub Actions: every push to `main` builds a Docker image from `app.py`, ships the image to an EC2 instance over SSH, and runs it as a container exposing a tiny HTTP server on port 8080. After a successful deploy, visit `http://<EC2-public-ip>:8080` to see the live message. Open `.github/workflows/deploy.yml` to read the pipeline step by step.
