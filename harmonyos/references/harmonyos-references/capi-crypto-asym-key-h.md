---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-asym-key-h
title: crypto_asym_key.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_asym_key.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fc6072c03816b5931aefceebe8565e1f85a4c8eada139c1e77a668bdb0f932be
---

## 概述

PhonePC/2in1TabletTVWearable

声明非对称密钥接口。

**引用文件：** <CryptoArchitectureKit/crypto\_asym\_key.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoAsymKeyApi](capi-cryptoasymkeyapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) | OH\_CryptoKeyPair | 定义密钥对结构体。 |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) | OH\_CryptoPubKey | 定义公钥结构体。 |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) | OH\_CryptoPrivKey | 定义私钥结构体。 |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) | OH\_CryptoAsymKeyGenerator | 定义非对称密钥生成器结构体。 |
| [OH\_CryptoPrivKeyEncodingParams](pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams.md) | OH\_CryptoPrivKeyEncodingParams | 定义私钥编码参数结构体。 |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) | OH\_CryptoAsymKeySpec | 定义非对称密钥规格结构体。 |
| [OH\_CryptoAsymKeyGeneratorWithSpec](cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec.md) | OH\_CryptoAsymKeyGeneratorWithSpec | 定义带规格的非对称密钥生成器。 |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) | OH\_CryptoEcPoint | 定义EC点结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoAsymKey\_ParamType](capi-crypto-asym-key-h.md#cryptoasymkey_paramtype) | CryptoAsymKey\_ParamType | 定义非对称密钥参数类型。 |
| [Crypto\_EncodingType](capi-crypto-asym-key-h.md#crypto_encodingtype) | Crypto\_EncodingType | 定义编码格式。 |
| [CryptoPrivKeyEncoding\_ParamType](capi-crypto-asym-key-h.md#cryptoprivkeyencoding_paramtype) | CryptoPrivKeyEncoding\_ParamType | 定义私钥编码参数类型。 |
| [CryptoAsymKeySpec\_Type](capi-crypto-asym-key-h.md#cryptoasymkeyspec_type) | CryptoAsymKeySpec\_Type | 定义非对称密钥规格类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Create(const char \*algoName, OH\_CryptoAsymKeyGenerator \*\*ctx)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create) | 通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。  注意：创建的资源必须通过[OH\_CryptoAsymKeyGenerator\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Generate(OH\_CryptoAsymKeyGenerator \*ctx, OH\_CryptoKeyPair \*\*keyCtx)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate) | 随机生成非对称密钥（密钥对）。  注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)销毁keyCtx内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_Convert(OH\_CryptoAsymKeyGenerator \*ctx, Crypto\_EncodingType type, Crypto\_DataBlob \*pubKeyData, Crypto\_DataBlob \*priKeyData, OH\_CryptoKeyPair \*\*keyCtx)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert) | 将非对称密钥数据转换为密钥对。  注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)销毁keyCtx内存。 |
| [const char \*OH\_CryptoAsymKeyGenerator\_GetAlgoName(OH\_CryptoAsymKeyGenerator \*ctx)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_getalgoname) | 获取非对称密钥算法名称。 |
| [void OH\_CryptoAsymKeyGenerator\_Destroy(OH\_CryptoAsymKeyGenerator \*ctx)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_destroy) | 销毁非对称密钥生成器实例。 |
| [void OH\_CryptoKeyPair\_Destroy(OH\_CryptoKeyPair \*keyCtx)](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy) | 销毁非对称密钥对实例。 |
| [OH\_CryptoPubKey \*OH\_CryptoKeyPair\_GetPubKey(OH\_CryptoKeyPair \*keyCtx)](capi-crypto-asym-key-h.md#oh_cryptokeypair_getpubkey) | 从密钥对中获取公钥实例。 |
| [OH\_CryptoPrivKey \*OH\_CryptoKeyPair\_GetPrivKey(OH\_CryptoKeyPair \*keyCtx)](capi-crypto-asym-key-h.md#oh_cryptokeypair_getprivkey) | 获取密钥对的私钥。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPubKey\_Encode(OH\_CryptoPubKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, Crypto\_DataBlob \*out)](capi-crypto-asym-key-h.md#oh_cryptopubkey_encode) | 根据指定的编码格式输出公钥数据。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPubKey\_GetParam(OH\_CryptoPubKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)](capi-crypto-asym-key-h.md#oh_cryptopubkey_getparam) | 从公钥实例获取指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGenerator\_SetPassword(OH\_CryptoAsymKeyGenerator \*ctx, const unsigned char \*password, uint32\_t passwordLen)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_setpassword) | 设置非对称密钥生成器上下文的密码。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_Create(OH\_CryptoPrivKeyEncodingParams \*\*ctx)](capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_create) | 创建私钥编码参数。  注意：创建的资源必须通过[OH\_CryptoPrivKeyEncodingParams\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKeyEncodingParams\_SetParam(OH\_CryptoPrivKeyEncodingParams \*ctx, CryptoPrivKeyEncoding\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_setparam) | 设置私钥编码参数。 |
| [void OH\_CryptoPrivKeyEncodingParams\_Destroy(OH\_CryptoPrivKeyEncodingParams \*ctx)](capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_destroy) | 销毁私钥编码参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_Encode(OH\_CryptoPrivKey \*key, Crypto\_EncodingType type, const char \*encodingStandard, OH\_CryptoPrivKeyEncodingParams \*params, Crypto\_DataBlob \*out)](capi-crypto-asym-key-h.md#oh_cryptoprivkey_encode) | 从私钥实例获取指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoPrivKey\_GetParam(OH\_CryptoPrivKey \*key, CryptoAsymKey\_ParamType item, Crypto\_DataBlob \*value)](capi-crypto-asym-key-h.md#oh_cryptoprivkey_getparam) | 获取私钥的指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec(const char \*curveName, OH\_CryptoAsymKeySpec \*\*spec)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_geneccommonparamsspec) | 生成EC通用参数规格。  注意：使用完成后必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁spec内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GenDhCommonParamsSpec(int pLen, int skLen, OH\_CryptoAsymKeySpec \*\*spec)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_gendhcommonparamsspec) | 生成DH通用参数规格。  注意：使用完成后必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁spec内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_Create(const char \*algoName, CryptoAsymKeySpec\_Type type, OH\_CryptoAsymKeySpec \*\*spec)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_create) | 根据给定的算法名称和规格类型创建非对称密钥规格。  注意：创建的资源必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setparam) | 设置非对称密钥规格的指定参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_SetCommonParamsSpec(OH\_CryptoAsymKeySpec \*spec, OH\_CryptoAsymKeySpec \*commonParamsSpec)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setcommonparamsspec) | 设置非对称密钥规格的通用参数规格。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeySpec\_GetParam(OH\_CryptoAsymKeySpec \*spec, CryptoAsymKey\_ParamType type, Crypto\_DataBlob \*value)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_getparam) | 获取非对称密钥规格的指定参数。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。 |
| [void OH\_CryptoAsymKeySpec\_Destroy(OH\_CryptoAsymKeySpec \*spec)](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy) | 销毁非对称密钥规格。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_Create(OH\_CryptoAsymKeySpec \*keySpec, OH\_CryptoAsymKeyGeneratorWithSpec \*\*generator)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_create) | 创建带规格的非对称密钥生成器。  注意：创建的资源必须通过[OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair(OH\_CryptoAsymKeyGeneratorWithSpec \*generator, OH\_CryptoKeyPair \*\*keyPair)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_genkeypair) | 根据非对称密钥规格生成密钥对。  注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)释放keyPair内存。 |
| [void OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy(OH\_CryptoAsymKeyGeneratorWithSpec \*generator)](capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_destroy) | 销毁带规格的非对称密钥生成器。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Create(const char \*curveName, Crypto\_DataBlob \*ecKeyData, OH\_CryptoEcPoint \*\*point)](capi-crypto-asym-key-h.md#oh_cryptoecpoint_create) | 创建EC点。  注意：创建的资源必须通过[OH\_CryptoEcPoint\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoecpoint_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_GetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)](capi-crypto-asym-key-h.md#oh_cryptoecpoint_getcoordinate) | 获取EC点的x和y坐标。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放x和y内存 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_SetCoordinate(OH\_CryptoEcPoint \*point, Crypto\_DataBlob \*x, Crypto\_DataBlob \*y)](capi-crypto-asym-key-h.md#oh_cryptoecpoint_setcoordinate) | 设置EC点的x和y坐标。 |
| [OH\_Crypto\_ErrCode OH\_CryptoEcPoint\_Encode(OH\_CryptoEcPoint \*point, const char \*format, Crypto\_DataBlob \*out)](capi-crypto-asym-key-h.md#oh_cryptoecpoint_encode) | 将EC点编码为指定格式。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [void OH\_CryptoEcPoint\_Destroy(OH\_CryptoEcPoint \*point)](capi-crypto-asym-key-h.md#oh_cryptoecpoint_destroy) | 销毁EC点。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### CryptoAsymKey\_ParamType

PhonePC/2in1TabletTVWearable

```
1. enum CryptoAsymKey_ParamType
```

**描述**

定义非对称密钥参数类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_DSA\_P\_DATABLOB = 101 | DSA算法的素模数p。 |
| CRYPTO\_DSA\_Q\_DATABLOB = 102 | DSA算法中密钥参数q（p-1的素因子）。 |
| CRYPTO\_DSA\_G\_DATABLOB = 103 | DSA算法的参数g。 |
| CRYPTO\_DSA\_SK\_DATABLOB = 104 | DSA算法的私钥sk。 |
| CRYPTO\_DSA\_PK\_DATABLOB = 105 | DSA算法的公钥pk。 |
| CRYPTO\_ECC\_FP\_P\_DATABLOB = 201 | ECC算法中表示椭圆曲线Fp域的素数p。 |
| CRYPTO\_ECC\_A\_DATABLOB = 202 | ECC算法中椭圆曲线的第一个系数a。 |
| CRYPTO\_ECC\_B\_DATABLOB = 203 | ECC算法中椭圆曲线的第二个系数b。 |
| CRYPTO\_ECC\_G\_X\_DATABLOB = 204 | ECC算法中基点g的x坐标。 |
| CRYPTO\_ECC\_G\_Y\_DATABLOB = 205 | ECC算法中基点g的y坐标。 |
| CRYPTO\_ECC\_N\_DATABLOB = 206 | ECC算法中基点g的阶n。 |
| CRYPTO\_ECC\_H\_INT = 207 | ECC算法中的余因子h。 |
| CRYPTO\_ECC\_SK\_DATABLOB = 208 | ECC算法中的私钥sk。 |
| CRYPTO\_ECC\_PK\_X\_DATABLOB = 209 | ECC算法中，公钥pk（椭圆曲线上的一个点）的x坐标。 |
| CRYPTO\_ECC\_PK\_Y\_DATABLOB = 210 | ECC算法中，公钥pk（椭圆曲线上的一个点）的y坐标。 |
| CRYPTO\_ECC\_FIELD\_TYPE\_STR = 211 | ECC算法中，椭圆曲线的域类型（当前只支持Fp域）。 |
| CRYPTO\_ECC\_FIELD\_SIZE\_INT = 212 | ECC算法中域的大小，单位为bits（注：对于Fp域，域的大小为素数p的bits长度）。 |
| CRYPTO\_ECC\_CURVE\_NAME\_STR = 213 | ECC算法中的SECG（Standards for Efficient Cryptography Group）曲线名称。 |
| CRYPTO\_RSA\_N\_DATABLOB = 301 | RSA算法中的模数n。 |
| CRYPTO\_RSA\_D\_DATABLOB = 302 | RSA算法中的私钥sk（即私钥指数d）。 |
| CRYPTO\_RSA\_E\_DATABLOB = 303 | RSA算法中的公钥pk（即公钥指数e）。 |
| CRYPTO\_DH\_P\_DATABLOB = 401 | DH算法中的素数p。 |
| CRYPTO\_DH\_G\_DATABLOB = 402 | DH算法中的参数g。 |
| CRYPTO\_DH\_L\_INT = 403 | DH算法中私钥长度，单位为bit。 |
| CRYPTO\_DH\_SK\_DATABLOB = 404 | DH算法中的私钥sk。 |
| CRYPTO\_DH\_PK\_DATABLOB = 405 | DH算法中的公钥pk。 |
| CRYPTO\_ED25519\_SK\_DATABLOB = 501 | Ed25519算法中的私钥sk。 |
| CRYPTO\_ED25519\_PK\_DATABLOB = 502 | Ed25519算法中的公钥pk。 |
| CRYPTO\_X25519\_SK\_DATABLOB = 601 | X25519算法中的私钥sk。 |
| CRYPTO\_X25519\_PK\_DATABLOB = 602 | X25519算法中的公钥pk。 |

### Crypto\_EncodingType

PhonePC/2in1TabletTVWearable

```
1. enum Crypto_EncodingType
```

**描述**

定义编码格式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_PEM = 0 | PEM格式密钥类型。 |
| CRYPTO\_DER = 1 | DER格式密钥类型。 |

### CryptoPrivKeyEncoding\_ParamType

PhonePC/2in1TabletTVWearable

```
1. enum CryptoPrivKeyEncoding_ParamType
```

**描述**

定义私钥编码参数类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_PRIVATE\_KEY\_ENCODING\_PASSWORD\_STR = 0 | 表示密码字符串。 |
| CRYPTO\_PRIVATE\_KEY\_ENCODING\_SYMMETRIC\_CIPHER\_STR = 1 | 表示对称加密字符串。 |

### CryptoAsymKeySpec\_Type

PhonePC/2in1TabletTVWearable

```
1. enum CryptoAsymKeySpec_Type
```

**描述**

定义非对称密钥规格类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_ASYM\_KEY\_COMMON\_PARAMS\_SPEC = 0 | 通用参数规格。 |
| CRYPTO\_ASYM\_KEY\_PRIVATE\_KEY\_SPEC = 1 | 私钥规格。 |
| CRYPTO\_ASYM\_KEY\_PUBLIC\_KEY\_SPEC = 2 | 公钥规格。 |
| CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC = 3 | 密钥对规格。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoAsymKeyGenerator\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Create(const char *algoName, OH_CryptoAsymKeyGenerator **ctx)
```

**描述**

通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。

注意：创建的资源必须通过[OH\_CryptoAsymKeyGenerator\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_destroy)销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成生成器的算法名称。  例如"RSA1024|PRIMES\_2"。 |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*\*ctx | 指向非对称密钥生成器上下文的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGenerator\_Generate()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Generate(OH_CryptoAsymKeyGenerator *ctx, OH_CryptoKeyPair **keyCtx)
```

**描述**

随机生成非对称密钥（密钥对）。

注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*ctx | 非对称密钥生成器实例。 |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*\*keyCtx | 指向非对称密钥对实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGenerator\_Convert()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Convert(OH_CryptoAsymKeyGenerator *ctx, Crypto_EncodingType type, Crypto_DataBlob *pubKeyData, Crypto_DataBlob *priKeyData, OH_CryptoKeyPair **keyCtx)
```

**描述**

将非对称密钥数据转换为密钥对。

注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)销毁keyCtx内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*ctx | 非对称密钥生成器实例。 |
| [Crypto\_EncodingType](capi-crypto-asym-key-h.md#crypto_encodingtype) type | 编码格式。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*pubKeyData | 公钥数据。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*priKeyData | 私钥数据。 |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*\*keyCtx | 指向非对称密钥对实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGenerator\_GetAlgoName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_CryptoAsymKeyGenerator_GetAlgoName(OH_CryptoAsymKeyGenerator *ctx)
```

**描述**

获取非对称密钥算法名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*ctx | 非对称密钥生成器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回非对称密钥算法名称。 |

### OH\_CryptoAsymKeyGenerator\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoAsymKeyGenerator_Destroy(OH_CryptoAsymKeyGenerator *ctx)
```

**描述**

销毁非对称密钥生成器实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*ctx | 非对称密钥生成器实例。 |

### OH\_CryptoKeyPair\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoKeyPair_Destroy(OH_CryptoKeyPair *keyCtx)
```

**描述**

销毁非对称密钥对实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*keyCtx | 密钥对实例。 |

### OH\_CryptoKeyPair\_GetPubKey()

PhonePC/2in1TabletTVWearable

```
1. OH_CryptoPubKey *OH_CryptoKeyPair_GetPubKey(OH_CryptoKeyPair *keyCtx)
```

**描述**

从密钥对中获取公钥实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*keyCtx | 密钥对实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \* | 返回从密钥对中得到的公钥实例。 |

### OH\_CryptoKeyPair\_GetPrivKey()

PhonePC/2in1TabletTVWearable

```
1. OH_CryptoPrivKey *OH_CryptoKeyPair_GetPrivKey(OH_CryptoKeyPair *keyCtx)
```

**描述**

获取密钥对的私钥。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*keyCtx | 密钥对实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \* | 返回从密钥对中得到的私钥实例。 |

### OH\_CryptoPubKey\_Encode()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPubKey_Encode(OH_CryptoPubKey *key, Crypto_EncodingType type, const char *encodingStandard, Crypto_DataBlob *out)
```

**描述**

根据指定的编码格式输出公钥数据。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*key | 公钥实例。 |
| [Crypto\_EncodingType](capi-crypto-asym-key-h.md#crypto_encodingtype) type | 编码类型。 |
| const char \*encodingStandard | 编码格式。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 输出的公钥结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoPubKey\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPubKey_GetParam(OH_CryptoPubKey *key, CryptoAsymKey_ParamType item, Crypto_DataBlob *value)
```

**描述**

从公钥实例获取指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPubKey](capi-cryptoasymkeyapi-oh-cryptopubkey.md) \*key | 公钥实例。 |
| [CryptoAsymKey\_ParamType](capi-crypto-asym-key-h.md#cryptoasymkey_paramtype) item | 非对称密钥参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 参数输出值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_INVALID\_PARAMS：参数无效。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGenerator\_SetPassword()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_SetPassword(OH_CryptoAsymKeyGenerator *ctx, const unsigned char *password, uint32_t passwordLen)
```

**描述**

设置非对称密钥生成器上下文的密码。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGenerator](capi-cryptoasymkeyapi-oh-cryptoasymkeygenerator.md) \*ctx | 指向非对称加密上下文的指针。 |
| const unsigned char \*password | 表示密码。 |
| uint32\_t passwordLen | 表示密码长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoPrivKeyEncodingParams\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_Create(OH_CryptoPrivKeyEncodingParams **ctx)
```

**描述**

创建私钥编码参数。

注意：创建的资源必须通过[OH\_CryptoPrivKeyEncodingParams\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPrivKeyEncodingParams](pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams.md) \*\*ctx | 私钥编码参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoPrivKeyEncodingParams\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_SetParam(OH_CryptoPrivKeyEncodingParams *ctx, CryptoPrivKeyEncoding_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置私钥编码参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPrivKeyEncodingParams](pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams.md) \*ctx | 私钥编码参数。 |
| [CryptoPrivKeyEncoding\_ParamType](capi-crypto-asym-key-h.md#cryptoprivkeyencoding_paramtype) type | 私钥编码参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 私钥编码参数值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoPrivKeyEncodingParams\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoPrivKeyEncodingParams_Destroy(OH_CryptoPrivKeyEncodingParams *ctx)
```

**描述**

销毁私钥编码参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPrivKeyEncodingParams](pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams.md) \*ctx | 私钥编码参数。 |

### OH\_CryptoPrivKey\_Encode()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPrivKey_Encode(OH_CryptoPrivKey *key, Crypto_EncodingType type, const char *encodingStandard, OH_CryptoPrivKeyEncodingParams *params, Crypto_DataBlob *out)
```

**描述**

从私钥实例获取指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*key | 私钥。 |
| [Crypto\_EncodingType](capi-crypto-asym-key-h.md#crypto_encodingtype) type | 私钥编码类型。 |
| const char \*encodingStandard | 编码标准。  例如"PKCS8"。 |
| [OH\_CryptoPrivKeyEncodingParams](pi-cryptoasymkeyapi-oh-cryptoprivkeyencodingparams.md) \*params | 私钥编码参数，可以为NULL，如果要加密私钥，则应设置此参数。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 编码结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoPrivKey\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoPrivKey_GetParam(OH_CryptoPrivKey *key, CryptoAsymKey_ParamType item, Crypto_DataBlob *value)
```

**描述**

获取私钥的指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoPrivKey](capi-cryptoasymkeyapi-oh-cryptoprivkey.md) \*key | 私钥。 |
| [CryptoAsymKey\_ParamType](capi-crypto-asym-key-h.md#cryptoasymkey_paramtype) item | 非对称密钥参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 输出数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenEcCommonParamsSpec(const char *curveName, OH_CryptoAsymKeySpec **spec)
```

**描述**

生成EC通用参数规格。

注意：使用完成后必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁spec内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*curveName | ECC曲线名称。 |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*\*spec | 指向EC通用参数规格的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_GenDhCommonParamsSpec()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenDhCommonParamsSpec(int pLen, int skLen, OH_CryptoAsymKeySpec **spec)
```

**描述**

生成DH通用参数规格。

注意：使用完成后必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁spec内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int pLen | 素数p的字节长度。 |
| int skLen | 私钥的字节长度。 |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*\*spec | 指向DH通用参数规格的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_Create(const char *algoName, CryptoAsymKeySpec_Type type, OH_CryptoAsymKeySpec **spec)
```

**描述**

根据给定的算法名称和规格类型创建非对称密钥规格。

注意：创建的资源必须通过[OH\_CryptoAsymKeySpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成规格的算法名称。  例如"RSA"。 |
| [CryptoAsymKeySpec\_Type](capi-crypto-asym-key-h.md#cryptoasymkeyspec_type) type | 非对称密钥规格类型。 |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*\*spec | 指向非对称密钥规格的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置非对称密钥规格的指定参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*spec | 非对称密钥规格。 |
| [CryptoAsymKey\_ParamType](capi-crypto-asym-key-h.md#cryptoasymkey_paramtype) type | 非对称密钥参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 输入数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_SetCommonParamsSpec()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetCommonParamsSpec(OH_CryptoAsymKeySpec *spec, OH_CryptoAsymKeySpec *commonParamsSpec)
```

**描述**

设置非对称密钥规格的通用参数规格。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*spec | 非对称密钥规格。 |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*commonParamsSpec | 通用参数规格。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_GetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type, Crypto_DataBlob *value)
```

**描述**

获取非对称密钥规格的指定参数。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放value内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*spec | 非对称密钥规格。 |
| [CryptoAsymKey\_ParamType](capi-crypto-asym-key-h.md#cryptoasymkey_paramtype) type | 非对称密钥参数类型。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | 输出数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeySpec\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoAsymKeySpec_Destroy(OH_CryptoAsymKeySpec *spec)
```

**描述**

销毁非对称密钥规格。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*spec | 非对称密钥规格。 |

### OH\_CryptoAsymKeyGeneratorWithSpec\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_Create(OH_CryptoAsymKeySpec *keySpec, OH_CryptoAsymKeyGeneratorWithSpec **generator)
```

**描述**

创建带规格的非对称密钥生成器。

注意：创建的资源必须通过[OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeySpec](capi-cryptoasymkeyapi-oh-cryptoasymkeyspec.md) \*keySpec | 非对称密钥规格。 |
| [OH\_CryptoAsymKeyGeneratorWithSpec](cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec.md) \*\*generator | 带规格的非对称密钥生成器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(OH_CryptoAsymKeyGeneratorWithSpec *generator, OH_CryptoKeyPair **keyPair)
```

**描述**

根据非对称密钥规格生成密钥对。

注意：使用完成后必须通过[OH\_CryptoKeyPair\_Destroy](capi-crypto-asym-key-h.md#oh_cryptokeypair_destroy)释放keyPair内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGeneratorWithSpec](cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec.md) \*generator | 带规格的非对称密钥生成器。 |
| [OH\_CryptoKeyPair](capi-cryptoasymkeyapi-oh-cryptokeypair.md) \*\*keyPair | 指向密钥对的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoAsymKeyGeneratorWithSpec\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoAsymKeyGeneratorWithSpec_Destroy(OH_CryptoAsymKeyGeneratorWithSpec *generator)
```

**描述**

销毁带规格的非对称密钥生成器。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoAsymKeyGeneratorWithSpec](cryptoasymkeyapi-oh-cryptoasymkeygeneratorwithspec.md) \*generator | 带规格的非对称密钥生成器。 |

### OH\_CryptoEcPoint\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEcPoint_Create(const char *curveName, Crypto_DataBlob *ecKeyData, OH_CryptoEcPoint **point)
```

**描述**

创建EC点。

注意：创建的资源必须通过[OH\_CryptoEcPoint\_Destroy](capi-crypto-asym-key-h.md#oh_cryptoecpoint_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*curveName | 曲线名称。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*ecKeyData | EC点数据，支持"04 || x || y"、"02 || x"或"03 || x"格式。如果ecKeyData参数为NULL，将创建一个空的EC点规格。 |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) \*\*point | 指向EC点的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEcPoint\_GetCoordinate()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEcPoint_GetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)
```

**描述**

获取EC点的x和y坐标。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放x和y内存

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) \*point | EC点。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*x | EC点的x坐标,可以为NULL。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*y | EC点的y坐标,可以为NULL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEcPoint\_SetCoordinate()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEcPoint_SetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)
```

**描述**

设置EC点的x和y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) \*point | EC点。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*x | EC点的x坐标。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*y | EC点的y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEcPoint\_Encode()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoEcPoint_Encode(OH_CryptoEcPoint *point, const char *format, Crypto_DataBlob *out)
```

**描述**

将EC点编码为指定格式。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) \*point | EC点。 |
| const char \*format | 编码格式,支持"UNCOMPRESSED"和"COMPRESSED"。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | 编码后的EC点数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERTION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoEcPoint\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoEcPoint_Destroy(OH_CryptoEcPoint *point)
```

**描述**

销毁EC点。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoEcPoint](capi-cryptoasymkeyapi-oh-cryptoecpoint.md) \*point | EC点。 |
