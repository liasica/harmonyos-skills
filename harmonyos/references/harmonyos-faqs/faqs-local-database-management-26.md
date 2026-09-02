---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-26
title: 分布式对象必须要把默认obj的属性的每一个项值都设置undefined否则都会倒灌
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 分布式对象必须要把默认obj的属性的每一个项值都设置undefined否则都会倒灌
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:314807ecdac7d66333b4ff0f2c40839c1979ca36f1bd397d2a3f02dc77995179
---

在分布式对象组网时，如果两个对象的数据不一致，需要进行一次同步。后加入组网的对象的数据被视为最新数据，将覆盖先加入组网的数据。当新对象属性值为undefined时，系统会保留旧对象对应属性值，并接收已有数据。
