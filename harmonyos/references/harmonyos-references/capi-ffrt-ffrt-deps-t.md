---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-deps-t
title: ffrt_deps_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_deps_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5a3d443524ebad093fd341561712d3c6c8581f721438890e71d18ffa00211a86
---

```c
typedef struct {...} ffrt_deps_t
```

## 概述

依赖结构体，用于保存任务的依赖列表。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t len | 依赖数量。 |
| const [ffrt\_dependence\_t\*](capi-ffrt-ffrt-dependence-t.md) items | 依赖数据数组。 |
