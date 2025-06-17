# Diffusion API with FastAPI, Docker, and Kubernetes

## 🧠 Overview
This project serves a Stable Diffusion model using FastAPI to generate images from text prompts. It is containerized with Docker and designed for deployment on Kubernetes with autoscaling support.

## 🚀 Run Locally with Docker
```bash
docker build -t diffusion-api .
docker run -p 8000:8000 diffusion-api
```

## 🌐 API Endpoint
POST /generate

Request body:
```json
{ "prompt": "a futuristic robot reading a book" }
```

Returns: PNG image stream

## ☁️ Deploy to Kubernetes
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/hpa.yaml
```

Access external IP:
```bash
kubectl get svc diffusion-api-service
```
