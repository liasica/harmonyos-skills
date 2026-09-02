---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-changedata
title: CloudDisk_ChangeData
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > CloudDisk_ChangeData
category: harmonyos-references
scraped_at: 2026-09-02T15:01:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:578ef91ad2f3df587dfc1aa6783efdd7e2f2c60a5c4ffe579571496302171929
---

```c
typedef struct CloudDisk_ChangeData  {...} CloudDisk_ChangeData
```

## 概述

定义了同步根路径下单个文件变更事件的数据结构。该结构包含有关文件变更的详细信息，包括唯一ID、父目录的唯一ID、相对路径、变更类型、文件大小和时间戳。

**起始版本：** 21

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t updateSequenceNumber{0} | 变更事件的更新序列号。每次文件更改时单调递增加1，用于增量变更查询。范围：[0, 2^64 - 1]。 |
| CloudDisk\_FileIdInfo fileId | 全局唯一的文件ID。在文件的生命周期内保持不变。 |
| CloudDisk\_FileIdInfo parentFileId | 文件或目录所属父目录的唯一ID。 |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) relativePathInfo | 同步根路径下的文件，相对于同步根路径的相对路径。 |
| [CloudDisk\_OperationType](capi-oh-cloud-disk-manager-h.md#clouddisk_operationtype) operationType | 此文件的变更操作类型（如：创建、删除、移动等）。 |
| uint64\_t size{0} | 文件大小，单位：Byte。 |
| uint64\_t mtime{0} | 文件修改时间，单位：ms。 |
| uint64\_t timeStamp{0} | 变更事件发生时间，单位：ms。 |
