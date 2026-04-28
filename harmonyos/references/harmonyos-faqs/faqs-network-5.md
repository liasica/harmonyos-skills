---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-5
title: 如何理解connection.getDefaultNet返回对象netHandle中的netId
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何理解connection.getDefaultNet返回对象netHandle中的netId
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cf5c75aeb8b0e9dd9326136c36206bbb81d3b9bf29b48c56f9294d66a7592e7f
---

**问题现象**

netId的值0表示未联网，100表示已联网。

**解决措施**

在正常情况下，netHandle中的netId为0表示未连接网络，大于等于100表示已连接网络。

**参考链接**

[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)
