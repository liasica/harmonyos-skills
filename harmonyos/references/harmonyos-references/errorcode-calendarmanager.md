---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-calendarmanager
title: 日历服务错误码
breadcrumb: API参考 > 应用服务 > Calendar Kit（日历服务） > 错误码 > 日历服务错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:64613f0f98c9f82ed007669d76185b6b0b6008b7483e5f7d9e37e01f09b83cd8
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 23900001 参数值错误

**错误信息**

Parameter value error.

**错误描述**

参数值错误。

**可能原因**

1. 参数为字符串时，长度超范围。
2. 参数值超范围。
3. 传入的id不存在。
4. 权限有限制。

**处理步骤**

1. 检查参数字符串长度是否超范围。
2. 检查参数值是否超范围。
3. 通过getEvents接口获取id对应的日程，检查传入的id是否存在。
4. 检查权限是否有限制。

## 23900003 未找到指定的账户

**错误信息**

The specified account was not found.

**错误描述**

未找到指定的账户。

**可能原因**

输入账号与创建的账户不一致，导致查询的账户不存在。

**处理步骤**

确保使用已创建的账户，不要使用未创建的账户。

## 23900004 内部程序错误

**错误信息**

Internal program errors.

**错误描述**

内部程序错误。

**可能原因**

1. dataShare数据库执行错误。
2. 空指针错误。
3. 数据解析错误。

**处理步骤**

内部异常，请稍后重试。

## 23900005 该日程不支持编辑

**错误信息**

This event cannot be edited.

**错误描述**

该日程不支持编辑。

**可能原因**

id对应的日程不支持编辑。

**处理步骤**

1. 检查日程所在账户类型，仅本地账户支持查看和编辑。
2. 检查日程类型，重要日程不支持查看和编辑。
