---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter
title: "@ohos.hiTraceMeter (性能打点)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiTraceMeter (性能打点)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:562f080bd45e6a06f16099e71c0eb6811498cfd1ae749b8b8fb9258c652bd7b3
---

本模块提供了跟踪进程轨迹，度量程序执行性能的打点能力，支持异步耗时任务跟踪、同步耗时任务跟踪、整数变量跟踪等多种性能分析场景。本模块打点的数据供HiTraceMeter工具分析使用，能够帮助开发者快速定位性能瓶颈，优化应用性能。

详细开发流程请参考：[使用HiTraceMeter跟踪性能（ArkTS）](../harmonyos-guides/hitracemeter-guidelines-arkts.md)。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 建议使用API version 19的性能打点接口，后续性能打点接口[startTrace()](js-apis-hitracemeter.md#hitracemeterstarttrace)、[finishTrace()](js-apis-hitracemeter.md#hitracemeterfinishtrace)、[traceByValue()](js-apis-hitracemeter.md#hitracemetertracebyvalue)将逐步废弃。
* 性能打点接口[startTrace()](js-apis-hitracemeter.md#hitracemeterstarttrace)、[finishTrace()](js-apis-hitracemeter.md#hitracemeterfinishtrace)、[traceByValue()](js-apis-hitracemeter.md#hitracemetertracebyvalue)固定使用COMMERCIAL级别。
* [用户态trace格式](../harmonyos-guides/hitracemeter-view.md#用户态trace格式说明)使用竖线 | 作为分隔符，所以通过性能打点接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。
* [用户态trace](../harmonyos-guides/hitracemeter-view.md#用户态trace格式说明)总长度限制512字符，超过的部分将会被截断。

## 导入模块

```js
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
```

## hiTraceMeter.startTrace

startTrace(name: string, taskId: number): void

标记一个异步跟踪耗时任务的开始。调用成功后，创建一条异步跟踪记录。

**说明** 

* 必须与finishTrace()方法配合使用。
* 调用finishTrace()时，name和taskId参数必须与startTrace()完全一致。
* 对于多个同名任务，如果并行执行则需要使用不同的taskId，以区分不同的任务。

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startTrace传入的taskId需不同。

如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishTrace()](js-apis-hitracemeter.md#hitracemeterfinishtrace)中的示例。

从API version 19开始，建议使用[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)接口（需与[finishAsyncTrace()](js-apis-hitracemeter.md#hitracemeterfinishasynctrace19)接口配套使用），以便分级控制跟踪输出与跟踪聚类。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要跟踪的任务名称。  由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议该参数的长度不要超过420Byte。 |
| taskId | number | 是 | 任务id。  用来区分具有相同名称的多个不同的任务，需确保并发执行的同名任务之间的任务id具有唯一性。 |

**示例：**

```js
hiTraceMeter.startTrace("myTestFunc", 1);  // 开始异步跟踪任务
```

## hiTraceMeter.finishTrace

finishTrace(name: string, taskId: number): void

标记一个异步跟踪耗时任务的结束。调用成功后，完成该任务的跟踪。

**说明** 

* finishTrace的name和taskId必须与流程开始的[startTrace()](js-apis-hitracemeter.md#hitracemeterstarttrace)对应参数值一致。
* 从API version 19开始，建议使用[finishAsyncTrace()](js-apis-hitracemeter.md#hitracemeterfinishasynctrace19)接口（需与[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)接口配套使用）。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要跟踪的任务名称，必须与流程开始的[startTrace()](js-apis-hitracemeter.md#hitracemeterstarttrace)对应参数值一致。 |
| taskId | number | 是 | 任务id，必须与流程开始的[startTrace()](js-apis-hitracemeter.md#hitracemeterstarttrace)对应参数值一致。 |

**示例：**

```js
// 跟踪并行执行的同名任务
hiTraceMeter.startTrace("myTestFunc", 1);
// 业务流程......
hiTraceMeter.startTrace("myTestFunc", 2);  // 第二个跟踪的任务开始，同时第一个跟踪的同名任务还没结束，出现了并行执行，需要不同的taskId来区分不同的任务。
// 业务流程......
hiTraceMeter.finishTrace("myTestFunc", 1);
// 业务流程......
hiTraceMeter.finishTrace("myTestFunc", 2);
```

```js
// 跟踪串行执行的同名任务
hiTraceMeter.startTrace("myTestFunc", 1);
// 业务流程......
hiTraceMeter.finishTrace("myTestFunc", 1);  // 第一个跟踪的任务结束
// 业务流程......
hiTraceMeter.startTrace("myTestFunc", 1);   // 第二个跟踪的同名任务开始，同名的待跟踪任务串行执行。
// 业务流程......
hiTraceMeter.finishTrace("myTestFunc", 1);
```

## hiTraceMeter.traceByValue

traceByValue(name: string, count: number): void

用来标记一个跟踪的整数变量，该变量的数值会不断变化。适用于需要实时监控数值变化（如网络请求次数、缓存命中率、内存占用等）的场景，能够帮助开发者快速发现异常波动，分析数据趋势。

**说明** 

从API version 19开始，建议使用[traceByValue19+()](js-apis-hitracemeter.md#hitracemetertracebyvalue19)接口，以便分级控制跟踪输出。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要跟踪的整数变量名称。  由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议该参数的长度不要超过420Byte。 |
| count | number | 是 | 整数变量的值。 |

**示例：**

```js
let traceCount = 3;  // 定义要跟踪的整数变量初始值
hiTraceMeter.traceByValue("myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue("myTestCount", traceCount);  // 当myTestCount发生变化时，记录新值。
// 业务流程......
```

## HiTraceOutputLevel19+

枚举，跟踪输出级别。

**说明** 

低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为INFO；nolog版本阈值为COMMERCIAL。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEBUG | 0 | 仅用于调试的输出级别，优先级最低。低于系统跟踪输出级别阈值时打点不会生效。 |
| INFO | 1 | 用于log版本的输出级别，log版本阈值为INFO。 |
| CRITICAL | 2 | 用于log版本的输出级别，优先级高于INFO，用于需要重点关注的trace事件。 |
| COMMERCIAL | 3 | 用于nolog版本的输出级别，优先级最高。nolog版本阈值为COMMERCIAL。 |
| MAX | COMMERCIAL | 输出级别范围限制，MAX = COMMERCIAL。 |

## hiTraceMeter.startAsyncTrace19+

startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string, customArgs?: string): void

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。

**说明** 

如果有多个相同name的任务需要跟踪或者对同一个任务要跟踪多次，并且任务同时被执行，则开发者每次调用startAsyncTrace传入的taskId需不同。如果具有相同name的任务是串行执行的，则taskId可以相同。具体示例可参考[finishAsyncTrace()](js-apis-hitracemeter.md#hitracemeterfinishasynctrace19)中的示例。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](js-apis-hitracemeter.md#hitraceoutputlevel19) | 是 | 跟踪输出级别。 |
| name | string | 是 | 要跟踪的任务名称。  由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name、customCategory、customArgs的长度之和不要超过420Byte。 |
| taskId | number | 是 | 任务id。  用来区分具有相同名称的多个不同的任务，需确保并发执行的同名任务之间的任务id具有唯一性。 |
| customCategory | string | 是 | 自定义聚类名称，用于聚合同一类异步跟踪打点。  由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name、customCategory、customArgs的长度之和不要超过420Byte。 |
| customArgs | string | 否 | 自定义键值对，格式key=value，多个键值对用逗号分隔，用于记录额外的业务信息或调试信息（如记录用户ID、操作类型等）。当需要附加自定义数据用于trace分析时传入此参数，不需要附加数据时不传入即可。默认值为空字符串。由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name、customCategory、customArgs的长度之和不要超过420Byte。 |

**示例：**

```js
// 不需要customCategory参数时，可传入空字符串
// 不需要customArgs参数时，可不传入该参数或传入空字符串
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "", "");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 2, "");
// 多个键值对用逗号分隔
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 3, "categoryTest", "key1=value");
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 4, "categoryTest", "key1=value1,key2=value2");
```

## hiTraceMeter.finishAsyncTrace19+

finishAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number): void

标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。

**说明** 

finishAsyncTrace的level、name和taskId必须与流程开始的[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)对应参数值一致。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](js-apis-hitracemeter.md#hitraceoutputlevel19) | 是 | 跟踪输出级别，必须与流程开始的[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)的level参数值一致。 |
| name | string | 是 | 要跟踪的任务名称，必须与流程开始的[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)的name参数值一致。 |
| taskId | number | 是 | 任务id，必须与流程开始的[startAsyncTrace()](js-apis-hitracemeter.md#hitracemeterstartasynctrace19)的taskId参数值一致。 |

**示例：**

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
hiTraceMeter.finishAsyncTrace(COMMERCIAL, "myTestFunc", 1);
```

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// 跟踪并行执行的同名任务
// 第一个跟踪的任务开始
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "categoryTest", "key=value");
// 业务流程......
// 第二个跟踪的任务开始，同时第一个跟踪的同名任务还没结束，出现了并行执行，对应接口的taskId需要不同
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 2, "categoryTest", "key=value");
// 业务流程......
// 第一个跟踪的任务结束
hiTraceMeter.finishAsyncTrace(COMMERCIAL, "myTestFunc", 1);
// 业务流程......
// 第二个跟踪的任务结束
hiTraceMeter.finishAsyncTrace(COMMERCIAL, "myTestFunc", 2);
```

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// 跟踪串行执行的同名任务
// 第一个跟踪的任务开始
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "categoryTest", "key=value");
// 业务流程......
// 第一个跟踪的任务结束
hiTraceMeter.finishAsyncTrace(COMMERCIAL, "myTestFunc", 1);
// 业务流程......
// 第二个跟踪的同名任务开始，同名的待跟踪任务串行执行
hiTraceMeter.startAsyncTrace(COMMERCIAL, "myTestFunc", 1, "categoryTest", "key=value");
// 业务流程......
// 第二个跟踪的同名任务结束
hiTraceMeter.finishAsyncTrace(COMMERCIAL, "myTestFunc", 1);
```

## hiTraceMeter.startSyncTrace19+

startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void

标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。

**说明** 

适用于需要跟踪同步代码块执行耗时的场景，能够帮助开发者定位同步操作的耗时问题，优化应用响应速度。具体示例可参考[finishSyncTrace()](js-apis-hitracemeter.md#hitracemeterfinishsynctrace19)中的示例。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](js-apis-hitracemeter.md#hitraceoutputlevel19) | 是 | 跟踪输出级别。 |
| name | string | 是 | 要跟踪的任务名称。  由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name和customArgs的总长度不要超过420Byte。 |
| customArgs | string | 否 | 键值对，格式key=value，多个键值对用逗号分隔，用于记录额外的业务信息或调试信息（如记录函数参数、返回值等）。当需要附加自定义数据用于同步跟踪的trace分析时传入此参数，不需要附加数据时不传入即可。默认值为空字符串。由于单条trace记录的总长度限制为512Byte，超过的部分将会被截断，建议name和customArgs的总长度不要超过420Byte。 |

**示例：**

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// 不需要customArgs参数时，可不传入该参数或传入空字符串
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "");
// 多个键值对用逗号分隔
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key=value");
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc", "key1=value1,key2=value2");
```

## hiTraceMeter.finishSyncTrace19+

finishSyncTrace(level: HiTraceOutputLevel): void

标记一个同步跟踪耗时任务的结束，分级控制跟踪输出。

**说明** 

finishSyncTrace的level必须与流程开始的[startSyncTrace()](js-apis-hitracemeter.md#hitracemeterstartsynctrace19)对应参数值一致。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](js-apis-hitracemeter.md#hitraceoutputlevel19) | 是 | 跟踪输出级别。 |

**示例：**

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
hiTraceMeter.finishSyncTrace(COMMERCIAL);
```

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
// 可嵌套使用，相邻的startSyncTrace与finishSyncTrace匹配
// 第一个跟踪的任务开始
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc1", "key=value");
// 业务流程......
// 第二个跟踪的任务开始
hiTraceMeter.startSyncTrace(COMMERCIAL, "myTestFunc2", "key=value");
// 业务流程......
// 第二个跟踪的任务结束
hiTraceMeter.finishSyncTrace(COMMERCIAL);
// 业务流程......
// 第一个跟踪的任务结束
hiTraceMeter.finishSyncTrace(COMMERCIAL);
```

## hiTraceMeter.traceByValue19+

traceByValue(level: HiTraceOutputLevel, name: string, count: number): void

整数跟踪事件，分级控制跟踪输出。用来标记一个预先定义需要跟踪的整数变量名及整数值。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [HiTraceOutputLevel](js-apis-hitracemeter.md#hitraceoutputlevel19) | 是 | 跟踪输出级别。 |
| name | string | 是 | 要跟踪的整数变量名称。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议该参数的长度不要超过420Byte。 |
| count | number | 是 | 整数变量的值。 |

**示例：**

```js
const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
let traceCount = 3;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
traceCount = 4;
hiTraceMeter.traceByValue(COMMERCIAL, "myTestCount", traceCount);
// 业务流程......
```

## hiTraceMeter.isTraceEnabled19+

isTraceEnabled(): boolean

判断当前是否开启应用trace捕获。

**元服务API**：从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 使用[hitrace](../harmonyos-guides/hitrace.md)命令行工具等方式开启采集时返回true。未开启采集或停止采集后返回false，此时调用HiTraceMeter性能跟踪打点接口无效。 |

**示例：**

```js
if (hiTraceMeter.isTraceEnabled()) {
  // 业务流程......
} else {
  // 业务流程......
}
```

## TraceEventListener22+

type TraceEventListener = (traceStatus: boolean) => void

定义应用trace捕获开关状态切换时的回调函数类型。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| traceStatus | boolean | 是 | 当前应用trace捕获开关状态。  true：开启；false：关闭。 |

## hiTraceMeter.registerTraceListener22+

registerTraceListener(callback: TraceEventListener): number

注册应用trace捕获开关通知回调，使用callback异步回调。

**说明** 

* 注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。
* 回调函数保存在应用进程内，一个进程最多可以注册10个回调函数。
* 若注册的回调包含耗时操作，当回调被执行时，注册或注销行为会被阻塞（等待回调执行完成）。因此，建议不要在应用主线程中注册或注销包含耗时操作的回调，避免发生应用冻屏。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TraceEventListener](js-apis-hitracemeter.md#traceeventlistener22) | 是 | 注册的回调函数，用于监听应用trace捕获开关状态变化。当trace捕获开关状态发生变化时（从开启变为关闭或从关闭变为开启），会触发此回调并传入当前的trace状态。注册成功后会立即执行一次回调，后续每次trace捕获开关状态变化都会触发回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 回调注册状态。  >= 0：注册成功，返回用于注销的回调索引，索引范围[0, 9]；  -1：已达到最大回调函数注册数量；  -2：无效参数，参数非TraceEventListener类型。 |

**示例：**

```js
// 注册的回调函数定义
let callback: hiTraceMeter.TraceEventListener = (traceStatus: boolean) => {
  if (traceStatus) {
    // 当前应用trace捕获开启
    // ...
  } else {
    // 当前应用trace捕获关闭
    // ...
  }
};

// 注册应用trace捕获开关通知回调
let index = hiTraceMeter.registerTraceListener(callback);
if (index < 0) {
  // 异常处理......
}
```

## hiTraceMeter.unregisterTraceListener22+

unregisterTraceListener(index: number): number

注销通过registerTraceListener()注册的trace捕获开关通知回调函数。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 已注册回调函数索引，取值范围[0, 9]，即[registerTraceListener()](js-apis-hitracemeter.md#hitracemeterregistertracelistener22)调用成功时的返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 回调注销状态。  0：注销成功；  -1：目标索引的回调函数未注册；  -2：无效索引，参数index值不在[0, 9]范围内。 |

**示例：**

```js
// 注销应用trace捕获开关通知回调，index为hiTraceMeter.registerTraceListener返回的回调索引
let ret = hiTraceMeter.unregisterTraceListener(index);
if (ret < 0) {
  // 异常处理......
}
```
