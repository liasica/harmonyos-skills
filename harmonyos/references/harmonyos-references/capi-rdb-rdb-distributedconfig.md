---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-distributedconfig
title: Rdb_DistributedConfig
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_DistributedConfig
category: harmonyos-references
scraped_at: 2026-04-28T07:59:36+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:0e77df2cb8cf5918fd6f975d5f7d5518abe96d786c1d12b900451392cfe86b10
---

```
1. typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```

## 概述

PhonePC/2in1TabletTVWearable

记录表的分布式配置信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb\_DistributedConfig结构的版本。 |
| bool isAutoSync | 表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用[OH\_Rdb\_CloudSync](capi-relational-store-h.md#oh_rdb_cloudsync)接口触发端云同步。 |
