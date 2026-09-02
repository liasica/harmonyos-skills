---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nearlink
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1fe3cf1fc51b930cafeef5b7af2fc11352d8ecaec0472438efac495338b787b5
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1009700003

**错误信息**

NearLink is off.

**错误描述**

当星闪开关未打开时调用接口，将返回该错误码。

**可能原因**

星闪开关未打开。

**处理步骤**

在设备的设置界面，通过“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径打开星闪后重试，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700020

**错误信息**

The UUID is already registered.

**错误描述**

当对应UUID的端口通道已经被注册，将返回该错误码。

**可能原因**

重复调用注册端口通道接口并传入相同UUID。

**处理步骤**

调用[dataTransfer.destroyPort](nearlink-data-transfer-api.md#destroyport)接口销毁对应UUID的端口通道，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700021

**错误信息**

The number of ports exceeds the upper limit.

**错误描述**

端口注册数量超上限，将返回该错误码。

**可能原因**

数据传输业务通道分配达到上限。

**处理步骤**

调用[dataTransfer.destroyPort](nearlink-data-transfer-api.md#destroyport)接口销毁其他已注册的端口通道，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700022

**错误信息**

The UUID is not registered.

**错误描述**

没有注册对应UUID的端口。

**可能原因**

尝试销毁一个未注册的端口。

**处理步骤**

确认要销毁的端口已注册，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700023

**错误信息**

The data writing process is congested.

**错误描述**

发送数传数据异常。

**可能原因**

协议层或芯片处理数据拥塞。

**处理步骤**

控制数据写入流量，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700050

**错误信息**

Coordinated Devices Set Management not supported.

**错误描述**

不支持合作设备集管理。

**可能原因**

本设备不支持合作设备集管理特性。

**处理步骤**

如需使用合作设备集功能，请使用支持星闪合作设备集管理特性的设备，比如支持星闪音频的部分手机、平板等，或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1009700099

**错误信息**

Operation failed.

**错误描述**

当系统内部处理出错，将返回该错误码。

**可能原因**

其他未知错误。

在设备已配对的情况下再调用[startPairing](nearlink-remote-device.md#startpairing)发起配对，会返回该错误码。

**处理步骤**

进行重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
