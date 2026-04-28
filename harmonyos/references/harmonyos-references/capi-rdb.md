---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb
title: RDB
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 模块 > RDB
category: harmonyos-references
scraped_at: 2026-04-28T07:59:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:59840412dd3687cc80cac7f164d13850a873ccc66713cdb80e1bfe6611fdacc9
---

## 概述

PhonePC/2in1TabletTVWearable

分布式数据管理（Distributed data manager，data）支持单设备的各种结构化数据的持久化，以及端云间的同步、共享功能。

分布式数据管理定义了一系列数据类型，可以对数据进行增删改查。

**起始版本：** 11

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [data\_asset.h](capi-data-asset-h.md) | 提供资产类型数据结构。  资产是指一种可以在数据管理中使用的数据结构，可以存储及查询一个文件的名称、绝对路径、相对路径、创建时间、修改时间、状态、占用空间等属性。 |
| [oh\_cursor.h](capi-oh-cursor-h.md) | 提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。 |
| [oh\_data\_value.h](capi-oh-data-value-h.md) | 提供与单条数据值相关的函数和枚举。  从API version 18开始，OH\_ColumnType从oh\_cursor.h移动至此头文件呈现，对于此类型，API version 18之前即支持使用，各版本均可正常使用。 |
| [oh\_data\_values.h](capi-oh-data-values-h.md) | 提供与多条数据值相关的函数和枚举。 |
| [oh\_data\_values\_buckets.h](capi-oh-data-values-buckets-h.md) | 提供与存储数据值相关的结构定义、函数和枚举。 |
| [oh\_predicates.h](capi-oh-predicates-h.md) | 表示关系型数据库（RDB）的谓词。 |
| [oh\_rdb\_crypto\_param.h](capi-oh-rdb-crypto-param-h.md) | 提供与关系型数据库加密参数相关的函数和枚举。 |
| [oh\_rdb\_transaction.h](capi-oh-rdb-transaction-h.md) | 提供与数据库事务相关的函数和枚举。 |
| [oh\_rdb\_types.h](capi-oh-rdb-types-h.md) | 提供与数据值相关的类型定义。 |
| [oh\_value\_object.h](capi-oh-value-object-h.md) | 提供类型转换方法。 |
| [oh\_values\_bucket.h](capi-oh-values-bucket-h.md) | 用于存储键值对的类型。 |
| [relational\_store.h](capi-relational-store-h.md) | 提供管理关系数据库（RDB）方法的接口，未标注支持向量数据库的接口仅支持关系型数据库。 |
| [relational\_store\_error\_code.h](capi-relational-store-error-code-h.md) | 声明关系型数据库（RDB）的错误码信息。 |
