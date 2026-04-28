---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T07:59:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:afb102a7135ef5f75f302c9332e4574f67103c8cd0a9d178f5251131c5ac5ed4
---

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。支持通过[ResultSet.getSendableRow](arkts-apis-data-relationalstore-resultset.md#getsendablerow12)方法获取Sendable数据，进行跨线程传递。

为保证插入并读取数据成功，建议一条数据不超过2MB。如果数据超过2MB，插入操作将成功，读取操作将失败。

大数据量场景下查询数据可能会导致耗时长甚至应用卡死，如有相关操作可参考文档[批量数据写数据库场景](../harmonyos-guides/batch-database-operations-guide.md)，且有建议如下：

* 单次查询数据量不超过5000条。
* 在[TaskPool](js-apis-taskpool.md)中查询。
* 拼接SQL语句尽量简洁。
* 合理地分批次查询。

该模块提供以下关系型数据库相关的常用功能：

* [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md)：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
* [RdbStore](arkts-apis-data-relationalstore-rdbstore.md)：提供管理关系数据库（RDB）方法的接口。
* [ResultSet](arkts-apis-data-relationalstore-resultset.md)：提供用户调用关系型数据库查询接口之后返回的结果集合。
* [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)：提供用户调用关系型数据库[queryWithoutRowCount](arkts-apis-data-relationalstore-rdbstore.md#querywithoutrowcount23)、[querySqlWithoutRowCount](arkts-apis-data-relationalstore-rdbstore.md#querysqlwithoutrowcount23)等查询接口之后返回的结果集合。与[ResultSet](arkts-apis-data-relationalstore-resultset.md)相比，LiteResultSet不包含查询结果的总行数信息。
* [Transaction](arkts-apis-data-relationalstore-transaction.md)：提供管理事务对象的接口。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```
1. import { relationalStore } from '@kit.ArkData';
```
