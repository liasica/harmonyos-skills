---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-35
title: 如何实现Web和Webview对前端常用框架（如Vue，React）的适配
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何实现Web和Webview对前端常用框架（如Vue，React）的适配
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b33f96d0e1b9f50f2969a68d75c4f12ee16fef6b7563f259bcb86be9133bb4f2
---

以Vue工程为例，使用runJavaScript API和javaScriptProxy API实现与Vue工程的交互。

* runJavaScript API异步执行JavaScript脚本并返回结果。
* javaScriptProxy API注入JavaScript对象到window对象并调用方法。
* 可以将Vue中的方法绑定到document对象上，实现Vue与JavaScript脚本的交互。

**参考链接**

[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)

[javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)
