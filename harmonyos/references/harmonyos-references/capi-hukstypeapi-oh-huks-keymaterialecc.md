---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialecc
title: OH_Huks_KeyMaterialEcc
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialEcc
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:db36a9317042e8f4f44ad1c3e7434385d9c00bd7b074f192b6bf1971da8c536d
---

```c
struct OH_Huks_KeyMaterialEcc {...}
```

## 概述

定义ECC密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | 密钥的长度，单位：Bit。 |
| uint32\_t xSize | x值的长度，单位：Byte。 |
| uint32\_t ySize | y值的长度，单位：Byte。 |
| uint32\_t zSize | z值的长度，单位：Byte。 |
