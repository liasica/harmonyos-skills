---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-faq
title: ArkData常见问题
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > ArkData常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:24+08:00
doc_updated_at: 2026-03-06
content_hash: sha256:fe9d30ed9a741914c19c8c450141ae49b0413b819720d5b058a533ed47501869
---

## 如何查看关系型数据库详细的SQL执行异常信息

可以调用[on('sqliteErrorOccurred')](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#onsqliteerroroccurred20)获取SQL执行时出现的异常信息。

## 如何查看关系型数据库生成的SQL语句

可以调用[relationalStore.getInsertSqlInfo](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetinsertsqlinfo20)获取用于插入数据的SQL语句。

可以调用[relationalStore.getUpdateSqlInfo](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetupdatesqlinfo20)获取用于更新数据的SQL语句。

可以调用[relationalStore.getDeleteSqlInfo](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetdeletesqlinfo20)获取用于删除数据的SQL语句。

可以调用[relationalStore.getQuerySqlInfo](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetquerysqlinfo20)获取用于查询数据的SQL语句。

## 关系型数据库不同文件说明

当使用关系型数据时，可能会生成不同的文件产物，不同的文件对应作用具体可见下表。

| **文件类型** | **说明** |
| --- | --- |
| .db | 数据库持久化文件，用于存储数据库数据。 |
| .db-wal | 用于保存操作日志，可以在事务失败时回滚更改，确保数据一致性。  该文件仅在数据库采用WAL模式时存在（系统默认日志方式即为WAL（Write Ahead Log）模式）。 |
| .db-shm | 共享内存文件，用于协调多个数据库连接对同一db文件的更改，防止数据冲突。  该文件仅在数据库采用WAL模式时存在（系统默认日志方式即为WAL（Write Ahead Log）模式）。 |
| .key\_lock | 用于保存文件锁信息。 |
| .pub\_key | 用于保存数据库密钥信息。  该文件仅在配置了数据库加密且未配置自定义加密参数时（即通过[StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)配置encrypt为true且未配置cryptoParam）存在。 |
| .db-dwr | 用于保存文件头信息。 |
| .db-compare | 用于保存所有DDL语句。 |
