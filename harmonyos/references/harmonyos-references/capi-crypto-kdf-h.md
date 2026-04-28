---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-kdf-h
title: crypto_kdf.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_kdf.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42a8178eafa6af8222c75db5665f7198a10c5f68e2707cfab153d6a408b2ca52
---

## 概述

PhonePC/2in1TabletTVWearable

定义密钥派生接口。

**引用文件：** <CryptoArchitectureKit/crypto\_kdf.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoKdfApi](capi-cryptokdfapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) | OH\_CryptoKdf | 定义密钥派生函数（KDF）结构。 |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) | OH\_CryptoKdfParams | 定义密钥派生函数（KDF）参数结构。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoKdf\_ParamType](capi-crypto-kdf-h.md#cryptokdf_paramtype) | CryptoKdf\_ParamType | 定义密钥派生函数（KDF）参数类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_Create(const char \*algoName, OH\_CryptoKdfParams \*\*params)](capi-crypto-kdf-h.md#oh_cryptokdfparams_create) | 创建密钥派生函数（KDF）参数。  注意：创建的资源必须通过[OH\_CryptoKdfParams\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdfParams\_SetParam(OH\_CryptoKdfParams \*params, CryptoKdf\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-kdf-h.md#oh_cryptokdfparams_setparam) | 设置密钥派生函数（KDF）参数。 |
| [void OH\_CryptoKdfParams\_Destroy(OH\_CryptoKdfParams \*params)](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy) | 销毁密钥派生函数（KDF）参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Create(const char \*algoName, OH\_CryptoKdf \*\*ctx)](capi-crypto-kdf-h.md#oh_cryptokdf_create) | 创建密钥派生函数（KDF）实例。  注意：创建的资源必须通过[OH\_CryptoKdf\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdf_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoKdf\_Derive(OH\_CryptoKdf \*ctx, const OH\_CryptoKdfParams \*params, int keyLen, Crypto\_DataBlob \*key)](capi-crypto-kdf-h.md#oh_cryptokdf_derive) | 派生密钥。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放key内存。 |
| [void OH\_CryptoKdf\_Destroy(OH\_CryptoKdf \*ctx)](capi-crypto-kdf-h.md#oh_cryptokdf_destroy) | 销毁密钥派生函数（KDF）实例。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### CryptoKdf\_ParamType

PhonePC/2in1TabletTVWearable

```
1. enum CryptoKdf_ParamType
```

**描述**

定义密钥派生函数（KDF）参数类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_KDF\_KEY\_DATABLOB = 0 | 表示KDF的密钥或密码。 |
| CRYPTO\_KDF\_SALT\_DATABLOB = 1 | 表示KDF的盐值。 |
| CRYPTO\_KDF\_INFO\_DATABLOB = 2 | 表示KDF的信息。 |
| CRYPTO\_KDF\_ITER\_COUNT\_INT = 3 | 表示PBKDF2的迭代次数。 |
| CRYPTO\_KDF\_SCRYPT\_N\_UINT64 = 4 | 表示SCRYPT KDF的n参数。 |
| CRYPTO\_KDF\_SCRYPT\_R\_UINT64 = 5 | 表示SCRYPT KDF的r参数。 |
| CRYPTO\_KDF\_SCRYPT\_P\_UINT64 = 6 | 表示SCRYPT KDF的p参数。 |
| CRYPTO\_KDF\_SCRYPT\_MAX\_MEM\_UINT64 = 7 | 表示SCRYPT KDF的最大内存使用量。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoKdfParams\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)
```

**描述**

创建密钥派生函数（KDF）参数。

注意：创建的资源必须通过[OH\_CryptoKdfParams\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdfparams_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | KDF算法名称。  例如"HKDF|SHA384|EXTRACT\_AND\_EXPAND"、"PBKDF2|SHA384"。 |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*\*params | KDF参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKdfParams\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置密钥派生函数（KDF）参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | KDF参数。 |
| [CryptoKdf\_ParamType](capi-crypto-kdf-h.md#cryptokdf_paramtype) type | KDF参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | KDF参数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKdfParams\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)
```

**描述**

销毁密钥派生函数（KDF）参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | KDF参数。 |

### OH\_CryptoKdf\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)
```

**描述**

创建密钥派生函数（KDF）实例。

注意：创建的资源必须通过[OH\_CryptoKdf\_Destroy](capi-crypto-kdf-h.md#oh_cryptokdf_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | KDF算法名称。 |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*\*ctx | KDF实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKdf\_Derive()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key)
```

**描述**

派生密钥。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放key内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*ctx | KDF实例。 |
| [const OH\_CryptoKdfParams](capi-cryptokdfapi-oh-cryptokdfparams.md) \*params | KDF参数。 |
| int keyLen | 密钥派生长度。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*key | 派生出的密钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoKdf\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)
```

**描述**

销毁密钥派生函数（KDF）实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKdf](capi-cryptokdfapi-oh-cryptokdf.md) \*ctx | KDF实例。 |
