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

> 最后一次完整同步：**2026-09-04**

| 分类 | 数量 | 入口 |
|---|---:|---|
| 版本说明 (`harmonyos-releases`) | 1249 | [INDEX.md](harmonyos/references/harmonyos-releases/INDEX.md) |
| 指南 (`harmonyos-guides`) | 5719 | [INDEX.md](harmonyos/references/harmonyos-guides/INDEX.md) |
| API 参考 (`harmonyos-references`) | 4761 | [INDEX.md](harmonyos/references/harmonyos-references/INDEX.md) |
| 最佳实践 (`best-practices`) | 512 | [INDEX.md](harmonyos/references/best-practices/INDEX.md) |
| FAQ (`harmonyos-faqs`) | 4595 | [INDEX.md](harmonyos/references/harmonyos-faqs/INDEX.md) |
| 变更预告 (`harmonyos-roadmap`) | 13 | [INDEX.md](harmonyos/references/harmonyos-roadmap/INDEX.md) |
| **合计** | **16849** | [INDEX.md](harmonyos/references/INDEX.md) |

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

脚本会自行切换到 `scraper/` 目录，在任意路径下都能执行；首次运行自动创建虚拟环境并安装依赖。命令行参数原样透传，例如 `scraper/sync.sh --root harmonyos-guides`。

### 手动执行

```bash
cd scraper
uv sync                              # 按 uv.lock 安装依赖（含 pytest），首次或依赖变更后执行
```

| 用途 | 命令 |
|---|---|
| 全量同步 | `uv run python -m scripts.sync` |
| 仅某一类 | `uv run python -m scripts.sync --root harmonyos-guides` |
| dry-run（仅发现，不抓取） | `uv run python -m scripts.sync --dry-run` |
| 限量调试 | `uv run python -m scripts.sync --limit 50` |
| 强制重抓 | `uv run python -m scripts.sync --force` |
| 单元测试 | `uv run pytest -v` |

`--root` 可选值：`harmonyos-releases` / `harmonyos-guides` / `harmonyos-references` / `best-practices` / `harmonyos-faqs` / `harmonyos-roadmap`。

### 工作流程

两阶段，全部走华为文档站自己的接口（`config/whitelist.yaml` 的 `api_base`），不需要浏览器：

1. **discover**（各根并行）：每个根调一次 `getCatalogTree`，整棵目录树一次返回；展平后得到每篇文档的 objectId、标题与面包屑（根标题 > 各级目录 > 本节点）。任一根失败或树里没有文档则整体退出（退出码 1），不改 manifest 与 INDEX，避免残缺清单把整个分类误标 stale。
2. **fetch**（concurrency=16）：并发调 `getDocumentById` 拉正文 HTML，转 Markdown 后按 sha256 增量写盘到 `harmonyos/references/`；manifest 里没有记录时以磁盘副本 frontmatter 的 `content_hash` 为准，全新环境（如 CI）不会整库重写。正文没变但 url、标题、面包屑或更新时间变化时也会重写文件以刷新 frontmatter。每完成 50 篇 flush 一次 manifest，便于中断恢复。抓取失败的文档若磁盘上还有上次的副本，仍保留在 INDEX 中。

转换规则：正文开头的 h1 即标题，不重复输出；接口原文顶层章节是 h4，标题文本前的 `[h2]` 标记表示再低一级，处理后整体上移到从 `##` 开始；「说明 / 注意 / 须知 / 警告」提示框的图标图片换成对应文字标签；代码块语言取自 `<pre>` 的 class；链接转绝对 URL 并剥离 CDN 签名参数，再把白名单内的链接改写为仓库内相对路径。

时间预估（参考实测）：

| 步骤 | 单次成本 |
|---|---|
| discover（6 根并行） | 约 1 秒 |
| fetch | 约 100 篇/秒 |
| 全量（约 16800 篇，含写盘） | 约 6 分钟 |

### 断点续传

- `data/manifest.json` 每 50 篇 flush 一次
- 同日内已 `last_checked_at` 的文档下次启动跳过（除非 `--force`）

