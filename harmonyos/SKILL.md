---
name: harmonyos
description: 当用户编写、调试或审查 HarmonyOS NEXT 应用（ArkTS / ArkUI / Stage 模型 / @ohos.* API / DevEco Studio / hvigor / hdc），需要查阅华为开发者官方文档（版本说明 / 指南 / API 参考 / 最佳实践 / FAQ），或询问 HarmonyOS API 签名、错误码、能力可用性时使用。先在 `references/INDEX.md` 中 grep 关键词定位目标路径，再 Read 命中的 `.md`，不要遍历目录或一次性读多个文件。
---

# HarmonyOS

HarmonyOS NEXT 开发者文档离线镜像。来源：`developer.huawei.com/consumer/cn/doc/`。每个 `.md` 顶部带 YAML frontmatter，含原始 URL、面包屑、`doc_updated_at` 等元信息。

## 快速上手

1. 通过索引定位文件——不要直接 grep `references/`：

   ```bash
   rg -n "<关键词>" references/INDEX.md | head
   ```

2. Read 命中的 `.md`。文件前 8 行 frontmatter 给出原始 URL 与最后更新时间。

3. 当用户需要参考链接时，从 frontmatter 的 `url` 字段返回——这是华为官方文档的规范引用。

## 分类

| 路径 | 内容 |
|---|---|
| `references/harmonyos-releases/` | 版本说明、API Level、SDK 变更日志 |
| `references/harmonyos-guides/` | 应用框架、ArkTS、ArkUI、媒体、网络等使用指南 |
| `references/harmonyos-references/` | API 参考（`@ohos.*` 模块、组件签名、错误码） |
| `references/best-practices/` | 性能、兼容性、能耗等官方最佳实践 |
| `references/harmonyos-faqs/` | 常见问题与解答 |

每个分类有专属 `INDEX.md`（含标题与统计），范围明确时可缩到分类内查找：

```bash
rg -n "UIAbility" references/harmonyos-references/INDEX.md
rg -n "@ohos\.app\.ability" references/harmonyos-references/INDEX.md
```

## 内链已本地化

文档中原本指向 5 个白名单根 URL 的链接已自动改写为指向本仓库内 `.md` 的相对路径。指向白名单外的链接保留为绝对 https URL。

## 工作流程

1. 先弄清用户问的是什么——功能查询、API 签名、错误码、版本差异，还是最佳实践？
2. 用关键词在 `references/INDEX.md` 中匹配（明显属于某个分类时可直接到对应 `<category>/INDEX.md`）
3. 仅 `Read` 命中的 `.md`，不要主动读邻居文件，除非确有必要
4. 回答时引用 frontmatter 的 `url` 字段作为出处
5. 如果本地文件比用户项目要求的版本陈旧（对比 `doc_updated_at`），或本地完全没命中而该话题确属鸿蒙领域，再用 WebFetch 拉取实时页并明确说明走了在线兜底

## 质量约束

- `@ohos.*` API 的签名、入参、返回值以 `references/` 内的文档为准，不要凭训练时记忆补全
- ArkUI 示例优先使用声明式语法（`@Entry` / `@Component` / `build()`），除非文档明确是 NDK 或系统服务
- 不要修改 `references/` 下任何文件——它们是只读参考资料
- 不要把 frontmatter 字段（`content_hash` / `scraped_at` / `category`）当成代码内容塞进生成的代码里
- 当两份文档冲突（例如旧版指南与新版本说明），明确指出冲突并同时引用两边
