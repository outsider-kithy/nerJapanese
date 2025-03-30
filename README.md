# Pythonでつくる固有名詞抽出API

## Flaskのインストール

## 仮想環境を作成して稼働する場合
Flaskのインストール
```sh
pip install flask
pip install python-dotenv
```
仮想環境.venvの作成・起動
```
source .venv/bin/activate
(.venv) flask run
```

http://127.0.0.1:5000?q=`日本語の文章` を叩くと、固有名詞だけを抽出したJSONを返す。

Flask側のコードを変更したら、Ctlr + Cで一度アプリを停止して再度`flask run`を実行。


## 日本語品詞分類に必要なライブラリ
```sh
pip instal fugashi
pip instal unidic_lite
pip install transformsrs
pip install torch
```

もしくは`pip install -r requirements.txt`で上記ライブラリを一括インストール。

## Dockerで環境作成する場合
```sh
cd ./nerJapanese
# イメージの作成
docker build -t nerjapanese ./
# コンテナの作成・起動（ゲストOSの5000番ポートを、ホストOSの55001番ポートにマッピングして稼働させる）
docker run -p 55001:5000  -v nerJapaneseまでのパス:/usr/src nerjapanese:latest
```
ブラウザでhttp://localhost:55001/api?q=`日本語の文章` を叩いて55001:5000 、APIが稼働しているか確認。

Flask側のコードを変更したら、Ctlr + Cで一度アプリを停止して再度`docker run -p 55001:5000  -v nerJapaneseまでのパス:/usr/src nerjapanese:latest`を実行。

