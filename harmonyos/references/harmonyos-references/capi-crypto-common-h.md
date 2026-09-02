---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-crypto-common-h
title: crypto_common.h
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > C API > 头文件 > crypto_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e58562cbf27c7ba1e33a948fd2fba7b8500e2b82519675981d374f473054569d
---

## 概述

定义加解密通用的数据结构和错误码。

**引用文件：** <CryptoArchitectureKit/crypto\_common.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：** [CryptoCommonApi](capi-cryptocommonapi.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) | Crypto\_DataBlob | 加解密数据结构体。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Crypto\_ErrCode](capi-crypto-common-h.md#oh_crypto_errcode) | OH\_Crypto\_ErrCode | 枚举错误码。 |
| [Crypto\_CipherMode](capi-crypto-common-h.md#crypto_ciphermode) | Crypto\_CipherMode | 定义加解密模式。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [void OH\_Crypto\_FreeDataBlob(Crypto\_DataBlob \*dataBlob)](capi-crypto-common-h.md#oh_crypto_freedatablob) | 释放数据Blob的内存。 |

## 枚举类型说明

### OH\_Crypto\_ErrCode

```c
enum OH_Crypto_ErrCode
```

**描述**

枚举错误码。

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_SUCCESS = 0 | 表示操作成功。  **起始版本：** 12 |
| CRYPTO\_INVALID\_PARAMS = 401 | 表示输入参数无效。  **起始版本：** 12 |
| CRYPTO\_NOT\_SUPPORTED = 801 | 表示不支持的功能或算法。  **起始版本：** 12 |
| CRYPTO\_MEMORY\_ERROR = 17620001 | 表示内存操作失败。  **起始版本：** 12 |
| CRYPTO\_PARAMETER\_CHECK\_FAILED = 17620003 | 表示参数校验失败。  **起始版本：** 20 |
| CRYPTO\_INVALID\_CALL = 17620004 | 表示无效的函数调用。  **起始版本：** 26.0.0 |
| CRYPTO\_OPERTION\_ERROR = 17630001 | 表示加解密操作错误。  **起始版本：** 12 |

### Crypto\_CipherMode

```c
enum Crypto_CipherMode
```

**描述**

定义加解密模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO\_ENCRYPT\_MODE = 0 | 表示加密操作。 |
| CRYPTO\_DECRYPT\_MODE = 1 | 表示解密操作。 |

## 函数说明

### OH\_Crypto\_FreeDataBlob()

```c
void OH_Crypto_FreeDataBlob(Crypto_DataBlob *dataBlob)
```

**描述**

释放数据Blob的内存。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Crypto\_DataBlob](capi-cryptocommonapi-crypto-datablob.md) \*dataBlob | [in] 待释放的数据Blob。 |
