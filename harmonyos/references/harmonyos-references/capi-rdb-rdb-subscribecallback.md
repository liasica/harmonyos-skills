---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback
title: Rdb_SubscribeCallback
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_SubscribeCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5264d06e7e3fab8e0e6a688ee0ae07484bda26315cc8c6eb4d5d42c1a0365eba
---

```c
typedef union Rdb_SubscribeCallback {...} Rdb_SubscribeCallback
```

## 概述

表示回调函数。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rdb\_DetailsObserver](capi-relational-store-h.md#rdb_detailsobserver) detailsObserver | 端云数据更改事件的细节的回调函数。 |
| [Rdb\_BriefObserver](capi-relational-store-h.md#rdb_briefobserver) briefObserver | 端云数据更改事件的回调函数。 |
