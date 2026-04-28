---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-crypto-param-h
title: oh_rdb_crypto_param.h
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 头文件 > oh_rdb_crypto_param.h
category: harmonyos-references
scraped_at: 2026-04-28T07:59:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:700bc7e1d441d1855f5c5b81ce9ff167fa80ef290c65d2fe235368ca22ac6cf8
---

## 概述

PhonePC/2in1TabletTVWearable

提供与关系型数据库加密参数相关的函数和枚举。

**引用文件：** <database/rdb/oh\_rdb\_crypto\_param.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 20

**相关模块：** [RDB](capi-rdb.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) | OH\_Rdb\_CryptoParam | 指定打开加密数据库时使用的加密参数。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Rdb\_EncryptionAlgo](capi-oh-rdb-crypto-param-h.md#rdb_encryptionalgo) | Rdb\_EncryptionAlgo | 数据库加密算法。 |
| [Rdb\_HmacAlgo](capi-oh-rdb-crypto-param-h.md#rdb_hmacalgo) | Rdb\_HmacAlgo | 打开数据库时支持的HMAC算法。 |
| [Rdb\_KdfAlgo](capi-oh-rdb-crypto-param-h.md#rdb_kdfalgo) | Rdb\_KdfAlgo | 打开数据库时支持的KDF算法。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam \*OH\_Rdb\_CreateCryptoParam(void)](capi-oh-rdb-crypto-param-h.md#oh_rdb_createcryptoparam) | 创建一个[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例对象。 |
| [int OH\_Rdb\_DestroyCryptoParam(OH\_Rdb\_CryptoParam \*param)](capi-oh-rdb-crypto-param-h.md#oh_rdb_destroycryptoparam) | 销毁一个[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例对象。 |
| [int OH\_Crypto\_SetEncryptionKey(OH\_Rdb\_CryptoParam \*param, const uint8\_t \*key, int32\_t length)](capi-oh-rdb-crypto-param-h.md#oh_crypto_setencryptionkey) | 设置[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)对象的密钥数据。 |
| [int OH\_Crypto\_SetIteration(OH\_Rdb\_CryptoParam \*param, int64\_t iteration)](capi-oh-rdb-crypto-param-h.md#oh_crypto_setiteration) | 设置打开加密数据库时使用的KDF算法迭代次数。 |
| [int OH\_Crypto\_SetEncryptionAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](capi-oh-rdb-crypto-param-h.md#oh_crypto_setencryptionalgo) | 设置打开加密数据库时使用的加密算法。 |
| [int OH\_Crypto\_SetHmacAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](capi-oh-rdb-crypto-param-h.md#oh_crypto_sethmacalgo) | 设置打开加密数据库时使用的HMAC算法。 |
| [int OH\_Crypto\_SetKdfAlgo(OH\_Rdb\_CryptoParam \*param, int32\_t algo)](capi-oh-rdb-crypto-param-h.md#oh_crypto_setkdfalgo) | 设置打开加密数据库时使用的KDF算法。 |
| [int OH\_Crypto\_SetCryptoPageSize(OH\_Rdb\_CryptoParam \*param, int64\_t size)](capi-oh-rdb-crypto-param-h.md#oh_crypto_setcryptopagesize) | 设置打开加密数据库时使用的页大小。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Rdb\_EncryptionAlgo

PhonePC/2in1TabletTVWearable

```
1. enum Rdb_EncryptionAlgo
```

**描述**

数据库加密算法。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| RDB\_AES\_256\_GCM = 0 | 表示数据库使用RDB\_AES\_256\_GCM加密。 |
| RDB\_AES\_256\_CBC | 表示数据库使用RDB\_AES\_256\_CBC加密。 |
| RDB\_PLAIN\_TEXT | 表示数据库不加密。  **起始版本：** 22 |

### Rdb\_HmacAlgo

PhonePC/2in1TabletTVWearable

```
1. enum Rdb_HmacAlgo
```

**描述**

打开数据库时支持的HMAC算法。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| RDB\_HMAC\_SHA1 = 0 | RDB\_HMAC\_SHA1算法。 |
| RDB\_HMAC\_SHA256 | RDB\_HMAC\_SHA256算法。 |
| RDB\_HMAC\_SHA512 | RDB\_HMAC\_SHA512算法。 |

### Rdb\_KdfAlgo

PhonePC/2in1TabletTVWearable

```
1. enum Rdb_KdfAlgo
```

**描述**

打开数据库时支持的KDF算法。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| RDB\_KDF\_SHA1 = 0 | RDB\_KDF\_SHA1算法。 |
| RDB\_KDF\_SHA256 | RDB\_KDF\_SHA256算法。 |
| RDB\_KDF\_SHA512 | RDB\_KDF\_SHA512算法。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Rdb\_CreateCryptoParam()

PhonePC/2in1TabletTVWearable

```
1. OH_Rdb_CryptoParam *OH_Rdb_CreateCryptoParam(void)
```

**描述**

创建一个[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例对象。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) | 成功时返回指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。  否则返回nullptr。使用完成后，必须通过[OH\_Rdb\_DestroyCryptoParam](capi-oh-rdb-crypto-param-h.md#oh_rdb_destroycryptoparam)接口释放内存。 |

### OH\_Rdb\_DestroyCryptoParam()

PhonePC/2in1TabletTVWearable

```
1. int OH_Rdb_DestroyCryptoParam(OH_Rdb_CryptoParam *param)
```

**描述**

销毁一个[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetEncryptionKey()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetEncryptionKey(OH_Rdb_CryptoParam *param, const uint8_t *key, int32_t length)
```

**描述**

设置[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)对象的密钥数据。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| const uint8\_t \*key | 表示指向数组数据的指针。 |
| int32\_t length | 表示密钥数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetIteration()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetIteration(OH_Rdb_CryptoParam *param, int64_t iteration)
```

**描述**

设置打开加密数据库时使用的KDF算法迭代次数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| int64\_t iteration | 表示迭代次数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetEncryptionAlgo()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetEncryptionAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

**描述**

设置打开加密数据库时使用的加密算法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| int32\_t algo | 表示加密算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetHmacAlgo()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetHmacAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

**描述**

设置打开加密数据库时使用的HMAC算法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| int32\_t algo | 表示HMAC算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetKdfAlgo()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetKdfAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

**描述**

设置打开加密数据库时使用的KDF算法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| int32\_t algo | 表示KDF算法。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |

### OH\_Crypto\_SetCryptoPageSize()

PhonePC/2in1TabletTVWearable

```
1. int OH_Crypto_SetCryptoPageSize(OH_Rdb_CryptoParam *param, int64_t size)
```

**描述**

设置打开加密数据库时使用的页大小。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md) \*param | 表示指向[OH\_Rdb\_CryptoParam](capi-rdb-oh-rdb-cryptoparam.md)实例的指针。 |
| int64\_t size | 表示页大小，单位为字节，取值应为2的幂值，最小值为1024，最大值65536。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。  如果执行成功，返回RDB\_OK。  如果输入参数无效，返回RDB\_E\_INVALID\_ARGS。 |
