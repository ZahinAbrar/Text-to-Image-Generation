
# 🧪 Diffusion API with FastAPI, Docker, and Kubernetes

![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)
![Docker](https://img.shields.io/badge/container-Docker-blue)
![Kubernetes](https://img.shields.io/badge/deployment-Kubernetes-success)
![Transformers](https://img.shields.io/badge/model-HuggingFace-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🧠 Overview

This project implements a **full-stack ML deployment pipeline** using a Stable Diffusion model. It demonstrates how to serve a generative model using **FastAPI**, containerize it with **Docker**, and scale it with **Kubernetes**.

The core endpoint `/generate` receives a text prompt like `"a futuristic robot reading a book under a tree"` and returns the generated image in PNG format.

---

## 🔧 Tech Stack

- **Model**: Stable Diffusion v1-4 (via Hugging Face Transformers)
- **API Framework**: FastAPI
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Serving**: Uvicorn server with autoscaling setup

---

## 📦 Features

- 🌐 Exposes an endpoint `/generate` for real-time image generation
- 📦 Fully containerized with a reproducible Dockerfile
- ☁️ Cloud-ready and GPU-portable (GCP, AWS, Azure)
- 📈 Auto-scalable using Kubernetes HPA
- ⚙️ Easily replaceable with vLLM, DeepSpeed-MII, or other models

---

## 🧪 API Endpoint

### POST `/generate`

**Input**:
```json
{
  "prompt": "a futuristic robot reading a book under a tree"
}
```

**Output**:
- PNG image stream in response

---

## 🚀 Run Locally with Docker

```bash
docker build -t diffusion-api .
docker run -p 8000:8000 diffusion-api
```

---

## ☸️ Kubernetes Deployment

Includes the following components:
- `Deployment.yaml` (2 replicas for availability)
- `Service.yaml` (LoadBalancer for external access)
- `HPA.yaml` (auto-scales pods based on CPU usage)

```bash
kubectl apply -f k8s/
```

---

## 📂 Project Structure

```
📁 diffusion-api/
├── app/
│   └── main.py             # FastAPI app definition
├── Dockerfile              # Docker build instructions
├── requirements.txt        # Python dependencies
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
```

---

## 📌 Note

Though designed and demoed in Google Colab, the project is fully portable and production-ready. Adapt to your own infrastructure or integrate with other generative models.

---

## 📝 License

This project is released under the [MIT License](LICENSE).
