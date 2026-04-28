---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-11
title: 通过RdbStore.query()获取resultSet对象，出现resultSet的rowCount返回结果为-1
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 通过RdbStore.query()获取resultSet对象，出现resultSet的rowCount返回结果为-1
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8b5f1d0671d21520bf323876b18e09a62b5ac0051de8ff6103242ebd7c9dab71
---

查询失败，返回结果为-1。

以下是一种可能的情况：

如果RdbPredicates对象传入错误的表名，调用query接口后，返回的ResultSet对象不会为空，也不会立即抛出异常。但在对ResultSet对象进行操作时，会触发异常。

ROWCOUNT == 0：表中无数据。

ROWCOUNT == -1：表示没有表。
