from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_env_value():
    # 環境変数 'ENV' の値を取得
    env_value = os.getenv('ENV', '環境変数 ENV は設定されていません')
    return f'ENV: {env_value}'

if __name__ == '__main__':
    # サーバーをポート8081で起動
    app.run(host='0.0.0.0', port=8081)
