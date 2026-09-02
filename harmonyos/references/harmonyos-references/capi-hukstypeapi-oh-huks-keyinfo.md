---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyinfo
title: OH_Huks_KeyInfo
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aa18f2e59da607cb47954bedfafeb338135d3af3e5bbea07403aed68e225b77f
---

```c
struct OH_Huks_KeyInfo {...}
```

## 概述

定义密钥信息的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) alias | 密钥的别名。 |
| struct [OH\_Huks\_ParamSet](capi-hukstypeapi-oh-huks-paramset.md) \*paramSet | 指向密钥参数集的指针。 |
