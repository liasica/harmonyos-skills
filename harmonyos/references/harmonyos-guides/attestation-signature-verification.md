---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/attestation-signature-verification
title: 签名验签识别真实请求
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 签名验签识别真实请求
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:caebcd5bd2c51b3a1473f14d2161be78f99832a71d494990e31e2c2376af2aef
---

## 概述

您的应用服务器在接收到来自应用的请求时，如果没有有效的完整性校验手段，可能会接收到被篡改或者伪造的应用请求。但是应用可以使用应用私钥对重要的业务请求进行签名，并在服务器使用保存的应用公钥进行验签，以此**识别被篡改或伪造的应用请求**。

## 交互流程

**图1** 签名验签识别真实请求流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/onnoNTY3S8-V6nQjItwb3Q/zh-cn_image_0000002583478415.png?HW-CC-KV=V1&HW-CC-Date=20260427T234325Z&HW-CC-Expire=86400&HW-CC-Sign=80B7F9F27133B19EF2853606B579F7142E61FE765EC64D8F45927A6DD93BB07D)

### 签名验签识别真实请求流程

使用保存在应用服务器中的应用公钥对业务请求进行验证，业务请求中请勿携带密钥证明证书链。

说明

华为服务器可能会限制来自特定应用的认证流量，以避免单个应用的流量过大出现过载，从而导致其他应用处理失败，因此请勿在每次业务请求时都对应用公钥和应用ID进行证明。

当密钥证明接口由于流量过载或其他原因不可用时，应用需要考虑异常处理方案，避免出现应用基本功能不可用。

具体的步骤如下：

1. **获取挑战值Challenge**：为了在步骤3“发送业务请求”中，能够防重放攻击，建议您的应用先从应用服务器获取一次性的挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。
2. **使用应用私钥对业务请求进行签名**：应用调用Universal Keystore Kit的签名接口使用应用私钥对业务请求数据和挑战值Challenge进行签名，Universal Keystore Kit返回签名数据给应用。
3. **发送业务请求**：应用发送业务请求到应用服务器，携带签名数据、应用公钥ID、挑战值Challenge等。
4. **根据应用公钥ID查找应用公钥**：应用服务器根据应用公钥ID查找应用公钥，并校验挑战值Challenge。
5. **使用应用公钥对请求的签名进行校验**：应用服务器使用应用公钥对请求中的签名进行校验。

* **[应用端开发](attestation-signature-verification-apps.md)**
* **[服务器端开发](attestation-signature-verification-servers.md)**
