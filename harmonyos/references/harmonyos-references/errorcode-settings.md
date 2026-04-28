---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-settings
title: 设置数据项错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > 设置数据项错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:10:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c61506c5a42243506b9a2fe4737dce6ee97c1868e6f2f204a1dbb8b21d0b6c9
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 14800000 参数检查失败

PhonePC/2in1TabletTVWearable

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

PhonePC/2in1TabletTVWearable

**错误信息**

Original service error.

**错误描述**

原始服务错误。

**可能原因**

当前上下文环境非UIAbility界面。

**处理步骤**

切换当前上下文环境，使用UIAbility模型。

## 16900010 参数检查失败

PhonePC/2in1TabletTVWearable

**错误信息**

Parameter error.

**错误描述**

参数类型或格式错误。

**可能原因**

1. 空参数错误 (Null Argument Error)。
2. 参数值范围错误 (Value Range Error)。

**处理步骤**

请检查必选参数是否传入。如果参数校验失败，请阅读参数规格约束，并根据可能原因进行排查。
