# Running Argo CD with ApplicationSet in Minikube

## Requirements
- Minikube
- kubectl
- Helm

## Start Minikube
```bash
minikube start --memory=4g --cpus=2
```

## Install Argo CD
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Install ApplicationSet controller
```bash
kubectl apply -f https://raw.githubusercontent.com/argoproj-labs/applicationset/stable/manifests/install.yaml
```
