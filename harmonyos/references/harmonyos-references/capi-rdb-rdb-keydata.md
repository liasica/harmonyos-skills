---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keydata
title: Rdb_KeyData
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyData
category: harmonyos-references
scraped_at: 2026-09-02T15:00:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:715b660ffcb799c4b03460a8b16af465b4e3cc41905c45c1461ec15eb7222e87
---

```c
union Rdb_KeyData { ... }
```

## 概述

存放变化的具体数据。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t integer | 存放uint64\_t类型的数据。 |
| double real | 存放double类型的数据。 |
| const char\* text | 存放字符串类型的数据。 |
