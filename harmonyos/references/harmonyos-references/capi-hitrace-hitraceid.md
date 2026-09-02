---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid
title: HiTraceId
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiTraceId
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4cc91f861538964019906ec294ef56485a2c5371bd6fcf22778302effd5a4ff
---

```c
typedef struct HiTraceId {...} HiTraceId
```

## 概述

用于标识调用链的结构体。

使用场景：

* 跨服务调用追踪：在分布式系统中，用于标识和关联同一业务请求在不同服务间的调用链路。
* 性能分析：配合HiTrace链路追踪功能，分析应用性能瓶颈和调用耗时。
* 日志关联：在日志系统中，通过HiTraceId将同一请求的不同阶段日志关联起来，便于问题排查。
* 调用链可视化：通过HiTraceId实现端到端的调用链路可视化，帮助理解系统行为。

**起始版本：** 12

**相关模块：** [HiTrace](capi-hitrace.md)

**所在头文件：** [trace.h](capi-trace-h.md)

## 汇总

### 成员变量

如果字节序为小端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64\_t valid | 1 | HiTraceId是否有效，1表示有效，0表示无效。用于判断HiTraceId结构体是否包含有效的跟踪信息。 |
| uint64\_t ver | 3 | HiTraceId的版本号，用于标识HiTraceId结构体的版本。不同版本可能有不同的字段布局或功能特性。 |
| uint64\_t chainId | 60 | HiTraceId的跟踪链标识，用于唯一标识跨进程/跨设备的调用链。在整个分布式跟踪过程中保持不变，用于关联同一业务流程的所有跟踪信息。 |
| uint64\_t flags | 12 | HiTraceId的跟踪标志位，用于指定跟踪选项或特性。不同的标志位组合可以控制跟踪的详细程度和行为。 |
| uint64\_t spanId | 26 | HiTraceId的分支标识，用于标识调用链中的当前调用节点。每次创建新的分支时会生成新的spanId，用于构建调用树结构。 |
| uint64\_t parentSpanId | 26 | HiTraceId的父分支标识，用于标识调用链中当前节点的父节点。通过parentSpanId可以追溯调用的来源，实现调用链的层级关系。 |

如果字节序为大端模式，结构体顺序如下表所示：

| 字段 | 字段bit数 | 描述 |
| --- | --- | --- |
| uint64\_t chainId | 60 | HiTraceId的跟踪链标识，用于唯一标识跨进程/跨设备的调用链。在整个分布式跟踪过程中保持不变，用于关联同一业务流程的所有跟踪信息。 |
| uint64\_t ver | 3 | HiTraceId的版本号，用于标识HiTraceId结构体的版本。不同版本可能有不同的字段布局或功能特性。 |
| uint64\_t valid | 1 | HiTraceId是否有效，1表示有效，0表示无效。用于判断HiTraceId结构体是否包含有效的跟踪信息。 |
| uint64\_t parentSpanId | 26 | HiTraceId的父分支标识，用于标识调用链中当前节点的父节点。通过parentSpanId可以追溯调用的来源，实现调用链的层级关系。 |
| uint64\_t spanId | 26 | HiTraceId的分支标识，用于标识调用链中的当前调用节点。每次创建新的分支时会生成新的spanId，用于构建调用树结构。 |
| uint64\_t flags | 12 | HiTraceId的跟踪标志位，用于指定跟踪选项或特性。不同的标志位组合可以控制跟踪的详细程度和行为。 |
