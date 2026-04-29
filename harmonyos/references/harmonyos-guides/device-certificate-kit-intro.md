---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-certificate-kit-intro
title: Device Certificate Kit简介
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > Device Certificate Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f89e3e47d253add5f8da064785ce9f24ba1a9df9372fa27239280d232bfd5430
---

Device Certificate Kit（设备证书服务）面向应用开发者，提供了[证书算法库](device-certificate-kit-intro.md#证书算法库)和[证书管理](device-certificate-kit-intro.md#证书管理)的能力。

## 证书算法库

证书算法库提供接口用于解析和验证数字证书。

证书算法库向应用提供证书、证书扩展域段、证书吊销列表的解析及校验能力，以及证书链的校验能力。

通过调用证书算法库框架接口，开发者可以忽略底层不同三方算法库的差异，实现快速开发。

**常见使用场景**

应用对接收的服务端证书或用户输入的证书进行解析，获取证书基本字段或扩展字段用于显示或校验，并使用CA证书链和CRL校验证书的合法性。

### 框架原理

系统提供证书算法库框架，开发者只需要调用API接口层即可实现证书的操作，证书算法库框架能够屏蔽不同三方算法库的差异。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ch-qKnLXRh6kWcPKHQj_vA/zh-cn_image_0000002589244681.png?HW-CC-KV=V1&HW-CC-Date=20260429T053120Z&HW-CC-Expire=86400&HW-CC-Sign=F05B6AEFCF2AB49D540CD107B1BFE1EB17FE3456D96A572EE4A1EFBBAC5CF586)

### 与相关Kit的关系

证书算法库的功能使用时，涉及公钥的生成和获取，这部分依赖[Crypto Architecture Kit](crypto-architecture-kit-intro.md)加解密算法框架服务的能力。

## 证书管理

证书管理主要提供系统级的证书管理能力，通过证书管理模块可以确保证书在传输和存储过程中的安全性，防止未经授权的访问和使用。

当前提供的能力包括：

1. 应用证书凭据的安装、获取、使用及删除的能力。
2. 用户CA证书的安装、获取及删除的能力。
3. 应用可以调用证书管理提供的接口拉起证书管理应用界面对CA证书、凭据进行管理。

通过证书管理能力，可以实现证书全生命周期（安装、存储、使用和销毁）的管理和安全使用。

**常见使用场景**

1. 应用证书凭据的使用场景包括：业务安装应用证书凭据，在网络链接双向认证的场景下，使用应用证书凭据对业务数据进行签名，并获取应用证书凭据，将签名结果和应用证书凭据发送对端，最后删除应用证书凭据。
2. 用户CA证书的使用场景包括：业务安装用户CA证书，在网络链接过程中获取用户CA证书以校验对端身份，在证书过期或被吊销的情况下可以删除用户CA证书。
3. 证书管理对话框使用场景：业务调用证书管理提供的对话框接口，直接拉起证书管理应用界面，可以实现证书的查看、安装、删除以及凭据的安装、查看、删除操作。

### 与相关Kit的关系

证书管理的功能使用时，涉及凭据的安装和使用，这部分依赖[Universal Keystore Kit](huks-overview.md)密钥管理服务的能力。

## 约束与限制

Device Certificate Kit不具备生成或签发证书及证书吊销列表的能力。生成或签发证书及证书吊销列表的能力由证书颁发机构（CA）来完成，不由单个应用签发。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见详情请参见[模拟器与真机的差异](ide-emulator-specification.md)。
