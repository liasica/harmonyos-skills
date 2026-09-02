---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi-oh-huks-externalcryptoparamset
title: OH_Huks_ExternalCryptoParamSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ExternalCryptoParamSet
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4080c37a4acbb24c6560ddc6a5cf0886baca585beda2c29bc04bea508e80c03b
---

```c
typedef struct OH_Huks_ExternalCryptoParamSet {...} OH_Huks_ExternalCryptoParamSet
```

## 概述

定义外部加密参数集合的结构体。

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](capi-huksexternalcryptotypeapi.md)

**所在头文件：** [native\_huks\_external\_crypto\_type.h](capi-native-huks-external-crypto-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t paramSetSize | 参数集合所占内存大小，单位：Byte。  **起始版本：** 22 |
| uint32\_t paramsCnt | 参数集合中的参数数量。  **起始版本：** 22 |
| [OH\_Huks\_ExternalCryptoParam](capi-huksexternalcryptotypeapi-oh-huks-externalcryptoparam.md) params[] | 参数数组，大小由paramSetSize与paramsCnt决定。  **起始版本：** 22 |
