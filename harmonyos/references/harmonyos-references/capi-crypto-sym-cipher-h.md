---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-sym-cipher-h
title: crypto_sym_cipher.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_sym_cipher.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7ece8415d45e65a107cca7b983f0791ee0eeab3f3a7e4a9e4cd0894d7b18c02d
---

## 概述

定义对称密钥加解密接口。

**引用文件：** <CryptoArchitectureKit/crypto\_sym\_cipher.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoSymCipherApi](capi-cryptosymcipherapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) | OH\_CryptoSymCipher | 对称密钥加解密结构体，表示对称密钥加解密上下文。 |
| [OH\_CryptoSymCipherParams](capi-cryptosymcipherapi-oh-cryptosymcipherparams.md) | OH\_CryptoSymCipherParams | 对称密钥加解密参数结构体，表示对称密钥加解密参数。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoSymCipher\_ParamsType](capi-crypto-sym-cipher-h.md#cryptosymcipher_paramstype) | CryptoSymCipher\_ParamsType | 定义加解密参数类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipherParams\_Create(OH\_CryptoSymCipherParams \*\*params)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_create) | 创建对称密钥加解密参数。  注意：创建的资源必须通过[OH\_CryptoSymCipherParams\_Destroy](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipherParams\_SetParam(OH\_CryptoSymCipherParams \*params, CryptoSymCipher\_ParamsType paramsType, Crypto\_DataBlob \*value)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam) | 设置加解密参数。 |
| [void OH\_CryptoSymCipherParams\_Destroy(OH\_CryptoSymCipherParams \*params)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy) | 销毁加解密参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipher\_Create(const char \*algoName, OH\_CryptoSymCipher \*\*ctx)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create) | 根据给定的算法名称创建对称密钥加解密上下文。  注意：创建的资源必须通过[OH\_CryptoSymCipher\_Destroy](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipher\_Init(OH\_CryptoSymCipher \*ctx, Crypto\_CipherMode mod, OH\_CryptoSymKey \*key, OH\_CryptoSymCipherParams \*params)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init) | 使用给定的加解密模式、密钥和参数初始化加解密操作。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipher\_Update(OH\_CryptoSymCipher \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update) | 更新加解密数据，输出已加密或已解密的数据。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSymCipher\_Final(OH\_CryptoSymCipher \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final) | 结束加解密操作，输出最终结果。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [const char \*OH\_CryptoSymCipher\_GetAlgoName(OH\_CryptoSymCipher \*ctx)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_getalgoname) | 获取对称密钥加解密算法名称。 |
| [void OH\_CryptoSymCipher\_Destroy(OH\_CryptoSymCipher \*ctx)](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy) | 销毁对称密钥加解密上下文。 |

## 枚举类型说明

### CryptoSymCipher\_ParamsType

```c
enum CryptoSymCipher_ParamsType
```

**描述**

定义加解密参数类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_IV\_DATABLOB = 100 | 初始化向量（IV）参数。 |
| CRYPTO\_AAD\_DATABLOB = 101 | AEAD模式（如GCM、CCM）下的附加认证数据（AAD）。 |
| CRYPTO\_TAG\_DATABLOB = 102 | AEAD模式（如GCM、CCM）中的认证标签（Tag），用于数据完整性校验。 |

## 函数说明

