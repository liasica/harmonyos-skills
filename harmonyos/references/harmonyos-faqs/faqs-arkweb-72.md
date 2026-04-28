---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-72
title: Web组件是否支持通过URL Scheme协议跳转其它App
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件是否支持通过URL Scheme协议跳转其它App
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4bb64010d032c4d0b3a80c241ff4ecbabfd7a31afee7f289d4fa76507538a6c1
---

Web组件支持通过URL Scheme跳转到其它App。开发者可以通过Web组件的[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调拦截默认跳转逻辑，并在其中使用Deep Linking或App Linking的方式自定义跳转逻辑完成应用跳转。

**参考链接**

[使用Deep Linking实现应用间跳转](../harmonyos-guides/deep-linking-startup.md)

[使用App Linking实现应用间跳转](../harmonyos-guides/app-linking-startup.md)
