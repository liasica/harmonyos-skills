---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-3
title: 为什么Web组件的onKeyEvent键盘事件不生效
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 为什么Web组件的onKeyEvent键盘事件不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:52cb7d36e58a37a312dd61b473bc0fcaf74a90e3be39234f3255f01b1f1bc54b
---

**问题现象**

Web组件设置onKeyEvent监听键盘事件，该事件不触发。

**解决措施**

onKeyEvent为通用键盘事件API，当前Web组件不支持该事件。Web组件监听键盘事件可以使用onInterceptKeyEvent回调函数。

**参考链接**

[onInterceptKeyEvent](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptkeyevent9)
