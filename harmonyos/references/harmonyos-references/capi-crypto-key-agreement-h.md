---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-key-agreement-h
title: crypto_key_agreement.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_key_agreement.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ff4f6d9d21d7d626c230cfec2557680cb125904547a396d05f9e076526fd4a40
---

## 概述

定义密钥协商接口。

**引用文件：** <CryptoArchitectureKit/crypto\_key\_agreement.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoKeyAgreementApi](capi-cryptokeyagreementapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) | OH\_CryptoKeyAgreement | 密钥协商结构体，表示密钥协商上下文。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_Create(const char \*algoName, OH\_CryptoKeyAgreement \*\*ctx)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_create) | 根据给定的算法名称创建密钥协商上下文。  注意：创建的资源必须通过[OH\_CryptoKeyAgreement\_Destroy](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKeyAgreement\_GenerateSecret(OH\_CryptoKeyAgreement \*ctx, OH\_CryptoPrivKey \*privkey, OH\_CryptoPubKey \*pubkey, Crypto\_DataBlob \*secret)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret) | 生成共享秘密值。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放secret内存。 |
| [void OH\_CryptoKeyAgreement\_Destroy(OH\_CryptoKeyAgreement \*ctx)](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy) | 销毁密钥协商上下文。 |

## 函数说明

### OH\_CryptoKeyAgreement\_Create()

```c
OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx)
```

**描述**

根据给定的算法名称创建密钥协商上下文。

注意：创建的资源必须通过[OH\_CryptoKeyAgreement\_Destroy](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 密钥协商算法名称，不能为NULL。取值如下：  - 从API version 20开始支持ECDH系列："ECC224"、"ECC256"、"ECC384"、"ECC521"。  - 从API version 20开始支持ECDH BrainPool系列："ECC\_BrainPoolP160r1"、"ECC\_BrainPoolP160t1"、"ECC\_BrainPoolP192r1"、"ECC\_BrainPoolP192t1"、"ECC\_BrainPoolP224r1"、"ECC\_BrainPoolP224t1"、"ECC\_BrainPoolP256r1"、"ECC\_BrainPoolP256t1"、"ECC\_BrainPoolP320r1"、"ECC\_BrainPoolP320t1"、"ECC\_BrainPoolP384r1"、"ECC\_BrainPoolP384t1"、"ECC\_BrainPoolP512r1"、"ECC\_BrainPoolP512t1"。  - 从API version 20开始支持"ECC\_Secp256k1"。  - 从API version 20开始支持"X25519"。  - 从API version 20开始支持DH系列："DH\_modp1536"、"DH\_modp2048"、"DH\_modp3072"、"DH\_modp4096"、"DH\_modp6144"、"DH\_modp8192"、"DH\_ffdhe2048"、"DH\_ffdhe3072"、"DH\_ffdhe4096"、"DH\_ffdhe6144"、"DH\_ffdhe8192"。  - 从API版本26.0.0开始支持"ECC192"。 |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*\*ctx | [out] 指向密钥协商上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：algoName或ctx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密钥协商操作失败。 |

**参考：**

[OH\_CryptoKeyAgreement\_GenerateSecret](capi-crypto-key-agreement-h.md#oh_cryptokeyagreement_generatesecret) 生成共享秘密值。

### OH\_CryptoKeyAgreement\_GenerateSecret()

```c
OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey, OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret)
```

**描述**

生成共享秘密值。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放secret内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*ctx | [in] 密钥协商上下文。不能为NULL。 |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*privkey | [in] 私钥。不能为NULL。 |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*pubkey | [in] 公钥。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*secret | [out] 指向用于存储共享秘密值的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将secret初始化为{0}，不要预分配secret->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx、privkey、pubkey或secret为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密钥协商操作失败。可能的原因：公钥和私钥不属于同一曲线或算法，或公钥数据无效。 |

### OH\_CryptoKeyAgreement\_Destroy()

```c
void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx)
```

**描述**

销毁密钥协商上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyAgreement](capi-cryptokeyagreementapi-oh-cryptokeyagreement.md) \*ctx | [in] 密钥协商上下文。 |
