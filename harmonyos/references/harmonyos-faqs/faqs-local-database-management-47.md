---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-47
title: 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:234f7d4fd0a546aa060ce987a7945294dfd3489b2e05b6cdd04048f179272117
---

查询数据库可以使用[@ohos.data.relationalStore](../harmonyos-references/js-apis-data-relationalstore.md)模块提供的[query](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#query10)方法，该方法是异步方法，因此对于查询数据库操作，不需要开子线程。
