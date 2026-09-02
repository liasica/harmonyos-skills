---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-failedlist
title: CloudDisk_FailedList
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_FailedList
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99d792375a0099ead32662c65ad9fcbd3166cf97244fa7810937b0227090f63a
---

```c
typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```

## 概述

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) pathInfo | 失败文件的绝对路径信息。 |
| [CloudDisk\_ErrorReason](capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) errorReason | 文件同步失败的原因。 |
