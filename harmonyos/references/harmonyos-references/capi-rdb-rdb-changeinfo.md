---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-changeinfo
title: Rdb_ChangeInfo
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ChangeInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:59:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:722bae4e17de875a7cacf57ab609e9b85dd09ebbef8cc482348a81b1c3a2ceb3
---

```
1. typedef struct Rdb_ChangeInfo {...} Rdb_ChangeInfo
```

## 概述

PhonePC/2in1TabletTVWearable

记录端云同步过程详情。

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
| const char\* tableName | 表示发生变化的表的名称。 |
| int ChangeType | 表示发生变化的数据的类型，数据或者资产附件发生变化。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) inserted | 记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) updated | 记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) deleted | 记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。 |
