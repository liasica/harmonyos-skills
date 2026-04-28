---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-overview
title: 密钥协商介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥协商 > 密钥协商介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:19b9bc70a0bf6958038fdcf927438738c5400ae39253b11ddfc83e388b3b2f3b
---

为了避免恶意第三方获取到保密信息，密钥本身是不可以直接在设备间传输的。一般情况下，会采取密钥协商的方式，安全地在双方（或多方）间共享密钥。密钥协商只会传输密钥的公钥部分，私钥仍存留在设备内，以保护数据的安全性和机密性。

两台设备间进行密钥协商，双方各准备一个非对称密钥，并互换非对称密钥的公钥，以对端公钥与己端私钥协商出一个密钥，该密钥在两台设备相同。

说明

* 轻量级智能穿戴不支持密钥协商功能。
* 使用现有密钥别名作为协商结果密钥别名会把现有密钥覆盖。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 支持的算法

以下为密钥协商支持的规格说明。

| 算法 | 备注 | 协商的密钥长度 | 协商密钥可用算法 | API级别 |
| --- | --- | --- | --- | --- |
| ECDH | 协商密钥类型为ECC类型密钥。 | 256 | AES/256  HMAC/256 | 8+ |
| DH | 协商密钥类型为DH类型密钥。 | 2048 | AES/128/192/256  HMAC/8-1024  SM4/128  DES/64  3DES/128/192 | 8+ |
| X25519 | 协商密钥类型为X25519类型密钥。 | 256 | AES/256  HMAC/256 | 8+ |
