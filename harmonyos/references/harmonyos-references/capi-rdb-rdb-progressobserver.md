---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressobserver
title: Rdb_ProgressObserver
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ProgressObserver
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:68f3d095cdbe2bdbd0d5a9fc600cc506e2dccc1f9bf2d6ef095cbc58c9dbfce7
---

```c
typedef struct Rdb_ProgressObserver {...} Rdb_ProgressObserver
```

## 概述

端云同步进度观察者。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void\* context | 端云同步进度观察者的上下文。 |
| [Rdb\_ProgressCallback](capi-relational-store-h.md#rdb_progresscallback) callback | 端云同步进度观察者的回调函数。 |
