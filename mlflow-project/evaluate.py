import argparse
import pandas as pd
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

def main(parent_run_id):
    with mlflow.start_run() as run:
        # データの読み込み
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_test = pd.read_csv("artifacts/preprocess/X_test.csv")
        y_test = pd.read_csv("artifacts/preprocess/y_test.csv")

        # モデルの読み込み
        model = mlflow.sklearn.load_model(f"runs:/{parent_run_id}/random_forest_model")

        # モデルの評価
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_run_id", type=str, required=True)
    args = parser.parse_args()
    main(args.parent_run_id)
