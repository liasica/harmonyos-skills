---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-deprecated
title: @deprecated
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @deprecated
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e01345d7a7ed9066ee50cb330a4c93a392e380ce49c803aa5cb2e5d06eaa08bf
---

@deprecated标签指明一个标识在代码中已经被弃用。

## 语法

@deprecated [<some text>]

## 示例

可以单独使用@deprecated标记，也可以包含一些描述有关deprecated的详细信息的文本。

例：说明自版本2.0以来旧函数已被弃用

```
1. /**
2. * @deprecated since version 2.0
3. */
4. export function old() {}
```
