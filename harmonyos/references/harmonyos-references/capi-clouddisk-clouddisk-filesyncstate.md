---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-filesyncstate
title: CloudDisk_FileSyncState
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_FileSyncState
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:09a7517de466d67515aafc5bf534020d80e5d0c2207e25dfc8ed3c1eefeae212
---

```c
typedef struct CloudDisk_FileSyncState {...} CloudDisk_FileSyncState
```

## 概述

文件的同步状态。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) filePathInfo | 文件的路径信息。 |
| [CloudDisk\_SyncState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncstate) syncState | 文件的同步状态。 |
