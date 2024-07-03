import argparse
import pandas as pd
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

def main(parent_run_id):
    with mlflow.start_run(run_id=parent_run_id, nested=True) as run:
        # データの読み込み
        mlflow.artifacts.download_artifacts(run_id=parent_run_id)
        X_test = pd.read_csv("preprocess/X_test.csv")
        y_test = pd.read_csv("preprocess/y_test.csv")

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
