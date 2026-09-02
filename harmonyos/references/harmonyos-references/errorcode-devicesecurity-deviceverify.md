---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicesecurity-deviceverify
title: DeviceVerify（应用设备状态检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > ArkTS API错误码 > DeviceVerify（应用设备状态检测）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad92132d2a30cfb552b8900e010b191b53cdc30bd52f40ae67217874bd3199a7
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 201 权限校验失败

**错误信息**

has no permission.

**错误描述**

权限校验失败。

**可能原因**

应用hap未开通Device Security服务。

**处理步骤**

1. 请参见[开通Device Security服务](../harmonyos-guides/devicesecurity-deviceverify-activateservice.md)在AppGallery Connect开启“应用设备状态检测”开关。
2. 重新[申请调试Profile](../app/agc-help-add-debugprofile-0000001914423102.md)，将新申请到的Profile作为工程的签名文件后重试。

## 1003300005 内部异常

**错误信息**

internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. Access device certificate failed.

**错误描述**

内部异常。

**可能原因**

接口执行流程中调用系统其它接口出现异常。

**处理步骤**

请优先重试，若重试不成功，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请帮助。

## 1003300006 访问云端服务器异常

**错误信息**

access cloud server fail.

**错误描述**

访问云端服务器异常。

**可能原因**

设备未联网或设备网络不稳定。

**处理步骤**

如未联网，请连接网络后重新发起请求，如联网，可能是网络不稳定，请重试。
