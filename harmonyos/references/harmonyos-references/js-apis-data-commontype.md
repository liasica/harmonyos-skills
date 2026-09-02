---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-commontype
title: "@ohos.data.commonType (数据通用类型)"
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.commonType (数据通用类型)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:85c1c85c1e8da049c50b5447cb4aa0dc7f3a84d3f6cff9680b52117329fba89a
---

数据通用类型（commonType）是数据管理中通用的数据类型，提供了资产状态枚举、资产信息和键值对存储等基础数据类型，用于支持分布式数据管理场景下的数据统一表示和传递。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { commonType } from '@kit.ArkData';
```

## AssetStatus

描述资产附件的状态枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ASSET\_NORMAL | 1 | 表示资产状态正常。 |
| ASSET\_INSERT | 2 | 表示资产需要插入到云端。 |
| ASSET\_UPDATE | 3 | 表示资产需要更新到云端。 |
| ASSET\_DELETE | 4 | 表示资产需要在云端删除。 |
| ASSET\_ABNORMAL | 5 | 表示资产状态异常。 |
| ASSET\_DOWNLOADING | 6 | 表示资产正在下载到本地设备。 |

## Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息，相关示例见[在跨端迁移中使用分布式数据对象迁移数据](../harmonyos-guides/data-sync-of-distributed-data-object.md#在跨端迁移中使用分布式数据对象迁移数据)的示例代码。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 资产的名称。 |
| uri | string | 否 | 否 | 资产的uri，在系统里的绝对路径。 |
| path | string | 否 | 否 | 资产在应用沙箱里的路径。 |
| createTime | string | 否 | 否 | 资产被创建出来的时间。 |
| modifyTime | string | 否 | 否 | 资产最后一次被修改的时间。 |
| size | string | 否 | 否 | 资产占用空间的大小（单位：字节（Byte），取值为非负整数）。 |
| status | [AssetStatus](js-apis-data-commontype.md#assetstatus) | 否 | 是 | 资产的状态，默认值为ASSET\_NORMAL。 |

## Assets

type Assets = Array<Asset>

表示[Asset](js-apis-data-commontype.md#asset)类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

| 类型 | 说明 |
| --- | --- |
| Array<[Asset](js-apis-data-commontype.md#asset)> | 表示Asset类型的数组。 |

## ValueType

type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets

表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

| 类型 | 说明 |
| --- | --- |
| null | 表示值类型为空。 |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| Uint8Array | 表示值类型为Uint8类型的数组。 |
| Asset | 表示值类型为附件[Asset](js-apis-data-commontype.md#asset)。 |
| Assets | 表示值类型为附件数组[Assets](js-apis-data-commontype.md#assets)。 |

## ValuesBucket

type ValuesBucket = Record<string, ValueType>

用于存储键值对的类型。该类型不是并发安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**系统能力：** SystemCapability.DistributedDataManager.CommonType

| 类型 | 说明 |
| --- | --- |
| Record<string, [ValueType](js-apis-data-commontype.md#valuetype)> | 表示键值对类型。键的类型为string，值的类型为[ValueType](js-apis-data-commontype.md#valuetype)。 |
