---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-placeholderinfo
title: OH_CloudDisk_PlaceholderInfo
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_PlaceholderInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0bfa214cffbd9dd694b371fa06e1e350ddf42348d570f3fed79c3c8536b4143f
---

```c
typedef struct OH_CloudDisk_PlaceholderInfo {...} OH_CloudDisk_PlaceholderInfo
```

## 概述

占位符相关操作使用的文件元数据信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t logicalSize | 占位符文件的逻辑大小，表示其对应云端文件的大小，单位为字节。  **起始版本：** 26.0.1 |
| uint64\_t atimeMs | 占位符文件对应云端文件的创建时间，单位为毫秒。  **起始版本：** 26.0.1 |
| uint64\_t mtimeMs | 占位符文件对应云端文件的最后一次修改时间，单位为毫秒。  **起始版本：** 26.0.1 |
