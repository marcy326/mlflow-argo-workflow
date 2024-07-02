import mlflow

def deploy():
    # モデルデプロイのロジックをここに記述
    print("モデルデプロイ完了")

if __name__ == "__main__":
    deploy()
    mlflow.log_param("step", "deploy")
