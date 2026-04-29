---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-intro
title: 应用真实性证明简介
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 应用真实性证明简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:446301af2109aba22abaf9a1fb10dd4419e48be10c36127a58d46db09cbc839a
---

您可以利用应用真实性证明能力在服务器验证来自应用的请求，具体包括验证请求是否源自真实应用、真实设备，以及请求内容是否未经篡改。

说明

为方便您理解此功能的应用场景，提高接入效率，特此更新该文档，原《设备真实性证明》文档更改为《应用真实性证明》。

## 基础概念

* 应用公私钥对：用于验证应用请求真实性的非对称算法密钥对，包含应用公钥和应用私钥，比如RSA、ECC算法的密钥对。
* 应用公钥ID：为应用公钥生成的唯一ID，用于您的应用服务器标识和查找应用公钥。
* 应用ID：包含了应用身份相关的信息，如应用包名，应用签名密钥Hash。
* 密钥证明证书链：华为服务器在验证应用公钥来自真实的设备和真实的应用后签发的证书链，证书链中包含了应用公钥和您的应用ID。

## 概述

您的应用可以通过调用Universal Keystore Kit相关接口，并在您的服务器上完成对应的校验，以验证应用请求的真实性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/UUUGrkqLRoOOm2hbQhf5Qg/zh-cn_image_0000002589244717.png?HW-CC-KV=V1&HW-CC-Date=20260429T053208Z&HW-CC-Expire=86400&HW-CC-Sign=E149E3F0DFB716980184F5B90B607E1BD3B1EBD4A89E76E523D2482ECE92B287)

本文介绍如何在您的应用和应用服务器上验证应用请求真实性，使用过程为：

**前置操作：创建密钥确立可信凭证**（一个用户只需要进行一次此操作）

1. 应用调用Universal Keystore Kit的密钥生成接口，创建一对唯一的应用公私钥对，该公私钥对存储在基于硬件的安全环境。
2. 应用再调用Universal Keystore Kit的密钥证明接口，对应用公钥和应用ID签发密钥证明证书链。
3. 应用服务器对密钥证明证书链进行校验，以及校验证书链中的应用ID是否正确。
4. 应用服务器保存密钥证明证书链中的应用公钥，并与登录用户进行关联。

   说明

   在应用创建的应用公私钥对和服务器保存的应用公钥可用的情况下，您不应该重复进行上述的创建密钥确立可信凭证流程。

**业务请求证明：签名验签识别真实请求**

1. 应用进行关键业务处理时（如免密支付、营销活动）调用Universal Keystore Kit的签名接口，使用应用私钥对业务请求进行签名。
2. 应用服务器使用保存的应用公钥对签名进行验签，验签成功即可说明该请求来自真实的设备和应用，以及内容未被篡改。

本方案通过华为服务器证明应用公钥来自真实的设备并签发密钥证明证书链，从而**识别模拟器等非真实设备**的场景。

密钥证明证书链中，包含了应用包名、应用签名证书的公钥hash和应用类型（debug或release）等应用ID信息。服务器通过验证这些信息，可以判断收到的请求是否来自真实的应用，从而有效识别重打包、仿冒应用等非真实应用的场景。

密钥证明证书链同时还包含了应用公钥，对应的私钥存储在基于硬件的安全环境中，您可以使用此私钥对重要的业务请求进行签名，以此**识别通过抓包等方法篡改或伪造应用请求**的攻击场景。

## 约束与限制

由于此能力需要证明请求来自真实的设备，因此在模拟器上不会提供真实的实现。具体来说，应用在模拟器上调用密钥证明接口时，会返回一个模拟的固定证书链，该证书链无法通过华为服务器提供的根CA证书的校验。

### 服务配额

| 接口 | 配额 | 配额说明 |
| --- | --- | --- |
| 密钥证明接口 | 35次/秒/应用 | 默认情况下，每个应用调用密钥证明接口（[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11) / [OH\_Huks\_AnonAttestKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_anonattestkeyitem)）的瞬时流量每秒不超过35次请求。如果应用需要修改服务配额，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)申请修改配额。 |
