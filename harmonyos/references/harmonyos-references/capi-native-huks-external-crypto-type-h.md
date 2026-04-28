---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-type-h
title: native_huks_external_crypto_type.h
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 头文件 > native_huks_external_crypto_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e726474b363530d3608e5296ee8801af122e375ae3a7a0cd75b370ceddb4814e
---

## 概述

PC/2in1

定义面向外部密钥管理扩展的结构体与枚举类型。

**引用文件：** <huks/native\_huks\_external\_crypto\_type.h>

**库：** libhuks\_external\_crypto.z.so

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](capi-huksexternalcryptotypeapi.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Huks\_ExternalCryptoParam](sexternalcryptotypeapi-oh-huks-externalcryptoparam.md) | OH\_Huks\_ExternalCryptoParam | 定义参数集合中单个参数的结构体。 |
| [OH\_Huks\_ExternalCryptoParamSet](ternalcryptotypeapi-oh-huks-externalcryptoparamset.md) | OH\_Huks\_ExternalCryptoParamSet | 定义外部加密参数集合的结构。 |

### 枚举

PC/2in1

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Huks\_ExternalCryptoTag](capi-native-huks-external-crypto-type-h.md#oh_huks_externalcryptotag) | OH\_Huks\_ExternalCryptoTag | 列举参数集合中使用的标签值。 |

### 宏定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| OH\_HUKS\_EXTERNAL\_CRYPTO\_MAX\_PROVIDER\_NAME\_LEN 100 | 定义provider名称的最大字节长度。  **起始版本：** 22 |
| OH\_HUKS\_EXTERNAL\_CRYPTO\_MAX\_RESOURCE\_ID\_LEN 512 | 定义资源ID的最大字节长度。  **起始版本：** 22 |

## 枚举类型说明

PC/2in1

### OH\_Huks\_ExternalCryptoTag

PC/2in1

```
1. enum OH_Huks_ExternalCryptoTag
```

**描述**

列举参数集合中使用的标签值。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN = OH\_HUKS\_TAG\_TYPE\_BYTES | 200001 | PIN码。 |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME = OH\_HUKS\_TAG\_TYPE\_BYTES | 200002 | 能力名称。 |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA = OH\_HUKS\_TAG\_TYPE\_BYTES | 200003 | 附加数据。 |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_UID = OH\_HUKS\_TAG\_TYPE\_INT | 200004 | 调用方的UID。 |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE = OH\_HUKS\_TAG\_TYPE\_INT | 200005 | 证书链用途。 |
| OH\_HUKS\_EXT\_CRYPTO\_TAG\_TIMEOUT = OH\_HUKS\_TAG\_TYPE\_UINT | 200006 | 获取属性操作的超时时间，单位：s。 |

### OH\_Huks\_ExternalPinAuthState

PC/2in1

```
1. enum OH_Huks_ExternalPinAuthState
```

**描述**

列举Ukey PIN码认证状态。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_NO\_AUTH = 0 | PIN码未认证。 |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED = 1 | PIN码认证成功。 |
| OH\_HUKS\_EXT\_CRYPTO\_PIN\_LOCKED = 2 | PIN码被锁。 |
