---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h
title: crypto_kdf.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_kdf.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f6acc3946af5f9741b2c51f388094f91fef77605078f9198cc2518ae8452b7df
---

## 概述

定义密钥派生接口。

**引用文件：** <CryptoArchitectureKit/crypto\_kdf.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoKdfApi](capi-cryptokdfapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) | OH\_CryptoKdf | KDF结构体，表示KDF上下文。 |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) | OH\_CryptoKdfParams | KDF参数结构体，表示KDF参数。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoKdf\_ParamType](capi-crypto-kdf-h.md#cryptokdf_paramtype) | CryptoKdf\_ParamType | 定义KDF参数类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_Create(const char \*algoName, OH\_CryptoKdfParams \*\*params)](capi-crypto-kdf-h.md#oh_cryptokdfparams_create) | 创建KDF参数。  注意：创建的资源必须通过[OH\_CryptoKdfParams\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_SetParam(OH\_CryptoKdfParams \*params, CryptoKdf\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam) | 设置KDF参数。 |
| [void OH\_CryptoKdfParams\_Destroy(OH\_CryptoKdfParams \*params)](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy) | 销毁KDF参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Create(const char \*algoName, OH\_CryptoKdf \*\*ctx)](capi-crypto-kdf-h.md#oh_cryptokdf_create) | 根据给定的算法名称创建KDF上下文。  注意：创建的资源必须通过[OH\_CryptoKdf\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdf_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Derive(OH\_CryptoKdf \*ctx, const OH\_CryptoKdfParams \*params, int keyLen, Crypto\_DataBlob \*key)](capi-crypto-kdf-h.md#oh_cryptokdf_derive) | 派生密钥。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放key内存。 |
| [void OH\_CryptoKdf\_Destroy(OH\_CryptoKdf \*ctx)](capi-crypto-kdf-h.md#oh_cryptokdf_destroy) | 销毁KDF上下文。 |

## 枚举类型说明

### CryptoKdf\_ParamType

```c
enum CryptoKdf_ParamType
```

**描述**

定义KDF参数类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_KDF\_KEY\_DATABLOB = 0 | 表示KDF的密钥或密码。 |
| CRYPTO\_KDF\_SALT\_DATABLOB = 1 | 表示KDF的盐值。 |
| CRYPTO\_KDF\_INFO\_DATABLOB = 2 | 表示KDF的Info信息。 |
| CRYPTO\_KDF\_ITER\_COUNT\_INT = 3 | 表示PBKDF2的迭代次数。 |
| CRYPTO\_KDF\_SCRYPT\_N\_UINT64 = 4 | 表示SCRYPT KDF的n参数。 |
| CRYPTO\_KDF\_SCRYPT\_R\_UINT64 = 5 | 表示SCRYPT KDF的r参数。 |
| CRYPTO\_KDF\_SCRYPT\_P\_UINT64 = 6 | 表示SCRYPT KDF的p参数。 |
| CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64 = 7 | 表示SCRYPT KDF的最大内存参数。 |

## 函数说明

### OH\_CryptoKdfParams\_Create()

```c
OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)
```

**描述**

创建KDF参数。

注意：创建的资源必须通过[OH\_CryptoKdfParams\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] KDF参数算法名称，不能为NULL。取值如下：  - 从API version 20开始支持"HKDF"、"PBKDF2"、"SCRYPT"。  - 从API version 22开始支持"X963KDF"。 |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*\*params | [out] 指向KDF参数指针的指针。params不能为NULL，\*params必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：algoName或params为NULL，或者algoName不是支持的KDF类型。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoKdfParams\_SetParam](capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam) 设置KDF参数。

### OH\_CryptoKdfParams\_SetParam()

```c
OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置KDF参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | [in] KDF参数。不能为NULL。 |
| [CryptoKdf\_ParamType](capi-crypto-kdf-h.md#cryptokdf_paramtype) type | [in] KDF参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [in] KDF参数值。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：params或value为NULL，value->data为NULL，或者type对于KDF算法无效。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：参数拷贝内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoKdfParams\_Destroy()

```c
void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)
```

**描述**

销毁KDF参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | [in] KDF参数。 |

### OH\_CryptoKdf\_Create()

```c
OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)
```

**描述**

根据给定的算法名称创建KDF上下文。

注意：创建的资源必须通过[OH\_CryptoKdf\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdf_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] KDF算法名称。不能为NULL。格式为"KDF类型|摘要算法"，取值如下：  - 从API version 20开始支持"PBKDF2|SHA1"、"PBKDF2|SHA224"、"PBKDF2|SHA256"、"PBKDF2|SHA384"、"PBKDF2|SHA512"、"PBKDF2|SM3"。从API version 26.0.0开始支持"PBKDF2|SHA3-256"、"PBKDF2|SHA3-384"、"PBKDF2|SHA3-512"。  - 从API version 20开始支持"HKDF|SHA1"、"HKDF|SHA224"、"HKDF|SHA256"、"HKDF|SHA384"、"HKDF|SHA512"、"HKDF|SM3"。HKDF支持可选的第三个参数指定模式："EXTRACT\_AND\_EXPAND"（默认）、"EXTRACT\_ONLY"、"EXPAND\_ONLY"，示例："HKDF|SHA256|EXTRACT\_ONLY"。从API version 26.0.0开始支持"HKDF|SHA3-256"、"HKDF|SHA3-384"、"HKDF|SHA3-512"。  - 从API version 20开始支持"SCRYPT"。  - 从API version 22开始支持"X963KDF|SHA1"、"X963KDF|SHA224"、"X963KDF|SHA256"、"X963KDF|SHA384"、"X963KDF|SHA512"。从API version 26.0.0开始支持"X963KDF|SHA3-256"、"X963KDF|SHA3-384"、"X963KDF|SHA3-512"。 |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*\*ctx | [out] 指向KDF上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：algoName或ctx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoKdf\_Derive](capi-crypto-kdf-h.md#oh_cryptokdf_derive) 派生密钥。

### OH\_CryptoKdf\_Derive()

```c
OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key)
```

**描述**

派生密钥。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放key内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*ctx | [in] KDF上下文。不能为NULL。 |
| [const OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | [in] KDF参数。不能为NULL。 |
| int keyLen | [in] 派生密钥的字节长度。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*key | [out] 指向用于存储派生密钥的Crypto\_DataBlob结构体的指针。不能为NULL。 调用前需将key初始化为{0}，不要预分配key->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx、params或key为NULL，或者keyLen小于等于0，或者缺少必需的参数（如HKDF的密钥、Scrypt的密码或盐值）。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密钥派生失败。 |

### OH\_CryptoKdf\_Destroy()

```c
void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)
```

**描述**

销毁KDF上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*ctx | [in] KDF上下文。 |
