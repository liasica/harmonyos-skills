---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/sexternalcryptotypeapi-oh-huks-externalcryptoparam
title: OH_Huks_ExternalCryptoParam
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ExternalCryptoParam
category: harmonyos-references
scraped_at: 2026-04-29T13:58:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f5c394f8922842f83d8ea38d617da68f45cc63a0f9edaac70295f1b571aad790
---

```
1. typedef struct {...} OH_Huks_ExternalCryptoParam
```

## 概述

PC/2in1

定义参数集合中单个参数的结构体。

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](capi-huksexternalcryptotypeapi.md)

**所在头文件：** [native\_huks\_external\_crypto\_type.h](capi-native-huks-external-crypto-type-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 标签值。 |
| union {  bool boolParam;  int32\_t int32Param;  uint32\_t uint32Param;  uint64\_t uint64Param;  [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) blob;  } | 标签内容。  boolParam：布尔类型参数。  int32Param：int32\_t类型参数。  uint32Param：uint32\_t类型参数。  uint64Param：uint64\_t类型参数。  blob：OH\_Huks\_Blob类型参数。 |
