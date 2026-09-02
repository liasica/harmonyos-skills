---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h
title: crypto_sym_key.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_sym_key.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e4f119dd569420637b32c6af0975aae1cbeae00d314db9c84ed71289b05e5a31
---

## 概述

定义对称密钥接口。

**引用文件：** <CryptoArchitectureKit/crypto\_sym\_key.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoSymKeyApi](capi-cryptosymkeyapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) | OH\_CryptoSymKey | 对称密钥结构体，表示对称密钥。 |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) | OH\_CryptoSymKeyGenerator | 对称密钥生成器结构体，表示对称密钥生成器。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Create(const char \*algoName, OH\_CryptoSymKeyGenerator \*\*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create) | 根据给定的算法名称创建对称密钥生成器。例如AES256。  注意：创建的资源必须通过[OH\_CryptoSymKeyGenerator\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Generate(OH\_CryptoSymKeyGenerator \*ctx, OH\_CryptoSymKey \*\*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate) | 随机生成对称密钥。  注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Convert(OH\_CryptoSymKeyGenerator \*ctx, const Crypto\_DataBlob \*keyData, OH\_CryptoSymKey \*\*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_convert) | 将对称密钥数据转换为对称密钥。  注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。 |
| [const char \*OH\_CryptoSymKeyGenerator\_GetAlgoName(OH\_CryptoSymKeyGenerator \*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_getalgoname) | 获取对称密钥生成器的算法名称。 |
| [void OH\_CryptoSymKeyGenerator\_Destroy(OH\_CryptoSymKeyGenerator \*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy) | 销毁对称密钥生成器。 |
| [const char \*OH\_CryptoSymKey\_GetAlgoName(OH\_CryptoSymKey \*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkey_getalgoname) | 从对称密钥中获取对称密钥算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKey\_GetKeyData(OH\_CryptoSymKey \*keyCtx, Crypto\_DataBlob \*out)](capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata) | 从对称密钥中获取对称密钥数据。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoSymKey\_Destroy(OH\_CryptoSymKey \*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy) | 销毁对称密钥。 |

## 函数说明

### OH\_CryptoSymKeyGenerator\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Create(const char *algoName, OH_CryptoSymKeyGenerator **ctx)
```

**描述**

根据给定的算法名称创建对称密钥生成器。例如AES256。

注意：创建的资源必须通过[OH\_CryptoSymKeyGenerator\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)销毁

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 对称密钥算法名称，不能为NULL。取值如下：  - 从API version 12开始支持"AES128"、"AES192"、"AES256"、"3DES192"、"HMAC|SHA1"、"HMAC|SHA224"、"HMAC|SHA256"、"HMAC|SHA384"、"HMAC|SHA512"、"HMAC|SM3"、"HMAC|MD5"。从API version 26.0.0开始支持"HMAC|SHA3-256"、"HMAC|SHA3-384"、"HMAC|SHA3-512"。  - 从API version 12开始支持"SM4\_128"。  - 从API version 20开始支持"DES64"。  - 从API version 22开始支持"ChaCha20"。  - 从API version 26.0.0开始支持"RC2"、"RC4"、"Blowfish"、"CAST"。注意仅支持将对称密钥数据转换为对称密钥，不支持随机生成。 |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*\*ctx | [out] 指向对称密钥生成器指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx为NULL或algoName为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoSymKeyGenerator\_Generate](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate) 随机生成对称密钥。

[OH\_CryptoSymKeyGenerator\_Convert](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_convert) 将对称密钥数据转换为对称密钥。

### OH\_CryptoSymKeyGenerator\_Generate()

```c
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Generate(OH_CryptoSymKeyGenerator *ctx, OH_CryptoSymKey **keyCtx)
```

**描述**

随机生成对称密钥。

注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | [in] 对称密钥生成器。不能为NULL。 |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*\*keyCtx | [out] 指向对称密钥指针的指针。keyCtx不能为NULL，\*keyCtx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或keyCtx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_INVALID\_CALL：无效的函数调用。可能的原因：算法不支持随机生成密钥（如RC2、RC4、Blowfish、CAST），请使用OH\_CryptoSymKeyGenerator\_Convert接口。适用版本：26.0.0+  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoSymKeyGenerator\_Convert()

```c
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Convert(OH_CryptoSymKeyGenerator *ctx, const Crypto_DataBlob *keyData, OH_CryptoSymKey **keyCtx)
```

**描述**

将对称密钥数据转换为对称密钥。

注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | [in] 对称密钥生成器。不能为NULL。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*keyData | [in] 用于生成对称密钥的数据。不能为NULL。 |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*\*keyCtx | [out] 指向对称密钥指针的指针。keyCtx不能为NULL，\*keyCtx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx、keyData或keyCtx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoSymKeyGenerator\_GetAlgoName()

```c
const char *OH_CryptoSymKeyGenerator_GetAlgoName(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

获取对称密钥生成器的算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | [in] 对称密钥生成器。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回对称密钥算法名称，不需要调用者释放，在生成器销毁后不可使用。 |

### OH\_CryptoSymKeyGenerator\_Destroy()

```c
void OH_CryptoSymKeyGenerator_Destroy(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

销毁对称密钥生成器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | [in] 对称密钥生成器。 |

### OH\_CryptoSymKey\_GetAlgoName()

```c
const char *OH_CryptoSymKey_GetAlgoName(OH_CryptoSymKey *keyCtx)
```

**描述**

从对称密钥中获取对称密钥算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | [in] 对称密钥。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回算法名称，不需要调用者释放，在密钥销毁后不可使用。 |

### OH\_CryptoSymKey\_GetKeyData()

```c
OH_Crypto_ErrCode OH_CryptoSymKey_GetKeyData(OH_CryptoSymKey *keyCtx, Crypto_DataBlob *out)
```

**描述**

从对称密钥中获取对称密钥数据。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | [in] 对称密钥。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储密钥数据的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：keyCtx或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoSymKey\_Destroy()

```c
void OH_CryptoSymKey_Destroy(OH_CryptoSymKey *keyCtx)
```

**描述**

销毁对称密钥。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | [in] 对称密钥。 |
