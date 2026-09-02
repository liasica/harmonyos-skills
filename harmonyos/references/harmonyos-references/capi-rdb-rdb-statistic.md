---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-statistic
title: Rdb_Statistic
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_Statistic
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:34c42178bf4751ddbe0f38842e538d789eda1de26cc1e9706486cf469c4bb45a
---

```c
typedef struct Rdb_Statistic {...} Rdb_Statistic
```

## 概述

描述数据库表的端云同步过程的统计信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int total | 表示数据库表中需要端云同步的总行数。 |
| int successful | 表示数据库表中端云同步成功的行数。 |
| int failed | 表示数据库表中端云同步失败的行数。 |
| int remained | 表示数据库表中端云同步剩余未执行的行数。 |