### OH\_CryptoSymCipherParams\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSymCipherParams_Create(OH_CryptoSymCipherParams **params)
```

**描述**

创建对称密钥加解密参数。

注意：创建的资源必须通过[OH\_CryptoSymCipherParams\_Destroy](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipherParams](capi-cryptosymcipherapi-oh-cryptosymcipherparams.md) \*\*params | [out] 指向加解密参数指针的指针。params不能为NULL，\*params必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：params为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

**参考：**

[OH\_CryptoSymCipherParams\_SetParam](capi-crypto-sym-cipher-h.md#oh_cryptosymcipherparams_setparam) 设置加解密参数。

### OH\_CryptoSymCipherParams\_SetParam()

```c
OH_Crypto_ErrCode OH_CryptoSymCipherParams_SetParam(OH_CryptoSymCipherParams *params, CryptoSymCipher_ParamsType paramsType, Crypto_DataBlob *value)
```

**描述**

设置加解密参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipherParams](capi-cryptosymcipherapi-oh-cryptosymcipherparams.md) \*params | [in] 加解密参数。不能为NULL。 |
| [CryptoSymCipher\_ParamsType](capi-crypto-sym-cipher-h.md#cryptosymcipher_paramstype) paramsType | [in] 设置的加解密参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [in] 参数值。本接口为浅拷贝，不会复制value中的数据。 调用者必须确保value指向的内存在[OH\_CryptoSymCipher\_Init](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)调用完成前保持有效。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：params或value为NULL，或paramsType无法识别。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

### OH\_CryptoSymCipherParams\_Destroy()

```c
void OH_CryptoSymCipherParams_Destroy(OH_CryptoSymCipherParams *params)
```

**描述**

销毁加解密参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipherParams](capi-cryptosymcipherapi-oh-cryptosymcipherparams.md) \*params | [in] 加解密参数。 |

### OH\_CryptoSymCipher\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSymCipher_Create(const char *algoName, OH_CryptoSymCipher **ctx)
```

**描述**

根据给定的算法名称创建对称密钥加解密上下文。

