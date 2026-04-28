---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h
title: crypto_digest.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_digest.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bbfb929160e30cbe21103958eb4873773e7e2c9bfb702143c69b31ecad2b8576
---

## 概述

PhonePC/2in1TabletTVWearable

定义摘要算法API。

**引用文件：** <CryptoArchitectureKit/crypto\_digest.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoDigestApi](capi-cryptodigestapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) | OH\_CryptoDigest | 定义摘要结构体。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Create(const char \*algoName, OH\_CryptoDigest \*\*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_create) | 根据给定的算法名称创建一个摘要实例。  注意：创建的资源必须通过[OH\_DigestCrypto\_Destroy](capi-crypto-digest-h.md#oh_digestcrypto_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Update(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*in)](capi-crypto-digest-h.md#oh_cryptodigest_update) | 更新摘要数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Final(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*out)](capi-crypto-digest-h.md#oh_cryptodigest_final) | 完成摘要计算。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [uint32\_t OH\_CryptoDigest\_GetLength(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_getlength) | 获取摘要长度。 |
| [const char \*OH\_CryptoDigest\_GetAlgoName(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_getalgoname) | 获取摘要算法名称。 |
| [void OH\_DigestCrypto\_Destroy(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_digestcrypto_destroy) | 销毁摘要实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoDigest\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoDigest_Create(const char *algoName, OH_CryptoDigest **ctx)
```

**描述**

根据给定的算法名称创建一个摘要实例。

注意：创建的资源必须通过[OH\_DigestCrypto\_Destroy](capi-crypto-digest-h.md#oh_digestcrypto_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成摘要实例的算法名称。  例如"SHA256"。 |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*\*ctx | 指向摘要实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoDigest\_Update()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoDigest_Update(OH_CryptoDigest *ctx, Crypto_DataBlob *in)
```

**描述**

更新摘要数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | 指向摘要实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 传入的消息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoDigest\_Final](capi-crypto-digest-h.md#oh_cryptodigest_final)

### OH\_CryptoDigest\_Final()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoDigest_Final(OH_CryptoDigest *ctx, Crypto_DataBlob *out)
```

**描述**

完成摘要计算。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | 指向摘要实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 返回的Md的计算结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoDigest\_Update](capi-crypto-digest-h.md#oh_cryptodigest_update)

### OH\_CryptoDigest\_GetLength()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_CryptoDigest_GetLength(OH_CryptoDigest *ctx)
```

**描述**

获取摘要长度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | 指向摘要实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回摘要长度。  如果输入参数ctx为NULL，则返回401，其他情况下返回0。 |

### OH\_CryptoDigest\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoDigest_GetAlgoName(OH_CryptoDigest *ctx)
```

**描述**

获取摘要算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | 指向摘要实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回摘要算法名称。 |

### OH\_DigestCrypto\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_DigestCrypto_Destroy(OH_CryptoDigest *ctx)
```

**描述**

销毁摘要实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | 指向摘要实例。 |
