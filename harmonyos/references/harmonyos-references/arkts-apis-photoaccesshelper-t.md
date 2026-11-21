---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-t
title: Types
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Types
category: harmonyos-references
scraped_at: 2026-11-21T09:16:17+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:9c4eb126838d0cd713da9bcdcc4ac2c233cff27ab36d86042169c741a2abfea9
---

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## MemberType

type MemberType = number | string | boolean

表示PhotoAsset的成员类型。

成员类型为下表类型的并集。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型。 |

## PhotoAssetParams21+

type PhotoAssetParams = Record<string, MemberType>[]

文件属性名称及其值的Record类型数组。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| Record<string, [MemberType](arkts-apis-photoaccesshelper-t.md#membertype)>[] | 文件属性名称及其值的Record类型数组。 |

## OperationValueType22+

type OperationValueType = number | string | boolean

表示不同谓词需要匹配的值。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型。 |
