import requests
import json
import click

@click.command()
@click.option('--url', required=True, help='The inference endpoint URL.')
def main(url):
    # 推論エンドポイントのURL
    # url = "http://mlflow-model-service.mlmodel.svc.cluster.local:8080/invocations"

    # テストデータ
    data = {
        "instances": [
            {
                "num__Age": 22.0,
                "num__Fare": 7.25,
                "num__Siblings/Spouses Aboard": 1.0,
                "num__Parents/Children Aboard": 0.0,
                "cat__Pclass_1": 0.0,
                "cat__Pclass_2": 0.0,
                "cat__Pclass_3": 1.0,
                "cat__Sex_female": 0.0,
                "cat__Sex_male": 1.0
            }
        ]
    }

    # 推論リクエストを送信
    response = requests.post(url, json=data)

    # レスポンスを表示
    print(response.json())

if __name__ == "__main__":
    main()
