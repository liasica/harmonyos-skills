---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-throws
title: "@throws"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @throws
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b796b917bf58176355350edab3077e0859f80a9af7277454b45a7ce15e9f7a3a
---

@throws标签用于函数，记录函数可能引发的错误。可以在一个ArkTSDoc注释中多次使用@throws标记。

## 语法

@throws description

## 示例

使用带有描述的 @throws 标记：

```screen
/**
 * @throws Will throw an error if the argument is null.
 */
export function bar(x: number) {
  throw new Error();
}
```
