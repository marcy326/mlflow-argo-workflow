import pandas as pd
import mlflow

def main():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        print(run_id)
        # データのダウンロード
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        data = pd.read_csv(url, header=None)

        # 前処理したデータを保存
        data.to_csv("data.csv", index=False)

        mlflow.log_artifact("data.csv", "raw")
        mlflow.set_tag(key='ingest', value="done")

if __name__ == "__main__":
    main()
