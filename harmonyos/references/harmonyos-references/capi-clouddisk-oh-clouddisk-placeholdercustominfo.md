---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-placeholdercustominfo
title: OH_CloudDisk_PlaceholderCustomInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_PlaceholderCustomInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f173619b25f45bf8f589cf266553b305d3cdde73c59922f06ead4961a5f64de0
---

```c
typedef struct OH_CloudDisk_PlaceholderCustomInfo OH_CloudDisk_PlaceholderCustomInfo
```

## 概述

与占位符关联的不透明自定义信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t dataLength | 自定义信息的长度，单位为字节。  **起始版本：** 26.0.1 |
| const uint8\_t \*data | 指向自定义信息的指针。  **起始版本：** 26.0.1 |
