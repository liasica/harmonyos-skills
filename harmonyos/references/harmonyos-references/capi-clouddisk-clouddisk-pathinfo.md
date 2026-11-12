---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo
title: CloudDisk_PathInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_PathInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:54025b7332f6c5c50ad7dce2372205459737b5da9b20ec3496047f3e0f117a32
---

```c
typedef struct CloudDisk_PathInfo {...} CloudDisk_PathInfo
typedef struct CloudDisk_PathInfo CloudDisk_FileIdInfo
typedef struct CloudDisk_PathInfo CloudDisk_SyncFolderPath
```

## 概述

文件路径信息。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*value | 文件的路径，以'\0'字符结尾。 |
| size\_t length | 文件路径的长度，不包括结尾的'\0'字符。 |
