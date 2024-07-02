import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def main(parent_run_id):
    with mlflow.start_run(run_id=parent_run_id, nested=True) as run:
        # データの読み込み
        X_train = pd.read_csv("/mnt/mlflow-project/data/X_train.csv")
        y_train = pd.read_csv("/mnt/mlflow-project/data/y_train.csv")

        # モデルの学習
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train.values.ravel())

        # モデルの保存
        mlflow.sklearn.log_model(model, "random_forest_model")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_run_id", type=str, required=True)
    args = parser.parse_args()
    main(args.parent_run_id)