意外中断后再跑一次 `python -m scripts.sync` 即可从断点继续。

### 自动同步

仓库自带 [`.github/workflows/sync-docs.yml`](.github/workflows/sync-docs.yml)：每天北京时间 04:00 在 GitHub Actions 上跑一次全量同步（`--force`，只调华为文档接口，几分钟完成）。仅当 `harmonyos/` 下有变更时才提交（连同 README 统计）并推送到 `master`，随后创建 Release，tag 与版本号为 `YYYY-MM-DD.<short sha>`（如 `2026-09-02.a1b2c3d`）；无变更则不产生提交。同步日志作为 artifact 保留 14 天。discover 失败或本次抓取错误率超过 20% 时脚本以非 0 退出，工作流失败且不提交。

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
└── logs/sync-YYYY-MM-DD.log

harmonyos/references/                        # 文档产物，入库
├── INDEX.md                                 # 全量路径清单
└── <category>/INDEX.md + *.md               # 各分类文档
```

每个 `.md` 顶部 frontmatter：

```yaml
---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide
title: 应用开发导读
breadcrumb: 指南 > 基础入门 > 应用开发导读
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:00+08:00
doc_updated_at: 2026-08-29      # 接口返回的 displayUpdateTime，即页面上显示的更新时间
content_hash: sha256:...
---
```

`title` / `breadcrumb` 含 `: ` 或以 `@`、`-` 等 YAML 指示符开头时，输出为 JSON 双引号形式（例如 `title: "@ohos.app.ability.UIAbility (UIAbility)"`），保证 frontmatter 是合法 YAML。

## 维护

- 退出码：任一根 discover 失败或本次抓取错误率超过 20% 为 1；`--root` 取值不合法为 2
- 抓取失败看 `data/logs/sync-*.log` 里的 `fetch failed` 条目；`manifest.json` 中 `status=error` 列出失败 URL
- 接口（截至 2026-09-02）：
  - `POST <api_base>getCatalogTree`，body `{"language":"cn","catalogName":"<分类>","objectId":"<根文档 id>"}`，返回 `value.catalogTreeList`，节点字段 `nodeName` / `relateDocument` / `children`
  - `POST <api_base>getDocumentById`，body `{"objectId":"<id>","version":"","catalogName":"<分类>","language":"cn"}`，返回 `value.title`、`value.content.content`（HTML）、`value.displayUpdateTime`
  - 接口字段变化时改 `scripts/discover.py` 与 `scripts/fetcher.py`

## 已知限制

- 文档 URL 统一为 `https://developer.huawei.com/consumer/cn/doc/<分类>/<objectId>`，不带站点侧边栏链接里的 `?istab=1&m=1`
- 图片等资源链接上的 CDN 临时签名参数（`HW-CC-KV` / `HW-CC-Date` / `HW-CC-Expire` / `HW-CC-Sign`）在转换时剥离：它们按分钟变化且 24 小时过期，保留会让每次抓取的 hash 都不同。因此 Markdown 里的图片链接只用于标识资源，不保证可直接访问
- 站点已下线的文档只从 INDEX 移除（manifest 标 `stale`），磁盘上的 `.md` 不删除
- 同一 objectId 若在多个目录节点下出现，只保留首次出现位置的面包屑
- objectId 为 `index` 的文档存为 `index-doc.md`：在 macOS 这类大小写不敏感的文件系统上，`index.md` 与分类索引 `INDEX.md` 是同一个文件
- 视频 / 音频没有 Markdown 形式，转为 `[视频](url)` / `[音频](url)` 链接

## 白名单根 URL

| 类别 | URL |
|---|---|
| 版本说明 | https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-allversion |
| 指南 | https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide |
| API 参考 | https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api |
| 最佳实践 | https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smart-reach |
| FAQ | https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-phone |
| 变更预告 | https://developer.huawei.com/consumer/cn/doc/harmonyos-roadmap/changelogs-overview-pre |

目录树里的文档按所属根归类；正文中指向白名单外的链接保留为绝对 URL。
