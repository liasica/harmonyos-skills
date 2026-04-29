---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialrsa
title: OH_Huks_KeyMaterialRsa
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialRsa
category: harmonyos-references
scraped_at: 2026-04-29T13:58:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d44c8e50493ce91819cd6f5048d0ee7c71e7713791b573a6158ece511fa73f92
---

```
1. struct OH_Huks_KeyMaterialRsa {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义Rsa密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | 密钥的长度。 |
| uint32\_t nSize | n值的长度。 |
| uint32\_t eSize | e值的长度。 |
| uint32\_t dSize | d值的长度。 |
