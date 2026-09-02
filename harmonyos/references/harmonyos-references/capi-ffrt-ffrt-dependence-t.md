---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-dependence-t
title: ffrt_dependence_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_dependence_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:86a4ff69810e2428a54051e004342b0a2f93a33e34857eb81bb0bb4e466d90e1
---

```c
typedef struct {...} ffrt_dependence_t
```

## 概述

依赖数据项结构，用于描述任务间的单个依赖关系。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ffrt\_dependence\_type\_t](capi-type-def-h.md#ffrt_dependence_type_t) type | 依赖类型。 |
| const void\* ptr | 依赖指针。数据依赖时指向数据，任务依赖时指向任务句柄。 |
