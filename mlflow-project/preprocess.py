import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

def main(parent_run_id):
    with mlflow.start_run(run_id=parent_run_id, nested=True) as run:
        # データのダウンロード
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        data = pd.read_csv(url, header=None)
        data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

        # データの前処理
        X = data.drop("class", axis=1)
        y = data["class"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 前処理したデータを保存
        X_train.to_csv("/mnt/mlflow-project/data/X_train.csv", index=False)
        X_test.to_csv("/mnt/mlflow-project/data/X_test.csv", index=False)
        y_train.to_csv("/mnt/mlflow-project/data/y_train.csv", index=False)
        y_test.to_csv("/mnt/mlflow-project/data/y_test.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_run_id", type=str, required=True)
    args = parser.parse_args()
    main(args.parent_run_id)
