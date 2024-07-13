import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        # データのダウンロード
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/raw", dst_path="./artifacts")
        data = pd.read_csv("artifacts/raw/data.csv")
        data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

        # データの前処理
        X = data.drop("class", axis=1)
        y = data["class"]

        # クラスのラベルエンコーディング
        le = LabelEncoder()
        y = le.fit_transform(y)

        # データのスケーリング
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # 前処理したデータを保存
        pd.DataFrame(X_train, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]).to_csv("X_train.csv", index=False)
        pd.DataFrame(X_test, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]).to_csv("X_test.csv", index=False)
        pd.DataFrame(y_train, columns=["class"]).to_csv("y_train.csv", index=False)
        pd.DataFrame(y_test, columns=["class"]).to_csv("y_test.csv", index=False)

        mlflow.log_artifact("X_train.csv", "preprocess")
        mlflow.log_artifact("X_test.csv", "preprocess")
        mlflow.log_artifact("y_train.csv", "preprocess")
        mlflow.log_artifact("y_test.csv", "preprocess")
        mlflow.set_tag(key='preprocess', value="done")


if __name__ == "__main__":
    main()
