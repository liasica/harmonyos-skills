---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errcode-devicesecurity-superprivacy
title: SuperPrivacyMode（超级隐私模式）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > ArkTS API错误码 > SuperPrivacyMode（超级隐私模式）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:d0342993dbcbe4fad0a5e4dc968b403094b11d188e0998e36f15def98b04f1d3
---

说明

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1006200001 通用错误

**错误信息**

general error.

**错误描述**

超级隐私接口通用错误。

**可能原因**

接口执行流程中调用其它系统接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1006200002 内部错误

**错误信息**

internal error.

**错误描述**

超级隐私接口内部错误。

**可能原因**

超级隐私模式出现内部错误，数据读取失败。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1006200005 该设备不支持超级隐私模式

**错误信息**

not support super privacy.

**错误描述**

当前设备不支持超级隐私模式。

**可能原因**

当前设备不具备该功能。

**处理步骤**

在支持的设备上运行，具体支持情况请参见开发指南中的[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。
