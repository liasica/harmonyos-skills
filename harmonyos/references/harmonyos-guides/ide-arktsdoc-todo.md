---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-todo
title: "@todo"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @todo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:225173070e8efc7ed9c57de637a36a9564e0a48af9937ec802f24f62137cd615
---

@todo 标签记录要完成的任务。在一个 ArkTSDoc 注释块中可以包含多个 @todo 标签。

## 语法

@todo text describing thing to do.

## 示例

使用 @todo 标签：

```screen
/**
 * @todo Write the documentation.
 * @todo Implement this function.
 */
export function foo() {
  // write me
}
```
