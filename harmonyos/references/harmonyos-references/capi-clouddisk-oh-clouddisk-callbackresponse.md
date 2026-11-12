---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-callbackresponse
title: OH_CloudDisk_CallbackResponse
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_CallbackResponse
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a7e85045aecf0ff1778bf5993c811299e7c833b8c0627ba2a4f848d1a00b5b4b
---

```c
typedef union OH_CloudDisk_CallbackResponse {...} OH_CloudDisk_CallbackResponse
```

## 概述

回调响应信息联合体。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_CloudDisk\_FetchData](capi-clouddisk-oh-clouddisk-fetchdata.md) \*fetchData | 获取数据响应。当callbackType为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_FETCH\_DATA时生效。  **起始版本：** 26.0.1 |
