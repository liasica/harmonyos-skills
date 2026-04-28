---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api_error_code
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:11:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7fff45deb0302f9c75e7f0867f2ca9930068bee668e019b7ca938addf162aa1c
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1008500001 网络错误

PhoneTabletWearable

**错误信息**

Network error. The network is unavailable.

**错误描述**

网络错误。

**可能原因**

网络未连接。

**处理步骤**

1. 检查网络配置。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1008500002 无绑定设备

PhoneTabletWearable

**错误信息**

No device is bound.

**错误描述**

无绑定设备。

**可能原因**

当前没有穿戴设备与手机连接。

**处理步骤**

1. 检查设备是否已正确连接手机。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1008500003 设备未连接

PhoneTabletWearable

**错误信息**

Device disconnected.

**错误描述**

设备未连接。

**可能原因**

1. 手机同设备侧蓝牙断开。
2. 运动健康APP与设备侧断联。

**处理步骤**

1. 检查设备侧与手机侧的蓝牙是否打开。
2. 检查运动健康APP中是否已绑定并连接设备。
3. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1008500004 应用未申请Wear Engine服务

PhoneTabletWearable

**错误信息**

App has not applied for the Wear Engine service.

**错误描述**

手机侧应用未申请Wear Engine服务。

**可能原因**

1. 申请WearEngine服务时未配置兼容选项。
2. 开发者未在开发者联盟申请WearEngine服务。

**处理步骤**

1. 登录开发者联盟[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)，勾选兼容选项。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1008500005 用户未授权

PhoneTabletWearable

**错误信息**

The HUAWEI ID is not authorized.

**错误描述**

用户华为账号鉴权失败。

**可能原因**

接口所需权限用户尚未授权。

**处理步骤**

参考[请求用户授权](../harmonyos-guides/request_user_authorization.md)，确认用户已授权相关权限。

## 1008500006 用户未同意隐私授权

PhoneTabletWearable

**错误信息**

User privacy is not agreed.

**错误描述**

用户未同意运动健康隐私授权。

**可能原因**

用户从未打开过运动健康App。

**处理步骤**

引导用户启动运动健康App，进行隐私授权。

## 1008500007 穿戴设备侧能力不支持

PhoneTabletWearable

**错误信息**

The device capability is not supported.

**错误描述**

穿戴设备不支持对应的能力。

**可能原因**

穿戴设备侧不支持完成当前接口成功调用所需的能力。

**处理步骤**

核查设备能力集。

## 1008500008 账号未登录

PhoneTabletWearable

**错误信息**

Account error. The user has not logged in with HUAWEI ID.

**错误描述**

账号未登录。

**可能原因**

账号未登录。

**处理步骤**

登录华为账号后再重新调用接口。

## 1008500009 账号异常

PhoneTabletWearable

**错误信息**

Account error. Failed to obtain account information with HUAWEI ID.

**错误描述**

账号异常。

**可能原因**

使用的华为账号注册地非中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

**处理步骤**

更换注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）账号再操作。

## 1008500010 无效设备ID

PhoneTabletWearable

**错误信息**

Device ID is invalid.

**错误描述**

无效设备ID。

**可能原因**

1. 传入了错误的设备ID。
2. 传入了过期的设备ID。

**处理步骤**

调用[getConnectedDevices](wearengine_api.md#getconnecteddevices)接口重新获取设备ID。

## 1008500011 无效文件

PhoneTabletWearable

**错误信息**

File is invalid.

**错误描述**

无效文件。

**可能原因**

传入的文件为无效文件。

**处理步骤**

1. 检查文件路径是否合法。
2. 检查文件是否存在。

## 1008500012 回调函数过多

PhoneTabletWearable

**错误信息**

Too many callbacks of the same type.

**错误描述**

回调函数过多。

**可能原因**

在同一个type上注册了过多的回调函数。

**处理步骤**

及时关闭已经不再使用的监听事件。

## 1008509999 内部错误

PhoneTabletWearable

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

1. 应用的签名证书等信息和云端不一致。
2. [randomId](wearengine_api.md#device)错误。
3. 应用未在metadata中配置clientId。
4. 在AGC未上传证书指纹，或上传的不正确，或上传的未生效。
5. WearEngine发生未知错误。

**处理步骤**

1. 调试时检查应用的签名证书等信息，与开发者联盟是否一致。
2. 断开重连设备。
3. 在metadata中配置[clientId](../harmonyos-guides/configuration_client_id.md)。
4. 确保在AGC上传正式的证书指纹，上传后24小时内会生效。
5. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
