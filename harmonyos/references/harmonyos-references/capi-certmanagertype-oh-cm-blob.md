---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-blob
title: OH_CM_Blob
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 结构体 > OH_CM_Blob
category: harmonyos-references
scraped_at: 2026-09-02T15:01:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c7110a77ad7cfca04666e709c77241168762b169761933c6d8b0baea5f03e95
---

```c
typedef struct {...} OH_CM_Blob
```

## 概述

定义存放数据的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](capi-certmanagertype.md)

**所在头文件：** [cm\_native\_type.h](capi-cm-native-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 数据大小。单位：Byte。 |
| uint8\_t \*data | 指向数据内存的指针。 |
