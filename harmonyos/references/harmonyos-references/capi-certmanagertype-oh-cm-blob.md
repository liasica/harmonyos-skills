---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-blob
title: OH_CM_Blob
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 结构体 > OH_CM_Blob
category: harmonyos-references
scraped_at: 2026-04-28T08:07:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5e68776f0bb1c611ee6c28b1916b4fedb8dbcb95c4d09ddbdfdee7470e27a914
---

```
1. typedef struct {...} OH_CM_Blob
```

## 概述

PhonePC/2in1TabletTVWearable

定义存放数据的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](capi-certmanagertype.md)

**所在头文件：** [cm\_native\_type.h](capi-cm-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据内存的指针。 |
