---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-62
title: 使用Web组件，在哪个回调事件中可以设置自定义用户代理
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 使用Web组件，在哪个回调事件中可以设置自定义用户代理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:205e7d7089bc39bdbf7f428aa4d397605d6e10d65152f786d2bbd822d8015c29
---

建议在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)回调事件中，使用[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)来设置自定义用户代理。
