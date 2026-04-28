---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-signature-h
title: crypto_signature.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_signature.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:59+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3ef81060af1b7c7c3ae53f782efcd5cb1363cdbfa7b82598fbb3e06e64cd180c
---

## 概述

PhonePC/2in1TabletTVWearable

定义验签接口。

**引用文件：** <CryptoArchitectureKit/crypto\_signature.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoSignatureApi](capi-cryptosignatureapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) | OH\_CryptoVerify | 定义验签结构体。 |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) | OH\_CryptoSign | 定义签名结构体。 |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) | OH\_CryptoEccSignatureSpec | 定义ECC签名规范结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) | CryptoSignature\_ParamType | 定义签名验签参数类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Create(const char \*algoName, OH\_CryptoVerify \*\*verify)](capi-crypto-signature-h.md#oh_cryptoverify_create) | 创建验签实例。  注意：创建的资源必须通过[OH\_CryptoVerify\_Destroy](capi-crypto-signature-h.md#oh_cryptoverify_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Init(OH\_CryptoVerify \*ctx, OH\_CryptoPubKey \*pubKey)](capi-crypto-signature-h.md#oh_cryptoverify_init) | 传入公钥初始化验签实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Update(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in)](capi-crypto-signature-h.md#oh_cryptoverify_update) | 追加待验签数据。 |
| [bool OH\_CryptoVerify\_Final(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*in, Crypto\_DataBlob \*signData)](capi-crypto-signature-h.md#oh_cryptoverify_final) | 对数据进行验签。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_Recover(OH\_CryptoVerify \*ctx, Crypto\_DataBlob \*signData, Crypto\_DataBlob \*rawSignData)](capi-crypto-signature-h.md#oh_cryptoverify_recover) | 对签名数据进行恢复操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放rawSignData内存。 |
| [const char \*OH\_CryptoVerify\_GetAlgoName(OH\_CryptoVerify \*ctx)](capi-crypto-signature-h.md#oh_cryptoverify_getalgoname) | 获取验签算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_SetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptoverify_setparam) | 设置验签参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoVerify\_GetParam(OH\_CryptoVerify \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptoverify_getparam) | 获取验签参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [void OH\_CryptoVerify\_Destroy(OH\_CryptoVerify \*ctx)](capi-crypto-signature-h.md#oh_cryptoverify_destroy) | 销毁验签实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Create(const char \*algoName, OH\_CryptoSign \*\*sign)](capi-crypto-signature-h.md#oh_cryptosign_create) | 根据给定的算法名称创建签名实例。  注意：创建的资源必须通过[OH\_CryptoSign\_Destroy](capi-crypto-signature-h.md#oh_cryptosign_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Init(OH\_CryptoSign \*ctx, OH\_CryptoPrivKey \*privKey)](capi-crypto-signature-h.md#oh_cryptosign_init) | 初始化签名实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Update(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in)](capi-crypto-signature-h.md#oh_cryptosign_update) | 更新需要签名的数据。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_Final(OH\_CryptoSign \*ctx, const Crypto\_DataBlob \*in, Crypto\_DataBlob \*out)](capi-crypto-signature-h.md#oh_cryptosign_final) | 完成签名操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [const char \*OH\_CryptoSign\_GetAlgoName(OH\_CryptoSign \*ctx)](capi-crypto-signature-h.md#oh_cryptosign_getalgoname) | 获取签名实例的算法名称。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_SetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, const Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptosign_setparam) | 设置签名实例的指定参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoSign\_GetParam(OH\_CryptoSign \*ctx, CryptoSignature\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-signature-h.md#oh_cryptosign_getparam) | 从签名实例获取指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [void OH\_CryptoSign\_Destroy(OH\_CryptoSign \*ctx)](capi-crypto-signature-h.md#oh_cryptosign_destroy) | 销毁签名实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Create(Crypto\_DataBlob \*eccSignature, OH\_CryptoEccSignatureSpec \*\*spec)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_create) | 创建ECC签名规范。  注意：创建的资源必须通过[OH\_CryptoEccSignatureSpec\_Destroy](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_GetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_getrands) | 获取ECC签名的r和s值。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放r和s内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_SetRAndS(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*r, Crypto\_DataBlob \*s)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_setrands) | 设置ECC签名的r和s值。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEccSignatureSpec\_Encode(OH\_CryptoEccSignatureSpec \*spec, Crypto\_DataBlob \*out)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_encode) | 将ECC签名规范编码为DER格式的签名。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoEccSignatureSpec\_Destroy(OH\_CryptoEccSignatureSpec \*spec)](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy) | 销毁ECC签名规范。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### CryptoSignature\_ParamType

PhonePC/2in1TabletTVWearable

```
1. enum CryptoSignature_ParamType
```

**描述**

定义签名验签参数类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_PSS\_MD\_NAME\_STR = 100 | 表示RSA算法中，使用PSS模式时，消息摘要功能的算法名。 |
| CRYPTO\_PSS\_MGF\_NAME\_STR = 101 | 表示RSA算法中，使用PSS模式时，掩码生成算法（目前仅支持MGF1）。 |
| CRYPTO\_PSS\_MGF1\_NAME\_STR = 102 | 表示RSA算法中，使用PSS模式时，MGF1掩码生成功能的消息摘要参数。 |
| CRYPTO\_PSS\_SALT\_LEN\_INT = 103 | 表示RSA算法中，使用PSS模式时，盐值的长度，长度以字节为单位。 |
| CRYPTO\_PSS\_TRAILER\_FIELD\_INT = 104 | 表示RSA算法中，使用PSS模式时，用于编码操作的整数，值为1。 |
| CRYPTO\_SM2\_USER\_ID\_DATABLOB = 105 | 表示SM2算法中，用户身份标识字段。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoVerify\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify)
```

**描述**

创建验签实例。

注意：创建的资源必须通过[OH\_CryptoVerify\_Destroy](capi-crypto-signature-h.md#oh_cryptoverify_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成验签实例的算法名称。  例如"RSA1024|PKCS1|SHA256" |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*\*verify | 指向验签实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoVerify\_Init()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey)
```

**描述**

传入公钥初始化验签实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*pubKey | 公钥对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoVerify\_Update](capi-crypto-signature-h.md#oh_cryptoverify_update)

[OH\_CryptoVerify\_Final](capi-crypto-signature-h.md#oh_cryptoverify_final)

### OH\_CryptoVerify\_Update()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in)
```

**描述**

追加待验签数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 传入的消息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoVerify\_Init](capi-crypto-signature-h.md#oh_cryptoverify_init)

[OH\_CryptoVerify\_Final](capi-crypto-signature-h.md#oh_cryptoverify_final)

### OH\_CryptoVerify\_Final()

PhonePC/2in1TabletTVWearable

```
1. bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData)
```

**描述**

对数据进行验签。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 传入的数据。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*signData | 签名数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 表示验签是否通过，true表示验签通过，false表示验签失败。 |

**参考：**

[OH\_CryptoVerify\_Init](capi-crypto-signature-h.md#oh_cryptoverify_init)

[OH\_CryptoVerify\_Update](capi-crypto-signature-h.md#oh_cryptoverify_update)

### OH\_CryptoVerify\_Recover()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData, Crypto_DataBlob *rawSignData)
```

**描述**

对签名数据进行恢复操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放rawSignData内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*signData | 签名数据。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*rawSignData | 验签恢复的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoVerify\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx)
```

**描述**

获取验签算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回验签算法名称。 |

### OH\_CryptoVerify\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置验签参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | 用于指定需要设置的验签参数。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 用于指定验签参数的具体值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoVerify\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

获取验签参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | 用于指定需要获取的验签参数。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 获取的验签参数的具体值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoVerify\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx)
```

**描述**

销毁验签实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoVerify](capi-cryptosignatureapi-oh-cryptoverify.md) \*ctx | 指向验签实例。 |

