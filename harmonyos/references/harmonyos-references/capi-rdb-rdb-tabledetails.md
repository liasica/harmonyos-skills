---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-tabledetails
title: Rdb_TableDetails
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_TableDetails
category: harmonyos-references
scraped_at: 2026-04-28T07:59:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9b8d0153cc570ba15b7ad2d27a82439899e8cf8b350bb8a2a8087387acde8057
---

```
1. typedef struct Rdb_TableDetails {...} Rdb_TableDetails
```

## 概述

PhonePC/2in1TabletTVWearable

描述数据库表执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* table | 数据库表名。 |
| [Rdb\_Statistic](capi-rdb-rdb-statistic.md) upload | 表示数据库表中端云同步上传过程的统计信息。 |
| [Rdb\_Statistic](capi-rdb-rdb-statistic.md) download | 表示数据库表中端云同步下载过程的统计信息。 |
