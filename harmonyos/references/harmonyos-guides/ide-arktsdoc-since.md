---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-since
title: @since
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @since
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b792d54f45c63278ff8ac781952276afa91cfcd2e421a83f2f2629850c2dfc61
---

@since标签表示在特定版本中添加了类、方法或其他符号。

## 语法

@since <versionDescription>

## 示例

使用 @since：

```
1. /**
2. * Provides access to user information.
3. * @since 1.0.1
4. */
5. export function UserRecord(): void {}
```
