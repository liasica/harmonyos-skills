---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-mac-h
title: crypto_mac.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_mac.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:08ec3cc9064c9fd6ed81ec43f69843936937edf68c9d53a20b819276bfc843ba
---

## 概述

PhonePC/2in1TabletTVWearable

定义MAC接口。

**引用文件：** <CryptoArchitectureKit/crypto\_mac.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：** [CryptoMacApi](capi-cryptomacapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) | OH\_CryptoMac | 定义MAC结构。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CryptoMac\_ParamType](capi-crypto-mac-h.md#cryptomac_paramtype) | CryptoMac\_ParamType | 定义MAC算法参数类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Create(const char \*algoName, OH\_CryptoMac \*\*ctx)](capi-crypto-mac-h.md#oh_cryptomac_create) | 根据给定的算法名称创建MAC实例。  注意：创建的资源必须通过[OH\_CryptoMac\_Destroy](capi-crypto-mac-h.md#oh_cryptomac_destroy)销毁。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_SetParam(OH\_CryptoMac \*ctx, CryptoMac\_ParamType type, const Crypto\_DataBlob \*value)](capi-crypto-mac-h.md#oh_cryptomac_setparam) | 设置MAC参数。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Init(OH\_CryptoMac \*ctx, const OH\_CryptoSymKey \*key)](capi-crypto-mac-h.md#oh_cryptomac_init) | 使用对称密钥初始化MAC实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Update(OH\_CryptoMac \*ctx, const Crypto\_DataBlob \*in)](capi-crypto-mac-h.md#oh_cryptomac_update) | 更新MAC实例。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_Final(OH\_CryptoMac \*ctx, Crypto\_DataBlob \*out)](capi-crypto-mac-h.md#oh_cryptomac_final) | 完成MAC操作。  注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。 |
| [OH\_Crypto\_ErrCode OH\_CryptoMac\_GetLength(OH\_CryptoMac \*ctx, uint32\_t \*length)](capi-crypto-mac-h.md#oh_cryptomac_getlength) | 获取MAC长度。 |
| [void OH\_CryptoMac\_Destroy(OH\_CryptoMac \*ctx)](capi-crypto-mac-h.md#oh_cryptomac_destroy) | 销毁MAC实例。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### CryptoMac\_ParamType

PhonePC/2in1TabletTVWearable

```
1. enum CryptoMac_ParamType
```

**描述**

定义MAC算法参数类型。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_MAC\_DIGEST\_NAME\_STR = 0 | HMAC消息认证码使用的摘要函数的算法名称，例如SHA256。 |
| CRYPTO\_MAC\_CIPHER\_NAME\_STR = 1 | CMAC消息认证码使用的对称加密算法名称，例如AES256。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CryptoMac\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_Create(const char *algoName, OH_CryptoMac **ctx)
```

**描述**

根据给定的算法名称创建MAC实例。

注意：创建的资源必须通过[OH\_CryptoMac\_Destroy](capi-crypto-mac-h.md#oh_cryptomac_destroy)销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*algoName | 用于生成MAC实例的算法名称。  例如"HMAC"、"CMAC"。 |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*\*ctx | MAC实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoMac\_SetParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_SetParam(OH_CryptoMac *ctx, CryptoMac_ParamType type, const Crypto_DataBlob *value)
```

**描述**

设置MAC参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
| [CryptoMac\_ParamType](capi-crypto-mac-h.md#cryptomac_paramtype) type | MAC参数类型。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*value | MAC参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoMac\_Init()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_Init(OH_CryptoMac *ctx, const OH_CryptoSymKey *key)
```

**描述**

使用对称密钥初始化MAC实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
| [const OH\_CryptoSymKey](capi-cryptosymkeyapi-oh-cryptosymkey.md) \*key | 对称密钥。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoMac\_Update](capi-crypto-mac-h.md#oh_cryptomac_update)

[OH\_CryptoMac\_Final](capi-crypto-mac-h.md#oh_cryptomac_final)

### OH\_CryptoMac\_Update()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_Update(OH_CryptoMac *ctx, const Crypto_DataBlob *in)
```

**描述**

更新MAC实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
| [const Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*in | 需要更新的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoMac\_Init](capi-crypto-mac-h.md#oh_cryptomac_init)

[OH\_CryptoMac\_Final](capi-crypto-mac-h.md#oh_cryptomac_final)

### OH\_CryptoMac\_Final()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_Final(OH_CryptoMac *ctx, Crypto_DataBlob *out)
```

**描述**

完成MAC操作。

注意：使用完成后必须通过[OH\_Crypto\_FreeDataBlob](capi-crypto-common-h.md#oh_crypto_freedatablob)释放out内存。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*out | MAC值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

**参考：**

[OH\_CryptoMac\_Init](capi-crypto-mac-h.md#oh_cryptomac_init)

[OH\_CryptoMac\_Update](capi-crypto-mac-h.md#oh_cryptomac_update)

### OH\_CryptoMac\_GetLength()

PhonePC/2in1TabletTVWearable

```
1. OH_Crypto_ErrCode OH_CryptoMac_GetLength(OH_CryptoMac *ctx, uint32_t *length)
```

**描述**

获取MAC长度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
| uint32\_t \*length | MAC长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | CRYPTO\_SUCCESS：操作成功。  CRYPTO\_NOT\_SUPPORTED：操作不支持。  CRYPTO\_MEMORY\_ERROR：内存错误。  CRYPTO\_PARAMETER\_CHECK\_FAILED：参数检查失败。  CRYPTO\_OPERATION\_ERROR：调用三方算法库API出错。 |

### OH\_CryptoMac\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_CryptoMac_Destroy(OH_CryptoMac *ctx)
```

**描述**

销毁MAC实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CryptoMac](capi-cryptomacapi-oh-cryptomac.md) \*ctx | MAC实例。 |
