---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-overview
title: 消息摘要计算介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息摘要计算介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eff768d114d4c9b3dcb9d492ef64dce00ea15ddf2b569ce59f25ea9fa88ceee7
---

消息摘要算法是一种能将任意长度的输入消息，通过特定运算生成固定长度摘要的算法。消息摘要算法也被称为哈希算法或单向散列算法。

在摘要算法相同时，生成的摘要值主要有下列特点：

* 当输入消息相同时，生成摘要序列相同。
* 当输入消息的长度不一致时，生成摘要序列长度固定（摘要长度由算法决定）。例如SHA256会生成256位，即32字节。

## 支持的算法与规格

当创建MD消息摘要时，需要使用表中“支持种类”一列，指定MD消息摘要算法规格。

| 摘要算法 | 支持种类 | 字节长度 | API版本 |
| --- | --- | --- | --- |
| HASH | SHA1 | 20 | 9+ |
| HASH | SHA224 | 28 | 9+ |
| HASH | SHA256 | 32 | 9+ |
| HASH | SHA384 | 48 | 9+ |
| HASH | SHA512 | 64 | 9+ |
| HASH | MD2 | 16 | 26.0.0+ |
| HASH | MD4 | 16 | 26.0.0+ |
| HASH | MD5 | 16 | 9+ |
| HASH | RIPEMD160 | 20 | 26.0.0+ |
| HASH | SM3 | 32 | 10+ |
| HASH | SHA3-256 | 32 | 22+ |
| HASH | SHA3-384 | 48 | 22+ |
| HASH | SHA3-512 | 64 | 22+ |

* **[消息摘要计算SHA256(ArkTS)](crypto-generate-message-digest.md)**
* **[消息摘要计算SHA256(C/C++)](crypto-generate-message-digest-ndk.md)**
* **[消息摘要计算MD5(ArkTS)](crypto-generate-message-digest-md5.md)**
* **[消息摘要计算MD5(C/C++)](crypto-generate-message-digest-md5-ndk.md)**
* **[消息摘要计算SHA3(ArkTS)](crypto-generate-message-digest-sha3.md)**
* **[消息摘要计算SHA3(C/C++)](crypto-generate-message-digest-sha3-ndk.md)**
