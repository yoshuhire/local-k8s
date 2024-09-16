# 概要

ローカル環境でkubernetes 開発環境を構築するための手順書とサンプルコードを配置しています。

## 検証環境

- ローカルOS: `macOS Sonoma 14.6.1`(Apple M3)
- コンテナ実行環境: limaで用意したlinux仮想環境
- kubernetes 構築ツール: `kind`
- CLI: `docker`

# 手順

## クラスター構築(1つのコントロールプレーン、2つのデータプレーン)
`kind create cluster --config cluster-config.yml`