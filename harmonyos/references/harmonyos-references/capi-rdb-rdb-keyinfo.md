---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keyinfo
title: Rdb_KeyInfo
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:abb4594fa8a093f8e2d735ef30d3ed5e21cbc7151ad36d6da4558e695ecaa9e9
---

```c
typedef struct {...} Rdb_KeyInfo
```

## 概述

描述发生变化的行的主键或者行号。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int count | 表示发生变化的主键或者行号的数量。 |
| int type | 表示主键或行号的类型[OH\_ColumnType](capi-oh-data-value-h.md#oh_columntype)。 |
| [Rdb\_KeyData](capi-rdb-rdb-keydata.md)\* data | 存放发生变化的具体数据。 |
