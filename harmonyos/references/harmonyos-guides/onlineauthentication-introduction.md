---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-introduction
title: Online Authentication Kit简介
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > Online Authentication Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dfae9f89092204e87f8fd5be63831f535ff448c366dcce7acb771431714a102e
---

Online Authentication Kit（在线认证服务）遵循FIDO（Fast Identity Online）、FIDO2、IIFAA（互联网可信认证联盟）和SOTER标准免密认证规范，提供免密身份认证的移动端能力。用户应用接入FIDO、FIDO2、IFAA或SOTER服务器后，可以使用相应的移动端能力，用生物特征（例如指纹、3D人脸）代替密码，实现免密登录、免密支付等业务场景。

## FIDO

FIDO是一种国际主流的免密认证标准，几乎所有的设备厂商都支持FIDO免密认证协议，同时众多生态APP厂商也广泛使用依赖该能力，包括中国工商银行，中国银行，农业银行，交通银行等各大行，以及众多证券，金融APP。

说明

请参考[sample-FIDOclientdemo](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_-fidoclientdemo_-arkts)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## IFAA

IIFAA互联网可信认证联盟，是2015年由中国信通院、蚂蚁集团、阿里巴巴、华为、中兴、三星联合发起的可信认证生态联盟。联盟致力于推动可信认证技术发展及行业应用，引领行业制定技术规范。其中本地免密技术规范，用于支持免密登录，免密支付等业务场景。

说明

请参考[sample-IFAAclientdemo](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit-sample-ifaaclientdemo-arkts)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## SOTER

SOTER提供一套生物认证平台和标准，使得业务可以采用设备上的传感器（如人脸传感器/指纹传感器）进行安全、高效的免密登录、免密支付等操作，当前已广泛应用于微信小程序/公众号、指纹支付等业务场景。

说明

请参考[samplecode-SOTERclientdemo](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_samplecode_-soterclientdemo_-arkts)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## 通行密钥

通行密钥（Passkey）是基于[FIDO2标准协议](https://fidoalliance.org/passkeys/)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）实现的一种简单又安全的登录方式。借用通行密钥，用户可使用指纹、人脸或手机解锁PIN码登录应用。相较于传统密码，通行密钥具有更便捷、安全的优势。

说明

请参考[samplecode-FIDO2clientdemo-arkts](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_arkts)以及[samplecode-FIDO2clientdemo-cpp](https://gitcode.com/HarmonyOS_Samples/online-authenticationkit_sample_fido2clientdemo_cpp)（见[网站链接免责声明](onlineauthentication-website-disclaimer.md)）。

## 场景介绍

支持IIFAA和FIDO免密身份认证的场景如下：

* 开通：开通（指纹/3D人脸）免密身份认证。
* 认证：使用（指纹/3D人脸）进行免密身份认证。
* 注销：注销已开通的（指纹/3D人脸）免密身份认证。

注：IFAA在本文中指HarmonyOS系统免密认证模块，IIFAA在本文中指联盟及相关技术规范。

支持通行密钥的场景如下：

* 通行密钥注册：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，在本设备上创建应用或网页的通行密钥。
* 本地免密认证：支持使用用户身份认证特征（如人脸、指纹、PIN码）作为平台认证器，使用通行密钥在本设备上进行应用或网页的免密认证。
* 跨设备扫码认证：支持使用已注册通行密钥的移动设备作为漫游认证器，使用跨设备扫码的方式，在其他设备上进行应用或网页的免密认证。

## 约束与限制

### 支持的国家和地区

中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

本Kit仅适用于Phone、PC/2in1、Tablet。

### 能力使用限制

Online Authentication Kit提供的FIDO、IFAA、SOTER及通行密钥能力有以下使用限制：

* 开发者应用需要部署相应的服务端。
* 要使用指纹或3D人脸的免密身份认证能力，移动端设备需要支持相应的生物特征，查询当前移动端设备是否支持可参见[User Authentication Kit](obtain-supported-authentication-capabilities.md)（需设备支持ATL4级别的认证可信等级）。
* 移动端设备在使用此能力时需要处于联网状态。

## 模拟器支持情况

本Kit暂不支持模拟器。
