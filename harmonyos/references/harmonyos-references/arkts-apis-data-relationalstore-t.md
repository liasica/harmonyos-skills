---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-t
title: Types
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Types
category: harmonyos-references
scraped_at: 2026-04-29T13:49:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6e5c54504ba932e02a572634efa95bb0932590de4771d76f42450ffdecb834b6
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## Assets10+

PhonePC/2in1TabletTVWearable

type Assets = Asset[]

表示[Asset](arkts-apis-data-relationalstore-i.md#asset10)类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| [Asset](arkts-apis-data-relationalstore-i.md#asset10)[] | 表示Asset类型的数组。 |

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets | Float32Array | bigint

用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| null | 表示值类型为空。 |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| Uint8Array | 表示值类型为Uint8类型的数组。 |
| Asset10+ | 表示值类型为附件[Asset](arkts-apis-data-relationalstore-i.md#asset10)。  当字段类型是Asset时，在创建表的sql语句中，类型应当为：ASSET。 |
| Assets10+ | 表示值类型为附件数组[Assets](arkts-apis-data-relationalstore-t.md#assets10)。  当字段类型是Assets时，在创建表的sql语句中，类型应当为：ASSETS。 |
| Float32Array12+ | 表示值类型为浮点数组。  当字段类型是Float32Array时，在创建表的sql语句中，类型应当为：floatvector(128)。 |
| bigint12+ | 表示值类型为任意长度的整数。  当字段类型是bigint时，在创建表的sql语句中，类型应当为：UNLIMITED INT，详见[通过关系型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-rdb-store.md)。  **说明：**  bigint类型字段不能比较大小，不适用以下谓词操作：between、notBetween、greaterThan、lessThan、greaterThanOrEqualTo、lessThanOrEqualTo、orderByAsc、orderByDesc。  bigint类型字段的数据写入时，需通过BigInt()方法或在数据尾部添加'n'的方式明确为bigint类型，如'let data = BigInt(1234)'或'let data = 1234n'。  bigint字段如果写入number类型的数据，则查询该数据的返回类型为number，而非bigint。 |

## ValuesBucket

PhonePC/2in1TabletTVWearable

type ValuesBucket = Record<string, ValueType>

用于存储键值对的类型。不支持Sendable跨线程传递。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Record<string, [ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 表示键值对类型。键的类型为string，值的类型为[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)。 |

## PRIKeyType10+

PhonePC/2in1TabletTVWearable

type PRIKeyType = number | string

用于表示数据库表某一行主键的数据类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| number | 主键的类型可以是number。 |
| string | 主键的类型可以是string。 |

## UTCTime10+

PhonePC/2in1TabletTVWearable

type UTCTime = Date

用于表示UTC类型时间的数据类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Date | UTC类型的时间。 |

## ModifyTime10+

PhonePC/2in1TabletTVWearable

type ModifyTime = Map<PRIKeyType, UTCTime>

用于存储数据库表的主键和修改时间的数据类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Map<[PRIKeyType](arkts-apis-data-relationalstore-t.md#prikeytype10), [UTCTime](arkts-apis-data-relationalstore-t.md#utctime10)> | 键表示是数据库表某一行的主键，值表示该行的最后修改时间，用UTC格式表示。 |

## RowData23+

PhonePC/2in1TabletTVWearable

type RowData = Array<ValueType>

用于表示数据库表中的某一行数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 表示[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)类型的数组。 |

## RowsData23+

PhonePC/2in1TabletTVWearable

type RowsData = Array<RowData>

用于表示数据库表中的多行数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| Array<[RowData](arkts-apis-data-relationalstore-t.md#rowdata23)> | 表示[RowData](arkts-apis-data-relationalstore-t.md#rowdata23)类型的数组。 |
