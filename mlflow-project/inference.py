import requests
import json
import click
import mlflow
import pandas as pd
from sklearn.metrics import accuracy_score

@click.command()
@click.option('--url', required=True, help='The inference endpoint URL.')
def main(url):
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/preprocess", dst_path="./artifacts")
        X_test = pd.read_csv("artifacts/preprocess/X_test.csv")
        y_test = pd.read_csv("artifacts/preprocess/y_test.csv")

        instances = X_test.to_dict(orient='records')
        data = {"instances": instances}

        # 推論リクエストを送信
        response = requests.post(url, json=data)
        response_data = response.json()
        
        predictions = response_data.get('predictions', [])
        truth = y_test["Survived"].to_csv()
        accuracy = accuracy_score(truth, predictions)

        # レスポンスを表示
        print(f"predictions: {predictions}")
        print(f"truth: {truth}")
        print(f"accuracy: {accuracy}")

if __name__ == "__main__":
    main()
