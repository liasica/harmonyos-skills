---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-7
title: 如何将Resource资源对象转成string类型
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何将Resource资源对象转成string类型
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f57c8e37821a68a3da76dc24c880760ce48a11f2370a74315a1ab8096eb7fc29
---

Resource 为字符串，支持使用 this.context.resourceManager.getStringSync($r('app.string.test').id)同步转换为字符串，也支持使用 $r('app.string.test', 2) 进行格式化。

**参考链接**

[getStringSync](../harmonyos-references/js-apis-resource-manager.md#getstringsync10)
