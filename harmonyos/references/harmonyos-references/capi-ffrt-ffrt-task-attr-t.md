---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-task-attr-t
title: ffrt_task_attr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_task_attr_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5dd76c28a211057b1247ac8df360ce5a1a728d6a02ba2cb085ccd2f42e8bc9be
---

```c
typedef struct {...} ffrt_task_attr_t
```

## 概述

任务属性结构体，用于存储任务的属性信息。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_task\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 任务属性的内部存储。请勿直接访问，通过[ffrt\_task\_attr\_init](capi-task-h.md#ffrt_task_attr_init)和ffrt\_task\_attr\_set\_\*等接口管理内容。 |
