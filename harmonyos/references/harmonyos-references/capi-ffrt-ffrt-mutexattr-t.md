---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t
title: ffrt_mutexattr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_mutexattr_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:07371756613cc5d667bfaed50f2ea99637fe6b2bb674f6afedb4dcbeb5bd14b1
---

```c
typedef struct {...} ffrt_mutexattr_t
```

## 概述

互斥锁属性结构体，用于存储互斥锁的属性信息。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| long storage | 互斥锁属性的内部存储。请勿直接访问，通过[ffrt\_mutexattr\_init](capi-mutex-h.md#ffrt_mutexattr_init)初始化。 |
