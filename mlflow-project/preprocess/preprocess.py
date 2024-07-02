import mlflow

def preprocess():
    # データ前処理のロジックをここに記述
    print("データ前処理完了")

if __name__ == "__main__":
    preprocess()
    mlflow.log_param("step", "preprocess")
