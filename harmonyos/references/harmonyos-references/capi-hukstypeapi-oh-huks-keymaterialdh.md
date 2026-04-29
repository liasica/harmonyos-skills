---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdh
title: OH_Huks_KeyMaterialDh
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyMaterialDh
category: harmonyos-references
scraped_at: 2026-04-29T13:58:20+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:05752cf36097b845922a0093508465c5620305175c9699adabc09bc6c76c0e19
---

```
1. struct OH_Huks_KeyMaterialDh {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义DH密钥的结构体类型。

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
| uint32\_t keySize | DH密钥的长度。 |
| uint32\_t pubKeySize | 公钥的长度。 |
| uint32\_t priKeySize | 私钥的长度。 |
| uint32\_t reserved | 保留。 |
