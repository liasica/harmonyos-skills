---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob
title: OH_Huks_Blob
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Blob
category: harmonyos-references
scraped_at: 2026-04-29T13:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b8f83fb8b7336d6c1cdac993f2059fe87cf6c6080c151bd08d178439d1a12d1e
---

```
1. struct OH_Huks_Blob {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义存放数据的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据内存的指针。 |
