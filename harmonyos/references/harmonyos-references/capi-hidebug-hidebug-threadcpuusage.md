---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage
title: HiDebug_ThreadCpuUsage
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_ThreadCpuUsage
category: harmonyos-references
scraped_at: 2026-09-02T15:02:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f4761342aa86fb49ceeac226c90a98d22e3c11f7f75b4b680d7dd1586e6cdc5a
---

```c
typedef struct HiDebug_ThreadCpuUsage {...} HiDebug_ThreadCpuUsage
```

## 概述

当前进程所有线程的CPU使用率结构体定义。

使用场景：

应用性能监控：获取线程CPU使用率，监控应用的运行状态和性能瓶颈。

线程性能优化：分析各线程的CPU占用情况，优化线程调度和资源分配。

系统调试：在调试阶段追踪线程的CPU使用情况，定位性能问题。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t threadId | 线程ID。 |
| double cpuUsage | 线程CPU使用率百分比。 |
| struct [HiDebug\_ThreadCpuUsage](capi-hidebug-hidebug-threadcpuusage.md) \*next | 下一个线程的使用率信息。 |
