---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-8
title: 如何解决Web组件加载的HTML页面内检测网络状态失败
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件加载的HTML页面内检测网络状态失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3f06c117a96f48597eed582b3463a3ee0fa31c8606e72bea9ad3afb64b723f2c
---

**问题现象**

在HTML页面中，使用window.navigator.onLine获取网络状态，在联网/断网情况下返回值均为false。

**解决措施**

配置应用以获取网络信息权限：ohos.permission.GET\_NETWORK\_INFO

**参考链接**

[ohos.permission.GET\_NETWORK\_INFO](../harmonyos-guides/permissions-for-all.md#ohospermissionget_network_info)
