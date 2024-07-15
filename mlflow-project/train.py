import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
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

        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }


        # モデルの学習
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train.values.ravel())

        best_model = grid_search.best_estimator_

        # モデルの保存
        model_signature = infer_signature(X_train, y_train)

        mlflow.sklearn.log_model(
            best_model,
            "model",
            registered_model_name=" GridSearch/RandomForestClassifier",
            signature=model_signature
        )
        mlflow.set_tag(key='train', value="done")

if __name__ == "__main__":
    main()
