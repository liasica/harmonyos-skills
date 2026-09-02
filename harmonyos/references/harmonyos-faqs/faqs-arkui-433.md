---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-433
title: 手表设备，息屏2分钟才能收到onHidden回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 手表设备，息屏2分钟才能收到onHidden回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c108326c8e2720bb176e2f64a6e3dbdac7ba9393f53be74ce269ad01b2b82de
---

**问题描述**

手表设备在系统熄屏后未收到onPageHide回调，屏亮时未收到onPageShow回调。

**解决措施**

在穿戴设备上，因穿戴设备为节省功耗采用延迟回调机制，应用熄屏后需等待两分钟才会收到窗口熄屏的回调，该行为是穿戴设备窗口的默认机制，开发者可以参考[@ohos.power (系统电源管理)](../harmonyos-references/js-apis-power.md)文档，检测当前设备是否处于活动状态。
