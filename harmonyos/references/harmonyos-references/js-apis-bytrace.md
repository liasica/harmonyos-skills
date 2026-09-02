---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace
title: "@ohos.bytrace (性能打点)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > 已停止维护的接口 > @ohos.bytrace (性能打点)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6b4cd4d40aab356cbe37d34ea86447abe7f8150226c15f79d5529ca6c8842dcc
---

本模块提供了追踪进程轨迹的能力，用于应用性能分析场景。开发者可以通过性能打点来追踪关键代码段的执行时间，定位性能瓶颈，优化应用性能。适用于应用启动耗时分析、业务流程性能监控、帧率分析等场景。

**说明** 

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口从API version 8开始废弃，建议使用新接口[@ohos.hiTraceMeter](js-apis-hitracemeter.md)替代。

## 导入模块

```ts
import { bytrace } from '@kit.PerformanceAnalysisKit';
```

## bytrace.startTrace

startTrace(name: string, taskId: number, expectedTime?: number): void

标记一个时间片跟踪任务的开始。

**说明** 

* 如果有多个相同name的任务需要追踪或者对同一个任务要追踪多次，并且这些跟踪任务会同时被执行，则每次调用startTrace的taskId必须不一致。如果具有相同name的跟踪任务是串行执行的，则taskId可以相同。在下面bytrace.finishTrace的示例中会举例说明。
* 从API version 7开始支持，从API version 8开始废弃。建议使用[startTrace](js-apis-hitracemeter.md#hitracemeterstarttrace)替代。

**系统能力**： SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 时间片跟踪任务名称。 |
| taskId | number | 是 | 时间片跟踪任务id。 |
| expectedTime | number | 否 | 期望的耗时时间（单位：ms）。设置该值后，系统会在实际执行时间超过期望值时产生性能警告。可选，默认为空表示不产生警告。 |

**示例：**

```ts
bytrace.startTrace("myTestFunc", 1);
bytrace.startTrace("myTestFunc", 1, 5); // 从startTrace到finishTrace流程的期望耗时为5ms
```

## bytrace.finishTrace

finishTrace(name: string, taskId: number): void

标记一个时间片跟踪事件的结束。

**说明** 

* finishTrace的name和taskId必须与流程开始的startTrace对应参数值一致。
* 从API version 7开始支持，从API version 8开始废弃。建议使用[finishTrace](js-apis-hitracemeter.md#hitracemeterfinishtrace)替代。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 时间片跟踪任务名称，必须与startTrace调用时的name参数值一致。 |
| taskId | number | 是 | 时间片跟踪任务id，必须与startTrace调用时的taskId参数值一致。 |

**示例：**

```ts
bytrace.finishTrace("myTestFunc", 1);
```

```ts
// 跟踪并行执行的同名任务
bytrace.startTrace("myTestFunc", 1);
// 业务流程......
bytrace.startTrace("myTestFunc", 2);  // 第二个跟踪任务开始，同时第一个同名跟踪任务还没结束，出现了并行执行，对应接口的taskId需要不同
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);
// 业务流程......
bytrace.finishTrace("myTestFunc", 2);
```

```ts
// 跟踪串行执行的同名任务
bytrace.startTrace("myTestFunc", 1);
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);  // 第一个跟踪任务结束
// 业务流程......
bytrace.startTrace("myTestFunc", 1);   // 第二个跟踪任务开始，同名跟踪任务串行执行
// 业务流程......
bytrace.finishTrace("myTestFunc", 1);
```

## bytrace.traceByValue

traceByValue(name: string, count: number): void

标记预追踪耗时任务的数值变量，该变量的数值会不断变化。traceByValue可独立使用，用于记录某个数值变量的变化轨迹。

**说明** 

从API version 7开始支持，从API version 8开始废弃。建议使用[traceByValue](js-apis-hitracemeter.md#hitracemetertracebyvalue)替代。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数值变量的名称。 |
| count | number | 是 | 数值变量的值。 |

**示例：**

```ts
let traceCount = 3;
bytrace.traceByValue("myTestCount", traceCount);
traceCount = 4;
bytrace.traceByValue("myTestCount", traceCount);
// 业务流程......
```
