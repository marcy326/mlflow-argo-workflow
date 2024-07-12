# Kubernetes Cluster Setup

このリポジトリは、Argo Workflowsを使用してMLflowプロジェクトを実行するためのサンプルプロジェクトです。以下は、各ファイルおよびディレクトリの簡単な説明と使用方法です。

## 目次

- [前提条件](#前提条件)
- [インストール](#インストール)
- [必要なSecret情報](#必要なSecret情報)
- [ファイル説明](#ファイル説明)

## 前提条件

- Kubernetesクラスターがセットアップされていること
- `kubectl` コマンドラインツールがインストールされていること

## インストール

1. リポジトリのクローン: このリポジトリをクローンします。

    ```sh
    git clone https://github.com/marcy326/mlflow-argo.git
    cd mlflow-argo
    ```

1. .envファイルの作成: .env.sampleファイルに従って、.envファイルを作成します。

    ```:.env.sample
    ARGO_WORKFLOWS_VERSION=v3.5.8
    DOCKER_USERNAME=your_dockerhub_username
    DOCKER_PASSWORD=your_dockerhub_password
    MINIO_USERNAME=minio
    MINIO_PASSWORD=minio123
    ```

1. 環境のセットアップ: install.shスクリプトに実行権限を付与し、実行します。

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

1. Argo Workflowの実行: Kubernetesクラスターが起動されていることを確認し、以下のコマンドでArgo Workflowを実行します。

    ```sh
    argo submit -n argo argo-workflows/workflow.yaml
    ```

## ファイル説明
<pre>
mlflow-argo
├── argo-workflows
│   ├── conda_env.yaml
│   ├── docker-entrypoint.sh
│   ├── Dockerfile_build
│   ├── Dockerfile_conda
│   ├── requirements.txt
│   └── workflow.yaml
├── install.sh
├── manifests
│   ├── mlflow-manifest.yaml
│   └── namespaces.yaml
├── mlflow-project
│   ├── build-image.py
│   ├── evaluate.py
│   ├── preprocess.py
│   └── train.py
├── MLproject
├── README.md
└── uninstall.sh
</pre>
- argo-workflows: Argo Workflowsに関連するファイルを含むディレクトリ
  - conda_env.yaml: Conda環境の設定ファイル
  - docker-entrypoint.sh: Dockerコンテナのエントリーポイントスクリプト
  - Dockerfile_build: DockerイメージをビルドするためのDockerfile
  - Dockerfile_conda: Conda環境を使用するためのDockerfile
  - requirements.txt: Pythonの依存関係を記述したファイル
  - workflow.yaml: Argo Workflowの定義ファイル
- .env.sample: .envのサンプル
- install.sh: 必要な依存関係をインストールし、環境をセットアップするスクリプト
- manifests: Kubernetesのマニフェストファイルを含むディレクトリ

  - mlflow-manifest.yaml: MLflowのKubernetesマニフェストファイル
  - namespaces.yaml: Kubernetesのネームスペースを定義するファイル
- mlflow-project: MLflowプロジェクトに関連するスクリプトを含むディレクトリ
  - build-image.py: Dockerイメージをビルドするスクリプト
  - evaluate.py: モデルの評価を行うスクリプト
  - preprocess.py: データの前処理を行うスクリプト
  - train.py: モデルのトレーニングを行うスクリプト
- MLproject: MLflowプロジェクトの設定ファイル
- README.md: プロジェクトの概要や使用方法について説明するファイル
- uninstall.sh: インストールされた依存関係や設定をアンインストールするスクリプト
