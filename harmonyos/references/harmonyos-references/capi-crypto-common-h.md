---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h
title: crypto_common.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4c3cb88afa126dc7d1541a818951fa29f9544d04ba63a5120c4186affdda41ab
---

## 概述

PhonePC/2in1TabletTVWearable

定义通用API接口。

**引用文件：** <CryptoArchitectureKit/crypto\_common.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoCommonApi](capi-cryptocommonapi.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) | Crypto\_DataBlob | 加解密数据结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | OH\_Crypto\_ErrCode | 加解密错误返回码枚举。 |
| [Crypto\_CipherMode](capi-crypto-common-h.md#crypto_ciphermode) | Crypto\_CipherMode | 定义加解密操作类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void OH\_Crypto\_FreeDataBlob(Crypto\_DataBlob \*dataBlob)](capi-crypto-common-h.md#oh_crypto_freedatablob) | 释放dataBlob数据。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Crypto\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Crypto_ErrCode
```

**描述**

加解密错误返回码枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_SUCCESS = 0 | 表示操作成功。 |
| CRYPTO\_INVALID\_PARAMS = 401 | 输入参数不合法。 |
| CRYPTO\_NOT\_SUPPORTED = 801 | 不支持的函数或算法。 |
| CRYPTO\_MEMORY\_ERROR = 17620001 | 内存错误。 |
| CRYPTO\_PARAMETER\_CHECK\_FAILED = 17620003 | 参数检查失败。  **起始版本：** 20 |
| CRYPTO\_OPERTION\_ERROR = 17630001 | 表示加解密操作错误。 |

### Crypto\_CipherMode

PhonePC/2in1TabletTVWearable

```
1. enum Crypto_CipherMode
```

**描述**

定义加解密操作类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_ENCRYPT\_MODE = 0 | 加密操作。 |
| CRYPTO\_DECRYPT\_MODE = 1 | 解密操作。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Crypto\_FreeDataBlob()

PhonePC/2in1TabletTVWearable

```
1. void OH_Crypto_FreeDataBlob(Crypto_DataBlob *dataBlob)
```

**描述**

释放dataBlob数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*dataBlob | 需要释放的dataBlob数据。 |
