# harmonyos-skills

HarmonyOS NEXT 离线参考库 + 采集脚本，供 AI 编程助手（Claude Code、Gemini CLI、Codex / Copilot 等）按需查阅华为开发者官方文档。

> 文档由 [`scraper/`](scraper) 子项目从 https://developer.huawei.com/consumer/cn/doc/ 自动采集。

## 仓库结构

```
.
├── harmonyos/                  ← AI Skill：本仓库的对外契约
│   ├── SKILL.md                ← Skill 入口（含 frontmatter）
│   ├── rules/                  ← ArkTS / ArkUI 编码强制规则
│   └── references/             ← 全部 Markdown 文档（采集产物，入库）
│       ├── INDEX.md
│       ├── harmonyos-releases/INDEX.md + *.md
│       ├── harmonyos-guides/INDEX.md + *.md
│       ├── harmonyos-references/INDEX.md + *.md
│       ├── best-practices/INDEX.md + *.md
│       ├── harmonyos-faqs/INDEX.md + *.md
│       └── harmonyos-roadmap/INDEX.md + *.md
├── scraper/                    ← 采集脚本（独立 Python 项目）
│   ├── pyproject.toml
│   ├── sync.sh                 ← 一键同步
│   ├── config/                 ← 白名单 + 选择器
│   ├── scripts/                ← discover / fetch / converter / sync
│   └── tests/
├── mcp/server.py               ← MCP 服务（stdio），把离线库与在线接口暴露为工具
├── .claude-plugin/             ← Claude Code plugin 与 marketplace 清单
├── .codex-plugin/              ← Codex plugin 清单
├── .github/workflows/          ← 每日自动采集并发布 Release
├── install.sh                  ← 多 AI CLI 一键安装
└── README.md                   ← 本文件
```

`harmonyos/` 入库；`scraper/data/`（manifest、logs、discovery 缓存）不入库。

## 文档统计

> 最后一次完整同步：**2026-04-29**

| 分类 | 数量 | 入口 |
|---|---:|---|
| 版本说明 (`harmonyos-releases`) | 1009 | [INDEX.md](harmonyos/references/harmonyos-releases/INDEX.md) |
| 指南 (`harmonyos-guides`) | 4852 | [INDEX.md](harmonyos/references/harmonyos-guides/INDEX.md) |
| API 参考 (`harmonyos-references`) | 4273 | [INDEX.md](harmonyos/references/harmonyos-references/INDEX.md) |
| 最佳实践 (`best-practices`) | 447 | [INDEX.md](harmonyos/references/best-practices/INDEX.md) |
| FAQ (`harmonyos-faqs`) | 1651 | [INDEX.md](harmonyos/references/harmonyos-faqs/INDEX.md) |
| 变更预告 (`harmonyos-roadmap`) | 0 | [INDEX.md](harmonyos/references/harmonyos-roadmap/INDEX.md) |
| **合计** | **12232** | [INDEX.md](harmonyos/references/INDEX.md) |

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
| **Gemini CLI** | `ln -s <repo>/harmonyos ~/.gemini/skills/harmonyos` |
| **OpenAI Codex CLI** | `ln -s <repo>/harmonyos ~/.codex/skills/harmonyos` |
| **GitHub Copilot CLI** | `ln -s <repo>/harmonyos ~/.copilot/skills/harmonyos` |
| **Cursor** | `ln -s <repo>/harmonyos ~/.cursor/skills/harmonyos` |
| **OpenCode** | 在 `~/.config/opencode/opencode.json` 加 `"skills": ["<repo>/harmonyos"]` |

### 更新

| 安装方式 | 更新命令 |
|---|---|
| 一键脚本 | `cd ~/.local/share/harmonyos-skills && git pull` |
| 手动 symlink | 在 clone 的 repo 目录执行 `git pull`（symlink 自动指向最新内容） |
| Claude Code plugin | `/plugin update harmonyos-skills` |

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

