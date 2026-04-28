---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid
title: HiTraceId
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiTraceId
category: harmonyos-references
scraped_at: 2026-04-28T08:11:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28f654d096686c93fb9381edec14a2783af28be7eafdab1edfeccfe462d6c8d4
---

```
1. typedef struct HiTraceId {...} HiTraceId
```

## 概述

PhonePC/2in1TabletTVWearable

HiTraceId定义。

**起始版本：** 12

**相关模块：** [HiTrace](capi-hitrace.md)

**所在头文件：** [trace.h](capi-trace-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

如果字节序为小端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64\_t valid | 1 | HiTraceId是否有效。 |
| uint64\_t ver | 3 | HiTraceId的版本号。 |
| uint64\_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64\_t flags | 12 | HiTraceId的跟踪标志位。 |
| uint64\_t spanId | 26 | HiTraceId的分支标识。 |
| uint64\_t parentSpanId | 26 | HiTraceId的父分支标识。 |

如果字节序为大端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64\_t chainId | 60 | HiTraceId的跟踪链标识。 |
| uint64\_t ver | 3 | HiTraceId的版本号。 |
| uint64\_t valid | 1 | HiTraceId是否有效。 |
| uint64\_t parentSpanId | 26 | HiTraceId的父分支标识。 |
| uint64\_t spanId | 26 | HiTraceId的分支标识。 |
| uint64\_t flags | 12 | HiTraceId的跟踪标志位。 |
