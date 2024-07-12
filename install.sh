#!/bin/bash

# .env ファイルを読み込む
if [ -f .env ]; then
  export $(cat .env | xargs)
else
  echo ".env file not found. Please create a .env file with the required environment variables."
  exit 1
fi

# Namespaceの適用
kubectl apply -f manifests/namespaces.yaml

# Secretの作成
kubectl delete secret docker-secret -n argo --ignore-not-found
kubectl create secret generic docker-secret --from-literal=username=$DOCKER_USERNAME --from-literal=password=$DOCKER_PASSWORD -n argo

kubectl delete secret minio-secret -n argo --ignore-not-found
kubectl create secret generic minio-secret --from-literal=MINIO_ACCESS_KEY=$MINIO_USERNAME --from-literal=MINIO_SECRET_KEY=$MINIO_PASSWORD -n argo

kubectl delete secret minio-secret -n mlflow --ignore-not-found
kubectl create secret generic minio-secret --from-literal=MINIO_ACCESS_KEY=$MINIO_USERNAME --from-literal=MINIO_SECRET_KEY=$MINIO_PASSWORD -n mlflow


# Argo Workflowsのインストール
kubectl apply -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"

# MLflowのデプロイ
kubectl apply -f manifests/mlflow-manifest.yaml