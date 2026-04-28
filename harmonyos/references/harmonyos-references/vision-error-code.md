---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-error-code
title: ArkTS API错误码
breadcrumb: API参考 > AI > Vision Kit（场景化视觉服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:19:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db019ff5396aa55a1d86a9eb6932135683344bcb4dd42c66e5d07d4d7d2af7e3
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1008301002 路由跳转失败

PhoneTablet

**错误信息**

Route switching failed.

**错误描述**

路由跳转失败。

**可能原因**

输入参数不符合要求，或路由跳转异常。

**处理步骤**

检查输入参数是否符合[InteractiveLivenessConfig](vision-interactive-liveness.md#interactivelivenessconfig)要求，过一段时间重试，并做好相关的逻辑判断。

## 1008302000 检测算法初始化

PhoneTablet

**错误信息**

Detection algorithm initialization.

**错误描述**

检测算法初始化未完成，无检测数据返回。

**可能原因**

获取结果时还未进行活体检测。

**处理步骤**

活体检测完成之后再获取结果。

## 1008302001 检测超时

PhoneTablet

**错误信息**

Detection timeout.

**错误描述**

检测超时，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

**可能原因**

检测时，长时间没有按照提示完成相关动作，导致检测超时了。

**处理步骤**

检测时请按提示完成相关动作。

## 1008302002 动作错误

PhoneTablet

**错误信息**

Action mutual exclusion error.

**错误描述**

动作错误，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

**可能原因**

检测时，没有按照提示完成相关动作，导致检测失败了。

**处理步骤**

检测时请按提示完成相关动作。

## 1008302003 连续性检测失败

PhoneTablet

**错误信息**

Continuity Check Failure.

**错误描述**

连续性检测失败，跳转失败页面。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

**可能原因**

检测多个动作时，没有按照提示完成相关动作，导致连续性检测失败了。

**处理步骤**

检测时请按提示完成相关动作。

## 1008302004 检测未完成

PhoneTablet

**错误信息**

The test is not complete.

**错误描述**

检测未完成。如果配置了失败页面或者back路由跳转，建议有重新检测的场景。

**可能原因**

检测过程中退出检测。

**处理步骤**

检测时请按提示完成相关动作。

## 1013700002 服务异常

PhonePC/2in1Tablet

**错误信息**

The service is abnormal.

**错误描述**

使用功能时，底层服务异常。

**可能原因**

1. 底层能力绑定失败。

**处理步骤**

建议在线提单，详细步骤请见[在线提单指导](https://developer.huawei.com/consumer/cn/support/feedback/#/)
