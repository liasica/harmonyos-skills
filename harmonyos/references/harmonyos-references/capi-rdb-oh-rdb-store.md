---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-store
title: OH_Rdb_Store
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > OH_Rdb_Store
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3cbc2f116809d341cd01be0f5818d869e3a628f74bacb7a6d07b13c9477858f3
---

```c
typedef struct {...} OH_Rdb_Store
```

## 概述

表示数据库实例。需通过[OH\_Rdb\_GetOrOpen](capi-relational-store-h.md#oh_rdb_getoropen)或[OH\_Rdb\_CreateOrOpen](capi-relational-store-h.md#oh_rdb_createoropen)等函数获得。

**起始版本：** 10

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t id | OH\_Rdb\_Store结构体的唯一标识符。 |
