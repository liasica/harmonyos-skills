---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdsa
title: OH_Huks_KeyMaterialDsa
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialDsa
category: harmonyos-references
scraped_at: 2026-04-29T13:58:20+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:c145bfad6c6fd7d432bf301df8f6068aba3e50148b51baa6059a0954aa620fce
---

```
1. struct OH_Huks_KeyMaterialDsa {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义DSA密钥的结构体类型。

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
| uint32\_t xSize | x值的长度。 |
| uint32\_t ySize | y值的长度。 |
| uint32\_t pSize | p值的长度。 |
| uint32\_t qSize | q值的长度。 |
| uint32\_t gSize | g值的长度。 |
