---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-37
title: 如何在Web请求时添加header头
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在Web请求时添加header头
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:edf1290e541de5d4c368c33230e7652ffd4dd045e163d11247f678750fb07737
---

可以通过loadUrl方法设置headers。该方法接收两个参数：url表示需要加载的URL，headers为数组类型表示附加的HTTP请求头。

```ts
// With parameter headers
this.controller.loadUrl('www.example.com', [{ headerKey: "headerKey", headerValue: "headerValue" }]);
```

**参考链接**

[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)

[WebHeader](../harmonyos-references/arkts-apis-webview-i.md#webheader)
