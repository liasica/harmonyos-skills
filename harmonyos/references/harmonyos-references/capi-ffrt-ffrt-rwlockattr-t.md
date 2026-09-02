---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-rwlockattr-t
title: ffrt_rwlockattr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_rwlockattr_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44f77cee463e5b28a193b3692b2df4c7780a07314c8ce30d26d33766693757dc
---

```c
typedef struct {...} ffrt_rwlockattr_t
```

## 概述

读写锁属性结构体，用于存储读写锁的属性信息。

**起始版本：** 18

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| long storage | 读写锁属性的内部存储。请勿直接访问，直接访问可能导致读写锁属性失效。 |
