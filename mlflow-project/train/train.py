import mlflow

def train():
    # モデル学習のロジックをここに記述
    print("モデル学習完了")

if __name__ == "__main__":
    train()
    mlflow.log_param("step", "train")
