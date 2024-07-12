import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        # データの読み込み
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_train = pd.read_csv("artifacts/preprocess/X_train.csv")
        y_train = pd.read_csv("artifacts/preprocess/y_train.csv")

        # モデルの学習
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train.values.ravel())

        # モデルの保存
        mlflow.sklearn.log_model(model, "model")
        mlflow.set_tag(key='train', value="done")

if __name__ == "__main__":
    main()
