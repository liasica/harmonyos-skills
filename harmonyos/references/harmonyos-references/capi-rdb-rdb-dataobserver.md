---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-dataobserver
title: Rdb_DataObserver
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_DataObserver
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:12fefeabed0d4bc029f89b5327db219ee44b39ef4e5eca90c263b0b584c63d7c
---

```c
typedef struct Rdb_DataObserver {...} Rdb_DataObserver
```

## 概述

表示数据观察者。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void\* context | 表示数据观察者的上下文。 |
| [Rdb\_SubscribeCallback](capi-rdb-rdb-subscribecallback.md) callback | 数据观察者的回调。 |
