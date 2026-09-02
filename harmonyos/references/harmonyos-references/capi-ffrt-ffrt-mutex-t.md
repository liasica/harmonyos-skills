---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t
title: ffrt_mutex_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_mutex_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ef3fd93441102f689cdfe73f56eb4e73bd9f9da27a6dc5a509bce7774d6f7be9
---

```c
typedef struct {...} ffrt_mutex_t
```

## 概述

互斥锁结构体，用于存储互斥锁的内部数据。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_mutex\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 互斥锁的内部存储。请勿直接访问，通过ffrt\_mutex\_\*等接口管理。 |
