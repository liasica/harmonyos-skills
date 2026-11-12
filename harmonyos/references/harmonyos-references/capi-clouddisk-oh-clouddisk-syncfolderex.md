---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-syncfolderex
title: OH_CloudDisk_SyncFolderEx
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_SyncFolderEx
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4cee5000b6e8ee42bbfea73d161529bc43410f442fc87a114a7a6da0c1a4c28f
---

```c
typedef struct OH_CloudDisk_SyncFolderEx {...} OH_CloudDisk_SyncFolderEx
```

## 概述

带占位符的同步根路径属性信息，包含同步根路径、同步状态、显示名称和是否支持占位符等信息，用于云盘同步功能中的带占位符同步根路径管理。使用时必须将版本字段设置为有效的版本宏(例如[OH\_CLOUD\_DISK\_SYNC\_FOLDER\_EX\_VERSION\_1](capi-oh-cloud-disk-manager-h.md#宏定义))，然后才能传递结构到任何API。运行时使用版本来确定字段有效；当指定低版本时，在较高版本中引入的字段将被忽略。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t version | 该结构体的版本信息。必须初始化为有效的版本宏，例如[OH\_CLOUD\_DISK\_SYNC\_FOLDER\_EX\_VERSION\_1](capi-oh-cloud-disk-manager-h.md#宏定义)。  **起始版本：** 26.0.1 |
| CloudDisk\_SyncFolderPath path | 同步根路径，用于指定带占位符的云盘同步根目录位置。  **起始版本：** 26.0.1 |
| [CloudDisk\_SyncFolderState](capi-oh-cloud-disk-manager-h.md#clouddisk_syncfolderstate) state | 同步根路径状态。  **起始版本：** 26.0.1 |
| [CloudDisk\_DisplayNameInfo](capi-clouddisk-clouddisk-displaynameinfo.md) displayNameInfo | 同步根路径别名信息，用于设置同步根路径的显示名称，便于用户识别和管理。  **起始版本：** 26.0.1 |
| bool isSupportPlaceHolder | 同步根是否支持占位符。  **起始版本：** 26.0.1 |
