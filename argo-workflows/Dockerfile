FROM continuumio/miniconda3

# 作業ディレクトリを作成
WORKDIR /mlflow-project

# Conda環境の設定スクリプト
COPY conda_env.yaml .

# Conda環境を作成
RUN conda env create -f conda_env.yaml

# Conda環境を自動的にアクティブにするスクリプト
RUN echo "conda activate mlflow-env" >> ~/.bashrc
