---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param
title: OH_Huks_Param
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Param
category: harmonyos-references
scraped_at: 2026-04-29T13:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9878ece52521be75b6a8da7705979034bb81e7b534596c87a048e13bb376f982
---

```
1. struct OH_Huks_Param {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义参数集中的参数结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 标签值。 |
| union {  bool boolParam;  int32\_t int32Param;  uint32\_t uint32Param;  uint64\_t uint64Param;  [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) blob;  } | boolParam：bool型参数。  int32Param：int32\_t型参数。  uint32Param：uint32\_t型参数。  uint64Param：uint64\_t型参数。  blob：OH\_Huks\_Blob型参数。 |
