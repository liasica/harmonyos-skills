---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialrsa
title: OH_Huks_KeyMaterialRsa
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialRsa
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0a870df377b9d831cf6eeee4e6a62a522fc82c2b2a654b1045ba5da57c83e45
---

```c
struct OH_Huks_KeyMaterialRsa {...}
```

## 概述

定义RSA密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | 密钥的长度，单位：Bit。 |
| uint32\_t nSize | n值的长度，单位：Byte。 |
| uint32\_t eSize | e值的长度，单位：Byte。 |
| uint32\_t dSize | d值的长度，单位：Byte。 |
