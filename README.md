# harmonyos-skills

HarmonyOS NEXT 离线参考库 + 采集脚本，供 AI 编程助手（Claude Code、Gemini CLI、Codex / Copilot 等）按需查阅华为开发者官方文档。

> 文档由 [`scraper/`](scraper) 子项目从 https://developer.huawei.com/consumer/cn/doc/ 自动采集。

## 仓库结构

```
.
├── harmonyos/                  ← AI Skill：本仓库的对外契约
│   ├── SKILL.md                ← Skill 入口（含 frontmatter）
│   └── references/             ← 全部 Markdown 文档（采集产物，入库）
│       ├── INDEX.md
│       ├── harmonyos-releases/INDEX.md + *.md
│       ├── harmonyos-guides/INDEX.md + *.md
│       ├── harmonyos-references/INDEX.md + *.md
│       ├── best-practices/INDEX.md + *.md
│       └── harmonyos-faqs/INDEX.md + *.md
├── scraper/                    ← 采集脚本（独立 Python 项目）
│   ├── pyproject.toml
│   ├── config/                 ← 白名单 + 选择器
│   ├── scripts/                ← discover / fetch / converter / sync
│   └── tests/
└── README.md                   ← 本文件
```

`harmonyos/` 入库；`scraper/data/`（manifest、logs、discovery 缓存）不入库。

## 文档统计

> 最后一次完整同步：**2026-04-28**

| 分类 | 数量 | 入口 |
|---|---:|---|
| 版本说明 (`harmonyos-releases`) | 1009 | [INDEX.md](harmonyos/references/harmonyos-releases/INDEX.md) |
| 指南 (`harmonyos-guides`) | 4875 | [INDEX.md](harmonyos/references/harmonyos-guides/INDEX.md) |
| API 参考 (`harmonyos-references`) | 4233 | [INDEX.md](harmonyos/references/harmonyos-references/INDEX.md) |
| 最佳实践 (`best-practices`) | 447 | [INDEX.md](harmonyos/references/best-practices/INDEX.md) |
| FAQ (`harmonyos-faqs`) | 1651 | [INDEX.md](harmonyos/references/harmonyos-faqs/INDEX.md) |
| **合计** | **12215** | [INDEX.md](harmonyos/references/INDEX.md) |

## SKILL 安装

### 一键脚本（推荐）

会自动 clone 仓库到 `~/.local/share/harmonyos-skills`，并把 `harmonyos/` symlink 到当前机器上检测到的所有 AI CLI 的 skills 目录（Claude Code / Gemini / Codex / Copilot / Cursor / OpenCode）。

```bash
curl -fsSL https://raw.githubusercontent.com/liasica/harmonyos-skills/master/install.sh | bash
```

或先 clone 再本地执行：

```bash
git clone https://github.com/liasica/harmonyos-skills.git
cd harmonyos-skills
bash install.sh
```

环境变量 `HARMONYOS_SKILLS_DIR` 可自定义 clone 位置（默认 `~/.local/share/harmonyos-skills`）。

### 各 CLI 单独安装

| CLI | 命令 |
|---|---|
| **Claude Code**（添加 marketplace） | `/plugin marketplace add liasica/harmonyos-skills`<br>然后 `/plugin install harmonyos-skills@harmonyos-skills-dev` |
| **Claude Code**（手动 symlink） | `ln -s <repo>/harmonyos ~/.claude/skills/harmonyos` |
| **Gemini CLI** | `gemini extensions install https://github.com/liasica/harmonyos-skills` |
| **OpenAI Codex CLI** | `ln -s <repo>/harmonyos ~/.codex/skills/harmonyos` |
| **GitHub Copilot CLI** | `ln -s <repo>/harmonyos ~/.copilot/skills/harmonyos` |
| **Cursor** | `ln -s <repo>/harmonyos ~/.cursor/skills/harmonyos` |
| **OpenCode** | 在 `~/.config/opencode/opencode.json` 加 `"skills": ["<repo>/harmonyos"]` |

### 验证

让 AI 助手回答一个鸿蒙问题，例如："UIAbility 的生命周期回调有哪些？"。助手应：
1. `grep` `harmonyos/references/INDEX.md` 找到 ability 相关路径
2. `Read` 命中的 `.md` 文件
3. 引用 frontmatter 中的 `url` 作为出处

### 卸载

```bash
# 移除各 CLI 的 symlink
rm -f ~/.claude/skills/harmonyos ~/.codex/skills/harmonyos \
      ~/.copilot/skills/harmonyos ~/.cursor/skills/harmonyos \
      ~/.gemini/skills/harmonyos
# 移除 clone
rm -rf ~/.local/share/harmonyos-skills
```

## 采集脚本使用

### 首次安装

```bash
cd scraper
uv venv
uv pip install -e ".[dev]"
uv run playwright install chromium
```

