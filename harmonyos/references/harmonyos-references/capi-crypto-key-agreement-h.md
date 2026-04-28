---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h
title: crypto_key_agreement.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_key_agreement.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:530147377174ae228c2ba1f89973eddc02872acd7f114da7c2c776b8accd8632
---

## 概述

PhonePC/2in1TabletTVWearable

定义密钥协商接口。

**引用文件：** <CryptoArchitectureKit/crypto\_key\_agreement.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoKeyAgreementApi](capi-cryptokeyagreementapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) | OH\_CryptoKeyAgreement | 定义密钥协商结构。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_Create(const char \*algoName, OH\_CryptoKeyAgreement \*\*ctx)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create) | 根据给定的算法名称创建密钥协商实例。  注意：创建的资源必须通过[OH\_CryptoKeyAgreement\_Destroy](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_GenerateSecret(OH\_CryptoKeyAgreement \*ctx, OH\_CryptoPrivKey \*privkey, OH\_CryptoPubKey \*pubkey, Crypto\_DataBlob \*secret)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret) | 生成密钥协商的秘密值。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放secret内存。 |
| [void OH\_CryptoKeyAgreement\_Destroy(OH\_CryptoKeyAgreement \*ctx)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy) | 销毁密钥协商实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoKeyAgreement\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx)
```

**描述**

根据给定的算法名称创建密钥协商实例。

注意：创建的资源必须通过[OH\_CryptoKeyAgreement\_Destroy](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成密钥协商实例的算法名称。  例如"ECC"、"X25519"。 |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*\*ctx | 密钥协商实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKeyAgreement\_GenerateSecret()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey, OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret)
```

**描述**

生成密钥协商的秘密值。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放secret内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*ctx | 密钥协商实例。 |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*privkey | 私钥。 |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*pubkey | 公钥。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*secret | 秘密值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKeyAgreement\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx)
```

**描述**

销毁密钥协商实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*ctx | 密钥协商实例。 |
