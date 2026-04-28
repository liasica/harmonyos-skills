---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t
title: ffrt_fiber_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_fiber_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:11+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5e2590bac638e02e7e827acd0e789428f30141f0dbaa1bf01315d1e916a6233b
---

```
1. typedef struct {...} ffrt_fiber_t
```

## 概述

PhonePC/2in1TabletTVWearable

纤程结构。

**起始版本：** 20

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uintptr\_t storage[ffrt\_fiber\_storage\_size] | 纤程上下文占用空间。 |
