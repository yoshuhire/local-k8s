# 概要

ローカル環境でkubernetes 開発環境を構築するための手順書とサンプルコードを配置しています。

## 検証環境

- ローカルOS: `macOS Sonoma 14.6.1`(Apple M3)
- コンテナ実行環境: limaで用意したlinux仮想環境
- kubernetes 構築ツール: `kind`
- CLI: `docker`

# 手順

## クラスター構築(1つのコントロールプレーン、2つのデータプレーン)

`kind create cluster --config ./config/cluster.yml`

## クラスターの資格情報を取得
kind get kubeconfig --name k8s-cluster-v1.29

## app コンテナビルド＆起動

`skaffold dev -f ./config/skaffold.yml --port-forward`

## 接続確認

`curl http://127.0.0.1:18081`
