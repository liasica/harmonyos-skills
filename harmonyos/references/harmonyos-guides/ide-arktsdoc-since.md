---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-since
title: "@since"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @since
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2342c279548428564608a5a3c1fe9d55dc573176caaaafab0d24b0a283de03ff
---

@since标签表示在特定版本中添加了类、方法或其他符号。

## 语法

@since <versionDescription>

## 示例

使用 @since：

```screen
/**
 * Provides access to user information.
 * @since 1.0.1
 */
export function UserRecord(): void {}
```
