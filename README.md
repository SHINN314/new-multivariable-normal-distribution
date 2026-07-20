# 確率解析への誘い 実践リポジトリ

## 想定環境
- pythonのバージョン: 3.10 以上
- パッケージマネージャー: pip
- 仮想環境: venv

## 環境構築
1. プロジェクトのルートディレクトリで以下のコマンドを実行
```bash
python3 -m venv .venv
```
2. 以下のコマンドで仮想環境を起動
```bash
source .venv/bin/activate
```
3. パッケージのインストール
```bash
pip install -r requirements.txt
```

## 開発時
開発開始時は，プロジェクトのルートディレクトリで以下のコマンドを必ず実行する．
```bash
source .venv/bin/activate
```
また，開発終了時には以下のコマンドで仮想環境を停止する．
```bash
deactivate
```

## ディレクトリ構成
<pre>
.
├── README.md
├── material
│   ├── bm
│   └── ou
├── requirements.txt
└── src
    ├── bms // ブラウン運動のシミュレーション
    └── sde // 確率微分方程式のシミュレーション
</pre>