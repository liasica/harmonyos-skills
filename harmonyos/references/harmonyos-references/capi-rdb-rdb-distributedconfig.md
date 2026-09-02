---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-distributedconfig
title: Rdb_DistributedConfig
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_DistributedConfig
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ccb86c381048fe1b34d5f6f2d5812f78c8a1b287c04679747c231b41a923c095
---

```c
typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```

## 概述

记录表的分布式配置信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int version | 表示Rdb\_DistributedConfig结构体的版本。 |
| bool isAutoSync | 表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用[OH\_Rdb\_CloudSync](capi-relational-store-h.md#oh_rdb_cloudsync)接口触发端云同步。 |
