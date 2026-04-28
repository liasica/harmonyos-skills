---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-introduction
title: Account Kit简介
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62ebd267aa9895a0d85c018e2c3719da12869d0c6335a780b59c337127aa2527
---

## 场景介绍

Account Kit（华为账号服务）提供简单、快速、安全的登录功能，让用户快捷地使用华为账号登录应用。用户授权后，Account Kit可提供头像、昵称、手机号码等信息，帮助应用更了解用户。

## 能力范围

* [登录](account-quick-login-overview.md)：提供登录服务，让用户使用华为账号快速登录应用。
* [获取华为账号用户信息](account-get-user-info-overview.md)：获取用户的基本开放信息，如头像、昵称、手机号、收货地址、发票抬头、风险等级。
* [未成年人模式](account-overview-minorsprotection.md)：获取未成年人模式的开启状态及年龄段信息以进行内容分级，调整未成年人相关设置时可增加家长验证，还可调用接口引导用户开启或关闭未成年人模式。

## 亮点/特征

**一键登录**

应用可以通过华为账号一键登录功能获取手机号授权并完成登录，帮助应用建立用户体系或者打通原有的用户体系。优点如下：

* 便捷性：一键完成登录和手机号授权，为用户提供更加便捷易用的登录体验。
* 全场景：Phone、Tablet、PC/2in1设备登录体验一致，保障用户数据资产跨端延续。
* 效率高：无需单独集成SDK，减少开发者开发和运营成本。

**未成年人模式**

应用可以通过未成年人模式的相关能力帮助家长快速开启未成年人模式，守护未成年人健康使用电子设备和应用。有以下优点：

* 便捷性：统一管控未成年人模式入口，仅需一次设置，应用联动生效，避免各个应用内单独开启的繁琐操作，提升用户体验。
* 全面守护：应用与系统联动，为孩子提供全面的守护措施，如仅允许访问适龄应用、增强隐私保护、限制设备使用时长等。

## 示例代码

Account Kit提供的[SampleCode示例工程](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts)体现了Account Kit的[华为账号一键登录](account-phone-unionid-login.md)、[静默登录](account-silent-login.md)、[获取头像昵称](account-get-avatar-nickname.md)、[快速验证手机号](account-get-phonenumber.md)、[收货地址](account-choose-address-dev.md)、[发票抬头](account-select-invoice-title.md)、[未成年人模式](account-overview-minorsprotection.md)等特性，可参考该工程进行应用的相关内容开发。

## 基本概念

* **OpenID**：应用维度用户标识符，是华为账号用户在应用/元服务的唯一标识。不同应用/元服务（不管是否在同一个开发者账号下）获取到用户的OpenID不同。OpenID严格区分大小写。
* **UnionID**：开发者维度用户标识符，华为账号用户同一开发者账号下的唯一标识。开发者有多个应用/元服务时，同一个开发者账号下的应用/元服务获取到用户的UnionID相同。UnionID严格区分大小写。
* **GroupUnionID**：关联主体账号组维度用户标识符，是华为账号用户在关联主体账号组内的唯一标识。不同开发者账号加入同一关联主体账号组后，其组内所有开发者的应用/元服务获取到用户的GroupUnionID相同。
* **permission**：数据或接口权限，通过该权限判断应用是否能获取对应数据或调用对应接口。
* **scopes**：scope列表，用于获取用户数据。开发者向华为账号服务申请不同类型用户数据的标识。比如头像昵称（profile）、匿名手机号（quickLoginAnonymousPhone）等。
* **Authorization Code**：授权码，用户使用华为账号登录成功之后，可通过返回的凭据解析出授权码，通过授权码可获取Access Token、Refresh Token、ID Token等。
* **Access Token**：访问凭证，是访问被权限管控资源的应用级凭证。可使用Access Token调用获取用户信息接口获取用户信息。
* **ID Token**：用户身份凭证，是OIDC（[OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)）协议相对于OAuth 2.0协议扩展的一个用户身份凭证，包含用户信息。用户使用华为账号登录成功之后，可通过返回的凭据解析出Authorization Code、ID Token等数据。

## 约束与限制

| Account Kit提供的能力 | 支持的设备类型 |
| --- | --- |
| [获取头像昵称](account-get-avatar-nickname.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取手机号](account-get-phone-overview.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取收货地址](account-choose-address-dev.md) | Phone、Tablet、PC/2in1 |
| [获取发票抬头](account-select-invoice-title.md) | Phone、Tablet、PC/2in1 |
| [获取风险等级](account-get-risklevel-introduction.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [未成年人模式](account-overview-minorsprotection.md) | Phone、Tablet、PC/2in1、TV |
| [华为账号登录组件](../harmonyos-references/account-api-loginpanel.md) | Phone、Tablet、PC/2in1、TV |

### 支持的国家/地区

请参见[支持的国家/地区](account-appendix-support-regions.md)。

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器仅支持应用统一认证服务[authentication](../harmonyos-references/account-api-authentication.md)的登录和授权能力、[华为账号Button登录组件](../harmonyos-references/account-api-huawei-id-button.md)。
