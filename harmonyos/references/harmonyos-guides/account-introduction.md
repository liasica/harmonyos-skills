---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-introduction
title: Account Kit简介
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:54b879a6d38fe05ddfc2b8b890e65271b7f7a599e4332e0de5eb9281806b6eb6
---

## 场景介绍

Account Kit（华为账号服务）提供简单、快速、安全的登录功能，让用户快捷地使用华为账号登录应用。用户授权后，Account Kit可提供头像、昵称、手机号码等信息，帮助应用更了解用户。

## 能力范围

* [登录](account-quick-login-overview.md)：提供登录服务，让用户使用华为账号快速登录应用。
* [获取华为账号用户信息](account-get-user-info-overview.md)：获取用户的基本开放信息，如头像、昵称、手机号、收货地址、发票抬头、风险等级。
* [未成年人模式](account-overview-minorsprotection.md)：获取未成年人模式的开启状态及年龄段信息以进行内容分级，调整未成年人相关设置时可增加家长验证，还可调用接口引导用户开启或关闭未成年人模式。

## 亮点/特征

**一键登录**

应用可以通过华为账号一键登录功能获取手机号授权并完成登录，帮助应用建立用户体系或者与现有用户体系对接。优点如下：

* 便捷性：一键完成登录和手机号授权，为用户提供更加便捷易用的登录体验。
* 全场景：Phone、Tablet、PC/2in1、TV设备登录体验一致，保障用户数据资产跨端延续。
* 效率高：无需单独集成SDK，减少开发者开发和运营成本。

**未成年人模式**

应用可以通过未成年人模式的相关能力帮助家长快速开启未成年人模式，守护未成年人健康使用电子设备和应用。有以下优点：

* 便捷性：统一管控未成年人模式入口，仅需一次设置，应用联动生效，避免各个应用内单独开启的繁琐操作，提升用户体验。
* 全面守护：应用与系统联动，为孩子提供全面的守护措施，如仅允许访问适龄应用、增强隐私保护、限制设备使用时长等。

## 示例代码

Account Kit提供的[SampleCode示例工程](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts)体现了Account Kit的[华为账号一键登录](account-phone-unionid-login.md)、[静默登录](account-silent-login.md)、[获取头像昵称](account-get-avatar-nickname.md)、[获取手机号](account-get-phonenumber.md)、[收货地址](account-choose-address-dev.md)、[发票抬头](account-select-invoice-title.md)、[未成年人模式](account-overview-minorsprotection.md)等特性，可参考该工程进行应用的相关内容开发。

## 约束与限制

| Account Kit提供的能力 | 支持的设备类型 |
| --- | --- |
| [获取头像昵称](account-get-avatar-nickname.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取手机号](account-get-phonenumber.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取收货地址](account-choose-address-dev.md) | Phone、Tablet、PC/2in1、TV |
| [获取发票抬头](account-select-invoice-title.md) | Phone、Tablet、PC/2in1 |
| [获取风险等级](account-get-risklevel-introduction.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取实名年龄段](account-get-realname-age.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [未成年人模式](account-overview-minorsprotection.md) | Phone、Tablet、PC/2in1、TV |
| [登录按钮组件](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton) | Phone、Tablet、PC/2in1、TV |
| [登录面板组件](../harmonyos-references/account-api-loginpanel.md#loginpanel) | Phone、Tablet、PC/2in1、TV |

### 支持的国家/地区

请参见[支持的国家/地区](account-appendix-support-regions.md)。

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器仅支持应用统一认证服务[authentication](../harmonyos-references/account-api-authentication.md)的登录和授权能力、[华为账号Button登录组件](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton)。
* 不支持Wearable设备模拟器。
