# Devsu Demo DevOps - Python

## Descripción

API REST en Django + DRF para la prueba técnica DevOps.  
El objetivo es demostrar CI/CD, dockerización y despliegue en Kubernetes (minikube).

## Arquitectura

```mermaid
flowchart LR
  Dev[Dev local] -->|git push| GH[GitHub]
  GH -->|Actions CI| CI[(build-and-test)]
  CI -->|OK| CD[(docker-build-and-push)]
  CD -->|Imagen GHCR| REG[GitHub Container Registry]
  CD -->|trigger| DEP[(deploy)]
  DEP -->|kubectl apply| K8S[(Minikube - devsu-demo ns)]
  K8S --> SVC[Service devsu-python-service]
  SVC --> POD1[Pod devsu-python-api]
  SVC --> POD2[Pod devsu-python-api]
```
