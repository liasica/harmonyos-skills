---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-callbackreqhead
title: OH_CloudDisk_CallbackReqHead
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_CallbackReqHead
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:374923206bc30ca9b4b5758dd868c763827e79a1f3742e6eaeb311a8d67d3e49
---

```c
typedef struct OH_CloudDisk_CallbackReqHead {...} OH_CloudDisk_CallbackReqHead
```

## 概述

云盘回调请求头信息。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [CloudDisk\_SyncFolderPath](capi-clouddisk-clouddisk-pathinfo.md) syncFolderPath | 回调请求所属同步根路径。  **起始版本：** 26.0.1 |
| [OH\_CloudDisk\_CallbackType](capi-oh-cloud-disk-manager-h.md#oh_clouddisk_callbacktype) callbackType | 回调请求类型。  **起始版本：** 26.0.1 |
| [OH\_CloudDisk\_DataBuf](capi-clouddisk-oh-clouddisk-databuf.md) reqKey | 水合请求标识。  **起始版本：** 26.0.1 |
