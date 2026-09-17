---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keyinfo
title: Rdb_KeyInfo
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyInfo
category: harmonyos-references
scraped_at: 2026-09-18T06:47:46+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:055a9f5f4670c7b286574da1d39e9e2bdbdaee98a172a53702859d298176b72b
---

```c
typedef struct Rdb_KeyInfo {...} Rdb_KeyInfo
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
