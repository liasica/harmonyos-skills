---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-deprecated
title: "@deprecated"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @deprecated
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e5a3b402e29c4e444283d5a9d289124eb646a2bdde6f226383db724754199af4
---

@deprecated标签指明一个标识在代码中已经被弃用。

## 语法

@deprecated [<some text>]

## 示例

可以单独使用@deprecated标记，也可以包含一些描述有关deprecated的详细信息的文本。

例：说明自版本2.0以来旧函数已被弃用

```screen
/**
 * @deprecated since version 2.0
 */
export function old() {}
```
