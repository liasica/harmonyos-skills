---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-fusionconnectivity
title: 融合短距服务子系统错误码
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 错误码 > 融合短距服务子系统错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:08:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af8a5c7ed5eddfb71099ca511d4b6ca8660add9355cc2c4e85667c0dd86f7fbb
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 34900001 设备未注册

PhonePC/2in1Tablet

**错误信息**

The device is not bound.

**错误描述**

该设备未注册。

**可能原因**

应用未调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)注册设备。

**处理步骤**

应用调用[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)注册设备。

## 34900003 设备未配对

PhonePC/2in1Tablet

**错误信息**

The device is not paired.

**错误描述**

设备未配对。

**可能原因**

应用注册的设备未经过蓝牙配对。

**处理步骤**

执行设备蓝牙配对流程。

## 34900004 设备地址已被注册

PhonePC/2in1Tablet

**错误信息**

The device address has already been bound with PartnerAgentExtensionAbility.

**错误描述**

该设备地址已经注册过[PartnerAgentExtensionAbility](is-fusionconnectivity-partneragentextensionability.md)。

**可能原因**

应用重复注册一个地址。

**处理步骤**

应用调用[unbindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentunbinddevice)解注册当前设备，再重新注册[bindDevice](js-apis-fusionconnectivity-partneragent.md#partneragentbinddevice)新的Ability。

## 34900005 蓝牙关闭

PhonePC/2in1Tablet

**错误信息**

Bluetooth disabled.

**错误描述**

蓝牙关闭。

**可能原因**

蓝牙处于关闭状态。

**处理步骤**

打开蓝牙。

## 34900099 操作失败

PhonePC/2in1Tablet

**错误信息**

Operation failed.

**错误描述**

操作失败。

**可能原因**

因系统原因导致当前操作失败。

**处理步骤**

请重试该操作。
