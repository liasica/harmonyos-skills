---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h
title: crypto_rand.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_rand.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9228af577f4eacb59c73c9fc8d5a4c9fc99cf4e19d97e89a7f1ff07a8156fad3
---

## 概述

PhonePC/2in1TabletTVWearable

定义随机数生成器API。

**引用文件：** <CryptoArchitectureKit/crypto\_rand.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoRandApi](capi-cryptorandapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) | OH\_CryptoRand | 定义随机数生成器结构。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_Create(OH\_CryptoRand \*\*ctx)](capi-crypto-rand-h.md#oh_cryptorand_create) | 创建随机数生成器。  注意：创建的资源必须通过[OH\_CryptoRand\_Destroy](capi-crypto-rand-h.md#oh_cryptorand_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_GenerateRandom(OH\_CryptoRand \*ctx, int len, Crypto\_DataBlob \*out)](capi-crypto-rand-h.md#oh_cryptorand_generaterandom) | 生成随机数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [const char \*OH\_CryptoRand\_GetAlgoName(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_getalgoname) | 获取随机数生成器实例的算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_SetSeed(OH\_CryptoRand \*ctx, Crypto\_DataBlob \*seed)](capi-crypto-rand-h.md#oh_cryptorand_setseed) | 设置随机数生成器的种子。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_EnableHardwareEntropy(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_enablehardwareentropy) | 启用硬件熵源。 |
| [void OH\_CryptoRand\_Destroy(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_destroy) | 销毁随机数生成器实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoRand\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoRand_Create(OH_CryptoRand **ctx)
```

**描述**

创建随机数生成器。

注意：创建的资源必须通过[OH\_CryptoRand\_Destroy](capi-crypto-rand-h.md#oh_cryptorand_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*\*ctx | 指向随机数生成器实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoRand\_GenerateRandom()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoRand_GenerateRandom(OH_CryptoRand *ctx, int len, Crypto_DataBlob *out)
```

**描述**

生成随机数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | 随机数生成器实例。 |
| int len | 表示生成随机数的长度，单位为byte，范围在[1, INT\_MAX]。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 用于获取随机数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoRand\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoRand_GetAlgoName(OH_CryptoRand *ctx)
```

**描述**

获取随机数生成器实例的算法名称。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | 指向随机数生成器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回随机数生成器实例的算法名称。 |

### OH\_CryptoRand\_SetSeed()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoRand_SetSeed(OH_CryptoRand *ctx, Crypto_DataBlob *seed)
```

**描述**

设置随机数生成器的种子。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | 随机数生成器实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*seed | 种子数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoRand\_EnableHardwareEntropy()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoRand_EnableHardwareEntropy(OH_CryptoRand *ctx)
```

**描述**

启用硬件熵源。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | 随机数生成器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoRand\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoRand_Destroy(OH_CryptoRand *ctx)
```

**描述**

销毁随机数生成器实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | 随机数生成器实例。 |
