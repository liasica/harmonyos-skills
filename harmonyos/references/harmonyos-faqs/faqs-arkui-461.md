---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-461
title: AppStorage里面存储数据，如何保证不会有内存泄漏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > AppStorage里面存储数据，如何保证不会有内存泄漏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6765cb17c7f4ef2b555a8adf8e84e3fa6733c99c8b46248193586a17195fe6db
---

**问题描述**

在entryability里用AppStorage存储数据，'当需要访问数据时进行读取会存在内存泄漏吗？

**解决措施**

AppStorage是在应用启动时创建的单例，用于提供应用状态数据的中心存储，这些状态数据在应用级别可访问。AppStorage在应用运行过程中保留其属性，开发者自行管理AppStorage里面的变量生命周期，如不使用可以通过[delete接口](../harmonyos-references/ts-state-management.md#delete10)删掉。
