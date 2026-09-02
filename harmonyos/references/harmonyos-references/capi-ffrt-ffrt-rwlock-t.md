---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-rwlock-t
title: ffrt_rwlock_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_rwlock_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d7d9e0335e0185e645923510ba8eb5f435b4ba8dacfb39c93a4c2d2df502d25
---

```c
typedef struct {...} ffrt_rwlock_t
```

## 概述

读写锁结构体，用于存储读写锁的内部数据。

**起始版本：** 18

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_rwlock\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 读写锁的内部存储。请勿直接访问，通过ffrt\_rwlock\_\*等接口管理。 |
