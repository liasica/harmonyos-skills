---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo
title: CloudDisk_PathInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_PathInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:05:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4c58ae924411ba4d499f2817b9243a1da8f73986254db9f8eda9bf6fe4203ebe
---

```
1. typedef struct CloudDisk_PathInfo {...} CloudDisk_PathInfo
2. typedef struct CloudDisk_PathInfo CloudDisk_FieldInfo
3. typedef struct CloudDisk_PathInfo CloudDisk_SyncFolderPath
```

## 概述

PC/2in1Tablet

文件路径信息。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| char \*value | 文件的路径，以'\0'字符结尾。 |
| size\_t length | 文件路径的长度，不包括结尾的'\0'字符。 |
