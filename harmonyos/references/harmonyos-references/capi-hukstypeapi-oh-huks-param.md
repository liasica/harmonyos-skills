---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param
title: OH_Huks_Param
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Param
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f99e564f7be7444e92ef24b4bed3de37a4ace95407f64afe0bdc8ea79e412753
---

```c
struct OH_Huks_Param {...}
```

## 概述

定义参数集中的参数结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t tag | 标签值。 |
| union {  bool boolParam;  int32\_t int32Param;  uint32\_t uint32Param;  uint64\_t uint64Param;  [struct OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) blob;  } | boolParam：布尔型参数。  int32Param：int32\_t型参数。  uint32Param：uint32\_t型参数。  uint64Param：uint64\_t型参数。  blob：OH\_Huks\_Blob型参数。 |
