---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-returns
title: "@returns"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @returns
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:44c2d566df56c5e849fdf81f1544ce7af942b286d19ca7998f61100272cc23c2
---

@returns标签用于记录函数返回值。

## 语法

@returns [description]

## 示例

```screen
/**
 * Returns the sum of a and b
 * @param a
 * @param b
 * @returns Sum of a and b
 */
export function sum(a: number, b: number): number{
  return a + b;
}
```
