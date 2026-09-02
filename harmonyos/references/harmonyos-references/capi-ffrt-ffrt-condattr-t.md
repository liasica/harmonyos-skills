---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-condattr-t
title: ffrt_condattr_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > C API > 结构体 > ffrt_condattr_t
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:21136b1ded750a7aa141efc8d88c2ed48a01b2c1b4f61a79f01b06810cd6f588
---

```c
typedef struct {...} ffrt_condattr_t
```

## 概述

条件变量属性结构体，用于存储条件变量的属性信息。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| long storage | 条件变量属性的内部存储。请勿直接访问。 |
