---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset
title: OH_Huks_ParamSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ParamSet
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7fbb6a01c7ab15dc2709b3707ec01e292f2d9ef7b10fbb2b051e1ce3e1559d73
---

```c
struct OH_Huks_ParamSet {...}
```

## 概述

定义参数集的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t paramSetSize | 参数集的内存大小。 |
| uint32\_t paramsCnt | 参数的个数。 |
| struct [OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) params[] | 参数数组。 |
