---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-71
title: 剪切板如何获取多样式数据类型的内容
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 剪切板如何获取多样式数据类型的内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5217409b0adf04e7d8b485475136998eb50d7578cdab130ae0fa856b2d0ca390
---

## 问题现象

针对多样式类型数据的内容，例如'application/x-styled-text'类型，通过pasteDataRecord.toPlainText()获取到的是空。剪切板如何获取多样式数据类型的内容？

## 解决方案

对于存储在系统剪贴板中的多样式数据，使用[PasteDataRecord.getValidTypes()](../harmonyos-references/js-apis-pasteboard.md#getvalidtypes14)方法获取剪贴板中数据类型与传入参数类型的交集的数据类型数组，交集结果表示请求的类型在剪贴板中存在。遍历数据类型数组，使用[PasteDataRecord.getData()](../harmonyos-references/js-apis-pasteboard.md#getdata14)方法获取对应类型的数据，通过不同RichEditor组件的控制器，实现不同类型数据的粘贴。请注意若剪贴板中不存在请求的数据类型，则对应类型的粘贴操作无法执行，对应RichEditor组件中内容不做更新。

具体示例代码可参考：[实现剪贴板复制粘贴的功能](https://gitee.com/harmonyos_samples/pasteboard)。
