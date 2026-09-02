---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-antifraudpicker
title: AntifraudPicker（反诈选择器）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > ArkTS API错误码 > AntifraudPicker（反诈选择器）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99a9475f3ef32e1e4c975e5539725932023aa0b9ed1941fdaaa6bbb72df9bbc4
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 201 权限校验失败

**错误信息**

Permission denied.

**错误描述**

权限校验失败。

**可能原因**

应用hap未申请ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER、ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER或ohos.permission.USE\_FRAUD\_APP\_PICKER权限。

**处理步骤**

只允许符合使用场景的应用申请该权限。在举报诈骗消息场景下，使用诈骗消息选择器时，需要先申请权限：ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER。在举报诈骗通话记录场景下，在使用诈骗通话记录选择器时，需要申请权限：ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER。申请方式请参考：[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。

## 401 参数检查失败

**错误信息**

Parameter error.

**错误描述**

参数检查失败。

**可能原因**

必选参数没有传入，或者参数类型、规格错误。

**处理步骤**

请检查必选参数是否没有传入，或者传的参数类型、规格是否错误。

## 1017100001 未知异常

**错误信息**

Unknown error.

**错误描述**

内部异常。

**可能原因**

接口执行流程中调用系统其它接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1017100002 不支持的设备类型

**错误信息**

The device type is not supported.

**错误描述**

不支持的设备类型异常。

**可能原因**

设备不是手机或平板。

**处理步骤**

将设备换成手机或平板后，重新发起请求。

## 1017600001 未知异常

**错误信息**

Unknown error.

**错误描述**

诈骗应用选择器内部异常。

**可能原因**

接口执行流程中调用系统其它接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1017600002 不支持的设备类型

**错误信息**

The device type is not supported.

**错误描述**

诈骗应用选择器不支持的设备类型异常。

**可能原因**

设备不是手机或平板。

**处理步骤**

将设备换成手机或平板后，重新发起请求。

## 1017600003 参数检查失败

**错误信息**

Parameter verification failed.

**错误描述**

反诈选择器接口参数检查失败。

**可能原因**

必选参数没有传入，或者参数类型、规格错误。

**处理步骤**

请检查必选参数是否没有传入，或者传的参数类型、规格是否错误。
