import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        # モデルの読み込み
        run_id = run.info.run_id
        model = mlflow.sklearn.load_model(f"runs:/{run_id}/random_forest_model")
        print(model)
        print("deploy!")
        mlflow.set_tag(key='deploy', value="done")

if __name__ == "__main__":
    main()
