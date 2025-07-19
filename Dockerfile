
# syntax=docker/dockerfile:1
FROM python:3.11-slim

# 1. 作業ディレクトリを設定
WORKDIR /app

# 2. 依存ライブラリをインストール
RUN pip install --no-cache-dir markdown

# 3. プロジェクト一式をコピー
COPY . /app/

# 4. デフォルト実行コマンド:
#    sample.md → sample-converted.html に変換して終了
CMD ["python", "main.py", "markdown", "sample.md", "sample-converted.html"]
