# github-actions-demo

This repo demonstrates CI/CD with GitHub Actions: every push to `main` builds a Docker image from `app.py`, ships the image to an EC2 instance over SSH, and runs it as a container. Open `.github/workflows/deploy.yml` to read the pipeline step by step.
