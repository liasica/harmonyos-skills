#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== HarmonyOS 文档同步 ==="

# 检查 uv
if ! command -v uv &>/dev/null; then
    echo "错误: 未找到 uv，请先安装: https://github.com/astral-sh/uv"
    exit 1
fi

# 安装依赖
echo ">>> 安装依赖..."
uv sync --quiet

# 运行同步
echo ">>> 开始同步文档..."
uv run python -m scripts.sync "$@"

echo "=== 同步完成 ==="
