---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-resultlist
title: CloudDisk_ResultList
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_ResultList
category: harmonyos-references
scraped_at: 2026-04-28T08:05:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c62feafde58e502027e2cd64335f6fac7d59deec562922a9edf68d8d250fab92
---

```
1. typedef struct CloudDisk_ResultList {...} CloudDisk_ResultList
```

## 概述

PC/2in1Tablet

表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

PC/2in1Tablet

### 成员变量

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) pathInfo | 文件的绝对路径信息。 |
| bool isSuccess{false} | 表示操作是否成功。true：表示操作成功；false：表示操作失败。默认值为false。 |
| [CloudDisk\_SyncState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncstate) syncState | 文件的同步状态。当isSuccess为true时才生效。 |
| [CloudDisk\_ErrorReason](capi-oh-cloud-disk-manager-h.md#clouddisk_errorreason) errorReason | 文件同步状态获取失败的原因。当isSuccess为false时才生效。 |
