---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-error-code
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > Share Kit（分享服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:18:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab69972cd2d8abe88201c71d7a997fbcb04525f7a9e1b3316ba8965382b11a24
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1003700001 数据记录超过上限

PhonePC/2in1TabletTV

**错误信息**

The number of records exceeds the maximum.

**错误描述**

数据记录数量超过上限。

**可能原因**

数据记录数量超过限制，当前上限为500项。

**处理步骤**

对用户可选分享内容数量做限制。

## 1003702001 数据记录格式非法/类型不支持

PhonePC/2in1TabletTV

**错误信息**

Record types are not support.(The batch and multiple selection modes support { @link UDMF.File } type records only.)

**错误描述**

数据记录类型不支持。

**可能原因**

1. 传入了类型无法识别、不支持或不匹配的数据记录。
2. SharedRecord数据记录中，uri、content全部为空。
3. uri格式非法。

**处理步骤**

1. 检查数据类型是否为已预置的[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型或者是已知的自定义类型。
2. 检查SharedRecord数据，uri、content是否全部为空。
3. 检查传入的uri字段格式。

## 1003702002 跨进程传输数据量超过上限

PhonePC/2in1TabletTV

**错误信息**

IPC data is oversized.

**错误描述**

跨进程传输数据超过上限200KB（包含want数据本身的字段）。

**可能原因**

1. 缩略图过大。
2. 文本内容过多。

**处理步骤**

1. 对SharedRecord中传入的缩略图二进制数据进行压缩处理。
2. 对用户可选文本内容做字数限制。

## 1003703001 数据解析失败

PhonePC/2in1TabletTV

**错误信息**

Parse data failed.

**错误描述**

分享数据关键信息通过want传递，非法want无法解析。

**可能原因**

调用[getContactInfo](share-system-share.md#getcontactinfo)/[getSharedData](share-system-share.md#getshareddata)接口时，输入参数格式非法，例如：解析字段不匹配（非分享类型数据）、解析字段不存在等。

**处理步骤**

1. 目标应用Ability中止本次分享数据处理。
2. 提示用户分享数据错误。
