---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-task-attr-t
title: ffrt_task_attr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_task_attr_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:08+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7d5c11127408fefacf88581c9b80ecbf0dc4ae5b6c17dc6408913094020289ca
---

```
1. typedef struct {...} ffrt_task_attr_t
```

## 概述

PhonePC/2in1TabletTVWearable

并行任务属性结构。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t storage[(ffrt\_task\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)] | 任务属性占用空间 |
