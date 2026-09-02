# HarmonyOS 开发者文档抓取器

将华为 HarmonyOS 开发者文档本地化为 Markdown 格式，供 AI 辅助开发使用。

## 抓取范围

| 分类 | 根 URL | 说明 |
|------|--------|------|
| `harmonyos-releases` | 版本说明 | HarmonyOS 版本发布说明 |
| `harmonyos-guides` | 指南 | 应用开发指南 |
| `harmonyos-references` | API 参考 | API 接口文档 |
| `best-practices` | 最佳实践 | 开发最佳实践 |
| `harmonyos-faqs` | FAQ | 常见问题解答 |
| `harmonyos-roadmap` | 变更预告 | API 与特性的变更预告、changelog |

抓取走华为文档站自己的接口（`getCatalogTree` 拿目录树、`getDocumentById` 拿正文），不需要浏览器，全量约几分钟。

## 快速开始

### 前置条件

- Python >= 3.12
- [uv](https://github.com/astral-sh/uv)（推荐）或 pip

### 一键同步

```bash
./sync.sh
```

首次运行会自动：
1. 创建虚拟环境
2. 安装依赖
3. 同步所有文档

### 手动运行

以下命令均需在本目录（`scraper/`）内执行。

```bash
# 安装依赖（含 dev 组的 pytest）
uv sync

# 运行同步
uv run python -m scripts.sync
```

## 命令行参数

```bash
uv run python -m scripts.sync [OPTIONS]
```

| 参数 | 说明 |
|------|------|
| `--limit N` | 只处理前 N 个 URL（调试用） |
| `--root CATEGORY` | 只处理指定分类的根（如 `harmonyos-guides`） |
| `--dry-run` | 只发现文档，不抓取 |
| `--force` | 忽略缓存和今日状态，强制重抓 |

退出码：0 成功；1 任一根 discover 失败或本次抓取错误率超过 20%（结果不可信，CI 据此不提交）；2 参数错误。

## 单元测试

```bash
uv run pytest -q
```

## 输出结构

```
harmonyos/references/
├── INDEX.md                          # 全量索引（按分类分组）
├── harmonyos-releases/               # 版本说明
│   ├── INDEX.md
│   └── *.md
├── harmonyos-guides/                 # 指南
│   ├── INDEX.md
│   └── *.md
├── harmonyos-references/             # API 参考
│   ├── INDEX.md
│   └── *.md
├── best-practices/                   # 最佳实践
│   ├── INDEX.md
│   └── *.md
├── harmonyos-faqs/                   # FAQ
│   ├── INDEX.md
│   └── *.md
└── harmonyos-roadmap/                # 变更预告
    ├── INDEX.md
    └── *.md
```

## 数据文件

| 文件 | 说明 |
|------|------|
| `data/manifest.json` | 文档元数据和同步状态 |
| `data/logs/` | 同步日志 |

## 配置

- `config/whitelist.yaml` - 抓取根 URL、接口地址与并发设置

## 增量同步

- 同一天内重复运行会跳过已检查的文档
- 内容哈希未变化时不会重写文件；manifest 缺失时以磁盘副本 frontmatter 的 `content_hash` 为准
- 使用 `--force` 强制全量更新
