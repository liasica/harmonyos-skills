---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-encryption-decryption-overview
title: 加密/解密介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 加密/解密 > 加密/解密介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09ff57bc6b29a146b1fe30bea0dbee0bd160e177f4588f8d3dfb62f2b7d10a7e
---

在HUKS中已经有密钥，需要对一段数据加密或是解密，均可以使用HUKS完成加密/解密操作。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 支持的算法

以下为密钥加密/解密支持的规格说明。

**手机、平板、PC/2in1设备、TV、智能穿戴规格**

| 算法/分组模式/填充模式 | 备注 | API级别 |
| --- | --- | --- |
| AES/CBC/NoPadding  AES/CBC/PKCS7  AES/CTR/NoPadding | IV参数必选；CBC模式下，若填充模式选择为NoPadding，因为该模式下要求明文数据必须按照固定长度的块进行加密，如果输入的数据长度不是16的倍数，就需要业务方自行填充，以满足块长度的要求。 | 8+ |
| AES/GCM/NoPadding | 加密：NONCE、AAD参数可选。不指定NONCE参数，将会以“密文 + AEAD + NONCE”格式进行拼接返回数据。AEAD长度为16，NONCE默认长度为12。  解密：AAD参数可选，NONCE、AEAD参数必选。 | 8+ |
| AES/CCM/NoPadding | 加密：NONCE、AAD参数可选。不指定NONCE参数，将会以“密文 + AEAD + NONCE”格式进行拼接返回数据。AEAD长度不指定默认为16，NONCE默认长度为7。  解密：AAD参数可选，NONCE、AEAD参数必选。  可指定AEAD长度，支持的AEAD长度为4、6、8、10、12、14、16。 | 22+ |
| RSA/ECB/NoPadding  RSA/ECB/PKCS1\_V1\_5  RSA/ECB/OAEP | OAEP填充模式支持的摘要算法：SHA256/SHA384/SHA512。 | 8+ |
| SM4/ECB/PKCS7 | ECB模式不推荐使用。 | 20+ |
| SM4/CBC/PKCS7 | IV 参数必选。 | 9+ |
| SM4/CTR/NoPadding  SM4/CBC/NoPadding  SM4/CFB/NoPadding  SM4/OFB/NoPadding | IV 参数必选。 | 12+ |
| SM2/-/NoPadding | 摘要算法SM3。 | 11+ |
| DES/CBC/NoPadding  DES/ECB/NoPadding | CBC模式下 IV 参数必选。 | 18+ |
| 3DES/CBC/NoPadding  3DES/ECB/NoPadding | CBC模式下 IV 参数必选。 | 18+ |

**轻量级智能穿戴规格**

| 算法/分组模式/填充模式 | 备注 | API级别 |
| --- | --- | --- |
| AES/GCM/NoPadding | 加密：NONCE、AAD参数可选。不指定NONCE参数，将会以“密文 + AEAD + NONCE”格式进行拼接返回数据。AEAD长度为16，NONCE默认长度为12。  解密：AAD参数可选，NONCE、AEAD参数必选。 | 8+ |
| AES/CBC/NoPadding  AES/CTR/NoPadding | IV参数必选。 | 11+ |
| DES/ECB/NoPadding | - | 12+ |
| DES/CBC/NoPadding | IV参数必选。 | 12+ |
| 3DES/ECB/NoPadding | - | 12+ |
| 3DES/CBC/NoPadding | IV参数必选。 | 12+ |
| RSA/ECB/NoPadding | - | 12+ |
| RSA/ECB/PKCS1\_V1\_5 | - | 12+ |
| RSA/ECB/OAEP | 摘要算法SHA256。 | 12+ |
