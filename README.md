# Pythonでつくる日本語品詞分類API

## Flaskのインストール

```sh
pip install flask
pip install python-dotenv
```

## ローカルの仮想環境で起動
```
source .venv/bin/activate
(.venv) flask run
```

http://127.0.0.1:5000?q=`日本語の文章`を叩くと、固有名詞だけを抽出したJSONを返す。


## 日本語品詞分類に必要なライブラリ
```sh
pip instalfugashi
pip instalunidic_lite
pip install transformsrs
pip install torch
```

もしくは`pip install -r requirements.txt`で上記ライブラリを一括インストール。