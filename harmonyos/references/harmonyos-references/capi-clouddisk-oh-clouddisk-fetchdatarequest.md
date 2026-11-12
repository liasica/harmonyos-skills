---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-fetchdatarequest
title: OH_CloudDisk_FetchDataRequest
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_FetchDataRequest
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a6389f46b9968f0e729f3212d8de181e978fd02ba2494ba30c24bc0e66b57740
---

```c
typedef struct OH_CloudDisk_FetchDataRequest {...} OH_CloudDisk_FetchDataRequest
```

## 概述

获取数据请求信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) filePath | 同步根内相对文件路径。  **起始版本：** 26.0.1 |
| [OH\_CloudDisk\_HydratePriority](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_hydratepriority) priority | 水合优先级。  **起始版本：** 26.0.1 |
