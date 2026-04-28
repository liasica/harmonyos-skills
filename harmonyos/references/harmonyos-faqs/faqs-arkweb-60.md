---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-60
title: 如何全局存储WebController
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何全局存储WebController
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:872d1809402acccb5a7a353b34289679b9ab3d56d73ea00b6637b7538b983e34
---

**问题场景：**

需要全局存储多个WebController对象，目前使用将Map存入AppStorage的方式不生效。

**解决方案：**

目前AppStorage中不支持存储Map类型的数据，因为Map不能被JSON序列化。可以改为使用数组类型存储，或者将Map转换为String类型，因为AppStorage只支持存储String类型的数据。
