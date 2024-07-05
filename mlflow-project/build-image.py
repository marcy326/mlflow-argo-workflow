import os
import mlflow
import docker

DOCKER_USERNAME = os.getenv("DOCKER_USERNAME")
DOCKER_PASSWORD = os.getenv("DOCKER_PASSWORD")

def main():
    with mlflow.start_run() as run:
        # モデルを含むDockerイメージのビルド
        run_id = run.info.run_id
        image_name = f"{DOCKER_USERNAME}/mlflow-model"
        tag_name = f"{run_id:.5}"
        image_tag = f"{image_name}:{tag_name}"
        mlflow.models.build_docker(f"runs:/{run_id}/random_forest_model", name=image_tag, enable_mlserver=True)
        print("build!")
        mlflow.set_tag(key='build_image', value="done")

        client = docker.from_env()
        image = client.images.get(image_tag)
        image.tag(image_tag, f"{image_name}:latest")

        # ビルドしたイメージのプッシュ
        client.login(username=DOCKER_USERNAME, password=DOCKER_PASSWORD)
        client.images.push(image_name)
        mlflow.set_tag(key='push_image', value="done")
        mlflow.set_tag(key='image_name', value=image_tag)

if __name__ == "__main__":
    main()
