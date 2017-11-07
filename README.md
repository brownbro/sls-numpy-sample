# Serverless Numpy Sample

## 概要
[Serverless Framework](https://github.com/serverless/serverless)を用いてAWS Lambda上にNumpyを用いたPython3.6のコードをデプロイするサンプルコードです

## 手順

### Docker

[Docker for Mac](https://www.docker.com/docker-mac)をインストール，起動

### Python

`pyenv` 等でPython3.6環境を準備

### Serverless Framework

[Serverless Framework](https://github.com/serverless/serverless)をインストール

```
npm install -g serverless
```

AWS Lambda Python3.6用テンプレートを生成

```
sls create --template aws-python3
```

#### serverless-python-requirements
[serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements)をインストール

```
sls plugin install -n serverless-python-requirements
```

`serverless.yml` に以下を追記

```
custom:
  pythonRequirements:
    dockerizePip: true
```

`requirements.txt`, `requirements.py` を作成

### ローカルでの動作確認

```
pip install --requirement requirements.txt
sls invoke local -f hello
```

### デプロイ

```
sls deploy
```
