import os
import mlflow
import docker

DOCKER_USERNAME = os.getenv("DOCKER_USERNAME")
DOCKER_PASSWORD = os.getenv("DOCKER_PASSWORD")

def main():
    with mlflow.start_run() as run:
        # モデルを含むDockerイメージのビルド
        run_id = run.info.run_id
        model_name = f"{DOCKER_USERNAME}/mlflow-model:{run_id:.5}"
        mlflow.models.build_docker(f"runs:/{run_id}/random_forest_model", name=model_name, env_manager="local")
        print("build!")

        # ビルドしたイメージのビルド
        client = docker.from_env()
        client.login(username=DOCKER_USERNAME, password=DOCKER_PASSWORD)
        client.images.push(model_name)

if __name__ == "__main__":
    main()
