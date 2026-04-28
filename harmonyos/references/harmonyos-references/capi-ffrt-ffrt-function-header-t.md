---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-function-header-t
title: ffrt_function_header_t
breadcrumb: API参考 > 系统 > 基础功能 > Function Flow Runtime Kit > C API > 结构体 > ffrt_function_header_t
category: harmonyos-references
scraped_at: 2026-04-28T08:10:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d5f13c7c6834ce8d5cdf18c56b205bc0dd29f02e51708eac8989228bb7ea811f
---

```
1. typedef struct {...} ffrt_function_header_t
```

## 概述

PhonePC/2in1TabletTVWearable

任务执行体。

**起始版本：** 10

**相关模块：** [FFRT](capi-ffrt.md)

**所在头文件：** [type\_def.h](capi-type-def-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) exec | 任务执行函数 |
| [ffrt\_function\_t](capi-type-def-h.md#ffrt_function_t) destroy | 任务销毁函数 |
| uint64\_t reserve[2] | 保留位需要设置为0 |
