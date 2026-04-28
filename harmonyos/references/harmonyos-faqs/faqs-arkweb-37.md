---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-37
title: 如何在Web请求时添加header头
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在Web请求时添加header头
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:af798809ca4d5c5e9893bf1dd84f0cf81ea0388483578d9f225dd524459f6267
---

可以通过loadUrl方法设置headers。该方法接收两个参数：url表示需要加载的URL，headers为数组类型表示附加的HTTP请求头。

```
1. // With parameter headers
2. this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
```

[AddHeader.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/AddHeader.ets#L34-L35)

**参考链接**

[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)

[WebHeader](../harmonyos-references/arkts-apis-webview-i.md#webheader)
