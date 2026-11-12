---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-fetchdata
title: OH_CloudDisk_FetchData
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_FetchData
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8ded9e6e7952af9680b8c432691facaa8f7d95f0519447867a462ee7fbad6444
---

```c
typedef struct OH_CloudDisk_FetchData {...} OH_CloudDisk_FetchData
```

## 概述

云端文件数据获取结果。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t offset | 本次数据在文件中的起始偏移，以字节为单位。  **起始版本：** 26.0.1 |
| uint64\_t size | 本次下载数据长度，以字节为单位。  **起始版本：** 26.0.1 |
| uint64\_t totalSize | 云端文件总大小，以字节为单位。  **起始版本：** 26.0.1 |
| [OH\_CloudDisk\_DataBuf](capi-clouddisk-oh-clouddisk-databuf.md) data | 文件数据缓冲区。  **起始版本：** 26.0.1 |
| bool isComplete | 是否是最后一块数据。true表示当前数据块是文件水合的最后一块；false表示后续还有数据需要传输。  **起始版本：** 26.0.1 |
