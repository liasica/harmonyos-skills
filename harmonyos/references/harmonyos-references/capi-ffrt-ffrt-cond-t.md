---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-cond-t
title: ffrt_cond_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_cond_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:86cdedb4c3d0c4a51ca26477762b439b33833a945243ab6fbff4bccb4dd9d73f
---

```c
typedef struct {...} ffrt_cond_t
```

## 概述

条件变量结构体，用于存储条件变量的内部数据。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_cond\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 条件变量的内部存储。请勿直接访问，通过ffrt\_cond\_\*等接口管理。 |
