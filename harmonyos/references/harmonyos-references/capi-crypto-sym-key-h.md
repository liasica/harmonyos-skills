---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-key-h
title: crypto_sym_key.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_sym_key.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:00+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:37c1ca0daaced7e877d1683dd8c91abb93b9e806d8813463747fe63e39340567
---

## 概述

PhonePC/2in1TabletTVWearable

定义对称密钥接口。

**引用文件：** <CryptoArchitectureKit/crypto\_sym\_key.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoSymKeyApi](capi-cryptosymkeyapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) | OH\_CryptoSymKey | 定义对称密钥结构体。 |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) | OH\_CryptoSymKeyGenerator | 定义对称密钥结构。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Create(const char \*algoName, OH\_CryptoSymKeyGenerator \*\*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create) | 根据给定的算法名称创建对称密钥生成器。  注意：创建的资源必须通过[OH\_CryptoSymKeyGenerator\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Generate(OH\_CryptoSymKeyGenerator \*ctx, OH\_CryptoSymKey \*\*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate) | 随机生成对称密钥。  注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKeyGenerator\_Convert(OH\_CryptoSymKeyGenerator \*ctx, const Crypto\_DataBlob \*keyData, OH\_CryptoSymKey \*\*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_convert) | 将对称密钥数据转换为对称密钥。  注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。 |
| [const char \*OH\_CryptoSymKeyGenerator\_GetAlgoName(OH\_CryptoSymKeyGenerator \*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_getalgoname) | 获取对称密钥生成器的算法名称。 |
| [void OH\_CryptoSymKeyGenerator\_Destroy(OH\_CryptoSymKeyGenerator \*ctx)](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy) | 销毁对称密钥生成器。 |
| [const char \*OH\_CryptoSymKey\_GetAlgoName(OH\_CryptoSymKey \*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkey_getalgoname) | 从对称密钥获取对称密钥算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymKey\_GetKeyData(OH\_CryptoSymKey \*keyCtx, Crypto\_DataBlob \*out)](capi-crypto-sym-key-h.md#oh_cryptosymkey_getkeydata) | 从密钥实例获取对称密钥数据。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoSymKey\_Destroy(OH\_CryptoSymKey \*keyCtx)](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy) | 销毁对称密钥实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoSymKeyGenerator\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Create(const char *algoName, OH_CryptoSymKeyGenerator **ctx)
```

**描述**

根据给定的算法名称创建对称密钥生成器。

注意：创建的资源必须通过[OH\_CryptoSymKeyGenerator\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成生成器的算法名称。  例如"AES256"、"AES128"、"SM4"等。 |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*\*ctx | 指向对称密钥生成器实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSymKeyGenerator\_Generate()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Generate(OH_CryptoSymKeyGenerator *ctx, OH_CryptoSymKey **keyCtx)
```

**描述**

随机生成对称密钥。

注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | 指向对称密钥生成器实例。 |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*\*keyCtx | 指向对称密钥的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSymKeyGenerator\_Convert()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Convert(OH_CryptoSymKeyGenerator *ctx, const Crypto_DataBlob *keyData, OH_CryptoSymKey **keyCtx)
```

**描述**

将对称密钥数据转换为对称密钥。

注意：使用完成后必须通过[OH\_CryptoSymKey\_Destroy](capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | 指向对称密钥生成器实例。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*keyData | 指向生成对称密钥的数据。 |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*\*keyCtx | 指向对称密钥实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSymKeyGenerator\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoSymKeyGenerator_GetAlgoName(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

获取对称密钥生成器的算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | 指向对称密钥生成器实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回对称密钥生成器算法名称。 |

### OH\_CryptoSymKeyGenerator\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoSymKeyGenerator_Destroy(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

销毁对称密钥生成器。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKeyGenerator](capi-cryptosymkeyapi-oh-cryptosymkeygenerator.md) \*ctx | 指向对称密钥生成器实例的指针。 |

### OH\_CryptoSymKey\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoSymKey_GetAlgoName(OH_CryptoSymKey *keyCtx)
```

**描述**

从对称密钥获取对称密钥算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | 指向对称密钥实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回对称密钥算法名称。 |

### OH\_CryptoSymKey\_GetKeyData()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSymKey_GetKeyData(OH_CryptoSymKey *keyCtx, Crypto_DataBlob *out)
```

**描述**

从密钥实例获取对称密钥数据。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | 指向对称密钥实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 获取到的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSymKey\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoSymKey_Destroy(OH_CryptoSymKey *keyCtx)
```

**描述**

销毁对称密钥实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*keyCtx | 指向对称密钥实例。 |
