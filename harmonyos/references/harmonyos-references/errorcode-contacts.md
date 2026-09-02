---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-contacts
title: Contacts错误码
breadcrumb: API参考 > 应用服务 > Contacts Kit（联系人服务） > 错误码 > Contacts错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d1ac1a258cbcc5e57b209fb66bde9865219486f501e6805f72c11c66bbbdac7f
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 16700001 系统内部错误

**错误信息**

General error.

**错误描述**

系统内部错误。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。

## 16700002 参数检查失败

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

## 16700003 禁止后台调用

**错误信息**

Background usage is prohibited.

**错误描述**

禁止后台调用。

**可能原因**

后台调用。

**处理步骤**

请调用方处于前台调用。

## 16700004 联系人数量超过限制

**错误信息**

The number of contacts exceeds the limit.

**错误描述**

联系人数量超过限制。

**可能原因**

传入的联系人数量超过限制。

**处理步骤**

请检查联系人数量。

## 16700101 查询数据库失败

**错误信息**

Failed to get value from contacts data.

**错误描述**

查询数据库失败。

**可能原因**

数据库操作失败。

**处理步骤**

当前访问数据库失败，请稍后重试。

## 16700102 增删改数据库失败

**错误信息**

Failed to set value to contacts data.

**错误描述**

增删改数据库失败。

**可能原因**

数据库操作失败。

**处理步骤**

当前访问数据库失败，请稍后重试。

## 16700103 用户取消

**错误信息**

User cancel.

**错误描述**

用户取消。

**可能原因**

用户取消本次操作。

**处理步骤**

当前用户主动取消操作，请稍后重试。

## 401 打开联系人头像文件失败

**错误信息**

Failed to open contact portrait file.

**错误描述**

无法打开联系人头像文件。

**可能原因**

头像文件路径错误、文件不存在、磁盘损坏。

**处理步骤**

检查文件是否存在。

## 401 系统内部错误

### 内部关联联系人ID无效

**错误信息**

Internal error. Invalid contact id. Failed to generate contact profile.

**错误描述**

内部关联联系人ID无效。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。

### 保存联系人头像失败

**错误信息**

Internal error. Failed to save contact portrait.

**错误描述**

保存联系人头像失败。

**可能原因**

头像文件异常、系统内部处理异常。

**处理步骤**

检查文件。

### 数据库查询插入结果集为空指针

**错误信息**

Internal error. The query resultSet is nullptr.

**错误描述**

数据库查询插入结果集为空指针。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。

### 数据库查询插入结果集存在但无数据

**错误信息**

Internal error. The query resultSet is empty.

**错误描述**

数据库查询插入结果集存在但无数据。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。

### 内部关联联系人rawId无效

**错误信息**

Internal error. Invalid contact rawId.

**错误描述**

内部关联联系人rawId无效。

**可能原因**

系统内部处理异常。

**处理步骤**

系统异常，请稍后重试。
