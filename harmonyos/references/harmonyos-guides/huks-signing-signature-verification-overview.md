---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-overview
title: 签名/验签介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 签名/验签 > 签名/验签介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f56016c67467073ac1f655bcef9b16f47d70f4518db6a1a36326f074d13b028a
---

为实现数据完整性保护和防抵赖，可使用生成/导入的密钥，对数据进行签名验签操作。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 支持的算法

以下为密钥签名/验签支持的规格说明。

**手机、平板、PC/2in1设备、TV、智能穿戴规格**

| 算法/摘要算法/填充模式 | 备注 | API级别 |
| --- | --- | --- |
| RSA/SHA256/PKCS1\_V1\_5  RSA/SHA384/PKCS1\_V1\_5  RSA/SHA512/PKCS1\_V1\_5  RSA/SHA256/PSS  RSA/SHA384/PSS  RSA/SHA512/PSS | 对于PSS模式，salt长度支持设置为摘要长度和最大长度（最大长度=密钥长度-摘要长度-2），对应枚举值详见[HuksRsaPssSaltLenType](../harmonyos-references/js-apis-huks.md#huksrsapsssaltlentype10)。 | 8+ |
| RSA/NoDigest/PKCS1\_V1\_5 | NoDigest需要指定TAG HuksKeyDigest.HUKS\_DIGEST\_NONE。由业务对明文做哈希，再将哈希后的数据传入，哈希后的数据长度必须满足RSA签名验签支持的摘要算法规格。 | 9+ |
| RSA/NoDigest/NoPadding | NoDigest需要指定TAG HuksKeyDigest.HUKS\_DIGEST\_NONE。明文长度必须等于密钥长度。 | 20+ |
| ECC/SHA256  ECC/SHA384  ECC/SHA512 | 签名是ASN1格式。  ECC算法支持的椭圆曲线函数包括：P-256、P-384、P-521。 | 8+ |
| ED25519/NoDigest | NoDigest需要指定TAG HuksKeyDigest.HUKS\_DIGEST\_NONE。 | 8+ |
| SM2/SM3 | 签名是ASN1格式。 | 9+ |
| SM2/NoDigest | 签名是ASN1格式。  NoDigest需要指定TAG HuksKeyDigest.HUKS\_DIGEST\_NONE。由业务对明文做SM3哈希，再将哈希后的数据传入，哈希后的数据长度必须满足SM2签名验签支持的摘要算法规格。 | 22+ |

**轻量级智能穿戴规格**

| 算法/摘要算法/填充模式 | 备注 | API级别 |
| --- | --- | --- |
| RSA/SHA256/PKCS1\_V1\_5 | - | 12+ |
| RSA/SHA256/PSS | - | 12+ |
| RSA/SHA1/ISO\_IEC\_9796\_2 | 数据最小长度=密钥长度-21字节 | 12+ |
| RSA/NoDigest/NoPadding | NoDigest需要指定TAG HuksKeyDigest.HUKS\_DIGEST\_NONE。明文长度必须等于密钥长度。 | 20+ |

**智能穿戴设备规格**

| 算法/摘要算法/填充模式 | 备注 | API级别 |
| --- | --- | --- |
| RSA/SHA1/ISO\_IEC\_9796\_2 | 只支持密钥长度1024~2048（含1024和2048，且必须是8的整数倍），数据最小长度=密钥长度-21字节。 | 16+ |

## 携带认证信息的签名类型

适用场景：当使用含有数字盾密码认证的密钥进行签名时，可以选择携带认证信息的签名类型，会在原始数据之前附加41字节认证信息后，再进行签名操作。认证信息会附加在签名前一起返回。验签时需将同样认证信息附加在原始数据前，再执行验签操作。从前到后依次为：

认证信息格式：4字节的版本号、4字节的用户认证类型、32字节的匿名化AuthId和1字节的是否校验数据哈希。

注意事项：AuthId包含匿名化处理过的身份信息，使用该接口时，开发者需在其隐私政策中对此匿名化数据的使用目的、存留策略和销毁方式进行说明。

使用方法：在签名的参数集中加上参数HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE，此参数的值请参考[HuksSecureSignType](../harmonyos-references/js-apis-huks.md#hukssecuresigntype9)。
