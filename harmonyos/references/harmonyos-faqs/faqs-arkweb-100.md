---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-100
title: 同层渲染场景下控件使能沉浸光感效果变透明
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 同层渲染场景下控件使能沉浸光感效果变透明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:52+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:ac5f017a6f7001c196d1caa278dd0977d0c9b4ef32b0ea1d256bc52a575e8a33
---

**问题现象**

同层渲染场景下将ArkUI的控件设置沉浸光感效果时，发现控件背景变透明。

**解决措施**

API 23及以前SDK在同层渲染场景下暂不支持沉浸光感效果，建议在影响业务场景的对应控件上关闭沉浸光感或者关闭同层渲染。

**参考链接**

[同层渲染](../harmonyos-guides/web-same-layer.md)
