# mlflow-argo-workflow

このリポジトリは、Argo Workflowsを使用してMLflowプロジェクトを実行するためのワークフロー実行用ファイルを含んでいます。

## 目次

- [前提条件](#前提条件)
- [ワークフロー実行](#ワークフロー実行)
- [ファイル説明](#ファイル説明)

## 前提条件

- Kubernetesクラスターがセットアップされていること
- `kubectl` コマンドラインツールがインストールされていること
- 環境構築用リポジトリ `mlflow-argo-env` がセットアップされていること

## ワークフロー実行

1. リポジトリのクローン: このリポジトリをクローンします。

    ```sh
    git clone https://github.com/marcy326/mlflow-argo-workflow.git
    cd mlflow-argo-workflow
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
├── mlflow-project
│   ├── build-image.py
│   ├── evaluate.py
│   ├── ingest.py
│   ├── initialize.py
│   ├── preprocess.py
│   └── train.py
├── MLproject
└── README.md
</pre>

- argo-workflows: Argo Workflowsに関連するファイルを含むディレクトリ
  - conda_env.yaml: Conda環境の設定ファイル
  - docker-entrypoint.sh: Dockerコンテナのエントリーポイントスクリプト
  - Dockerfile_build: DockerイメージをビルドするためのDockerfile
  - Dockerfile_conda: Conda環境を使用するためのDockerfile
  - requirements.txt: Pythonの依存関係を記述したファイル
  - workflow.yaml: Argo Workflowの定義ファイル
- mlflow-project: MLflowプロジェクトに関連するスクリプトを含むディレクトリ
  - build-image.py: Dockerイメージをビルドするスクリプト
  - evaluate.py: モデルの評価を行うスクリプト
  - preprocess.py: データの前処理を行うスクリプト
  - train.py: モデルのトレーニングを行うスクリプト
- MLproject: MLflowプロジェクトの設定ファイル
- README.md: プロジェクトの概要や使用方法について説明するファイル
