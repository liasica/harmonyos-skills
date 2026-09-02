---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressdetails
title: Rdb_ProgressDetails
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > C API > 结构体 > Rdb_ProgressDetails
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e6583847f58dc49fa9a8ac9dd855ce458d93c4f424b9ba6b9e1b2720368d1bed
---

```c
typedef struct Rdb_ProgressDetails {...} Rdb_ProgressDetails
```

## 概述

描述数据库整体执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：** [RDB](capi-rdb.md)

**所在头文件：** [relational\_store.h](capi-relational-store-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int version | 表示Rdb\_ProgressDetails结构体的版本。 |
| int schedule | 表示端云同步过程。 |
| int code | 表示端云同步过程的状态码。 |
| int32\_t tableLength | 表示端云同步的表的数量。 |
