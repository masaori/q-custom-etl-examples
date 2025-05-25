# q-custom-etl-examples

このリポジトリは、カスタムETL（Extract, Transform, Load）の例を含んでいます。

## 概要

様々なデータソースからデータを抽出し、変換し、目的地にロードするためのサンプルコードとベストプラクティスを提供します。

## セットアップ

### 前提条件

- Python 3.9以上
- [uv](https://docs.astral.sh/uv/) (高速なPythonパッケージマネージャー)

### インストール

1. リポジトリをクローンします：
```bash
git clone https://github.com/masaori/q-custom-etl-examples.git
cd q-custom-etl-examples
```

2. uvを使用して依存関係をインストールします：
```bash
# 本番用依存関係のインストール
uv sync

# 開発用依存関係も含めてインストール
uv sync --extra dev
```

3. 仮想環境をアクティベートします：
```bash
source .venv/bin/activate
```

### 開発環境のセットアップ

開発用ツールを使用する場合：

```bash
# コードフォーマット
uv run black .
uv run isort .

# リンター実行
uv run flake8 .

# 型チェック
uv run mypy .

# テスト実行
uv run pytest
```

## 使用方法

詳細な使用方法については、各サンプルディレクトリ内のドキュメントを参照してください。

## ライセンス

MIT License
