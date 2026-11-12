---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-databuf
title: OH_CloudDisk_DataBuf
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_DataBuf
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:85fa62d95b71c7101bc53575490a958dbac0db5a3984cdc86acbfec2a0d6aff9
---

```c
typedef struct OH_CloudDisk_DataBuf {...} OH_CloudDisk_DataBuf
```

## 概述

云盘数据缓冲区信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*data | 数据缓冲区指针。  **起始版本：** 26.0.1 |
| uint64\_t dataSize | 数据缓冲区大小，以字节为单位。  **起始版本：** 26.0.1 |
