---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam
title: 用户认证错误码
breadcrumb: API参考 > 系统 > 安全 > User Authentication Kit（用户认证服务） > 错误码 > 用户认证错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f26a6a6199f3a18026fcb49ad67076d210b21e44ad1683a33eb1f4fba4d90ef8
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 12500001 认证失败

PhonePC/2in1TabletWearable

**错误信息**

Authentication failed.

**错误描述**

认证失败。

**可能原因**

当前凭据与设备里已经录入的凭据比对失败。

**处理步骤**

重新发起认证。

## 12500002 身份认证系统通用错误码

PhonePC/2in1TabletWearable

**错误信息**

General operation error.

**错误描述**

开发者无法恢复的身份认证系统内部错误。

**可能原因**

1. NAPI层解析参数出错。
2. 用户认证服务的进程没有启动。
3. IPC通信的proxy客户端写数据出错。
4. IPC通信的stub服务端解析数据出错。
5. 获取driver服务出错。

**处理步骤**

系统服务内部工作异常，请稍后重新调用接口，或者重启设备尝试。

## 12500003 认证被取消

PhonePC/2in1TabletWearable

**错误信息**

Authentication canceled.

**错误描述**

认证被取消。

**可能原因**

1. 认证被用户手动取消。
2. 认证被后发起的认证请求抢占。

**处理步骤**

重新调用认证接口，发起认证。

## 12500004 认证操作超时

PhonePC/2in1TabletWearable

**错误信息**

Authentication timeout.

**错误描述**

认证操作超时。

**可能原因**

当前的认证操作超过了设定的时限。

**处理步骤**

重新调用认证接口，发起认证。

## 12500005 认证类型不支持

PhonePC/2in1TabletWearable

**错误信息**

The authentication type is not supported.

**错误描述**

认证类型不支持。

**可能原因**

1. 传入的认证类型参数不支持，例如调用userAuth模块的[getAvailableStatus](js-apis-useriam-userauth.md#userauthgetavailablestatus9)接口时传入的参数不是FACE或FINGERPRINT类型，则会返回12500005错误码。
2. 传入的认证类型参数在本设备上不支持，例如在没有部署指纹传感器的设备上发起指纹认证，则会返回12500005错误码。

**处理步骤**

请检查传入的认证类型参数，重新调用接口。

## 12500006 认证信任等级不支持

PhonePC/2in1TabletWearable

**错误信息**

The authentication trust level is not supported.

**错误描述**

认证信任等级不支持。

**可能原因**

1. 调用userAuth模块的[getAvailableStatus](js-apis-useriam-userauth.md#userauthgetavailablestatus9)或[getUserAuthInstance](js-apis-useriam-userauth.md#userauthgetuserauthinstance10)接口时，传入的authTrustLevel参数不在[ATL1, ATL2, ATL3, ATL4]范围内。
2. 当前的设备不支持该认证信任等级，例如在只部署了2D摄像头的设备上发起支付级别的人脸认证，则会返回12500006错误码。

**处理步骤**

检查传入的authTrustLevel是否在合理范围，如果在合理范围，则是当前的设备不支持该认证信任等级。

## 12500007 认证服务繁忙

PhonePC/2in1TabletWearable

**错误信息**

Authentication service is busy.

**错误描述**

认证服务繁忙。

**可能原因**

用户在身份认证控件界面点击了导航按钮时返回这个错误码，标识需要调用者拉起自定义认证界面。

**处理步骤**

稍后重新发起认证。

## 12500008 参数校验失败

PhonePC/2in1TabletWearable

**错误信息**

The parameter is out of range.

**错误描述**

参数取值超出合法范围。

**可能原因**

参数错误。

**处理步骤**

检查接口参数重新发起请求。

## 12500009 认证被锁定

PhonePC/2in1TabletWearable

**错误信息**

Authentication is locked out.

**错误描述**

认证被锁定。

**可能原因**

当前认证失败的次数超过了上限，触发防爆模式，认证被锁定。

**处理步骤**

稍后重新发起一次成功的认证。

## 12500010 该类型的凭据没有录入

PhonePC/2in1TabletWearable

**错误信息**

The type of credential has not been enrolled.

**错误描述**

该类型的凭据没有录入。

**可能原因**

例如调用userAuth模块的[getAvailableStatus](js-apis-useriam-userauth.md#userauthgetavailablestatus9)接口，传入的authType参数为FACE，但是当前的设备没有录入人脸凭据，则会返回12500010错误码。调用start接口发起人脸认证，但是目前的设备没有录入人脸凭据，则会返回12500010错误码。

**处理步骤**

检查是否录入该类型的凭据，如果没有录入，则需要成功录入该类型凭据后再调用相关接口。

## 12500011 提示/通知切换自定义认证

PhonePC/2in1TabletWearable

**错误信息**

Switched to the custom authentication process.

**错误描述**

切换到自定义认证流程。

**可能原因**

当前的认证操作被用户从控件取消，返回这个错误码，标识使用应用自定义认证。例如用户点击使用自定义认证，返回到应用自定义认证流程。

**处理步骤**

重新调用认证接口，发起认证。

## 12500013 密码过期

PhonePC/2in1TabletWearable

**错误信息**

Operation failed because of PIN expired.

**错误描述**

密码过期。

**可能原因**

由于系统锁屏口令过期，认证操作执行失败。当用户发起口令、指纹或者人脸认证，但是系统锁屏口令过期时，将会返回12500013错误码。

**处理步骤**

用户前往设置更新系统锁屏口令，再次发起认证。