### OH\_CryptoSign\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign)
```

**描述**

根据给定的算法名称创建签名实例。

注意：创建的资源必须通过[OH\_CryptoSign\_Destroy](capi-crypto-signature-h.md#oh_cryptosign_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成签名实例的算法名称。  例如"RSA|PKCS1|SHA384"、"ECC|SHA384"。 |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*\*sign | 签名实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSign\_Init()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey)
```

**描述**

初始化签名实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*privKey | 私钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoSign\_Update](capi-crypto-signature-h.md#oh_cryptosign_update)

[OH\_CryptoSign\_Final](capi-crypto-signature-h.md#oh_cryptosign_final)

### OH\_CryptoSign\_Update()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in)
```

**描述**

更新需要签名的数据。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 需要签名的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoSign\_Init](capi-crypto-signature-h.md#oh_cryptosign_init)

[OH\_CryptoSign\_Final](capi-crypto-signature-h.md#oh_cryptosign_final)

### OH\_CryptoSign\_Final()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

完成签名操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 需要签名的数据。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 签名结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoSign\_Init](capi-crypto-signature-h.md#oh_cryptosign_init)

[OH\_CryptoSign\_Update](capi-crypto-signature-h.md#oh_cryptosign_update)

### OH\_CryptoSign\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx)
```

**描述**

获取签名实例的算法名称。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回签名算法名称。 |

### OH\_CryptoSign\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, const Crypto_DataBlob *value)
```

**描述**

设置签名实例的指定参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | 签名参数类型。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 输入数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSign\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

从签名实例获取指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |
| [CryptoSignature\_ParamType](capi-crypto-signature-h.md#cryptosignature_paramtype) type | 签名参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 输出数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoSign\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoSign_Destroy(OH_CryptoSign *ctx)
```

**描述**

销毁签名实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoSign](capi-cryptosignatureapi-oh-cryptosign.md) \*ctx | 指向签名实例。 |

### OH\_CryptoEccSignatureSpec\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature, OH_CryptoEccSignatureSpec **spec)
```

**描述**

创建ECC签名规范。

注意：创建的资源必须通过[OH\_CryptoEccSignatureSpec\_Destroy](capi-crypto-signature-h.md#oh_cryptoeccsignaturespec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*eccSignature | ECC签名（DER格式），如果EccSignature参数为NULL，将创建一个空的ECC签名规范。 |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*\*spec | 输出的ECC签名规范。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEccSignatureSpec\_GetRAndS()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```

**描述**

获取ECC签名的r和s值。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放r和s内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | 指向ECC签名规范。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*r | r值。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*s | s值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEccSignatureSpec\_SetRAndS()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)
```

**描述**

设置ECC签名的r和s值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | 指向ECC签名规范。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*r | r值。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*s | s值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEccSignatureSpec\_Encode()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out)
```

**描述**

将ECC签名规范编码为DER格式的签名。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | 指向ECC签名规范。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 输出数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEccSignatureSpec\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec)
```

**描述**

销毁ECC签名规范。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEccSignatureSpec](capi-cryptosignatureapi-oh-cryptoeccsignaturespec.md) \*spec | 指向ECC签名规范。 |
