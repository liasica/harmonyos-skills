---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-digest-h
title: crypto_digest.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_digest.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91a231efff92f9555cccea4dad8415cea1773bfb917ebc2354717a3a807406dd
---

## 概述

定义摘要算法接口。

**引用文件：** <CryptoArchitectureKit/crypto\_digest.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoDigestApi](capi-cryptodigestapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) | OH\_CryptoDigest | 摘要结构体，表示摘要上下文。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Create(const char \*algoName, OH\_CryptoDigest \*\*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_create) | 根据给定的算法名称创建摘要上下文。  注意：创建的资源必须通过[OH\_DigestCrypto\_Destroy](capi-crypto-digest-h.md#oh_digestcrypto_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Update(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*in)](capi-crypto-digest-h.md#oh_cryptodigest_update) | 更新摘要数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoDigest\_Final(OH\_CryptoDigest \*ctx, Crypto\_DataBlob \*out)](capi-crypto-digest-h.md#oh_cryptodigest_final) | 完成摘要操作，输出摘要结果。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [uint32\_t OH\_CryptoDigest\_GetLength(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_getlength) | 获取摘要结果的长度。 |
| [const char \*OH\_CryptoDigest\_GetAlgoName(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_cryptodigest_getalgoname) | 获取摘要上下文的算法名称。 |
| [void OH\_DigestCrypto\_Destroy(OH\_CryptoDigest \*ctx)](capi-crypto-digest-h.md#oh_digestcrypto_destroy) | 销毁摘要上下文。 |

## 函数说明

### OH\_CryptoDigest\_Create()

```c
OH_Crypto_ErrCode OH_CryptoDigest_Create(const char *algoName, OH_CryptoDigest **ctx)
```

**描述**

根据给定的算法名称创建摘要上下文。

注意：创建的资源必须通过[OH\_DigestCrypto\_Destroy](capi-crypto-digest-h.md#oh_digestcrypto_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 摘要算法名称，不能为NULL。取值如下：  - 从API version 12开始支持"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"、"MD5"、"SM3"。  - 从API version 22开始支持"SHA3-256"、"SHA3-384"、"SHA3-512"。 |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*\*ctx | [out] 指向摘要上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx为NULL、algoName为NULL、或algoName不是支持的摘要算法名称。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：摘要操作失败。 |

**参考：**

[OH\_CryptoDigest\_Update](capi-crypto-digest-h.md#oh_cryptodigest_update) 更新摘要数据。

### OH\_CryptoDigest\_Update()

```c
OH_Crypto_ErrCode OH_CryptoDigest_Update(OH_CryptoDigest *ctx, Crypto_DataBlob *in)
```

**描述**

更新摘要数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | [in] 摘要上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待计算摘要的数据。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或in为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：摘要更新失败。 |

**参考：**

[OH\_CryptoDigest\_Final](capi-crypto-digest-h.md#oh_cryptodigest_final) 完成摘要操作，输出摘要结果。

### OH\_CryptoDigest\_Final()

```c
OH_Crypto_ErrCode OH_CryptoDigest_Final(OH_CryptoDigest *ctx, Crypto_DataBlob *out)
```

**描述**

完成摘要操作，输出摘要结果。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | [in] 摘要上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储摘要结果的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：摘要完成操作失败。 |

### OH\_CryptoDigest\_GetLength()

```c
uint32_t OH_CryptoDigest_GetLength(OH_CryptoDigest *ctx)
```

**描述**

获取摘要结果的长度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | [in] 摘要上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回摘要结果的字节长度。 特殊说明：如果输入参数ctx为NULL，返回401；其他失败场景返回0。 |

### OH\_CryptoDigest\_GetAlgoName()

```c
const char *OH_CryptoDigest_GetAlgoName(OH_CryptoDigest *ctx)
```

**描述**

获取摘要上下文的算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | [in] 摘要上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回摘要算法名称，不需要调用者释放，在上下文销毁后不可使用。 |

### OH\_DigestCrypto\_Destroy()

```c
void OH_DigestCrypto_Destroy(OH_CryptoDigest *ctx)
```

**描述**

销毁摘要上下文。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoDigest](capi-cryptodigestapi-oh-cryptodigest.md) \*ctx | [in] 摘要上下文。 |
