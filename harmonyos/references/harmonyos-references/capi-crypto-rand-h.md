---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-rand-h
title: crypto_rand.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_rand.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b67c2607dd894327d5609a1a93295f562364888a19dbf54c3a1767a3391abc70
---

## 概述

定义随机数生成器接口。

**引用文件：** <CryptoArchitectureKit/crypto\_rand.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoRandApi](capi-cryptorandapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) | OH\_CryptoRand | 随机数生成器结构体，表示随机数生成器上下文。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_Create(OH\_CryptoRand \*\*ctx)](capi-crypto-rand-h.md#oh_cryptorand_create) | 创建随机数生成器上下文。  注意：创建的资源必须通过[OH\_CryptoRand\_Destroy](capi-crypto-rand-h.md#oh_cryptorand_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_GenerateRandom(OH\_CryptoRand \*ctx, int len, Crypto\_DataBlob \*out)](capi-crypto-rand-h.md#oh_cryptorand_generaterandom) | 生成随机数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [const char \*OH\_CryptoRand\_GetAlgoName(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_getalgoname) | 获取随机数生成器的算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_SetSeed(OH\_CryptoRand \*ctx, Crypto\_DataBlob \*seed)](capi-crypto-rand-h.md#oh_cryptorand_setseed) | 设置随机数生成器的种子。 |
| [OH\_Crypto\_ErrCode OH\_CryptoRand\_EnableHardwareEntropy(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_enablehardwareentropy) | 启用硬件熵源。 |
| [void OH\_CryptoRand\_Destroy(OH\_CryptoRand \*ctx)](capi-crypto-rand-h.md#oh_cryptorand_destroy) | 销毁随机数生成器上下文。 |

## 函数说明

### OH\_CryptoRand\_Create()

```c
OH_Crypto_ErrCode OH_CryptoRand_Create(OH_CryptoRand **ctx)
```

**描述**

创建随机数生成器上下文。

注意：创建的资源必须通过[OH\_CryptoRand\_Destroy](capi-crypto-rand-h.md#oh_cryptorand_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*\*ctx | [out] 指向随机数生成器上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoRand\_GenerateRandom()

```c
OH_Crypto_ErrCode OH_CryptoRand_GenerateRandom(OH_CryptoRand *ctx, int len, Crypto_DataBlob *out)
```

**描述**

生成随机数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | [in] 随机数生成器上下文。不能为NULL。 |
| int len | [in] 随机数的字节长度。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储随机数的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或out为NULL，或len小于等于0。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoRand\_GetAlgoName()

```c
const char *OH_CryptoRand_GetAlgoName(OH_CryptoRand *ctx)
```

**描述**

获取随机数生成器的算法名称。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | [in] 随机数生成器上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回随机数生成器的算法名称，不需要调用者释放，上下文销毁后不可使用。 |

### OH\_CryptoRand\_SetSeed()

```c
OH_Crypto_ErrCode OH_CryptoRand_SetSeed(OH_CryptoRand *ctx, Crypto_DataBlob *seed)
```

**描述**

设置随机数生成器的种子。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | [in] 随机数生成器上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*seed | [in] 种子数据。本接口会对seed中的数据进行深拷贝，调用者在接口返回后可立即释放seed。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx为NULL，或seed无效（seed为NULL、seed->data为NULL、seed->len为0、或seed->len超过INT\_MAX）。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoRand\_EnableHardwareEntropy()

```c
OH_Crypto_ErrCode OH_CryptoRand_EnableHardwareEntropy(OH_CryptoRand *ctx)
```

**描述**

启用硬件熵源。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | [in] 随机数生成器上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoRand\_Destroy()

```c
void OH_CryptoRand_Destroy(OH_CryptoRand *ctx)
```

**描述**

销毁随机数生成器上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoRand](capi-cryptorandapi-oh-cryptorand.md) \*ctx | [in] 随机数生成器上下文。 |
