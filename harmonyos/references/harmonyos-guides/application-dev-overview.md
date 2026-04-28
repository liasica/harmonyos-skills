---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview
title: 应用开发准备
breadcrumb: 指南 > 应用开发准备 > 应用开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e752ce5e269d877684cadf5feba39db70ee77433531a6032773bdd6ffbf3b75
---

在开始应用开发前，需要先完成以下准备工作。

## 注册成为开发者

在华为开发者联盟网站上，[注册成为开发者](../start/registration-and-verification-0000001053628148.md)，并完成[实名认证](../start/rna-0000001062530373.md)，从而享受联盟开放的各类能力和服务。

## 创建应用

在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)（简称AGC）上，参考[创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建应用](../app/agc-help-create-app-0000002247955506.md)完成**HarmonyOS**应用的创建，从而使用各类服务。

## 配置安装DevEco Studio

安装最新版[DevEco Studio](https://developer.huawei.com/consumer/cn/download/)。具体安装指导请参见[安装DevEco Studio](ide-software-install.md)。

## 使用DevEco Studio创建应用工程

使用DevEco Studio创建应用工程。具体创建工程指导请参见[创建一个新的工程](ide-create-new-project.md)。

## 配置签名信息

使用模拟器和预览器调试无需配置签名信息，使用真机设备调试则需要对HAP进行签名。

目前提供了两种签名方式，请根据实际情况选择：

* [自动签名](ide-signing.md#section18815157237)：如果您只需要使用一台调试设备，建议使用DevEco Studio提供的自动签名。
* 手动签名：如果您使用多台调试设备或者会在断网情况下调试，您需要在AGC中[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)后，再[手动配置签名信息](ide-signing.md#section1240072619462)。

## （条件必选）添加公钥指纹

当应用需要使用以下开放能力的一种或多种时，为正常调试运行应用，需要预先添加公钥指纹。

* Account Kit（华为账号服务）
* Game Service Kit（游戏服务）
* Health Service Kit（运动健康服务）
* IAP Kit（应用内支付服务）
* Payment Kit（华为支付服务）
* Wallet Kit（钱包服务）
* Wear Engine Kit（穿戴服务）

说明

发布应用前，需要将调试应用的指纹更新为发布指纹。

添加公钥指纹，具体操作请参见[配置应用签名证书指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。
