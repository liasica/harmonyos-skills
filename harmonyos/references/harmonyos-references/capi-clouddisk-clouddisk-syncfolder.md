---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-syncfolder
title: CloudDisk_SyncFolder
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_SyncFolder
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f961ed98526a47c7d0eedabf74011ca236364c53400e72a6a90d9fc87ce044a1
---

```c
typedef struct CloudDisk_SyncFolder {...} CloudDisk_SyncFolder
```

## 概述

同步根属性信息。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| CloudDisk\_SyncFolderPath path | 同步根路径。 |
| [CloudDisk\_SyncFolderState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncfolderstate) state | 同步根路径状态。 |
| [CloudDisk\_DisplayNameInfo](capi-clouddisk-clouddisk-displaynameinfo.md) displayNameInfo | 同步根路径别名信息。 |
