---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keydata
title: Rdb_KeyData
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_KeyData
category: harmonyos-references
scraped_at: 2026-09-18T06:47:46+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:07693297b77c72fe779e2f5476f3d17ecb8a075ece17b7f48c4583bc773dc611
---

```c
union Rdb_KeyData { ... } *data
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
