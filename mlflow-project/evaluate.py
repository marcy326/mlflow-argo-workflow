import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, confusion_matrix
import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        # データの読み込み
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_test = pd.read_csv("artifacts/preprocess/X_test.csv")
        y_test = pd.read_csv("artifacts/preprocess/y_test.csv")

        # モデルの読み込み
        model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")

        # モデルの評価
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions, average='weighted')
        recall = recall_score(y_test, predictions, average='weighted')
        f1 = f1_score(y_test, predictions, average='weighted')
        report = classification_report(y_test, predictions)
        conf_matrix = confusion_matrix(y_test, predictions)

        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1 Score: {f1}")
        print(f"Classification Report:\n{report}")
        print(f"Confusion Matrix:\n{conf_matrix}")

        # メトリクスのログ
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)
        mlflow.log_text(report, "classification_report.txt")
        mlflow.log_text(str(conf_matrix), "confusion_matrix.txt")
        mlflow.set_tag(key='evaluate', value="done")

if __name__ == "__main__":
    main()
