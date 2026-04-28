---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-2
title: Web组件的onLoadIntercept返回结果是否影响onInterceptRequest
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件的onLoadIntercept返回结果是否影响onInterceptRequest
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:37+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:fbf137ace6bb9dee7184c36546dc3046ad7fc7ce147abfb56cfd9395677ccbdd
---

Web组件的onLoadIntercept的不同返回结果对应不同的操作：

* onLoadIntercept返回true时，直接拦截URL请求。
* onLoadIntercept返回false时，系统将触发onInterceptRequest回调。

**参考链接**

[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)
