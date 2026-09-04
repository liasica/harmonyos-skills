---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h
title: crypto_signature.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_signature.h
category: harmonyos-references
scraped_at: 2026-09-05T06:18:32+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:84d0837d7d46b3cdfe2ee1789e3f169bc785f11f71f58e7f0fb4a0eaf08a2688
---

## 概述

定义签名验签接口。

**引用文件：** <CryptoArchitectureKit/crypto\_signature.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoSignatureApi](capi-cryptosignatureapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) | OH\_CryptoVerify | 验签结构体，表示验签上下文。 |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) | OH\_CryptoSign | 签名结构体，表示签名上下文。 |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) | OH\_CryptoEccSignatureSpec | ECC签名规格结构体，表示ECC签名规格。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) | CryptoSignature\_ParamType | 定义签名参数类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Create(const char \*algoName, OH\_CryptoVerify \*\*verify)](capi-crypto-signature-h.md#oh_cryptoverify_create) | 根据给定的算法名称创建验签上下文。  注意：创建的资源必须通过[OH\_CryptoVerify\_Destroy](capi-crypto-signature-h.md#oh_cryptoverify_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Init(OH\_CryptoVerify \*ctx, OH\_CryptoPubKey \*pubKey)](capi-crypto-signature-h.md#oh_cryptoverify_init) | 使用给定的公钥初始化验签上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Update(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in)](capi-crypto-signature-h.md#oh_cryptoverify_update) | 追加待验签的消息数据。 |
| [bool OH\_CryptoVerify\_Final(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*signData)](capi-crypto-signature-h.md#oh_cryptoverify_final) | 验签消息数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Recover(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*signData, Crypto\_DataBlob \*rawSignData)](capi-crypto-signature-h.md#oh_cryptoverify_recover) | 恢复签名数据，仅支持RSA算法。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放rawSignData内存。 |
| [const char \*OH\_CryptoVerify\_GetAlgoName(OH\_CryptoVerify \*ctx)](capi-crypto-signature-h.md#oh_cryptoverify_getalgoname) | 获取验签上下文的算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_SetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptoverify_setparam) | 设置验签上下文的指定参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_GetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptoverify_getparam) | 获取验签上下文的指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [void OH\_CryptoVerify\_Destroy(OH\_CryptoVerify \*ctx)](capi-crypto-signature-h.md#oh_cryptoverify_destroy) | 销毁验签上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Create(const char \*algoName, OH\_CryptoSign \*\*sign)](capi-crypto-signature-h.md#oh_cryptosign_create) | 根据给定的算法名称创建签名上下文。  注意：创建的资源必须通过[OH\_CryptoSign\_Destroy](capi-crypto-signature-h.md#oh_cryptosign_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Init(OH\_CryptoSign \*ctx, OH\_CryptoPrivKey \*privKey)](capi-crypto-signature-h.md#oh_cryptosign_init) | 初始化签名上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Update(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in)](capi-crypto-signature-h.md#oh_cryptosign_update) | 更新待签名的数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Final(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](capi-crypto-signature-h.md#oh_cryptosign_final) | 结束签名操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [const char \*OH\_CryptoSign\_GetAlgoName(OH\_CryptoSign \*ctx)](capi-crypto-signature-h.md#oh_cryptosign_getalgoname) | 获取签名上下文的算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_SetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, const Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptosign_setparam) | 设置签名上下文的指定参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_GetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptosign_getparam) | 获取签名上下文的指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [void OH\_CryptoSign\_Destroy(OH\_CryptoSign \*ctx)](capi-crypto-signature-h.md#oh_cryptosign_destroy) | 销毁签名上下文。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Create(Crypto\_DataBlob \*eccSignature, OH\_CryptoEccSignatureSpec \*\*spec)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_create) | 创建ECC签名规格，同时支持SM2签名。  注意：创建的资源必须通过[OH\_CryptoEccSignatureSpec\_Destroy](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_GetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_getrands) | 获取ECC签名规格中的r和s值。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放r和s内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_SetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_setrands) | 设置ECC签名规格中的r和s值。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Encode(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*out)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_encode) | 将ECC签名规格编码为DER格式的签名数据。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoEccSignatureSpec\_Destroy(OH\_CryptoEccSignatureSpec \*spec)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy) | 销毁ECC签名规格。 |

## 枚举类型说明

### CryptoSignature\_ParamType

```c
enum CryptoSignature_ParamType
```

**描述**

定义签名参数类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_PSS\_MD\_NAME\_STR = 100 | 表示消息摘要函数的算法名称。 |
| CRYPTO\_PSS\_MGF\_NAME\_STR = 101 | 表示掩码生成函数的算法名称。 |
| CRYPTO\_PSS\_MGF1\_NAME\_STR = 102 | 表示MGF1掩码生成函数的消息摘要参数。 |
| CRYPTO\_PSS\_SALT\_LEN\_INT = 103 | 表示盐值的字节长度。 |
| CRYPTO\_PSS\_TRAILER\_FIELD\_INT = 104 | 表示尾部字段的值。 |
| CRYPTO\_SM2\_USER\_ID\_DATABLOB = 105 | 表示SM2算法的用户ID值。 |

## 函数说明

### OH\_CryptoVerify\_Create()

```c
OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify)
```

**描述**

根据给定的算法名称创建验签上下文。

注意：创建的资源必须通过[OH\_CryptoVerify\_Destroy](capi-crypto-signature-h.md#oh_cryptoverify_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 验签算法名称，不能为NULL。取值如下：  - RSA PKCS1模式：格式为"RSA|PKCS1|摘要"，示例："RSA|PKCS1|SHA256"、"RSA|PKCS1|SHA512"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - RSA PSS模式：格式为"RSA|PSS|摘要|MGF1摘要"，示例："RSA|PSS|SHA256|MGF1\_SHA256"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。MGF1摘要支持"MGF1\_MD5"、"MGF1\_SHA1"、"MGF1\_SHA224"、"MGF1\_SHA256"、"MGF1\_SHA384"、"MGF1\_SHA512"。  - RSA验签恢复：格式为"RSA|PKCS1|摘要|Recover"，示例："RSA|PKCS1|SHA256|Recover"、"RSA|PKCS1|SHA512|Recover"。摘要支持"NoHash"、"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - ECDSA算法：格式为"ECC|摘要"，示例："ECC|SHA256"、"ECC|SHA384"。摘要支持"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - DSA算法：格式为"DSA|摘要"，示例："DSA|SHA256"、"DSA|SHA384"。摘要支持"NoHash"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - SM2算法：取值为"SM2|SM3"。  - Ed25519算法：取值为"Ed25519"。 |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*\*verify | [out] 指向验签上下文指针的指针。verify不能为NULL，\*verify必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：verify为NULL，algoName为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持该算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoVerify\_Init](capi-crypto-signature-h.md#oh_cryptoverify_init) 使用给定的公钥初始化验签上下文。

### OH\_CryptoVerify\_Init()

```c
OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey)
```

**描述**

使用给定的公钥初始化验签上下文。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*pubKey | [in] 公钥。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或pubKey为NULL，或密钥类型与签名算法不匹配。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：验签初始化失败。 |

**参考：**

[OH\_CryptoVerify\_Update](capi-crypto-signature-h.md#oh_cryptoverify_update) 追加待验签的消息数据。

[OH\_CryptoVerify\_Final](capi-crypto-signature-h.md#oh_cryptoverify_final) 验签消息数据。

[OH\_CryptoVerify\_Recover](capi-crypto-signature-h.md#oh_cryptoverify_recover) 恢复签名数据。

### OH\_CryptoVerify\_Update()

```c
OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in)
```

**描述**

追加待验签的消息数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待验签的数据。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或in为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_INVALID\_CALL：无效的函数调用。适用版本：26.0.0+  CRYPTO\_OPERTION\_ERROR：验签更新失败。 |

**参考：**

[OH\_CryptoVerify\_Final](capi-crypto-signature-h.md#oh_cryptoverify_final) 验签消息数据。

### OH\_CryptoVerify\_Final()

```c
bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData)
```

**描述**

验签消息数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待验签的数据。如果数据已通过[OH\_CryptoVerify\_Update](capi-crypto-signature-h.md#oh_cryptoverify_update)接口更新了所有数据，此参数可以为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*signData | [in] 签名数据。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回bool类型的验签结果。返回true表示验签通过，返回false表示验签失败。可能的原因：公钥不正确、签名数据损坏、摘要算法不匹配、填充模式不匹配，或数据与原始签名数据不匹配。 |

### OH\_CryptoVerify\_Recover()

```c
OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData, Crypto_DataBlob *rawSignData)
```

**描述**

恢复签名数据，仅支持RSA算法。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放rawSignData内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*signData | [in] 签名数据。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*rawSignData | [out] 指向用于存储原始签名数据的Crypto\_DataBlob结构体的指针。不能为NULL。 调用前需将rawSignData初始化为{0}，不要预分配rawSignData->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx、signData或rawSignData为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_INVALID\_CALL：无效的函数调用。 适用版本：26.0.0+  CRYPTO\_OPERTION\_ERROR：恢复失败。可能的原因：签名数据长度与RSA密钥模数大小不匹配。 |

### OH\_CryptoVerify\_GetAlgoName()

```c
const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx)
```

**描述**

获取验签上下文的算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回验签算法名称，不需要调用者释放，在上下文销毁后不可使用。 |

### OH\_CryptoVerify\_SetParam()

```c
OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置验签上下文的指定参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | [in] 签名参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [in] 输入数据。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或value为NULL，value->data为NULL，value->len与type期望的大小不匹配，或type不是有效的CryptoSignature\_ParamType。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：设置参数失败。 |

### OH\_CryptoVerify\_GetParam()

```c
OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

获取验签上下文的指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。不能为NULL。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | [in] 签名参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [out] 指向用于存储输出数据的Crypto\_DataBlob结构体的指针。不能为NULL。 调用前需将value初始化为{0}，不要预分配value->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：ctx或value为NULL，或type不是有效的CryptoSignature\_ParamType。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：输出数据的内存分配失败。  CRYPTO\_OPERTION\_ERROR：获取参数失败。 |

### OH\_CryptoVerify\_Destroy()

```c
void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx)
```

**描述**

销毁验签上下文。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | [in] 验签上下文。 |

### OH\_CryptoSign\_Create()

```c
OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign)
```

**描述**

根据给定的算法名称创建签名上下文。

注意：创建的资源必须通过[OH\_CryptoSign\_Destroy](capi-crypto-signature-h.md#oh_cryptosign_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | [in] 签名算法名称，不能为NULL。取值如下：  - RSA PKCS1模式：格式为"RSA|PKCS1|摘要"，示例："RSA|PKCS1|SHA256"、"RSA|PKCS1|SHA512"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - RSA PSS模式：格式为"RSA|PSS|摘要|MGF1摘要"，示例："RSA|PSS|SHA256|MGF1\_SHA256"。摘要支持"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。MGF1摘要支持"MGF1\_MD5"、"MGF1\_SHA1"、"MGF1\_SHA224"、"MGF1\_SHA256"、"MGF1\_SHA384"、"MGF1\_SHA512"。  - RSA仅签名：格式为"RSA|PKCS1|摘要|OnlySign"，示例："RSA|PKCS1|SHA256|OnlySign"、"RSA|PKCS1|SHA512|OnlySign"。摘要支持"NoHash"、"MD5"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - ECDSA算法：格式为"ECC|摘要"，示例："ECC|SHA256"、"ECC|SHA384"。摘要支持"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - DSA算法：格式为"DSA|摘要"，示例："DSA|SHA256"、"DSA|SHA384"。摘要支持"NoHash"、"SHA1"、"SHA224"、"SHA256"、"SHA384"、"SHA512"。  - SM2算法：取值为"SM2|SM3"。  - Ed25519算法：取值为"Ed25519"。 |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*\*sign | [out] 指向签名上下文指针的指针。sign不能为NULL，\*sign必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：sign或algoName为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持该算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoSign\_Init](capi-crypto-signature-h.md#oh_cryptosign_init) 初始化签名上下文。

### OH\_CryptoSign\_Init()

```c
OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey)
```

**描述**

初始化签名上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*privKey | [in] 私钥。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或privKey为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：签名初始化失败。 |

**参考：**

[OH\_CryptoSign\_Update](capi-crypto-signature-h.md#oh_cryptosign_update) 更新待签名的数据。

[OH\_CryptoSign\_Final](capi-crypto-signature-h.md#oh_cryptosign_final) 结束签名操作。

### OH\_CryptoSign\_Update()

```c
OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in)
```

**描述**

更新待签名的数据。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待签名的数据。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或in为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_INVALID\_CALL：无效的函数调用。适用版本：26.0.0+  CRYPTO\_OPERTION\_ERROR：签名更新失败。 |

**参考：**

[OH\_CryptoSign\_Final](capi-crypto-signature-h.md#oh_cryptosign_final) 结束签名操作。

### OH\_CryptoSign\_Final()

```c
OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

结束签名操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | [in] 待签名的数据。如果数据已通过[OH\_CryptoSign\_Update](capi-crypto-signature-h.md#oh_cryptosign_update)接口更新了所有数据，此参数可以为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储签名结果的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或out为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：签名失败。 |

### OH\_CryptoSign\_GetAlgoName()

```c
const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx)
```

**描述**

获取签名上下文的算法名称。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回签名算法名称，不需要调用者释放，在上下文销毁后不可使用。 |

### OH\_CryptoSign\_SetParam()

```c
OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, const Crypto_DataBlob *value)
```

**描述**

设置签名上下文的指定参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | [in] 签名参数类型。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [in] 输入数据。本接口会对value中的数据进行深拷贝，调用者在接口返回后可立即释放value。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或value为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoSign\_GetParam()

```c
OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

获取签名上下文的指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。不能为NULL。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | [in] 签名参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | [out] 指向用于存储输出数据的Crypto\_DataBlob结构体的指针。不能为NULL。 调用前需将value初始化为{0}，不要预分配value->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：ctx或value为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  #CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoSign\_Destroy()

```c
void OH_CryptoSign_Destroy(OH_CryptoSign *ctx)
```

**描述**

销毁签名上下文。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | [in] 签名上下文。 |

### OH\_CryptoEccSignatureSpec\_Create()

```c
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature, OH_CryptoEccSignatureSpec **spec)
```

**描述**

创建ECC签名规格，同时支持SM2签名。

注意：创建的资源必须通过[OH\_CryptoEccSignatureSpec\_Destroy](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*eccSignature | [in] DER格式的ECC签名数据，如果为NULL则创建空的签名规格。 |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*\*spec | [out] 指向ECC签名规格指针的指针。spec不能为NULL，\*spec必须为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec为NULL或spec不为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：解析eccSignature失败，或eccSignature包含无效的DER编码ECDSA-Sig-Value。 |

**参考：**

[OH\_CryptoEccSignatureSpec\_GetRAndS](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_getrands) 获取ECC签名规格中的r和s值。

[OH\_CryptoEccSignatureSpec\_SetRAndS](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_setrands) 设置ECC签名规格中的r和s值。

### OH\_CryptoEccSignatureSpec\_GetRAndS()

```c
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```

**描述**

获取ECC签名规格中的r和s值。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放r和s内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | [in] ECC签名规格。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*r | [out] 指向用于存储r值的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将r初始化为{0}，不要预分配r->data内存。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*s | [out] 指向用于存储s值的Crypto\_DataBlob结构体的指针。不能为NULL。调用前需将s初始化为{0}，不要预分配s->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec、r或s为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

### OH\_CryptoEccSignatureSpec\_SetRAndS()

```c
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```

**描述**

设置ECC签名规格中的r和s值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | [in] ECC签名规格。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*r | [in] r值。本接口会对r和s中的数据进行深拷贝，调用者在接口返回后可立即释放r和s。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*s | [in] s值。不能为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec、r或s为NULL。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存操作失败。  CRYPTO\_OPERTION\_ERROR：密码操作失败。 |

**参考：**

[OH\_CryptoEccSignatureSpec\_Encode](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_encode) 将ECC签名规格编码为DER格式的签名数据。

### OH\_CryptoEccSignatureSpec\_Encode()

```c
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out)
```

**描述**

将ECC签名规格编码为DER格式的签名数据。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | [in] ECC签名规格。不能为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | [out] 指向用于存储编码签名数据的Crypto\_DataBlob结构体的指针。不能为NULL。 调用前需将out初始化为{0}，不要预分配out->data内存。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_PARAMETER\_CHECK\_FAILED：spec或out为NULL，或尚未通过[OH\_CryptoEccSignatureSpec\_SetRAndS](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_setrands)设置r和s值。  CRYPTO\_NOT\_SUPPORTED：不支持的操作或算法。  CRYPTO\_MEMORY\_ERROR：内存分配失败。  CRYPTO\_OPERTION\_ERROR：编码失败。 |

### OH\_CryptoEccSignatureSpec\_Destroy()

```c
void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec)
```

**描述**

销毁ECC签名规格。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | [in] ECC签名规格。 |
