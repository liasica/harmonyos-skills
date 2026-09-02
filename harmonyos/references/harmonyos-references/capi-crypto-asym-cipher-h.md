---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-cipher-h
title: crypto_asym_cipher.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_asym_cipher.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:07efba87da72dfc79e545ad5097ba2874e5b516eccd454d58a53af64adc38db1
---

## 概述

定义非对称加解密接口。

**引用文件：** <CryptoArchitectureKit/crypto\_asym\_cipher.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoAsymCipherApi](capi-cryptoasymcipherapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoAsymCipher](capi-cryptoasymcipherapi-oh-cryptoasymcipher.md) | OH\_CryptoAsymCipher | 非对称加解密结构体，表示非对称加解密上下文。 |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) | OH\_CryptoSm2CiphertextSpec | SM2密文规格结构体，表示SM2密文规格。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoSm2CiphertextSpec\_item](capi-crypto-asym-cipher-h.md#cryptosm2ciphertextspec_item) | CryptoSm2CiphertextSpec\_item | 定义SM2密文规格项类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Create(const char \*algoName, OH\_CryptoAsymCipher \*\*ctx)](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_create) | 根据给定的算法名称创建非对称加解密上下文。  注意：创建的资源必须通过[OH\_CryptoAsymCipher\_Destroy](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Init(OH\_CryptoAsymCipher \*ctx, Crypto\_CipherMode mode, OH\_CryptoKeyPair \*key)](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init) | 使用给定的加解密模式和密钥初始化非对称加解密上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymCipher\_Final(OH\_CryptoAsymCipher \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final) | 结束加解密操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoAsymCipher\_Destroy(OH\_CryptoAsymCipher \*ctx)](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_destroy) | 销毁非对称加解密上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Create(Crypto\_DataBlob \*sm2Ciphertext, OH\_CryptoSm2CiphertextSpec \*\*spec)](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_create) | 创建SM2密文规格。  注意：创建的资源必须通过[OH\_CryptoSm2CiphertextSpec\_Destroy](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_GetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*out)](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_getitem) | 获取SM2密文的指定项。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_SetItem(OH\_CryptoSm2CiphertextSpec \*spec, CryptoSm2CiphertextSpec\_item item, Crypto\_DataBlob \*in)](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_setitem) | 设置SM2密文规格的指定项。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSm2CiphertextSpec\_Encode(OH\_CryptoSm2CiphertextSpec \*spec, Crypto\_DataBlob \*out)](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_encode) | 将SM2密文规格编码为DER格式密文。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoSm2CiphertextSpec\_Destroy(OH\_CryptoSm2CiphertextSpec \*spec)](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_destroy) | 销毁SM2密文规格。 |

## 枚举类型说明

### CryptoSm2CiphertextSpec\_item

```c
enum CryptoSm2CiphertextSpec_item
```

**描述**

定义SM2密文规格项类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_X = 0 | 公钥x，也称为C1x。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C1\_Y = 1 | 公钥y，也称为C1y。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C2 = 2 | 哈希值，也称为C2。 |
| CRYPTO\_SM2\_CIPHERTEXT\_C3 = 3 | 密文数据，也称为C3。 |

## 函数说明

### OH\_CryptoAsymCipher\_Create()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Create(const char *algoName, OH_CryptoAsymCipher **ctx)
```

**描述**

根据给定的算法名称创建非对称加解密上下文。

注意：创建的资源必须通过[OH\_CryptoAsymCipher\_Destroy](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 非对称加解密算法名称，不能为NULL。取值如下：  - RSA算法PKCS1填充模式：取值为"RSA|PKCS1"。  - RSA算法OAEP填充模式：格式为"RSA|PKCS1\_OAEP|摘要|MGF1摘要"，示例："RSA|PKCS1\_OAEP|SHA256|MGF1\_SHA256"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。MGF1摘要支持"MGF1\_SHA1"、"MGF1\_SHA224"、"MGF1\_SHA256"、"MGF1\_SHA384"、"MGF1\_SHA512"。  - RSA算法NoPadding填充模式：取值为"RSA|NoPadding"。  - SM2算法：格式为"SM2|摘要"，示例："SM2|SM3"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"、"SM3"。 |
| [OH\_CryptoAsymCipher](capi-cryptoasymcipherapi-oh-cryptoasymcipher.md) \*\*ctx | [out] 指向非对称加解密上下文指针的指针。ctx不能为NULL，\*ctx必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：algoName或ctx为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

**参考：**

[OH\_CryptoAsymCipher\_Init](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_init) 初始化非对称加解密上下文。

### OH\_CryptoAsymCipher\_Init()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Init(OH_CryptoAsymCipher *ctx, Crypto_CipherMode mode, OH_CryptoKeyPair *key)
```

**描述**

使用给定的加解密模式和密钥初始化非对称加解密上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymCipher](capi-cryptoasymcipherapi-oh-cryptoasymcipher.md) \*ctx | [in] 非对称加解密上下文。不能为NULL。 |
| [Crypto\_CipherMode](capi-crypto-common-h.md#crypto_ciphermode) mode | [in] 加解密模式，加密或解密。 |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*key | [in] 非对称密钥。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或key为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：加解密初始化失败。 |

**参考：**

[OH\_CryptoAsymCipher\_Final](capi-crypto-asym-cipher-h.md#oh_cryptoasymcipher_final) 结束加解密操作。

### OH\_CryptoAsymCipher\_Final()

```c
OH_Crypto_ErrCode OH_CryptoAsymCipher_Final(OH_CryptoAsymCipher *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

结束加解密操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymCipher](capi-cryptoasymcipherapi-oh-cryptoasymcipher.md) \*ctx | [in] 非对称加解密上下文。不能为NULL。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待加密或解密的数据。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储加密或解密结果的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx、in或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：加解密完成失败。可能的原因：  RSA加密时明文超过密钥长度和填充模式允许的最大长度；  RSA解密时密钥错误或密文损坏；  SM2解密时密钥错误或密文损坏；  SM2密文的ASN.1结构无效。 |

### OH\_CryptoAsymCipher\_Destroy()

```c
void OH_CryptoAsymCipher_Destroy(OH_CryptoAsymCipher *ctx)
```

**描述**

销毁非对称加解密上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymCipher](capi-cryptoasymcipherapi-oh-cryptoasymcipher.md) \*ctx | [in] 非对称加解密上下文。 |

### OH\_CryptoSm2CiphertextSpec\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Create(Crypto_DataBlob *sm2Ciphertext, OH_CryptoSm2CiphertextSpec **spec)
```

**描述**

创建SM2密文规格。

注意：创建的资源必须通过[OH\_CryptoSm2CiphertextSpec\_Destroy](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*sm2Ciphertext | [in] DER格式的SM2密文，如果为NULL则创建空的SM2密文规格。 |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) \*\*spec | [out] 指向SM2密文规格指针的指针。spec不能为NULL，\*spec必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：解析SM2密文失败。可能的原因：输入数据不是有效的DER编码SM2密文。 |

**参考：**

[OH\_CryptoSm2CiphertextSpec\_GetItem](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_getitem) 获取SM2密文的指定项。

[OH\_CryptoSm2CiphertextSpec\_SetItem](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_setitem) 设置SM2密文规格的指定项。

### OH\_CryptoSm2CiphertextSpec\_GetItem()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_GetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *out)
```

**描述**

获取SM2密文的指定项。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) \*spec | [in] SM2密文规格。不能为NULL。 |
| [CryptoSm2CiphertextSpec\_item](capi-crypto-asym-cipher-h.md#cryptosm2ciphertextspec_item) item | [in] SM2密文规格项。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储输出数据的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

### OH\_CryptoSm2CiphertextSpec\_SetItem()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_SetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *in)
```

**描述**

设置SM2密文规格的指定项。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) \*spec | [in] SM2密文规格。不能为NULL。 |
| [CryptoSm2CiphertextSpec\_item](capi-crypto-asym-cipher-h.md#cryptosm2ciphertextspec_item) item | [in] SM2密文规格项。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 输入数据。不能为NULL。本接口会对输入数据进行深拷贝，调用者在接口返回后可立即释放in。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec或in为NULL、in->data为NULL或in->len为0。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：深拷贝的内存分配失败。  CRYPTO\_OPERTION\_ERROR：加解密操作失败。 |

**参考：**

[OH\_CryptoSm2CiphertextSpec\_Encode](capi-crypto-asym-cipher-h.md#oh_cryptosm2ciphertextspec_encode) 将SM2密文规格编码为DER格式密文。

### OH\_CryptoSm2CiphertextSpec\_Encode()

```c
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Encode(OH_CryptoSm2CiphertextSpec *spec, Crypto_DataBlob *out)
```

**描述**

将SM2密文规格编码为DER格式密文。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) \*spec | [in] SM2密文规格。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储编码数据的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec或out为NULL，或SM2密文字段（C1X、C1Y、C2、C3）未设置，或C3（hashData）长度不为32字节。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：编码失败。 |

### OH\_CryptoSm2CiphertextSpec\_Destroy()

```c
void OH_CryptoSm2CiphertextSpec_Destroy(OH_CryptoSm2CiphertextSpec *spec)
```

**描述**

销毁SM2密文规格。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSm2CiphertextSpec](capi-cryptoasymcipherapi-oh-cryptosm2ciphertextspec.md) \*spec | [in] SM2密文规格。 |
