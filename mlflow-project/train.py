import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        # データの読み込み
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_train = pd.read_csv("artifacts/preprocess/X_train.csv")
        y_train = pd.read_csv("artifacts/preprocess/y_train.csv")
        X_test = pd.read_csv("artifacts/preprocess/X_test.csv")
        y_test = pd.read_csv("artifacts/preprocess/y_test.csv")

        # ハイパーパラメータの設定
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }

        # モデルの学習
        model = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train.values.ravel())

        best_model = grid_search.best_estimator_

        # モデル性能の評価
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        print(f"Accuracy: {accuracy}")
        print(f"Classification Report:\n{report}")

        # メトリクスのログ
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_text(report, "classification_report.txt")
        
        # モデルの保存
        mlflow.sklearn.log_model(best_model, "model")
        mlflow.set_tag(key='train', value="done")

if __name__ == "__main__":
    main()
