---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-guidelines
title: 创建密钥确立可信凭证
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 创建密钥确立可信凭证
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b89db86ce51c0325f408f31effeda37c70f4d87d31a16f70b350f1933bb71b9
---

## 概述

应用在被攻击后可以发送伪造或篡改的请求，应用服务器不应该直接信任来自应用的请求信息。但是应用服务器可以基于密钥证明证书链证明应用请求，以此判断服务器接收到的请求是否来自真实的设备和真实的应用。

## 交互流程

**图1** 创建密钥确立可信凭证流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Azc_5MaQSZC5paTYtBPfnQ/zh-cn_image_0000002552798764.png?HW-CC-KV=V1&HW-CC-Date=20260427T234324Z&HW-CC-Expire=86400&HW-CC-Sign=00372EBA49B538857F23F504A1C0E64416E4DFB55BEBADAFF313AD02353D6144)

### 创建密钥确立可信凭证流程

应用创建密钥对后，将创建的公钥保存到应用服务器，一个用户只需要进行一次。

注意

* 为避免您的应用在调用密钥证明接口（[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11) / [OH\_Huks\_AnonAttestKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_anonattestkeyitem)）时被限流导致请求异常，请确保应用在全网设备中，每秒调用这些接口不超过35次。

  一个用户只需要执行一次创建密钥确立可信凭证流程，请勿在每次业务请求时都对应用公钥和应用ID进行证明。
* 当密钥证明接口由于流量过载或其他原因不可用时，应用需要考虑异常处理方案，避免出现应用基本功能不可用。

具体的步骤如下：

1. **查询应用公私钥对是否存在**：如果应用公私钥对已存在，则无需继续执行以下流程。
2. **创建应用公私钥对**：应用调用Universal Keystore Kit密钥生成接口创建一个非对称算法密钥对（包含应用公钥和应用私钥），比如RSA、ECC算法的密钥对。
3. **获取挑战值Challenge**：为了在步骤5“发送密钥证明证书链”中，能够防重放攻击，建议应用先从应用服务器获取一次性的挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。
4. **对应用公钥和应用ID进行证明**：应用调用Universal Keystore Kit密钥证明接口对生成的应用公钥、应用ID和挑战值Challenge进行证明。华为服务器对应用公钥、应用ID和挑战值Challenge进行证明，并返回密钥证明的证书链给应用。
5. **发送密钥证明证书链**：应用将密钥证明证书链发送到应用服务器。
6. **校验密钥证明证书链**：应用服务器使用官网提供的根证书对证书链合法性进行校验，以及对挑战值Challenge、应用ID进行校验。
7. **保存应用公钥**：应用服务器对证书链校验通过后，将密钥证明证书中的应用公钥保存到应用服务器。

说明

在“签名验签识别真实请求”流程中，为了便于应用服务器查找应用公钥，建议为应用公钥生成一个唯一的应用公钥ID，并在应用服务器中保存应用公钥ID和应用公钥的对应关系。同时，应用服务器应该返回应用公钥ID给应用，并由应用存储应用ID。

* **[应用端开发](device-attestation-apps.md)**
* **[服务器端开发](device-attestation-servers.md)**
