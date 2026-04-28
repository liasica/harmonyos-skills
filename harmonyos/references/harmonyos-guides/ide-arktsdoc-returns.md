---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-returns
title: @returns
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @returns
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3035275eb8f8f47168cf052df0f25a04fb129f975db070fc4c2aa72584a67a2d
---

@returns标签用于记录函数返回值。

## 语法

@returns [description]

## 示例

```
1. /**
2. * Returns the sum of a and b
3. * @param a
4. * @param b
5. * @returns Sum of a and b
6. */
7. export function sum(a: number, b: number): number{
8. return a + b;
9. }
```
