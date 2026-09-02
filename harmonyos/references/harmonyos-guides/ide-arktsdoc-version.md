---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-version
title: "@version"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @version
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5eb98faee4f3478f5006a906e3dcf0bb68f7570ef168c0a335e92409ac739a33
---

@version标签用于记录项目的版本。

## 语法

@version <version>

## 示例

使用 @version 标签：

```screen
/**
 * Calculates the square root of a number.
 * @version 1.2.3
 */
export function sqrt(x: number): number {
  return Math.sqrt(x);
}
```
