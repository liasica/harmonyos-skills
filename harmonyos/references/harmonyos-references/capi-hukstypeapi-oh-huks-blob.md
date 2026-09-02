---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob
title: OH_Huks_Blob
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Blob
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:af1bb753b0fe9de3d7f6e8275537a4cc9f8a5dbfcda3c8aa3d7ab27e3b5ed51e
---

```c
struct OH_Huks_Blob {...}
```

## 概述

定义存放数据的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据的指针。 |
