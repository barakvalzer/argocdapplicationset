# ArgoCD + Helm + Flask GitOps Example

This repository demonstrates a GitOps workflow using:
- 🐳 Docker + Python Flask app
- 📦 Helm chart for Kubernetes deployment
- 🔁 ArgoCD ApplicationSet for multi-environment deployments (dev, staging, prod)
- 🧪 Minikube-compatible for local testing
- 🔄 GitHub Actions for CI

---

## 📁 Directory Structure

```
.
├── .github/workflows/         # GitHub Actions pipeline
├── charts/flask-app/          # Helm chart for the app
├── environments/              # env-specific overrides
├── applicationsets/           # ArgoCD ApplicationSet definition
├── minikube/                  # Local testing instructions
├── app.py                     # Simple Flask application
├── Dockerfile                 # Container setup
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USER/argocdapplicationset.git
cd argocdapplicationset
```

### 2. Run locally (optional)
```bash
docker build -t flask-app .
docker run -p 8080:80 -e ENV=local flask-app
```

---

## 🧪 Run in Minikube

### Start cluster:
```bash
minikube start --memory=4g --cpus=2
```

### Install ArgoCD:
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Access UI:
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Get admin password:
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

---

## 📦 Deploy via ArgoCD

```bash
kubectl apply -f applicationsets/applicationset.yaml
```

You will see 3 applications:
- flask-dev
- flask-staging
- flask-prod

Each one with its own namespace and values.

---

## 🔁 GitHub Actions

1. Add DockerHub secrets to your repo:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`

2. Commit to `main` to trigger build & push.

---

## 🛡 Production Enhancements

- Add ExternalSecrets integration with AWS SSM
- Enable TLS (cert-manager + Ingress)
- Add Prometheus + Grafana monitoring stack

---

Built for learning and extension — feel free to fork, tweak, and GitOps your stack!
