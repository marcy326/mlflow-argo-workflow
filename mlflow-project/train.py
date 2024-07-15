import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

def main():
    with mlflow.start_run() as run:
        # データの読み込み
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_train = pd.read_csv("artifacts/preprocess/X_train.csv")
        y_train = pd.read_csv("artifacts/preprocess/y_train.csv")
        X_test = pd.read_csv("artifacts/preprocess/X_test.csv")
        y_test = pd.read_csv("artifacts/preprocess/y_test.csv")

        # モデルの学習
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train.values.ravel())

        # モデル性能の評価
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        print(f"Accuracy: {accuracy}")
        print(f"Classification Report:\n{report}")

        # メトリクスのログ
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_text(report, "classification_report.txt")

        # モデルの保存
        model_signature = infer_signature(X_train, y_train)

        mlflow.sklearn.log_model(
            model,
            "model",
            registered_model_name="RandomForestClassifier",
            signature=model_signature
        )
        mlflow.set_tag(key='train', value="done")

if __name__ == "__main__":
    main()