注意：创建的资源必须通过[OH\_CryptoSymCipher\_Destroy](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 对称加解密算法名称，不能为NULL。格式为"算法|模式|填充"，各部分以"|"分隔。算法包括：AES128、AES192、AES256、SM4\_128、3DES192、DES64、ChaCha20、RC2、Blowfish、CAST。模式包括：ECB、CBC、CTR、OFB、CFB、CFB1、CFB8、CFB64、CFB128、GCM、CCM、XTS、Poly1305。填充包括：NoPadding、PKCS5、PKCS7。各算法支持情况如下：  - 从API version 12开始支持AES系列：AES128、AES192、AES256算法，ECB、CBC、CTR、OFB、CFB、GCM、CCM模式，填充为NoPadding、PKCS7。 示例："AES128|GCM"、"AES256|CBC|PKCS7"。  - 从API version 12开始支持3DES系列：3DES192算法，ECB、CBC、OFB、CFB模式，填充为NoPadding、PKCS5、PKCS7。示例："3DES192|CBC|PKCS5"。  - 从API version 12开始支持SM4系列：SM4\_128算法，ECB、CBC、CTR、OFB、CFB、CFB128、GCM模式，填充为NoPadding、PKCS7。示例："SM4\_128|CBC|PKCS7"、"SM4\_128|GCM|NoPadding"。  - 从API version 20开始支持DES系列：DES64算法，ECB、CBC、OFB、CFB模式，填充为NoPadding、PKCS5、PKCS7。示例："DES64|CBC|PKCS5"。  - 从API version 22开始支持AES128\_WRAP、AES192\_WRAP、AES256\_WRAP算法。 示例："AES128\_WRAP"、"AES192\_WRAP"、"AES256\_WRAP"。  - 从API version 22开始支持"ChaCha20"、"ChaCha20|Poly1305"。 示例："ChaCha20|Poly1305"、"ChaCha20"。  - 从API version 26.0.0开始支持AES算法，XTS模式。 示例："AES128|XTS"、"AES256|XTS"。注意不支持AES192。  - 从API version 26.0.0开始支持RC2算法，ECB、CBC、OFB、CFB模式，填充为NoPadding、PKCS5、PKCS7。 示例："RC2|CBC|PKCS5"。  - 从API version 26.0.0开始支持"RC4"。 示例："RC4"。  - 从API version 26.0.0开始支持Blowfish算法，ECB、CBC、OFB、CFB模式，填充为NoPadding、PKCS5、PKCS7。示例："Blowfish|CBC|PKCS5"。  - 从API version 26.0.0开始支持CAST算法，ECB、CBC、OFB、CFB模式，填充为NoPadding、PKCS5、PKCS7。 示例："CAST|CBC|PKCS5"。填充说明：  - ECB、CBC模式涉及填充：当明文长度不是算法分组大小的整数倍时，必须使用PKCS5或PKCS7填充；使用NoPadding时，输入数据长度必须是算法分组大小的整数倍（AES和SM4为16字节，DES、3DES、RC2、Blowfish和CAST为8字节）。  - CTR、OFB、CFB、CFB1、CFB8、CFB64、CFB128、GCM、CCM模式将分组密码转化为流模式，不需要填充，指定任意填充均按NoPadding处理。  - XTS模式不涉及填充，不需要指定填充字段，指定任意填充均按NoPadding处理。  - ChaCha20为流密码算法，不需要指定填充字段，指定任意填充均按NoPadding处理。 |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*\*ctx | [out] 指向对称密钥加解密上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx为NULL或algoName为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数无效。适用版本：20+  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

**参考：**

[OH\_CryptoSymCipher\_Init](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init) 使用给定的加解密模式、密钥和参数初始化加解密操作。

### OH\_CryptoSymCipher\_Init()

```c
OH_Crypto_ErrCode OH_CryptoSymCipher_Init(OH_CryptoSymCipher *ctx, Crypto_CipherMode mod, OH_CryptoSymKey *key, OH_CryptoSymCipherParams *params)
```

**描述**

使用给定的加解密模式、密钥和参数初始化加解密操作。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*ctx | [in] 对称密钥加解密上下文。不能为NULL。 |
| [Crypto\_CipherMode](capi-crypto-common-h.md#crypto_ciphermode) mod | [in] 加解密模式，加密或解密。 |
| [OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*key | [in] 对称密钥。不能为NULL。 |
| [OH\_CryptoSymCipherParams](capi-cryptosymcipherapi-oh-cryptosymcipherparams.md) \*params | [in] 算法参数，例如IV。ECB模式下需为NULL，其他模式不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或key为NULL，或非ECB模式下IV缺失或长度错误。  CRYPTO\_NOT\_SUPPORTED：不支持的操作。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数无效。适用版本：20+  CRYPTO\_OPERTION\_ERROR：加解密初始化失败。可能的原因：密钥长度与算法不匹配。 |

**参考：**

[OH\_CryptoSymCipher\_Update](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update) 更新加解密数据，输出已加密或已解密的数据。

[OH\_CryptoSymCipher\_Final](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final) 结束加解密操作，输出最终结果。

### OH\_CryptoSymCipher\_Update()

```c
OH_Crypto_ErrCode OH_CryptoSymCipher_Update(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

更新加解密数据，输出已加密或已解密的数据。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*ctx | [in] 对称密钥加解密上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待加密或解密的数据。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储更新数据的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx、in或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数无效。适用版本：20+  CRYPTO\_OPERTION\_ERROR：加解密更新失败。 |

**参考：**

[OH\_CryptoSymCipher\_Final](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final) 结束加解密操作，输出最终结果。

### OH\_CryptoSymCipher\_Final()

```c
OH_Crypto_ErrCode OH_CryptoSymCipher_Final(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

结束加解密操作，输出最终结果。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*ctx | [in] 对称密钥加解密上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待加密或解密的数据。如果数据已通过[OH\_CryptoSymCipher\_Update](capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)接口更新了所有数据，此参数可以为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储最终结果的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数无效。适用版本：20+  CRYPTO\_OPERTION\_ERROR：加解密完成失败。可能的原因：  解密时IV或密钥错误；AEAD（GCM/CCM）认证标签验证失败（TAG、AAD、密文或密钥错误）；  分组密码（如AES-CBC/ECB）解密时密文长度不是分组大小的整数倍；  分组密码使用NoPadding加密时明文长度不是分组大小的整数倍。 |

### OH\_CryptoSymCipher\_GetAlgoName()

```c
const char *OH_CryptoSymCipher_GetAlgoName(OH_CryptoSymCipher *ctx)
```

**描述**

获取对称密钥加解密算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*ctx | [in] 对称密钥加解密上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回对称密钥加解密算法名称，不需要调用者释放，在上下文销毁后不可使用。 |

### OH\_CryptoSymCipher\_Destroy()

```c
void OH_CryptoSymCipher_Destroy(OH_CryptoSymCipher *ctx)
```

**描述**

销毁对称密钥加解密上下文。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSymCipher](capi-cryptosymcipherapi-oh-cryptosymcipher.md) \*ctx | [in] 对称密钥加解密上下文。 |
