---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-assessment
title: 评估管理错误码
breadcrumb: API参考 > 系统 > 基础功能 > Automatic Scene Configuration Kit（场景配置服务） > 错误码 > 评估管理错误码
category: harmonyos-references
scraped_at: 2026-11-12T09:55:50+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:26eed3a5f6be8dbf6fed2346747a9685fefd0ce070a6608e7fe1341ec1fcbb6a
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 36700001 评估内部错误

**错误信息**

Assessment internal error. Possible cause: IPC invocation failed internally.

**错误描述**

调用begin或end接口时，评估配置服务发生内部错误，操作失败，系统会产生此错误码。

**可能原因**

评估配置服务内部IPC调用失败。

**处理步骤**

重新调用接口尝试。若多次重试仍失败，请检查评估配置服务运行状态，或联系设备厂商技术支持。

## 36700002 评估配置服务已处于活动状态

**错误信息**

Assessment configuration service is already active. Possible cause: Assessment resource conflict.

**错误描述**

设备已处于评估状态时，再次调用begin接口，评估资源冲突，无法重复开始评估，系统会产生此错误码。

**可能原因**

1. 当前应用上一次评估尚未结束，再次调用begin接口开始新的评估。
2. 其他应用已开启评估且尚未结束。

**处理步骤**

1. 调用isActive接口查询当前评估状态。若返回true，先调用end接口结束当前评估，再开始新的评估。
2. 确认是否有其他应用已开启评估且尚未结束。如有，需由开启评估的应用调用end接口结束评估后，再开始新的评估。

## 36700003 评估配置服务未处于活动状态

**错误信息**

Assessment configuration service is not active. Possible cause: Not in assessment state.

**错误描述**

设备未处于评估状态时调用end接口，系统会产生此错误码。

**可能原因**

当前不存在进行中的评估，调用了end接口。

**处理步骤**

调用isActive接口确认当前评估状态，仅在返回true时调用end接口结束评估。

## 36700004 非法操作

**错误信息**

Invalid operation. Possible cause: Cannot terminate another active assessment.

**错误描述**

调用end接口时，尝试结束非本应用开启的评估，系统会产生此错误码。

**可能原因**

当前进行中的评估由其他应用开启，本应用无权结束该评估。

**处理步骤**

确认评估的开启方，由开启评估的应用调用end接口结束评估。
