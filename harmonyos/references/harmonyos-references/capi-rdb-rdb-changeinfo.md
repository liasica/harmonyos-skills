---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-changeinfo
title: Rdb_ChangeInfo
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ChangeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6645dd4e45a206b0c4729e5436aca0a653523ef1e458e1069e6149c3e0944b61
---

```c
typedef struct Rdb_ChangeInfo {...} Rdb_ChangeInfo
```

## 概述

记录端云同步过程详情。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb\_ChangeInfo结构体的版本。 |
| const char\* tableName | 表示发生变化的表的名称。 |
| int ChangeType | 表示发生变化的数据的类型。0表示数据发生变化，1表示资产附件发生变化。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) inserted | 记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) updated | 记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。 |
| [Rdb\_KeyInfo](capi-rdb-rdb-keyinfo.md) deleted | 记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。 |
