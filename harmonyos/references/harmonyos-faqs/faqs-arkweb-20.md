---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-20
title: javaScriptProxy和registerJavaScriptProxy有什么区别，能注册多少个对象
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > javaScriptProxy和registerJavaScriptProxy有什么区别，能注册多少个对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:cc7367e02e70a123d4e307109b061f62d49f8f340ee85298fae45ca40aab31ac
---

从功能上讲，二者都可以注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

从接口角度来看，javaScriptProxy是Web组件的方法，而registerJavaScriptProxy是WebviewController的方法。

从注册对象的角度来看，前者仅支持注册一个对象，而后者支持注册多个对象。

从生命周期上讲，javaScriptProxy在Web组件初始化调用，registerJavaScriptProxy在Web组件初始化完成后调用。

JavaScriptProxy可以参考[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)，registerJavaScriptProxy可以参考[registerJavaScriptProxy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)
