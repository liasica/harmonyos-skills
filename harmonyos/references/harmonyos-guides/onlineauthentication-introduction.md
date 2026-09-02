---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-introduction
title: Online Authentication Kit简介
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > Online Authentication Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9165f4c682910bd93a80b7093b79aea28c801f1ba2eda78cbf13a3fe61694714
---

Online Authentication Kit（在线认证服务）遵循多种端云在线身份认证协议，提供相应的免密认证、数字身份相关协议的移动端的能力。应用部署符合协议的服务器后，可以使用移动端相应的能力，实现免密认证和数字身份业务场景。

## 场景介绍

### 免密认证

基于账号密码的应用方式因输入复杂、难于记忆且易遭受网络钓鱼攻击等问题，在便捷性与安全性方面均存在不足。Online Authentication Kit遵循FIDO（Fast Identity Online）、FIDO2、IIFAA（International Internet Finance Authentication Alliance）和SOTER免密认证协议，可以支撑应用通过人脸/指纹方式进行免密认证登录，利用生物特征等来代替传统的密码，实现免密登录、免密支付等业务场景，有效提高了登录便捷性，同时也增强了安全性。

* **FIDO**：FIDO是一种国际主流的免密认证标准，众多生态应用厂商广泛使用FIDO免密认证协议，包含银行应用、证券或金融应用。
* **IFAA**：IIFAA互联网可信认证联盟，是2015年由中国信通院、蚂蚁集团、阿里巴巴、华为、中兴、三星联合发起的可信认证生态联盟。联盟致力于推动可信认证技术发展及行业应用，引领行业制定技术规范。其中IIFAA本地免密技术规范，用于支持免密登录、免密支付等业务场景。

  **说明** 

  IFAA在本文中指HarmonyOS系统免密认证模块，IIFAA在本文中指联盟及相关技术规范。
* **SOTER**：SOTER提供一套生物认证平台和标准，使得业务可以采用设备上的传感器（如人脸传感器/指纹传感器）进行安全、高效的免密登录、免密支付等操作，当前已广泛应用于微信小程序/公众号的指纹支付等业务场景。
* **通行密钥**：通行密钥（Passkey）是基于[FIDO2标准协议](https://fidoalliance.org/passkeys/)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）实现的一种简单又安全的登录方式。借用通行密钥，用户可使用指纹、人脸或手机解锁PIN码登录应用。相较于传统密码，通行密钥具有更便捷、安全的优势。

### 数字身份

针对传统身份凭证验证方式（如上传证件照片）存在的体验繁琐、隐私泄露等风险，Online Authentication Kit提供数字身份能力，支持DID（Decentralized Identifiers）分布式数字身份协议，可以支撑业务将数字化身份凭证安全存储于设备终端，用户通过生物认证授权安全便捷地使用凭证。在优化用户体验的同时，有效增强用户身份信息的隐私性与安全性。

DID是一种基于区块链的分布式数字身份协议，具备去中心化、可部分披露等特点，可实现数字身份的跨平台互通互认。Online Authentication Kit提供了符合DID协议的移动端的数字身份能力，结合应用在云侧部署的DID身份服务，可实现完整的跨平台数字身份业务场景。

## 约束与限制

### 支持的国家和地区

中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

| 能力 | 支持设备 |
| --- | --- |
| FIDO免密认证、IFAA免密认证、SOTER免密认证 | Phone（5.0.0(12)）、Tablet（5.0.0(12)）、PC/2in1（5.0.1(13)） |
| 通行密钥 | Phone（6.0.0(20)）、Tablet（6.0.0(20)）、PC/2in1（6.0.0(20)） |
| 数字身份 | Phone（26.0.0）、Tablet（26.0.0） |

### 能力使用限制

Online Authentication Kit提供的FIDO、IFAA、SOTER、通行密钥及数字身份能力有以下使用限制：

* 应用需要部署相应协议的服务器端。
* 要使用指纹或3D人脸的免密身份认证能力，移动端设备需要支持相应的生物特征，查询当前移动端设备是否支持可参见[User Authentication Kit](obtain-supported-authentication-capabilities.md)（需设备支持ATL4级别的认证可信等级）。
* 移动端设备在使用此能力时需要处于联网状态。

## 模拟器支持情况

本Kit暂不支持模拟器。
