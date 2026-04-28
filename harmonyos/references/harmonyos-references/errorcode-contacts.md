---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-contacts
title: Contacts错误码
breadcrumb: API参考 > 应用服务 > Contacts Kit（联系人服务） > 错误码 > Contacts错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:16:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0159631edb5641917ae565c201a77e1572edd4145bdf27da4227d8b0296f5c8b
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 16700001 系统内部错误

PhonePC/2in1TabletWearable

**错误信息**

general error.

**错误描述**

系统内部错误。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。

## 16700002 参数检查失败

PhonePC/2in1TabletWearable

**错误信息**

Invalid parameter value.

**错误描述**

参数校验失败。

**可能原因**

1. 空参数错误 (Null Argument Error)。
2. 参数格式错误 (Format Error)。
3. 参数值范围错误 (Value Range Error)。

**处理步骤**

请阅读参数规格约束，按照可能原因进行排查。

## 16700101 查询数据库失败

PhonePC/2in1TabletWearable

**错误信息**

Failed to get value from contacts data.

**错误描述**

查询数据库失败。

**可能原因**

数据库操作失败。

**处理步骤**

当前访问数据库失败，请稍后重试。

## 16700102 增删改数据库失败

PhonePC/2in1TabletWearable

**错误信息**

Failed to set value to contacts data.

**错误描述**

增删改数据库失败。

**可能原因**

数据库操作失败。

**处理步骤**

当前访问数据库失败，请稍后重试。

## 16700103 用户取消

PhonePC/2in1TabletWearable

**错误信息**

User canceled.

**错误描述**

用户取消。

**可能原因**

用户取消本次操作。

**处理步骤**

当前用户主动取消操作，请稍后重试。
