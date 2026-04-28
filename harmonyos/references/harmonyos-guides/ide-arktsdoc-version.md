---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-version
title: @version
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @version
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:35+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:c3ce99adfd8377c1d8c0c6c6fa80647aec164251c2cac2cf553f6b20f089c150
---

@version标签用于记录项目的版本。

## 语法

@version <version>

## 示例

使用 @version 标签：

```
1. /**
2. * Calculates the square root of a number.
3. * @version 1.2.3
4. */
5. export function sqrt(x: number): number {
6. return Math.sqrt(x);
7. }
```
