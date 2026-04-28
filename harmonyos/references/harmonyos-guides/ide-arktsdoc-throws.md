---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-throws
title: @throws
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @throws
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:42fe312dbe969d7116808680a9e1e33b000ff7fac6b877345000ba033bf4c3ff
---

@throws标签用于函数，记录函数可能引发的错误。可以在一个ArkTSDoc注释中多次使用@throws标记。

## 语法

@throws description

## 示例

使用带有描述的 @throws 标记：

```
1. /**
2. * @throws Will throw an error if the argument is null.
3. */
4. export function bar(x: number) {
5. throw new Error();
6. }
```
