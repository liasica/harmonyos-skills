---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-18
title: 数据库batchInsert和单个事务insert效率问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 数据库batchInsert和单个事务insert效率问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:db5925f440ae585d4319c2cbc3900bf8cdcc86edf44bf491f294e62d7f701d52
---

事务插入无法达到批量插入的效率。在插入100条记录时，单独事务插入需要执行100次数据库操作，而批量插入只需一次批量操作。批量插入接口在单次操作中完成数据写入，其内部已包含事务处理机制。
