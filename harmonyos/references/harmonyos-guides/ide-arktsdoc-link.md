---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-link
title: "{@link}"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 生成ArkTSDoc文档 > 标准标签 > {@link}
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c88a15d0e3bea9fbcbafcc0e191b13083c48a0e5648543bf5f2de28595d0d18
---

{@link} 用于创建指向指定namepath或网页的链接。使用 {@link} 标记时，可以使用不同格式提供链接文本。

## 语法

* {@link namepathOrURL}
* [link text]{@link namepathOrURL}
* {@link namepathOrURL|link text}
* {@link namepathOrURL link text (after the first space)}

## 示例

提供链接文本：

```screen
/**
 * See {@link MyClass}.
 * Also, check out {@link https://www.example.com/cn/ | Example} and
 * {@link https://www.example.com/cn/ Example}.
 */
export function myFunction() {}
```

**说明** 

若namepath是类名，如例子中的MyClass，用户需要在当前模块中定义该类才能进行正确的跳转。暂不支持对类中属性和方法的跳转。
