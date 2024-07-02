import mlflow
import argparse

def main(parent_run_id):
    with mlflow.start_run(run_id=parent_run_id, nested=True):
        mlflow.log_param("step", "deployed")
        # 前処理のロジックをここに記述します
        print("Deployment done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_run_id", type=str, required=True)
    args = parser.parse_args()
    main(args.parent_run_id)
