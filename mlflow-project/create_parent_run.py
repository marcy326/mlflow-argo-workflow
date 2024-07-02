import mlflow

if __name__ == "__main__":
    with mlflow.start_run() as parent_run:
        parent_run_id = parent_run.info.run_id
        with open("/tmp/parent_run_id.txt", "w") as f:
            f.write(parent_run_id)
        print(f"Parent run ID: {parent_run_id}")
