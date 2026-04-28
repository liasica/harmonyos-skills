---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-statistic
title: Rdb_Statistic
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_Statistic
category: harmonyos-references
scraped_at: 2026-04-28T07:59:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:509f27f1cb2b1bfdfb8cea2405dae7dc50ea733887a57bae5461e30fa75c9443
---

```
1. typedef struct Rdb_Statistic {...} Rdb_Statistic
```

## 概述

PhonePC/2in1TabletTVWearable

描述数据库表的端云同步过程的统计信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int total | 表示数据库表中需要端云同步的总行数。 |
| int successful | 表示数据库表中端云同步成功的行数。 |
| int failed | 表示数据库表中端云同步失败的行数。 |
| int remained | 表示数据库表中端云同步剩余未执行的行数。 |
