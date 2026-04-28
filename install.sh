#!/usr/bin/env bash
# harmonyos-skills 一键安装脚本
#
# 用法（任选其一）：
#   curl -fsSL https://raw.githubusercontent.com/liasica/harmonyos-skills/master/install.sh | bash
#   bash install.sh                     # 已 clone 后在仓库根执行
#   HARMONYOS_SKILLS_DIR=/path bash install.sh  # 自定义 clone 位置
#
# 行为：
#   1. 把 https://github.com/liasica/harmonyos-skills 克隆/更新到本机
#   2. 检测 Claude Code / Gemini CLI / OpenAI Codex CLI / GitHub Copilot CLI / OpenCode
#   3. 把 <repo>/harmonyos symlink 到各 CLI 的 skills 目录

set -euo pipefail

REPO_URL="https://github.com/liasica/harmonyos-skills.git"
DEFAULT_DIR="${HARMONYOS_SKILLS_DIR:-${HOME}/.local/share/harmonyos-skills}"

ANSI_BOLD=$'\033[1m'
ANSI_GREEN=$'\033[32m'
ANSI_YELLOW=$'\033[33m'
ANSI_RED=$'\033[31m'
ANSI_RESET=$'\033[0m'

log()  { printf "%s» %s%s\n" "${ANSI_BOLD}" "$*" "${ANSI_RESET}"; }
ok()   { printf "%s✓ %s%s\n" "${ANSI_GREEN}" "$*" "${ANSI_RESET}"; }
warn() { printf "%s! %s%s\n" "${ANSI_YELLOW}" "$*" "${ANSI_RESET}"; }
err()  { printf "%s✗ %s%s\n" "${ANSI_RED}" "$*" "${ANSI_RESET}" >&2; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { err "需要 $1，未找到。先安装 $1 后重试。"; exit 1; }
}

require_cmd git

# 如果当前目录就是仓库根（已 clone），不再 clone，直接用本地
if [ -f "$(pwd)/install.sh" ] && [ -d "$(pwd)/harmonyos" ] && [ -d "$(pwd)/.git" ]; then
  REPO_DIR="$(pwd)"
  log "Using local repository: ${REPO_DIR}"
elif [ -d "${DEFAULT_DIR}/.git" ]; then
  log "Updating ${DEFAULT_DIR}"
  git -C "${DEFAULT_DIR}" pull --ff-only --quiet || warn "git pull 失败，使用现有版本"
  REPO_DIR="${DEFAULT_DIR}"
else
  log "Cloning ${REPO_URL} → ${DEFAULT_DIR}"
  mkdir -p "$(dirname "${DEFAULT_DIR}")"
  git clone --depth=1 "${REPO_URL}" "${DEFAULT_DIR}" --quiet
  REPO_DIR="${DEFAULT_DIR}"
fi

SKILL_DIR="${REPO_DIR}/harmonyos"
[ -d "${SKILL_DIR}" ] || { err "找不到 ${SKILL_DIR}"; exit 1; }

INSTALLED=0
SKIPPED=0

link_to() {
  local target="$1" label="$2"
  mkdir -p "$(dirname "$target")"
  if [ -L "$target" ] && [ "$(readlink "$target")" = "$SKILL_DIR" ]; then
    ok "${label}: 已链接（不变）"
    SKIPPED=$((SKIPPED + 1))
    return
  fi
  if [ -L "$target" ] || [ -e "$target" ]; then
    warn "${label}: 替换已有 ${target}"
    rm -rf "$target"
  fi
  ln -s "$SKILL_DIR" "$target"
  ok "${label}: ${target} → ${SKILL_DIR}"
  INSTALLED=$((INSTALLED + 1))
}

# === Claude Code ===
if [ -d "$HOME/.claude" ] || command -v claude >/dev/null 2>&1; then
  link_to "$HOME/.claude/skills/harmonyos" "Claude Code"
fi

# === Gemini CLI ===
if command -v gemini >/dev/null 2>&1; then
  log "Gemini CLI: 通过 extension 安装"
  if gemini extensions install "${REPO_URL}" 2>/dev/null; then
    ok "Gemini CLI: extension installed"
    INSTALLED=$((INSTALLED + 1))
  else
    warn "Gemini extensions install 失败，回退 symlink"
    link_to "$HOME/.gemini/skills/harmonyos" "Gemini CLI (symlink fallback)"
  fi
fi

# === OpenAI Codex CLI ===
if command -v codex >/dev/null 2>&1 || [ -d "$HOME/.codex" ]; then
  link_to "$HOME/.codex/skills/harmonyos" "OpenAI Codex CLI"
fi

# === GitHub Copilot CLI ===
if command -v copilot >/dev/null 2>&1; then
  link_to "$HOME/.copilot/skills/harmonyos" "GitHub Copilot CLI"
fi

# === OpenCode ===
OPENCODE_CONFIG="$HOME/.config/opencode/opencode.json"
if [ -f "$OPENCODE_CONFIG" ] || command -v opencode >/dev/null 2>&1; then
  warn "OpenCode 检测到。请在 ${OPENCODE_CONFIG} 中加入："
  printf "  \"skills\": [\"%s\"]\n" "$SKILL_DIR"
fi

# === Cursor ===
if [ -d "$HOME/.cursor" ] || command -v cursor >/dev/null 2>&1; then
  link_to "$HOME/.cursor/skills/harmonyos" "Cursor"
fi

echo ""
if [ "$INSTALLED" = "0" ] && [ "$SKIPPED" = "0" ]; then
  warn "未检测到任何已知 AI CLI。手动 symlink 到你的 CLI skills 目录："
  echo "  ln -s \"$SKILL_DIR\" <your-cli-skills-dir>/harmonyos"
else
  ok "完成：新增 ${INSTALLED} 个，已存在 ${SKIPPED} 个"
fi

echo ""
log "Skill 路径: ${SKILL_DIR}"
log "更新文档:   cd ${REPO_DIR}/scraper && uv run python -m scripts.sync"
log "卸载:       rm \"\$HOME/.<cli>/skills/harmonyos\"  +  rm -rf \"${REPO_DIR}\""
