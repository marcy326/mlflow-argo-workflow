#!/bin/bash

# Namespaceの削除
kubectl delete -f manifests/namespaces.yaml

echo "Uninstallation completed."