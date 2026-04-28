---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-6
title: 卡片开发中如何实现数据持久化
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 卡片开发中如何实现数据持久化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f2e51ecdce331751493eaa5ba1f8dd9c8544aa51b7cf099c74f01f0944ffc9f0
---

HarmonyOS提供三种主要数据持久化方案：用户首选项(Preferences)适用于轻量级键值存储，键值型数据库(KV-Store)支持分布式数据同步，关系型数据库(RelationalStore)提供SQLite关系型数据管理能力。

* 用户首选项（Preferences）：将数据存入Preferences实例后，使用`flush()`方法实现数据持久化，建议在应用生命周期关键节点(如onBackground)主动调用以确保数据安全。
* 键值型数据库（KV-Store）：调用put()方法向键值型数据库中插入数据，KV-Store的put()方法支持同步/异步写入模式，适用于设备间数据同步场景，分布式特性要求调用方处理CONFLICT\_FOUND等异常状态。。
* 关系型数据库（RelationalStore）：获取RdbStore后，调用insert()接口插入数据。

**参考链接**

[用户首选项](../harmonyos-guides/data-persistence-by-preferences.md)

[键值型数据库](../harmonyos-guides/data-persistence-by-kv-store.md)

[关系型数据库](../harmonyos-guides/data-persistence-by-rdb-store.md)
