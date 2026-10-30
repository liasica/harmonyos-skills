---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-introduction
title: Account Kit简介
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit简介
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:54+08:00
doc_updated_at: 2026-10-30
content_hash: sha256:8a7ac0d65c39f17133a4ea508b9d39abbfd3c155c89a4ceef47fa8f0c4a14774
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

Account Kit提供的[华为账号登录按钮组件SampleCode](https://gitcode.com/HarmonyOS_Samples/application-services-snippets/tree/master/AccountKit/Accountkit-Samplecode-Clientdemo-HuaweiIDLogin-ArkTs)示例工程体现了Account Kit的[华为账号登录](account-unionid-login-button.md)、[自定义按钮登录](account-unionid-login-api.md)等特性，可参考该工程进行应用的相关内容开发。

## 约束与限制

| Account Kit提供的能力 | 能力描述 | 支持的开发者类型 | 支持的设备类型 |
| --- | --- | --- | --- |
| [华为账号一键登录](account-phone-unionid-login.md) | 使用该能力**需要申请“华为账号一键登录”权限**。华为账号一键登录是基于OAuth 2.0协议标准和OpenID Connect协议标准构建的OAuth 2.0授权登录系统，应用可以通过华为账号一键登录能力快捷地获取华为账号用户的身份标识和手机号，快速建立应用内的用户体系。 | 企业开发者 | Phone、Tablet、PC/2in1、TV |
| [华为账号登录](account-unionid-login-button.md) | 使用该能力**无需申请权限**。应用可以使用Account Kit提供的华为账号登录按钮组件及服务端交互获取华为账号用户身份标识UnionID、OpenID，通过UnionID、OpenID完成用户登录；或者与应用账号完成绑定，绑定后用于登录或者验证。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、TV |
| [自定义按钮登录](account-unionid-login-api.md) | 使用该能力**无需申请权限**。应用嵌入自定义登录按钮，调用华为账号登录API获取Authorization Code，与服务端交互获取UnionID、OpenID。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [静默登录](account-silent-login.md) | 使用该能力**无需申请权限**。在应用卸载重装、用户换机等场景，如登录的华为账号与重装、换机前一致，无需用户点击即可获取身份标识完成登录。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取头像昵称](account-get-avatar-nickname.md) | 使用该能力**无需申请权限**。当应用需要获取用户头像昵称信息，可使用Account Kit提供的头像昵称授权能力，用户允许应用获取头像昵称后，可快速完成个人信息填写。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取手机号](account-get-phonenumber.md) | 使用该能力**需要申请“获取您的手机号”权限**。当应用需要获取用户手机号时，可使用Account Kit提供的手机号授权能力，向用户发起手机号授权申请，经用户同意授权后，获取到手机号并为用户提供相应服务。 | 企业开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取收货地址](account-choose-address-dev.md) | 使用该能力**需要申请“获取收货地址”权限**。当应用需要获取用户收货地址时，可使用Account Kit提供的获取收货地址的能力，引导用户添加或选择已有的收货地址，并最终获取用户的收货地址。 | 企业开发者 | Phone、Tablet、PC/2in1、TV |
| [获取发票抬头](account-select-invoice-title.md) | 使用该能力**无需申请权限**。当应用需要获取用户发票抬头时，可使用Account Kit提供的发票助手能力，打开发票抬头选择页面，帮助用户快速选择或管理发票抬头。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1 |
| [获取风险等级](account-get-risklevel-introduction.md) | 使用该能力**需要申请权限**。当应用需要获取用户风险等级时，可使用Account Kit提供的获取用户风险等级能力。 | 企业开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [获取实名年龄段](account-get-realname-age.md) | 使用该能力**需要申请“获取您的年龄段”权限**。当应用需要获取用户实名年龄段信息时，可使用Account Kit的年龄段授权能力。用户授权后，应用可快速获取实名年龄段信息。 | 企业开发者 | Phone、Tablet、PC/2in1、Wearable、TV |
| [未成年人模式](account-overview-minorsprotection.md) | 使用该能力**无需申请权限**。应用通过接入Account Kit提供的未成年人模式能力与系统联动，可快速实现自动切换未成年人模式状态。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、TV |
| [华为账号按钮登录组件](../harmonyos-references/account-api-huawei-id-button.md) | 使用该能力**无需申请权限**。提供独立的华为账号登录按钮组件，支持多种样式，可嵌入应用自定义登录页面。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、TV |
| [华为账号登录面板组件](../harmonyos-references/account-api-loginpanel.md) | 使用该能力**无需申请权限**。提供半模态华为账号登录面板组件，集成登录按钮、隐私协议、其他登录方式入口等标准元素。 | 企业开发者、个人开发者 | Phone、Tablet、PC/2in1、TV |

### 支持的国家/地区

请参见[支持的国家/地区](account-appendix-support-regions.md)。

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* Wearable设备模拟器不支持Account Kit相关能力。其他模拟器仅支持应用统一认证服务[authentication](../harmonyos-references/account-api-authentication.md)的登录和授权能力、[华为账号Button登录组件](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton)。
