import mlflow

def main():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        print(run_id)

if __name__ == "__main__":
    main()