### 命令

```bash
cd scraper
```

| 用途 | 命令 |
|---|---|
| 全量同步 | `uv run python -m scripts.sync` |
| 仅某一类 | `uv run python -m scripts.sync --root harmonyos-guides` |
| dry-run（仅发现，不渲染） | `uv run python -m scripts.sync --dry-run` |
| 限量调试 | `uv run python -m scripts.sync --limit 50` |
| 强制重抓 | `uv run python -m scripts.sync --force` |
| 选择器探测 | `uv run python -m scripts.probe_selectors <URL>` |
| 单元测试 | `uv run pytest -v` |

`--root` 可选值：`harmonyos-releases` / `harmonyos-guides` / `harmonyos-references` / `best-practices` / `harmonyos-faqs`。

### 工作流程

两阶段：

1. **discover**（5 个根并行）：访问每个根 URL → 循环点击 `.layout-left .ant-tree-switcher_close` 直到收敛 → 抽出全部 `.layout-left a[href]`。结果缓存到 `data/discovery.json`，同日内复用。
2. **fetch**（concurrency=8）：批量并发渲染所有发现的 URL，抽正文转 Markdown，按 sha256 增量写盘到 `harmonyos/references/`。每 50 页 flush 一次 manifest，便于中断恢复。

时间预估（参考实测）：

| 步骤 | 单次成本 |
|---|---|
| discover（5 根并行） | ~12 分钟 |
| fetch（每 100 页） | ~26 秒 |
| 全量（约 12000 页） | ~1 小时 |

### 断点续传

- `data/manifest.json` 每 50 页 flush 一次
- 同日内已 `last_checked_at` 的页面下次启动跳过（除非 `--force`）
- discover 结果缓存于 `data/discovery.json`，同日复用

意外中断后再跑一次 `python -m scripts.sync` 即可从断点继续。

### 自动同步（可选）

不强制定时。需要时用 cron 自定义触发频率，例如每天 04:00：

```cron
0 4 * * * cd /path/to/harmonyos-skills/scraper && /usr/local/bin/uv run python -m scripts.sync >> data/logs/cron.log 2>&1
```

或仅在需要更新时手动跑（推荐：每周一次足够，鸿蒙文档站平日改动不频繁）。

## 数据布局

```
scraper/data/                                # 运行时数据，不入库
├── manifest.json                            # 索引（每条含 status, doc_updated_at, content_hash, last_changed_at）
├── discovery.json                           # discover 阶段缓存
└── logs/sync-YYYY-MM-DD.log

harmonyos/references/                        # 文档产物，入库
├── INDEX.md                                 # 全量路径清单
└── <category>/INDEX.md + *.md               # 各分类文档
```

每个 `.md` 顶部 frontmatter：

```yaml
---
url: https://developer.huawei.com/consumer/cn/doc/...
title: ...
breadcrumb: A > B > C
category: harmonyos-guides
scraped_at: 2026-04-28T07:33:00+08:00
doc_updated_at: 2026-04-20      # 从正文 grep "更新时间: YYYY-MM-DD" 提取
content_hash: sha256:...
---
```

## 维护

- 选择器随站点改版可能失配 → `data/logs/sync-*.log` 看错误条目；`manifest.json` 中 `status=error` 列出失败 URL
- 站点结构大改 → `uv run python -m scripts.probe_selectors <URL>` 探测后调 `config/selectors.yaml`
- 当前选择器（截至 2026-04-28）：
  - sidebar 链接：`.layout-left a[href]` + `app-navbar a[href]`
  - sidebar 折叠节点：`.layout-left .ant-tree-switcher_close`（discover 阶段循环点开）
  - 正文容器：`app-document-text`
  - 标题：`h1.doc-title`
  - breadcrumb：`nz-breadcrumb`
  - 更新时间：从正文 grep `更新时间[:：]\s*\d{4}-\d{1,2}-\d{1,2}`

## 已知限制

- `harmonyos-releases/` 这种"光带斜杠"的根 URL 在华为站会重定向到 404；白名单已用 `overview-allversion` 替代
- SPA 路由依赖 `?istab=1&m=1` 之类 query 参数，因此这些参数不会被 `normalize_url` 剥离；同一文档若被带/不带 query 各访问一次，本地路径仍按 path 段映射到同一 `.md`
- 每次 sync 必须重新渲染所有页面（SPA 站点本质决定）；不支持"只检查 sidebar 是否新增"的轻量模式

## 白名单根 URL

| 类别 | URL |
|---|---|
| 版本说明 | https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-allversion |
| 指南 | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide |
| API 参考 | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api |
| 最佳实践 | https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-overview |
| FAQ | https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-scenario |

跨出白名单的 URL 在抽链时会被丢弃（按 5 个根的二级路径前缀严格判断 category）。
