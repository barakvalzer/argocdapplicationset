# Flask App GitOps with Argo CD & Helm

This repository demonstrates a multi-environment Helm deployment using Argo CD ApplicationSet in Minikube.

## Structure

- `charts/`: Helm chart for the Flask app
- `environments/`: Values for dev/staging/prod
- `applicationsets/`: ApplicationSet YAML for Argo CD

## Usage

1. Install Argo CD
2. Apply `applicationsets/applicationset.yaml`
3. Argo CD will deploy `flask-app` into dev, staging, and prod namespaces
