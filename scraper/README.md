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
3. 安装 Playwright 浏览器
4. 同步所有文档

### 手动运行

```bash
# 安装依赖
uv sync

# 首次需要安装 Playwright 浏览器
uv run playwright install chromium

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
| `--dry-run` | 只发现 URL，不渲染 |
| `--force` | 忽略缓存和今日状态，强制重抓 |

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
└── harmonyos-faqs/                   # FAQ
    ├── INDEX.md
    └── *.md
```

## 数据文件

| 文件 | 说明 |
|------|------|
| `data/manifest.json` | 文档元数据和同步状态 |
| `data/discovery.json` | URL 发现缓存（当日有效） |
| `data/logs/` | 同步日志 |

## 配置

- `config/whitelist.yaml` - 抓取根 URL 和并发设置
- `config/selectors.yaml` - 页面元素选择器

## 增量同步

- 同一天内重复运行会跳过已检查的文档
- 内容哈希未变化时不会重写文件
- 使用 `--force` 强制全量更新
