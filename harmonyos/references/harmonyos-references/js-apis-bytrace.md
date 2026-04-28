---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace
title: @ohos.bytrace (性能打点)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > 已停止维护的接口 > @ohos.bytrace (性能打点)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5b337ff99e5623d1a1340e14be90dadd9ac2ef714d3a88be02eb4cc747805658
---

本模块提供了追踪进程轨迹。

说明

* 本模块接口从API Version 8开始废弃，建议使用新接口[@ohos.hiTraceMeter](js-apis-hitracemeter.md)替代。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bytrace } from '@kit.PerformanceAnalysisKit';
```

## bytrace.startTrace

PhonePC/2in1TabletTVWearable

startTrace(name: string, taskId: number, expectedTime?: number): void

标记一个时间片跟踪任务的开始。

说明

如果有多个相同name的任务需要追踪或者对同一个任务要追踪多次，并且这些跟踪任务会同时被执行，则每次调用startTrace的taskId必须不一致。如果具有相同name的跟踪任务是串行执行的，则taskId可以相同。在下面bytrace.finishTrace的示例中会举例说明。

**系统能力**： SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 时间片跟踪任务名称。 |
| taskId | number | 是 | 时间片跟踪任务id。 |
| expectedTime | number | 否 | 期望的耗时时间（单位：ms）。可选，默认为空。 |

**示例：**

```
1. bytrace.startTrace("myTestFunc", 1);
2. bytrace.startTrace("myTestFunc", 1, 5); // 从startTrace到finishTrace流程的期望耗时为5ms
```

## bytrace.finishTrace

PhonePC/2in1TabletTVWearable

finishTrace(name: string, taskId: number): void

标记一个时间片跟踪事件的结束。

说明

finishTrace的name和taskId必须与流程开始的startTrace对应参数值一致。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 时间片跟踪任务名称。 |
| taskId | number | 是 | 时间片跟踪任务id。 |

**示例：**

```
1. bytrace.finishTrace("myTestFunc", 1);
```

```
1. // 跟踪并行执行的同名任务
2. bytrace.startTrace("myTestFunc", 1);
3. // 业务流程......
4. bytrace.startTrace("myTestFunc", 2);  // 第二个跟踪任务开始，同时第一个同名跟踪任务还没结束，出现了并行执行，对应接口的taskId需要不同
5. // 业务流程......
6. bytrace.finishTrace("myTestFunc", 1);
7. // 业务流程......
8. bytrace.finishTrace("myTestFunc", 2);
```

```
1. // 跟踪串行执行的同名任务
2. bytrace.startTrace("myTestFunc", 1);
3. // 业务流程......
4. bytrace.finishTrace("myTestFunc", 1);  // 第一个跟踪任务结束
5. // 业务流程......
6. bytrace.startTrace("myTestFunc", 1);   // 第二个跟踪任务开始，同名跟踪任务串行执行
7. // 业务流程......
8. bytrace.finishTrace("myTestFunc", 1);
```

## bytrace.traceByValue

PhonePC/2in1TabletTVWearable

traceByValue(name: string, count: number): void

标记预追踪耗时任务的数值变量，该变量的数值会不断变化。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数值变量的名称。 |
| count | number | 是 | 数值变量的值 |

**示例：**

```
1. let traceCount = 3;
2. bytrace.traceByValue("myTestCount", traceCount);
3. traceCount = 4;
4. bytrace.traceByValue("myTestCount", traceCount);
5. // 业务流程......
```
