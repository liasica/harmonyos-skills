---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdh
title: OH_Huks_KeyMaterialDh
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialDh
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:041416e95981f73f6da1a41df7ca54319db55596d70b494aff77faf547861e27
---

```c
struct OH_Huks_KeyMaterialDh {...}
```

## 概述

定义DH密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| enum [OH\_Huks\_KeyAlg](capi-native-huks-type-h.md#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | DH密钥的长度，单位：Bit。 |
| uint32\_t pubKeySize | 公钥的长度，单位：Byte。 |
| uint32\_t priKeySize | 私钥的长度，单位：Byte。 |
| uint32\_t reserved | 保留字段。 |
