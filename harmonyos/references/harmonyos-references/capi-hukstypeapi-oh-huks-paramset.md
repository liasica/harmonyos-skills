---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset
title: OH_Huks_ParamSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_ParamSet
category: harmonyos-references
scraped_at: 2026-04-29T13:58:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:565eaa277ce5e0f86e58ca06e84ecf00044f3337bc90f2646787ee1b1fd60a12
---

```
1. struct OH_Huks_ParamSet {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义参数集的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t paramSetSize | 参数集的内存大小。 |
| uint32\_t paramsCnt | 参数的个数。 |
| struct [OH\_Huks\_Param](capi-hukstypeapi-oh-huks-param.md) params[] | 参数数组。 |
