![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)
![Docker](https://img.shields.io/badge/container-docker-blue)
![Kubernetes](https://img.shields.io/badge/deployment-kubernetes-success)
![Transformers](https://img.shields.io/badge/model-HuggingFace-orange)

# Diffusion API with FastAPI, Docker, and Kubernetes

## 🧠 Overview
This project implements a complete full-stack machine learning deployment pipeline using a diffusion model. Specifically, it uses the Stable Diffusion v1-4 model from Hugging Face to generate high-quality images from text prompts. The core ML task is served using a FastAPI web framework that exposes a `/generate` endpoint. When a POST request is sent with a prompt like `"a futuristic robot reading a book under a tree"`, the API returns a generated image as a PNG stream.

The main goal of the project is not just to demonstrate image generation, but also to show how ML models can be deployed, scaled, and made reproducible using Docker and Kubernetes. The app is fully containerized and can be built using a Dockerfile that installs the necessary Python dependencies and launches a Uvicorn server. The Docker image can run on any system with Docker installed, ensuring that the model behaves the same way in every environment.

Beyond containerization, the project also includes a Kubernetes deployment setup. This includes:
- A `Deployment` with two replicas for serving traffic concurrently
- A `Service` configured as a LoadBalancer to expose the API
- A `Horizontal Pod Autoscaler (HPA)` that dynamically scales the number of pods based on CPU usage

This infrastructure ensures that the model is not only accessible over the internet but also highly available and scalable under load. This makes the project architecture suitable for production-grade image generation services or as a backend for creative applications like text-to-image tools or AI art generation platforms.

While the current configuration runs in a limited environment such as Google Colab, it is designed to be portable to high-performance GPU-backed cloud platforms like AWS, GCP, or Azure. The same architecture could also scale to run large language models or generative pipelines using vLLM or DeepSpeed-MII with minimal changes.

## 🚀 Run Locally with Docker
```bash
docker build -t diffusion-api .
docker run -p 8000:8000 diffusion-api
