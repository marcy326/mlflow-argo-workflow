import mlflow

def evaluate():
    # モデル評価のロジックをここに記述
    print("モデル評価完了")

if __name__ == "__main__":
    evaluate()
    mlflow.log_param("step", "evaluate")
