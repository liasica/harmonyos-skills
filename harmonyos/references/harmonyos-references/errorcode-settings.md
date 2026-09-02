---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-settings
title: 设置数据项错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 设置数据项错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40e8c8a5027e91ce204a346eb60ef298070dcdfa44ce219ba5c596ebd3e7711a
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 14800000 参数检查失败

**错误信息**

Parameter error. Possible causes: 1. Parameter verification failed.

**错误描述**

1. 空参数错误。
2. 参数解析错误。

**可能原因**

1. 空参数错误 (Null Argument Error)。
2. 参数值范围错误 (Value Range Error)。

**处理步骤**

请检查必选参数是否传入。如果参数校验失败，请阅读参数规格约束，并根据可能原因进行排查。

## 14800010 上下文参数不是UIAbility类型

**错误信息**

Original service error.

**错误描述**

原始服务错误。

**可能原因**

当前上下文环境非UIAbility界面。

**处理步骤**

切换当前上下文环境，使用UIAbility模型。

## 16900010 参数检查失败

**错误信息**

Parameter error.

**错误描述**

参数类型或格式错误。

**可能原因**

1. 空参数错误 (Null Argument Error)。
2. 参数值范围错误 (Value Range Error)。

**处理步骤**

请检查必选参数是否传入。如果参数校验失败，请阅读参数规格约束，并根据可能原因进行排查。

## 16900020 打开设置页面失败

**错误信息**

Failed to open the settings page via redirection.

**错误描述**

打开设置页面失败。

**可能原因**

系统内部异常。

**处理步骤**

重启应用或者设备，再次尝试。
