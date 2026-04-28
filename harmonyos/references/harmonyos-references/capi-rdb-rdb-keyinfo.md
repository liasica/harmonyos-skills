---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keyinfo
title: Rdb_KeyInfo
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyInfo
category: harmonyos-references
scraped_at: 2026-04-28T07:59:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3e35e79cd6f0a8594f1a45edaa0e56815fa7b0eec181d3f84fbef806fa894c5a
---

```
1. typedef struct {...} Rdb_KeyInfo
```

## 概述

PhonePC/2in1TabletTVWearable

描述发生变化的行的主键或者行号。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int count | 表示发生变化的主键或者行号的数量。 |
| int type | 表示主键的类型[OH\_ColumnType](capi-oh-data-value-h.md#oh_columntype)。 |
| [Rdb\_KeyData](capi-rdb-rdb-keydata.md)\* data | 存放变化的具体数据 |
