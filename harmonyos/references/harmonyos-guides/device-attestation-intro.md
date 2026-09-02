---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-intro
title: 应用真实性证明简介
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 应用真实性证明简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:32+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:5975f2fa2ae4591b28a0c276eb9130c36baf13cb38b060077e3bce191a01ec45
---

您可以利用应用真实性证明能力在服务器验证来自应用的请求，具体包括验证请求是否源自真实应用、真实设备，以及请求内容是否未经篡改。

**说明** 

为方便您理解此功能的应用场景，提高接入效率，特此更新该文档，原《设备真实性证明》文档更改为《应用真实性证明》。

## 基础概念

* 应用公私钥对：用于验证应用请求真实性的非对称算法密钥对，包含应用公钥和应用私钥，比如RSA、ECC算法的密钥对。
* 应用公钥ID：为应用公钥生成的唯一ID，用于您的应用服务器标识和查找应用公钥。
* 应用ID：包含了应用身份相关的信息，如应用包名，应用签名密钥Hash。
* 密钥证明证书链：华为服务器在验证应用公钥来自真实的设备和真实的应用后签发的证书链，证书链中包含了应用公钥和您的应用ID。

## 概述

您的应用可以通过调用Universal Keystore Kit相关接口，并在您的服务器上完成对应的校验，以验证应用请求的真实性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/rWFxEZhkSnuEC4BYrzO70w/zh-cn_image_0000002736433473.png)

本文介绍如何在您的应用和应用服务器上验证应用请求真实性，使用过程为：

**前置操作：创建密钥确立可信凭证**

1. 应用调用Universal Keystore Kit的密钥生成接口，创建一对唯一的应用公私钥对，该公私钥对存储在基于硬件的安全环境。
2. 应用再调用Universal Keystore Kit的密钥证明接口，对应用公钥和应用ID签发密钥证明证书链。
3. 应用服务器对密钥证明证书链进行校验，以及校验证书链中的应用ID是否正确。
4. 应用服务器保存密钥证明证书链中的应用公钥。

**业务请求证明：签名验签识别真实请求**

1. 应用进行关键业务处理时（如免密支付、营销活动）调用Universal Keystore Kit的签名接口，使用应用私钥对业务请求进行签名。
2. 应用服务器使用保存的应用公钥对签名进行验签，验签成功即可说明该请求来自真实的设备和应用，以及内容未被篡改。

**说明** 

“对密钥和应用ID证明”步骤从API 26.0.0开始已支持离线密钥证明接口（[anonAttestKeyItemOffline](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitemoffline)），该接口没有服务配额限制，且与在线密钥证明接口（[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11)）提供了相同功能，推荐您的应用优先采用和集成离线接口。

对已经集成了在线密钥证明接口的应用，建议切换到离线密钥证明接口。

| 比较项 | 离线的密钥证明接口（推荐）  （[anonAttestKeyItemOffline](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitemoffline)） | 在线的密钥证明接口  （[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11) / [OH\_Huks\_AnonAttestKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_anonattestkeyitem)） |
| --- | --- | --- |
| 提供的功能 | 提供了对密钥和应用ID证明的能力 | 提供了对密钥和应用ID证明的能力 |
| 实现方案 | 使用设备本地缓存的CA证书签发证明，缓存的CA证书过期（有效期1个月）后才需要联网更新。 | 每次都需要访问华为服务器，使用服务器的CA证书签发证明 |
| 服务配额 | 无限制 | 35次/秒/应用 |

本方案通过证明应用公钥来自真实的设备并签发密钥证明证书链，从而**识别模拟器等非真实设备**的场景。

密钥证明证书链中，包含了应用包名、应用签名证书的公钥hash和应用类型（debug或release）等应用ID信息。服务器通过验证这些信息，可以判断收到的请求是否来自真实的应用，从而有效识别重打包、仿冒应用等非真实应用的场景。

密钥证明证书链同时还包含了应用公钥，对应的私钥存储在基于硬件的安全环境中，您可以使用此私钥对重要的业务请求进行签名，以此**识别通过抓包等方法篡改或伪造应用请求**的攻击场景。

## 约束与限制

由于此能力需要证明请求来自真实的设备，因此在模拟器上不会提供真实的实现。具体来说，应用在模拟器上调用密钥证明接口时，会返回一个模拟的固定证书链，该证书链无法通过华为服务器提供的根CA证书的校验。

### 服务配额

| 接口 | 配额 | 配额说明 |
| --- | --- | --- |
| 密钥证明接口（在线） | 35次/秒/应用 | 默认情况下，每个应用调用在线密钥证明接口（[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11) / [OH\_Huks\_AnonAttestKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_anonattestkeyitem)）的瞬时流量每秒不超过35次请求。如果应用的实际调用量超过服务配额，请切换为离线密钥证明接口。 |
| 密钥证明接口（离线） | 无限制 | 无限制 |
