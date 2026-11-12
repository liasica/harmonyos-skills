---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-oh-clouddisk-callbackcontext
title: OH_CloudDisk_CallbackContext
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 结构体 > OH_CloudDisk_CallbackContext
category: harmonyos-references
scraped_at: 2026-11-12T09:55:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8dc5a04b18bc17740597ad0741bd5758afb3607276645ebd8fb2052b244234ae
---

```c
typedef union OH_CloudDisk_CallbackContext {...} OH_CloudDisk_CallbackContext
```

## 概述

回调请求上下文信息联合体。

**起始版本：** 26.0.1

**相关模块：** [CloudDisk](capi-clouddisk.md)

**所在头文件：** [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_CloudDisk\_FetchDataRequest](capi-clouddisk-oh-clouddisk-fetchdatarequest.md) \*fetchData | 获取数据请求。当callbackType为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_FETCH\_DATA时生效。  **起始版本：** 26.0.1 |
| [CloudDisk\_PathInfo](capi-clouddisk-clouddisk-pathinfo.md) \*cancelFetchData | 取消获取数据请求。当callbackType为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_CANCEL\_FETCH\_DATA时生效。  **起始版本：** 26.0.1 |
| [OH\_CloudDisk\_DehydrateInfo](capi-clouddisk-oh-clouddisk-dehydrateinfo.md) \*dehydrateData | 脱水授权请求。当callbackType为OH\_CLOUD\_DISK\_CALLBACK\_TYPE\_DEHYDRATE时生效。  **起始版本：** 26.0.1 |
