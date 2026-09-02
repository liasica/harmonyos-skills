---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-param
title: "@param"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > @param
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a05f6482e62ad895f1bfddbcb88df72bdfc2938b36f68a411e3e3cacba9f8cab
---

@param标签提供函数参数的描述信息。

可以通过在描述之前插入一个连字符（-），使ArkTSDoc注释更具可读性。连字符前后需使用空格隔开。

## 语法

@param [<description>]

## 示例

下面的示例演示如何在 @param 标签中包含描述信息。

变量说明：

```screen
/**
 * @param somebody Somebody's name.
 */
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}
```

可以在变量说明前加个连字符（-），使之更加容易阅读：

```screen
/**
 * @param somebody - Somebody's name.
 */
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}
```
