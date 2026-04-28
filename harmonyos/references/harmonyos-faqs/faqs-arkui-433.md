---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-433
title: 手表设备，熄屏2分钟才能收到onHidden回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 手表设备，熄屏2分钟才能收到onHidden回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:645519b3ec9d2519ad1bcfcf27a9230ef5b1e258cde5b47a32f36f44794364db
---

**问题描述**

手表设备在系统熄屏后未收到onPageShow回调，屏亮时未收到onPageHide回调。

**解决措施**

在穿戴设备上，因穿戴设备为节省功耗采用延迟回调机制，应用熄屏后需等待两分钟才会收到窗口熄屏的回调，该行为是穿戴设备窗口的默认机制，开发者可以参考[@ohos.power (系统电源管理)](../harmonyos-references/js-apis-power.md)文档，检测当前设备是否处于活动状态。
