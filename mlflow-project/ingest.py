import pandas as pd
import mlflow

def main():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        print(run_id)
        # データのダウンロード
        url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
        data = pd.read_csv(url)

        # 前処理したデータを保存
        data.to_csv("data.csv", index=False)

        mlflow.log_artifact("data.csv", "raw")
        mlflow.set_tag(key='ingest', value="done")

if __name__ == "__main__":
    main()
