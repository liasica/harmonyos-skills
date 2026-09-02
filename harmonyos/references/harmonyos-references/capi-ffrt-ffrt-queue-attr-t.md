---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-queue-attr-t
title: ffrt_queue_attr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_queue_attr_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:082d73004a06afb165080fef89c513de8b205965b73d65b74babdcd52631eda6
---

```c
typedef struct {...} ffrt_queue_attr_t
```

## 概述

队列属性结构体，用于存储队列的属性信息。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_queue\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 队列属性的内部存储。请勿直接访问，通过[ffrt\_queue\_attr\_init](capi-queue-h.md#ffrt_queue_attr_init)和ffrt\_queue\_attr\_set\_\*等接口管理内容。 |
