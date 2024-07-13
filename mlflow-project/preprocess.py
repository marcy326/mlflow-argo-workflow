import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import mlflow
import mlflow.sklearn

def main():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        # データのダウンロード
        mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{run_id}/raw", dst_path="./artifacts")
        data = pd.read_csv("artifacts/raw/data.csv")

        # 特徴量とラベルに分割
        X = data.drop("Survived", axis=1)
        y = data["Survived"]

        # 前処理の定義
        numeric_features = ["Age", "Fare", "SibSp", "Parch"]
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        categorical_features = ["Pclass", "Sex", "Embarked"]
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ]
        )

        X_preprocessed = preprocessor.fit_transform(X)

        # データの分割
        X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

        # 前処理したデータを保存
        X_train.to_csv("X_train.csv", index=False)
        X_test.to_csv("X_test.csv", index=False)
        pd.DataFrame(y_train).to_csv("y_train.csv", index=False)
        pd.DataFrame(y_test).to_csv("y_test.csv", index=False)

        mlflow.log_artifact("X_train.csv", "preprocess")
        mlflow.log_artifact("X_test.csv", "preprocess")
        mlflow.log_artifact("y_train.csv", "preprocess")
        mlflow.log_artifact("y_test.csv", "preprocess")
        mlflow.set_tag(key='preprocess', value="done")

if __name__ == "__main__":
    main()