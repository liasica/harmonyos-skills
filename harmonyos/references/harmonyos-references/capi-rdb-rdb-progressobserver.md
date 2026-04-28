---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressobserver
title: Rdb_ProgressObserver
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ProgressObserver
category: harmonyos-references
scraped_at: 2026-04-28T07:59:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab99c3f74199130ec927ace0df668b0200dae2c5f77bd12e852f06ebfa2524b2
---

```
1. typedef struct Rdb_ProgressObserver {...} Rdb_ProgressObserver
```

## 概述

PhonePC/2in1TabletTVWearable

端云同步进度观察者。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| void\* context | 端云同步进度观察者的上下文。 |
| [Rdb\_ProgressCallback](capi-relational-store-h.md#rdb_progresscallback) callback | 端云同步进度观察者的回调函数。 |