## MCP 服务

[`mcp/server.py`](mcp/server.py) 是一个 stdio 传输的 MCP server，把本仓库暴露为工具，适合不方便直接读文件的客户端，或希望用结构化检索代替 grep 的场景。运行只依赖 [uv](https://github.com/astral-sh/uv)：依赖由脚本内的 PEP 723 元数据声明，首次运行时 uv 自动准备隔离环境（不会动 `scraper/` 的虚拟环境）。

| 工具 | 作用 |
|---|---|
| `list_categories` | 五个分类的标识、中文名与篇数 |
| `search_docs(query, category?, limit?, fulltext?)` | 默认按标题 / 路径匹配多个关键词；`fulltext=true` 用 `rg`（或 `grep`）做短语全文检索 |
| `read_doc(path, offset?, max_chars?)` | 按 `search_docs` 返回的相对路径或华为文档 URL 读正文与元信息，超长时分页 |
| `coding_rules()` | 返回 `harmonyos/rules/arkts-coding-rules.md` |
| `fetch_online(url_or_object_id)` | 调华为 documentPortal 接口拉最新正文并转 Markdown，本地没有或过旧时兜底 |

**Claude Code**：以 plugin 方式安装后自动启用（`plugin.json` 已注册 `mcpServers`）。用 symlink 方式安装的按下面手动配置。

**其他 MCP 客户端**（Claude Desktop、Cursor、Gemini CLI 的 `settings.json` 等 JSON 配置）：

```json
{
  "mcpServers": {
    "harmonyos-docs": {
      "command": "uv",
      "args": ["run", "/path/to/harmonyos-skills/mcp/server.py"]
    }
  }
}
```

**Codex CLI**（`~/.codex/config.toml`）：

```toml
[mcp_servers.harmonyos-docs]
command = 'uv'
args = ['run', '/path/to/harmonyos-skills/mcp/server.py']
```

本地验证：

```bash
uv run mcp/server.py
```

启动后等待 stdin 的 JSON-RPC 输入即表示正常，Ctrl+C 退出。

## 采集脚本使用

采集脚本是 `scraper/` 下的独立 Python 项目，**所有 `uv` 命令必须在 `scraper/` 目录内执行**。在仓库根目录直接跑 `uv run python -m scripts.sync` 会报 `No module named 'scripts'`，并在根目录误建一个空的 `.venv`。

### 一键同步（推荐）

```bash
scraper/sync.sh
```

脚本会自行切换到 `scraper/` 目录，在任意路径下都能执行；首次运行自动创建虚拟环境、安装依赖与 Playwright Chromium。命令行参数原样透传，例如 `scraper/sync.sh --root harmonyos-guides`。

### 手动执行

```bash
cd scraper
uv sync                              # 按 uv.lock 安装依赖（含 pytest），首次或依赖变更后执行
uv run playwright install chromium   # 首次执行
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

`--root` 可选值：`harmonyos-releases` / `harmonyos-guides` / `harmonyos-references` / `best-practices` / `harmonyos-faqs` / `harmonyos-roadmap`。

### 工作流程

两阶段：

1. **discover**（5 个根并行）：访问每个根 URL → 循环点击 `.layout-left .ant-tree-switcher_close` 直到收敛 → 抽出全部 `.layout-left a[href]`。结果缓存到 `data/discovery.json`，同日内复用。任一根失败或抽不到链接则整体退出（退出码 1），不改 manifest 与 INDEX，避免残缺清单把整个分类误标 stale。
2. **fetch**（concurrency=8）：并发渲染所有发现的 URL，抽正文转 Markdown，按 sha256 增量写盘到 `harmonyos/references/`；manifest 里没有记录时以磁盘副本 frontmatter 的 `content_hash` 为准，全新环境（如 CI）不会整库重写。每完成 50 页 flush 一次 manifest，便于中断恢复。抓取失败的文档若磁盘上还有上次的副本，仍保留在 INDEX 中。

时间预估（参考实测）：

| 步骤 | 单次成本 |
|---|---|
| discover（5 根并行） | ~12 分钟 |
| fetch（每 100 页） | ~26 秒 |
| 全量（约 12000 页） | ~1 小时 |

### 断点续传

- `data/manifest.json` 每 50 页 flush 一次
- 同日内已 `last_checked_at` 的页面下次启动跳过（除非 `--force`）
- discover 结果缓存于 `data/discovery.json`，同日复用；`--root` 的部分同步不写缓存，避免下次全量误用残缺清单

意外中断后再跑一次 `python -m scripts.sync` 即可从断点继续。

### 自动同步

仓库自带 [`.github/workflows/sync-docs.yml`](.github/workflows/sync-docs.yml)：每天北京时间 04:00 在 GitHub Actions 上跑一次全量同步（`--force`）。仅当 `harmonyos/` 下有变更时才提交（连同 README 统计）并推送到 `master`，随后创建 Release，tag 与版本号为 `YYYY-MM-DD.<short sha>`（如 `2026-09-02.a1b2c3d`）；无变更则不产生提交。同步日志作为 artifact 保留 14 天。discover 失败或本次抓取错误率超过 20% 时脚本以非 0 退出，工作流失败且不提交。

也可以手动触发（Actions 页的 Run workflow，或 `gh`），参数：

| 参数 | 默认 | 说明 |
|---|---|---|
| `root` | `all` | 只同步某一分类，调试用；选了分类就只跑不发布 |
| `limit` | 空 | 只处理前 N 个 URL，调试用；填了就只跑不发布 |
| `publish` | `true` | 有变更时是否提交并发布 Release |

```bash
gh workflow run sync-docs.yml
```

```bash
gh workflow run sync-docs.yml -f root=harmonyos-faqs -f limit=50
```

部分同步在 CI 这种没有 manifest 的全新环境里不重写 INDEX（清单不完整），所以只适合验证抓取流程本身。

本地也可以用 cron，例如每天 04:00：

```cron
0 4 * * * PATH=$HOME/.local/bin:/usr/local/bin:$PATH /path/to/harmonyos-skills/scraper/sync.sh >> /path/to/harmonyos-skills/scraper/data/logs/cron.log 2>&1
```

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

`title` / `breadcrumb` 含 `: ` 或以 `@`、`-` 等 YAML 指示符开头时，输出为 JSON 双引号形式（例如 `title: "@ohos.app.ability.UIAbility (UIAbility)"`），保证 frontmatter 是合法 YAML。

## 维护

- 退出码：任一根 discover 失败或本次抓取错误率超过 20% 为 1；`--root` 取值不合法为 2
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
- 同一文档常被带 / 不带 `?istab=1&m=1` 各发现一次，只抓先发现的那个，INDEX 按路径去重
- 图片等资源链接上的 CDN 临时签名参数（`HW-CC-KV` / `HW-CC-Date` / `HW-CC-Expire` / `HW-CC-Sign`）在转换时剥离：它们按分钟变化且 24 小时过期，保留会让每次抓取的 hash 都不同。因此 Markdown 里的图片链接只用于标识资源，不保证可直接访问
- 站点已下线的文档只从 INDEX 移除（manifest 标 `stale`），磁盘上的 `.md` 不删除

## 白名单根 URL

| 类别 | URL |
|---|---|
| 版本说明 | https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-allversion |
| 指南 | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide |
| API 参考 | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api |
| 最佳实践 | https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smart-reach |
| FAQ | https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-phone |
| 变更预告 | https://developer.huawei.com/consumer/cn/doc/harmonyos-roadmap/changelogs-overview-pre |

跨出白名单的 URL 在抽链时会被丢弃（按 5 个根的二级路径前缀严格判断 category）。
