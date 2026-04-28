---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-use-overview
title: 密钥使用介绍及通用流程
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥使用介绍及通用流程
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a93eed7cd49bcb4b0e4af493949e3ba60320e21783faee40eeafadeb31c0060
---

为了实现对数据机密性、完整性等保护，可使用生成/导入的密钥，对数据进行密钥操作，比如：

* [加密/解密](huks-encryption-decryption-overview.md)。
* [签名/验签](huks-signing-signature-verification-overview.md)。
* [密钥协商](huks-key-agreement-overview.md)。
* [密钥派生](huks-key-derivation-overview.md)。

本章节提供了以上常用密钥操作的示例，这部分示例均没有设置二次身份访问控制，如设置了密钥访问控制请参考[用户身份认证访问控制](huks-identity-authentication-overview.md)。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 通用开发流程

HUKS基于密钥会话来操作数据，使用密钥时基于以下流程：

1. （必选）初始化密钥会话[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)。

   传入密钥别名和密钥操作参数，初始化一个密钥会话并获取会话句柄。其中密钥操作参数必须包含对应密码算法所必须的参数，包括密码算法、密钥大小、密钥目的、工作模式、填充模式、散列模式、IV、NONCE、AAD等。
2. （可选）分段操作数据[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)。

   当使用的数据过大（超过100K）或是部分密码算法有要求时，需要对数据进行分段操作。否则可跳过此步骤。
3. （必选）结束密钥会话[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)。

   操作最后一段数据并结束密钥会话。

以上任一阶段中发生错误或不需要此次密钥操作数据，均需要取消会话[abortSession](../harmonyos-references/js-apis-huks.md#huksabortsession9)，终止密钥的使用。

注意

* 对于内存较小设备，建议业务根据设备存储能力，进行数据切分，循环调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)和[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)处理。
* 会话持续时间即[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)和[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)调用间隔，系统低内存时将清理超时会话，因此会话持续时间不宜过久（不建议超过1分钟）。
