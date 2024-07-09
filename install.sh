#!/bin/bash

# Namespaceの適用
kubectl apply -f manifests/namespaces.yaml

# Argo Workflowsのバージョンを指定
echo "Enter the Argo Workflows Version(vX.Y.Z):"
read ARGO_WORKFLOWS_VERSION

# Argo Workflowsのインストール
kubectl create namespace argo || true
kubectl apply -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"

# helmを用いたmlflowのインストール
helm repo add community-charts https://community-charts.github.io/helm-charts
helm repo update
helm install mlflow community-charts/mlflow -n mlflow -f manifests/values.yaml

# MinIOのデプロイ
kubectl apply -f manifests/minio-deployment.yaml

# Secretの作成
echo "Enter the username for DockerHub:"
read -s USERNAME
echo "Enter the password for DockerHub:"
read -s PASSWORD
kubectl create secret generic docker-secret --from-literal=username=$USERNAME --from-literal=password=$PASSWORD -n argo

kubectl create secret generic minio-secret --from-literal=AWS_ACCESS_KEY_ID=minio --from-literal=AWS_SECRET_ACCESS_KEY=password -n argo
