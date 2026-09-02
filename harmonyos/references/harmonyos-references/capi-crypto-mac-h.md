---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h
title: crypto_mac.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_mac.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec9e720070dccc233d2f1412a812831b93471738062a7d6c48ff62cbf48f9c53
---

## 概述

定义消息认证码接口。

**引用文件：** <CryptoArchitectureKit/crypto\_mac.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoMacApi](capi-cryptomacapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) | OH\_CryptoMac | MAC结构体，表示MAC上下文。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoMac\_ParamType](capi-crypto-mac-h.md#cryptomac_paramtype) | CryptoMac\_ParamType | 定义MAC算法参数类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Create(const char \*algoName, OH\_CryptoMac \*\*ctx)](capi-crypto-mac-h.md#oh_cryptomac_create) | 根据给定的算法名称创建MAC上下文。  注意：创建的资源必须通过[OH\_CryptoMac\_Destroy](capi-crypto-mac-h.md#oh_cryptomac_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_SetParam(OH\_CryptoMac \*ctx, CryptoMac\_ParamType type, const Crypto\_DataBlob \*value)](capi-crypto-mac-h.md#oh_cryptomac_setparam) | 设置MAC上下文的指定参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Init(OH\_CryptoMac \*ctx, const OH\_CryptoSymKey \*key)](capi-crypto-mac-h.md#oh_cryptomac_init) | 使用对称密钥初始化MAC上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Update(OH\_CryptoMac \*ctx, const Crypto\_DataBlob \*in)](capi-crypto-mac-h.md#oh_cryptomac_update) | 更新MAC数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Final(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out)](capi-crypto-mac-h.md#oh_cryptomac_final) | 结束MAC操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_GetLength(OH\_CryptoMac \*ctx, uint32\_t \*length)](capi-crypto-mac-h.md#oh_cryptomac_getlength) | 获取MAC结果的长度。 |
| [void OH\_CryptoMac\_Destroy(OH\_CryptoMac \*ctx)](capi-crypto-mac-h.md#oh_cryptomac_destroy) | 销毁MAC上下文。 |

## 枚举类型说明

### CryptoMac\_ParamType

```c
enum CryptoMac_ParamType
```

**描述**

定义MAC算法参数类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_MAC\_DIGEST\_NAME\_STR = 0 | HMAC的消息摘要算法名称，通过[OH\_CryptoMac\_SetParam](capi-crypto-mac-h.md#oh_cryptomac_setparam)设置。取值："SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"、"SM3"、"MD5"。从API version 26.0.0开始支持"SHA3-256"、"SHA3-384"、"SHA3-512"。  **起始版本：** 20 |
| CRYPTO\_MAC\_CIPHER\_NAME\_STR = 1 | CMAC的对称加密算法名称，通过[OH\_CryptoMac\_SetParam](capi-crypto-mac-h.md#oh_cryptomac_setparam)设置。取值："AES128"、"AES256"。  **起始版本：** 20 |

## 函数说明

### OH\_CryptoMac\_Create()

```c
OH_Crypto_ErrCode OH_CryptoMac_Create(const char *algoName, OH_CryptoMac **ctx)
```

**描述**

根据给定的算法名称创建MAC上下文。

注意：创建的资源必须通过[OH\_CryptoMac\_Destroy](capi-crypto-mac-h.md#oh_cryptomac_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] MAC算法名称，不能为NULL。支持“HMAC”和“CMAC”。 |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*\*ctx | [out] 指向MAC上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：algoName或ctx为NULL，或algoName不是"HMAC"或"CMAC"。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoMac\_SetParam](capi-crypto-mac-h.md#oh_cryptomac_setparam) 设置MAC上下文的指定参数。

### OH\_CryptoMac\_SetParam()

```c
OH_Crypto_ErrCode OH_CryptoMac_SetParam(OH_CryptoMac *ctx, CryptoMac_ParamType type, const Crypto_DataBlob *value)
```

**描述**

设置MAC上下文的指定参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。不能为NULL。 |
| [CryptoMac\_ParamType](capi-crypto-mac-h.md#cryptomac_paramtype) type | [in] MAC参数类型。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [in] 参数值。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx、value或value->data为NULL，type对当前MAC算法无效，或摘要/加密算法名称不支持。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：参数拷贝内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoMac\_Init](capi-crypto-mac-h.md#oh_cryptomac_init) 使用对称密钥初始化MAC上下文。

### OH\_CryptoMac\_Init()

```c
OH_Crypto_ErrCode OH_CryptoMac_Init(OH_CryptoMac *ctx, const OH_CryptoSymKey *key)
```

**描述**

使用对称密钥初始化MAC上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。不能为NULL。 |
| [const OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*key | [in] 对称密钥。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或key为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：MAC初始化失败。可能的原因：密钥长度与算法不匹配（例如CMAC使用AES-128需要16字节密钥）。 |

**参考：**

[OH\_CryptoMac\_Update](capi-crypto-mac-h.md#oh_cryptomac_update) 更新MAC数据。

### OH\_CryptoMac\_Update()

```c
OH_Crypto_ErrCode OH_CryptoMac_Update(OH_CryptoMac *ctx, const Crypto_DataBlob *in)
```

**描述**

更新MAC数据。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。不能为NULL。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待更新的数据。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或in为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：MAC更新失败。 |

**参考：**

[OH\_CryptoMac\_Final](capi-crypto-mac-h.md#oh_cryptomac_final) 结束MAC操作。

### OH\_CryptoMac\_Final()

```c
OH_Crypto_ErrCode OH_CryptoMac_Final(OH_CryptoMac *ctx, Crypto_DataBlob *out)
```

**描述**

结束MAC操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储MAC结果的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：MAC完成操作失败。 |

### OH\_CryptoMac\_GetLength()

```c
OH_Crypto_ErrCode OH_CryptoMac_GetLength(OH_CryptoMac *ctx, uint32_t *length)
```

**描述**

获取MAC结果的长度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。不能为NULL。 |
| uint32\_t \*length | [out] MAC结果的字节长度。不能为NULL。由调用者分配内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或length为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoMac\_Destroy()

```c
void OH_CryptoMac_Destroy(OH_CryptoMac *ctx)
```

**描述**

销毁MAC上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | [in] MAC上下文。 |
