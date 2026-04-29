---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-overview
title: 群组密钥介绍
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:08520bfc3cd3c5062663a310bc055dd5363be10361b6b32b0730ca4f0f5e4f9f
---

从API 23开始，HUKS支持群组密钥功能，该功能是针对同一开发者开发的多个HAP应用，提供的跨应用密钥共享能力。

当多个HAP在配置中指定相同的组标识时，可共享同一组密钥资源，实现密钥在开发者自有应用生态内的安全复用，无需重复生成或手动传递密钥，简化跨应用加密场景的密钥管理流程。

说明

* 仅在手机、平板、PC/2in1、智能穿戴上支持群组密钥功能。
* 群组密钥严格限定在同一开发者相同组的HAP范围内。不同开发者的相同组或者相同开发者的不同组，都无法相互访问对方的群组密钥，从而保障密钥的隔离性与安全性。

## 规格说明

| 支持的本地密钥操作 | API级别 | 说明 |
| --- | --- | --- |
| [密钥生成](huks-key-generation-overview.md) | 23+ | 支持生成群组密钥。 |
| [密钥导入](huks-key-import-overview.md) | 23+ | 支持导入群组密钥。 |
| [加密/解密](huks-encryption-decryption-overview.md) | 23+ | 支持使用群组密钥进行加密/解密。 |
| [签名/验签](huks-signing-signature-verification-overview.md) | 23+ | 支持使用群组密钥进行签名/验签。 |
| [密钥协商](huks-key-agreement-overview.md) | 23+ | 支持使用群组密钥进行密钥协商。 |
| [密钥派生](huks-key-derivation-overview.md) | 23+ | 支持使用群组密钥进行密钥派生。 |
| [访问控制](huks-identity-authentication-overview.md) | 23+ | 支持使用群组密钥进行二次访问控制。 |
| [HMAC](huks-hmac-overview.md) | 23+ | 支持使用群组密钥进行HMAC。 |
| [密钥删除](huks-delete-key-arkts.md) | 23+ | 支持删除群组密钥。 |
| [密钥证明](huks-key-attestation-overview.md) | 23+ | 支持群组密钥的合法性证明。 |
| [查询密钥是否存在](huks-check-key-arkts.md) | 23+ | 支持查询群组密钥是否存在。 |
| [获取密钥属性](huks-obtain-key-properties-arkts.md) | 23+ | 支持查询群组密钥的属性。支持获取DeveloperID和GroupID信息。 |
| [密钥导出](huks-export-key-arkts.md) | 23+ | 支持导出群组密钥。 |
| [查询密钥别名集](huks-list-aliases-arkts.md) | 23+ | 支持查询群组密钥别名集。 |
