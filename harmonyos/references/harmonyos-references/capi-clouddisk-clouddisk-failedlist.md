---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-failedlist
title: CloudDisk_FailedList
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_FailedList
category: harmonyos-references
scraped_at: 2026-04-28T08:05:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:30fe3521a1bdaa965134232acbf33021c8063b28d096d41aac1bc3c11aa170f1
---

```
1. typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```

## 概述

PC/2in1Tablet

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) pathInfo | 失败文件的绝对路径信息。 |
| [CloudDisk\_ErrorReason](capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) errorReason | 文件同步失败的原因。 |
