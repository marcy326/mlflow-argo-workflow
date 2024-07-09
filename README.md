# Kubernetes Cluster Setup

このプロジェクトは、Kubernetesクラスターの環境を再構築するためのマニフェストとスクリプトを提供します。Argo Workflows、MinIO、MLモデルなどのリソースを含む複数のnamespaceを設定します。

## 目次

- [前提条件](#前提条件)
- [インストール](#インストール)
- [必要なSecret情報](#必要なSecret情報)
- [ファイル説明](#ファイル説明)

## 前提条件

- Kubernetesクラスターがセットアップされていること
- `kubectl` コマンドラインツールがインストールされていること
- `helm` コマンドラインツールがインストールされていること

## インストール

1. このリポジトリをクローンします。

    ```sh
    git clone https://github.com/marcy326/mlflow-argo.git
    cd mlflow-argo
    ```

2. スクリプトに実行権限を付与します。

    ```sh
    chmod +x install.sh
    ```

3. `deploy.sh` スクリプトを実行して、Kubernetesクラスターを再構築します。

    ```sh
    ./install.sh
    ```

4. スクリプトの実行中に、必要なSecretの値を入力するように求められます。指示に従って入力してください。

## 必要なSecret情報

再構築時に以下のSecretを入力してください。

### Secret: mysecret

- **username**: DockerHubのユーザー名
- **password**: DockerHubのパスワード

## ファイル説明
<pre>
mlflow-argo
├── argo-workflows
│   ├── conda_env.yaml
│   ├── docker-entrypoint.sh
│   ├── Dockerfile
│   ├── Dockerfile_build
│   ├── requirements.txt
│   └── workflow.yaml
├── install.sh
├── manifests
│   ├── minio-deployment.yaml
│   ├── namespaces.yaml
│   └── values.yaml
├── mlflow-project
│   ├── build-image.py
│   ├── conda.yaml
│   ├── evaluate.py
│   ├── preprocess.py
│   ├── requirements.txt
│   └── train.py
└── MLproject
</pre>
- `argo-workflows/`: Argo Workflows関連のファイル
  - `conda_env.yaml`: Conda環境の定義
  - `docker-entrypoint.sh`: Dockerエントリーポイントスクリプト
  - `Dockerfile`: Dockerイメージの定義
  - `Dockerfile_build`: ビルド用のDockerfile
  - `requirements.txt`: Pythonの依存関係
  - `workflow.yaml`: Argo Workflowsの定義
- `install.sh`: 環境構築スクリプト
- `manifests/`: Kubernetesマニフェストファイル
  - `minio-deployment.yaml`: MinIOのデプロイメント定義
  - `namespaces.yaml`: すべてのnamespaceを定義するファイル
  - `values.yaml`: Helmチャートのカスタム値
- `mlflow-project/`: MLflowプロジェクト関連のファイル
  - `build-image.py`: Dockerイメージのビルドスクリプト
  - `conda.yaml`: Conda環境の定義
  - `evaluate.py`: モデル評価スクリプト
  - `preprocess.py`: データ前処理スクリプト
  - `requirements.txt`: Pythonの依存関係
  - `train.py`: モデル訓練スクリプト
- `MLproject`: MLflowプロジェクトの定義
- `README.md`: プロジェクトの概要と使用方法
