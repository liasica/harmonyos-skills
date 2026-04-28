---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage
title: HiDebug_ThreadCpuUsage
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiDebug_ThreadCpuUsage
category: harmonyos-references
scraped_at: 2026-04-28T08:11:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8f5838c40e79ea0c34f11d909330ba1437754f6f7475dfb7e47652eb7f8e1b95
---

```
1. typedef struct HiDebug_ThreadCpuUsage {...} HiDebug_ThreadCpuUsage
```

## 概述

PhonePC/2in1TabletTVWearable

应用程序所有线程的CPU使用率结构体定义。

**起始版本：** 12

**相关模块：** [HiDebug](capi-hidebug.md)

**所在头文件：** [hidebug\_type.h](capi-hidebug-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t threadId | 线程ID。 |
| double cpuUsage | 线程CPU使用率百分比。 |
| struct [HiDebug\_ThreadCpuUsage](capi-hidebug-hidebug-threadcpuusage.md) \*next | 下一个线程的使用率信息。 |
