---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t
title: ffrt_fiber_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_fiber_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8bcfabe2ada54c3f9ee141a6a88e6ebc0fd3c0a321963dc68a9596d49c2c1370
---

```c
typedef struct {...} ffrt_fiber_t
```

## 概述

纤程结构体，用于存储纤程执行上下文。

**起始版本：** 20

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uintptr\_t storage[ffrt\_fiber\_storage\_size] | 纤程执行上下文的内部存储。请勿直接访问，通过[ffrt\_fiber\_init](capi-fiber-h.md#ffrt_fiber_init)初始化，通过[ffrt\_fiber\_switch](capi-fiber-h.md#ffrt_fiber_switch)切换。 |
