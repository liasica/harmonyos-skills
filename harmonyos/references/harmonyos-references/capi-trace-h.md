---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trace-h
title: trace.h
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 头文件 > trace.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59d36927727704a22d7720d03398f149624bc97775301ae8a621e358b9248eda
---

## 概述

HiTraceMeter和HiTraceChain模块接口定义，通过这些接口实现性能打点和分布式跟踪功能。支持应用性能分析、跨服务调用链追踪、性能瓶颈定位等场景，能够解决分布式系统中调用链路难以追踪、性能问题难以定位的问题，提升系统可观测性和问题排查效率。性能打点通过在代码关键位置插入标记，记录函数执行时间；分布式跟踪通过HiTraceId实现跨线程、跨进程、跨设备的调用链追踪。

**说明** 

调用HiTraceMeter打点接口时，模块将依据[用户态trace格式](../harmonyos-guides/hitracemeter-view.md#用户态trace格式说明)对传入参数格式化、封装，生成单条Trace日志并写入内核。

* 由于内核侧单条Trace日志最大长度限制为512Byte，且接口内部封装开销需预留92Byte，为保证日志数据完整可靠，业务接入时需自行控制入参整体长度不超出420Byte（总长度512Byte - 系统预留92Byte）。
* 由于接口内部格式化流程以“|”作为内容分隔标识符，为避免日志解析错乱、数据异常，用户传入的所有文本参数中禁止包含该字符。

**引用文件：** <hitrace/trace.h>

**库：** libhitrace\_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

**相关模块：** [HiTrace](capi-hitrace.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) | HiTraceId | 用于标识调用链的结构体。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [HiTraceId\_Valid](capi-trace-h.md#hitraceid_valid) | HiTraceId\_Valid | HiTraceId是否有效标志。 |
| [HiTrace\_Version](capi-trace-h.md#hitrace_version) | HiTrace\_Version | HiTrace版本号。 |
| [HiTrace\_Flag](capi-trace-h.md#hitrace_flag) | HiTrace\_Flag | HiTrace跟踪标志。 |
| [HiTrace\_Tracepoint\_Type](capi-trace-h.md#hitrace_tracepoint_type) | HiTrace\_Tracepoint\_Type | 跟踪埋点类型枚举。 |
| [HiTrace\_Communication\_Mode](capi-trace-h.md#hitrace_communication_mode) | HiTrace\_Communication\_Mode | 跟踪通信类型枚举。 |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) | HiTrace\_Output\_Level | HiTrace输出级别。低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为[HITRACE\_LEVEL\_INFO](capi-trace-h.md#hitrace_output_level)；nolog版本阈值为[HITRACE\_LEVEL\_COMMERCIAL](capi-trace-h.md#hitrace_output_level)。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_HiTrace\_TraceEventListener)(bool traceStatus)](capi-trace-h.md#oh_hitrace_traceeventlistener) | OH\_HiTrace\_TraceEventListener | 定义应用trace捕获开关状态切换时的回调函数类型。 |
| [HiTraceId OH\_HiTrace\_BeginChain(const char \*name, int flags)](capi-trace-h.md#oh_hitrace_beginchain) | - | 开始跟踪。  当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId；当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。 |
| [void OH\_HiTrace\_EndChain()](capi-trace-h.md#oh_hitrace_endchain) | - | 结束跟踪。  结束跟踪并将当前线程TLS中的HiTraceId设置为无效。 |
| [HiTraceId OH\_HiTrace\_GetId()](capi-trace-h.md#oh_hitrace_getid) | - | 获取跟踪标识。  获取当前线程TLS中的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| [void OH\_HiTrace\_SetId(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_setid) | - | 设置跟踪标识。  将给定的[HiTraceId](capi-hitrace-hitraceid.md)设置到当前线程TLS中。若传入的参数无效，则不执行任何操作。 |
| [void OH\_HiTrace\_ClearId(void)](capi-trace-h.md#oh_hitrace_clearid) | - | 清除跟踪标识。  将当前线程TLS中的[HiTraceId](capi-hitrace-hitraceid.md)设置为无效。 |
| [HiTraceId OH\_HiTrace\_CreateSpan(void)](capi-trace-h.md#oh_hitrace_createspan) | - | 创建跟踪分支。  创建一个[HiTraceId](capi-hitrace-hitraceid.md)，使用当前线程TLS中的chainId、spanId初始化其chainId、parentSpanId，并为其生成一个新的spanId。 |
| [void OH\_HiTrace\_Tracepoint(HiTrace\_Communication\_Mode mode, HiTrace\_Tracepoint\_Type type, const HiTraceId \*id, const char \*fmt, ...)](capi-trace-h.md#oh_hitrace_tracepoint) | - | HiTraceMeter跟踪信息埋点。  type为客户端发送[HITRACE\_TP\_CS](capi-trace-h.md#hitrace_tracepoint_type)和服务端接收[HITRACE\_TP\_SR](capi-trace-h.md#hitrace_tracepoint_type)时，进行同步HiTraceMeter开始打点；type为客户端接收[HITRACE\_TP\_CR](capi-trace-h.md#hitrace_tracepoint_type)和服务端发送[HITRACE\_TP\_SS](capi-trace-h.md#hitrace_tracepoint_type)时，进行同步HiTraceMeter结束打点；type为通用类型[HITRACE\_TP\_GENERAL](capi-trace-h.md#hitrace_tracepoint_type)时，不会进行HiTraceMeter打点。  type为客户端发送[HITRACE\_TP\_CS](capi-trace-h.md#hitrace_tracepoint_type)和客户端接收[HITRACE\_TP\_CR](capi-trace-h.md#hitrace_tracepoint_type)的信息埋点需配套使用；type为服务端接收[HITRACE\_TP\_SR](capi-trace-h.md#hitrace_tracepoint_type)和服务端发送[HITRACE\_TP\_SS](capi-trace-h.md#hitrace_tracepoint_type)的信息埋点需配套使用。否则，HiTraceMeter开始与结束打点无法正常匹配。 |
| [void OH\_HiTrace\_InitId(HiTraceId \*id)](capi-trace-h.md#oh_hitrace_initid) | - | 初始化[HiTraceId](capi-hitrace-hitraceid.md)。 |
| [void OH\_HiTrace\_IdFromBytes(HiTraceId \*id, const uint8\_t \*pIdArray, int len)](capi-trace-h.md#oh_hitrace_idfrombytes) | - | 根据大端序字节数组创建[HiTraceId](capi-hitrace-hitraceid.md)。 |
| [bool OH\_HiTrace\_IsIdValid(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_isidvalid) | - | 判断[HiTraceId](capi-hitrace-hitraceid.md)是否有效。 |
| [bool OH\_HiTrace\_IsFlagEnabled(const HiTraceId \*id, HiTrace\_Flag flag)](capi-trace-h.md#oh_hitrace_isflagenabled) | - | 判断[HiTraceId](capi-hitrace-hitraceid.md)是否启用了跟踪标志flag。 |
| [void OH\_HiTrace\_EnableFlag(const HiTraceId \*id, HiTrace\_Flag flag)](capi-trace-h.md#oh_hitrace_enableflag) | - | 启用[HiTraceId](capi-hitrace-hitraceid.md)中指定的跟踪标志。 |
| [int OH\_HiTrace\_GetFlags(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_getflags) | - | 获取[HiTraceId](capi-hitrace-hitraceid.md)中设置的跟踪标志位。 |
| [void OH\_HiTrace\_SetFlags(HiTraceId \*id, int flags)](capi-trace-h.md#oh_hitrace_setflags) | - | 设置跟踪标志位到[HiTraceId](capi-hitrace-hitraceid.md)中。 |
| [uint64\_t OH\_HiTrace\_GetChainId(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_getchainid) | - | 获取[HiTraceId](capi-hitrace-hitraceid.md)中的跟踪链ID。 |
| [void OH\_HiTrace\_SetChainId(HiTraceId \*id, uint64\_t chainId)](capi-trace-h.md#oh_hitrace_setchainid) | - | 设置跟踪链ID到[HiTraceId](capi-hitrace-hitraceid.md)中。 |
| [uint64\_t OH\_HiTrace\_GetSpanId(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_getspanid) | - | 获取当前[HiTraceId](capi-hitrace-hitraceid.md)中的分支ID。 |
| [void OH\_HiTrace\_SetSpanId(HiTraceId \*id, uint64\_t spanId)](capi-trace-h.md#oh_hitrace_setspanid) | - | 设置分支ID到[HiTraceId](capi-hitrace-hitraceid.md)中。 |
| [uint64\_t OH\_HiTrace\_GetParentSpanId(const HiTraceId \*id)](capi-trace-h.md#oh_hitrace_getparentspanid) | - | 获取当前[HiTraceId](capi-hitrace-hitraceid.md)中的父分支ID。 |
| [void OH\_HiTrace\_SetParentSpanId(HiTraceId \*id, uint64\_t parentSpanId)](capi-trace-h.md#oh_hitrace_setparentspanid) | - | 设置[HiTraceId](capi-hitrace-hitraceid.md)结构的parentSpanId字段。 |
| [int OH\_HiTrace\_IdToBytes(const HiTraceId\* id, uint8\_t\* pIdArray, int len)](capi-trace-h.md#oh_hitrace_idtobytes) | - | 将[HiTraceId](capi-hitrace-hitraceid.md)序列化为大端序字节数组，支持本地缓存及跨设备传输。 |
| [void OH\_HiTrace\_StartTrace(const char \*name)](capi-trace-h.md#oh_hitrace_starttrace) | - | 标记一个同步跟踪耗时任务的开始。  同步跟踪打点接口[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)和[OH\_HiTrace\_FinishTrace](capi-trace-h.md#oh_hitrace_finishtrace)必须配对使用。  [OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)和[OH\_HiTrace\_FinishTrace](capi-trace-h.md#oh_hitrace_finishtrace)函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。  从API version 19开始，建议使用[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)接口，以便分级控制跟踪输出。 |
| [void OH\_HiTrace\_FinishTrace(void)](capi-trace-h.md#oh_hitrace_finishtrace) | - | 标记一个同步跟踪耗时任务的结束。  必须和[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)配对使用。跟踪解析时，和其前执行流程中最近的[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)进行匹配。  从API version 19开始，建议使用[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)接口，以便分级控制跟踪输出。 |
| [void OH\_HiTrace\_StartAsyncTrace(const char \*name, int32\_t taskId)](capi-trace-h.md#oh_hitrace_startasynctrace) | - | 标记一个异步跟踪耗时任务的开始。  用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。  必须和[OH\_HiTrace\_FinishAsyncTrace](capi-trace-h.md#oh_hitrace_finishasynctrace)配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。  如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。  如果具有相同name的任务是串行执行的，则taskId可以相同。  从API version 19开始，建议使用[OH\_HiTrace\_StartAsyncTraceEx](capi-trace-h.md#oh_hitrace_startasynctraceex)接口，以便分级控制跟踪输出与跟踪聚类。 |
| [void OH\_HiTrace\_FinishAsyncTrace(const char \*name, int32\_t taskId)](capi-trace-h.md#oh_hitrace_finishasynctrace) | - | 标记一个异步跟踪耗时任务的结束。  在异步操作完成后如回调函数中调用，进行结束打点。  和[OH\_HiTrace\_StartAsyncTrace](capi-trace-h.md#oh_hitrace_startasynctrace)配对使用，参数name和taskId必须与异步跟踪的开始打点接口的对应参数值保持一致。  从API version 19开始，建议使用[OH\_HiTrace\_FinishAsyncTraceEx](capi-trace-h.md#oh_hitrace_finishasynctraceex)接口，以便分级控制跟踪输出。 |
| [void OH\_HiTrace\_CountTrace(const char \*name, int64\_t count)](capi-trace-h.md#oh_hitrace_counttrace) | - | 用于跟踪给定整数变量名和整数值。  多次执行该接口可以跟踪给定整数变量在不同时刻的数值变化。  从API version 19开始，建议使用[OH\_HiTrace\_CountTraceEx](capi-trace-h.md#oh_hitrace_counttraceex)接口，以便分级控制跟踪输出。 |
| [void OH\_HiTrace\_StartTraceEx(HiTrace\_Output\_Level level, const char \*name, const char \*customArgs)](capi-trace-h.md#oh_hitrace_starttraceex) | - | 标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。  同步跟踪打点接口[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)和[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)必须配对使用。  [OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)和[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。 |
| [void OH\_HiTrace\_FinishTraceEx(HiTrace\_Output\_Level level)](capi-trace-h.md#oh_hitrace_finishtraceex) | - | 标记一个同步跟踪耗时任务的结束，分级控制跟踪输出。  必须和[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)配对使用，参数level必须与同步跟踪的开始打点接口[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)的对应参数值一致。  跟踪数据解析时，和其前执行流程中最近的[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)进行匹配。 |
| [void OH\_HiTrace\_StartAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId, const char \*customCategory, const char \*customArgs)](capi-trace-h.md#oh_hitrace_startasynctraceex) | - | 标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。  用于在异步操作执行前进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。  和[OH\_HiTrace\_FinishAsyncTraceEx](capi-trace-h.md#oh_hitrace_finishasynctraceex)配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。  如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。  如果具有相同name的任务是串行执行的，则taskId可以相同。  不同进程的taskId不会相互干扰。 |
| [void OH\_HiTrace\_FinishAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId)](capi-trace-h.md#oh_hitrace_finishasynctraceex) | - | 标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。  用于在异步操作完成后进行结束打点，例如在回调函数中调用。  和[OH\_HiTrace\_StartAsyncTraceEx](capi-trace-h.md#oh_hitrace_startasynctraceex)配对使用，参数level、name和taskId必须与异步跟踪开始打点接口的对应参数值保持一致。 |
| [void OH\_HiTrace\_CountTraceEx(HiTrace\_Output\_Level level, const char \*name, int64\_t count)](capi-trace-h.md#oh_hitrace_counttraceex) | - | 标记一个跟踪的整数变量，分级控制跟踪输出。 |
| [bool OH\_HiTrace\_IsTraceEnabled(void)](capi-trace-h.md#oh_hitrace_istraceenabled) | - | 判断当前是否开启应用trace捕获。 |
| [int32\_t OH\_HiTrace\_RegisterTraceListener(OH\_HiTrace\_TraceEventListener callback)](capi-trace-h.md#oh_hitrace_registertracelistener) | - | 注册应用trace捕获开关通知回调，使用callback异步回调。  注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。回调函数保存在应用进程内，一个进程最多可以注册10个回调函数。  若注册的回调包含耗时操作，当回调被执行时，注册或注销行为会被阻塞（等待回调执行完成）。因此，建议不要在应用主线程中注册或注销包含耗时操作的回调，避免发生应用冻屏。 |
| [int32\_t OH\_HiTrace\_UnregisterTraceListener(int32\_t index)](capi-trace-h.md#oh_hitrace_unregistertracelistener) | - | 注销应用trace捕获开关通知回调。  使用[OH\_HiTrace\_RegisterTraceListener](capi-trace-h.md#oh_hitrace_registertracelistener)返回的回调索引，注销该索引关联的回调函数。 |

## 枚举类型说明

### HiTraceId\_Valid

```c
enum HiTraceId_Valid
```

**描述**

HiTraceId是否有效标志。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_ID\_INVALID = 0 | 无效HiTraceId。  **起始版本：** 12 |
| HITRACE\_ID\_VALID = 1 | 有效HiTraceId。  **起始版本：** 12 |

### HiTrace\_Version

```c
enum HiTrace_Version
```

**描述**

HiTrace版本号。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_VER\_1 = 0 | 版本1。  **起始版本：** 12 |

### HiTrace\_Flag

```c
enum HiTrace_Flag
```

**描述**

HiTrace跟踪标志。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_FLAG\_DEFAULT = 0 | 默认标志。  **起始版本：** 12 |
| HITRACE\_FLAG\_INCLUDE\_ASYNC = 1 << 0 | 异步调用标志。  设置该标志，同时跟踪同步和异步调用；默认只跟踪同步调用。  **起始版本：** 12 |
| HITRACE\_FLAG\_DONOT\_CREATE\_SPAN = 1 << 1 | 无分支标志。  设置该标志，不创建分支信息；默认创建分支信息。  **起始版本：** 12 |
| HITRACE\_FLAG\_TP\_INFO = 1 << 2 | 埋点标志。  调试场景下设置该标志，调用信息埋点接口[OH\_HiTrace\_Tracepoint](capi-trace-h.md#oh_hitrace_tracepoint)时，会打印埋点信息hilog日志；默认不打印埋点信息hilog日志。  **起始版本：** 12 |
| HITRACE\_FLAG\_NO\_BE\_INFO = 1 << 3 | 无开始结束信息标志。  调试场景下设置该标志，调用开始跟踪接口[OH\_HiTrace\_BeginChain](capi-trace-h.md#oh_hitrace_beginchain)和结束跟踪接口[OH\_HiTrace\_EndChain](capi-trace-h.md#oh_hitrace_endchain)时，分别会打印开始、结束跟踪信息hilog日志；默认不打印开始、结束跟踪信息hilog日志。  **起始版本：** 12 |
| HITRACE\_FLAG\_DONOT\_ENABLE\_LOG = 1 << 4 | 日志关联标志。  设置该标志，不会在hilog日志中附加HiTraceId信息；默认会在hilog日志中附加HiTraceId信息。  **起始版本：** 12 |
| HITRACE\_FLAG\_FAULT\_TRIGGER = 1 << 5 | 故障触发标志。预置标志，暂未启用。  **起始版本：** 12 |
| HITRACE\_FLAG\_D2D\_TP\_INFO = 1 << 6 | 设备间埋点标志。[HITRACE\_FLAG\_TP\_INFO](capi-trace-h.md#hitrace_flag)的一个子集，调试场景下使用。  当已设置[HITRACE\_FLAG\_TP\_INFO](capi-trace-h.md#hitrace_flag)标志时，[HITRACE\_FLAG\_D2D\_TP\_INFO](capi-trace-h.md#hitrace_flag)标志不生效；当未设置[HITRACE\_FLAG\_TP\_INFO](capi-trace-h.md#hitrace_flag)标志时，设置[HITRACE\_FLAG\_D2D\_TP\_INFO](capi-trace-h.md#hitrace_flag)标志，此时调用信息埋点接口[OH\_HiTrace\_Tracepoint](capi-trace-h.md#oh_hitrace_tracepoint)，仅当mode参数为设备间通信[HITRACE\_CM\_DEVICE](capi-trace-h.md#hitrace_communication_mode)的情况下，会打印埋点信息hilog日志。  **起始版本：** 12 |

### HiTrace\_Tracepoint\_Type

```c
enum HiTrace_Tracepoint_Type
```

**描述**

跟踪埋点类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_TP\_CS = 0 | 客户端发送。  **起始版本：** 12 |
| HITRACE\_TP\_CR = 1 | 客户端接收。  **起始版本：** 12 |
| HITRACE\_TP\_SS = 2 | 服务端发送。  **起始版本：** 12 |
| HITRACE\_TP\_SR = 3 | 服务端接收。  **起始版本：** 12 |
| HITRACE\_TP\_GENERAL = 4 | 通用类型，标识HITRACE\_TP\_CS、HITRACE\_TP\_CR、HITRACE\_TP\_SS、HITRACE\_TP\_SR四种场景之外的埋点。  **起始版本：** 12 |

### HiTrace\_Communication\_Mode

```c
enum HiTrace_Communication_Mode
```

**描述**

跟踪通信类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_CM\_DEFAULT = 0 | 默认通信类型。  **起始版本：** 12 |
| HITRACE\_CM\_THREAD = 1 | 线程间通信。  **起始版本：** 12 |
| HITRACE\_CM\_PROCESS = 2 | 进程间通信。  **起始版本：** 12 |
| HITRACE\_CM\_DEVICE = 3 | 设备间通信。  **起始版本：** 12 |

### HiTrace\_Output\_Level

```c
enum HiTrace_Output_Level
```

**描述**

HiTrace输出级别。低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为[HITRACE\_LEVEL\_INFO](capi-trace-h.md#hitrace_output_level)；nolog版本阈值为[HITRACE\_LEVEL\_COMMERCIAL](capi-trace-h.md#hitrace_output_level)。

**起始版本：** 19

| 枚举项 | 描述 |
| --- | --- |
| HITRACE\_LEVEL\_DEBUG = 0 | 仅用于调试的输出级别，优先级最低。  **起始版本：** 19 |
| HITRACE\_LEVEL\_INFO = 1 | 用于log版本的输出级别。  **起始版本：** 19 |
| HITRACE\_LEVEL\_CRITICAL = 2 | 用于log版本的输出级别，优先级高于[HITRACE\_LEVEL\_INFO](capi-trace-h.md#hitrace_output_level)。  **起始版本：** 19 |
| HITRACE\_LEVEL\_COMMERCIAL = 3 | 用于nolog版本的输出级别，优先级最高。  **起始版本：** 19 |
| HITRACE\_LEVEL\_MAX = HITRACE\_LEVEL\_COMMERCIAL | 输出级别范围限制。  **起始版本：** 19 |

## 函数说明

### OH\_HiTrace\_TraceEventListener()

```c
typedef void (*OH_HiTrace_TraceEventListener)(bool traceStatus)
```

**描述**

定义应用trace捕获开关状态切换时的回调函数类型。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool traceStatus | 当前应用trace捕获开关状态。  true：开启；false：关闭。 |

### OH\_HiTrace\_BeginChain()

```c
HiTraceId OH_HiTrace_BeginChain(const char *name, int flags)
```

**描述**

开始跟踪。

当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId；当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 跟踪业务名，用于标识被跟踪的业务流程。建议使用简洁明了的名称，便于在分析时识别。 |
| int flags | 跟踪标志组合，见[HiTrace\_Flag](capi-trace-h.md#hitrace_flag)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) | [HiTraceId](capi-hitrace-hitraceid.md)结构体。 |

### OH\_HiTrace\_EndChain()

```c
void OH_HiTrace_EndChain()
```

**描述**

结束跟踪。

结束跟踪并将当前线程TLS中的HiTraceId设置为无效。

**起始版本：** 12

### OH\_HiTrace\_GetId()

```c
HiTraceId OH_HiTrace_GetId()
```

**描述**

获取跟踪标识。

获取当前线程TLS中的[HiTraceId](capi-hitrace-hitraceid.md)。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) | [HiTraceId](capi-hitrace-hitraceid.md)结构体。 |

### OH\_HiTrace\_SetId()

```c
void OH_HiTrace_SetId(const HiTraceId *id)
```

**描述**

设置跟踪标识。

将给定的[HiTraceId](capi-hitrace-hitraceid.md)设置到当前线程TLS中。若传入的参数无效，则不执行任何操作。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 要设置的[HiTraceId](capi-hitrace-hitraceid.md)。 |

### OH\_HiTrace\_ClearId()

```c
void OH_HiTrace_ClearId(void)
```

**描述**

清除跟踪标识。

将当前线程TLS中的[HiTraceId](capi-hitrace-hitraceid.md)设置为无效。

**起始版本：** 12

### OH\_HiTrace\_CreateSpan()

```c
HiTraceId OH_HiTrace_CreateSpan(void)
```

**描述**

创建跟踪分支。

创建一个[HiTraceId](capi-hitrace-hitraceid.md)，使用当前线程TLS中的chainId、spanId初始化其chainId、parentSpanId，并为其生成一个新的spanId。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) | [HiTraceId](capi-hitrace-hitraceid.md)结构体。 |

### OH\_HiTrace\_Tracepoint()

```c
void OH_HiTrace_Tracepoint(HiTrace_Communication_Mode mode, HiTrace_Tracepoint_Type type, const HiTraceId *id, const char *fmt, ...)
```

**描述**

HiTraceMeter跟踪信息埋点。

type为客户端发送[HITRACE\_TP\_CS](capi-trace-h.md#hitrace_tracepoint_type)和服务端接收[HITRACE\_TP\_SR](capi-trace-h.md#hitrace_tracepoint_type)时，进行同步HiTraceMeter开始打点；type为客户端接收[HITRACE\_TP\_CR](capi-trace-h.md#hitrace_tracepoint_type)和服务端发送[HITRACE\_TP\_SS](capi-trace-h.md#hitrace_tracepoint_type)时，进行同步HiTraceMeter结束打点；type为通用类型[HITRACE\_TP\_GENERAL](capi-trace-h.md#hitrace_tracepoint_type)时，不会进行HiTraceMeter打点。

type为客户端发送[HITRACE\_TP\_CS](capi-trace-h.md#hitrace_tracepoint_type)和客户端接收[HITRACE\_TP\_CR](capi-trace-h.md#hitrace_tracepoint_type)的信息埋点需配套使用；type为服务端接收[HITRACE\_TP\_SR](capi-trace-h.md#hitrace_tracepoint_type)和服务端发送[HITRACE\_TP\_SS](capi-trace-h.md#hitrace_tracepoint_type)的信息埋点需配套使用。否则，HiTraceMeter开始与结束打点无法正常匹配。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Communication\_Mode](capi-trace-h.md#hitrace_communication_mode) mode | 跟踪通信模式，见[HiTrace\_Communication\_Mode](capi-trace-h.md#hitrace_communication_mode)。 |
| [HiTrace\_Tracepoint\_Type](capi-trace-h.md#hitrace_tracepoint_type) type | 跟踪信息类型，见[HiTrace\_Tracepoint\_Type](capi-trace-h.md#hitrace_tracepoint_type)。 |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 实施信息埋点操作的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| const char \*fmt | HiTraceMeter打点操作传入的trace说明信息的格式化字符串，遵循 **ISO C（C89/C99/C17）printf 格式规范**。 |
| ... | 与格式字符串fmt里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

### OH\_HiTrace\_InitId()

```c
void OH_HiTrace_InitId(HiTraceId *id)
```

**描述**

初始化[HiTraceId](capi-hitrace-hitraceid.md)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要初始化的[HiTraceId](capi-hitrace-hitraceid.md)。 |

### OH\_HiTrace\_IdFromBytes()

```c
void OH_HiTrace_IdFromBytes(HiTraceId *id, const uint8_t *pIdArray, int len)
```

**描述**

根据大端序字节数组创建[HiTraceId](capi-hitrace-hitraceid.md)。

和[OH\_HiTrace\_IdToBytes](capi-trace-h.md#oh_hitrace_idtobytes)成对使用，解析序列化后的大端序字节数据，还原为HiTraceId。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要创建的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| const uint8\_t \*pIdArray | 大端序字节数组指针。 |
| int len | 大端序字节数组长度。 |

### OH\_HiTrace\_IsIdValid()

```c
bool OH_HiTrace_IsIdValid(const HiTraceId *id)
```

**描述**

判断[HiTraceId](capi-hitrace-hitraceid.md)是否有效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要判断是否有效的[HiTraceId](capi-hitrace-hitraceid.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：[HiTraceId](capi-hitrace-hitraceid.md)有效；false：[HiTraceId](capi-hitrace-hitraceid.md)无效。 |

### OH\_HiTrace\_IsFlagEnabled()

```c
bool OH_HiTrace_IsFlagEnabled(const HiTraceId *id, HiTrace_Flag flag)
```

**描述**

判断[HiTraceId](capi-hitrace-hitraceid.md)是否启用了跟踪标志flag。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要判断指定跟踪标志是否启用的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| [HiTrace\_Flag](capi-trace-h.md#hitrace_flag) flag | 指定的跟踪标志，见[HiTrace\_Flag](capi-trace-h.md#hitrace_flag)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：[HiTraceId](capi-hitrace-hitraceid.md)已启用flag；false：[HiTraceId](capi-hitrace-hitraceid.md)未启用flag。 |

### OH\_HiTrace\_EnableFlag()

```c
void OH_HiTrace_EnableFlag(const HiTraceId *id, HiTrace_Flag flag)
```

**描述**

启用[HiTraceId](capi-hitrace-hitraceid.md)中指定的跟踪标志。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要启用指定跟踪标志的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| [HiTrace\_Flag](capi-trace-h.md#hitrace_flag) flag | 指定的跟踪标志，见[HiTrace\_Flag](capi-trace-h.md#hitrace_flag)。 |

### OH\_HiTrace\_GetFlags()

```c
int OH_HiTrace_GetFlags(const HiTraceId *id)
```

**描述**

获取[HiTraceId](capi-hitrace-hitraceid.md)中设置的跟踪标志位。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要获取跟踪标志位的[HiTraceId](capi-hitrace-hitraceid.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | [HiTraceId](capi-hitrace-hitraceid.md)中设置的跟踪标志位。 |

### OH\_HiTrace\_SetFlags()

```c
void OH_HiTrace_SetFlags(HiTraceId *id, int flags)
```

**描述**

设置跟踪标志位到[HiTraceId](capi-hitrace-hitraceid.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要设置跟踪标志位的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| int flags | 指定的跟踪标志位，见[HiTrace\_Flag](capi-trace-h.md#hitrace_flag)。 |

### OH\_HiTrace\_GetChainId()

```c
uint64_t OH_HiTrace_GetChainId(const HiTraceId *id)
```

**描述**

获取[HiTraceId](capi-hitrace-hitraceid.md)中的跟踪链ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要获取跟踪链ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | 跟踪链ID。 |

### OH\_HiTrace\_SetChainId()

```c
void OH_HiTrace_SetChainId(HiTraceId *id, uint64_t chainId)
```

**描述**

设置跟踪链ID到[HiTraceId](capi-hitrace-hitraceid.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要设置跟踪链ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| uint64\_t chainId | 需要设置的跟踪链ID。 |

### OH\_HiTrace\_GetSpanId()

```c
uint64_t OH_HiTrace_GetSpanId(const HiTraceId *id)
```

**描述**

获取当前[HiTraceId](capi-hitrace-hitraceid.md)中的分支ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要获取分支ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | [HiTraceId](capi-hitrace-hitraceid.md)中设置的分支ID。 |

### OH\_HiTrace\_SetSpanId()

```c
void OH_HiTrace_SetSpanId(HiTraceId *id, uint64_t spanId)
```

**描述**

设置分支ID到[HiTraceId](capi-hitrace-hitraceid.md)中。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要设置分支ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| uint64\_t spanId | 需要设置的分支ID。 |

### OH\_HiTrace\_GetParentSpanId()

```c
uint64_t OH_HiTrace_GetParentSpanId(const HiTraceId *id)
```

**描述**

获取当前[HiTraceId](capi-hitrace-hitraceid.md)中的父分支ID。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要获取父分支ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint64\_t | [HiTraceId](capi-hitrace-hitraceid.md)中设置的父分支ID。 |

### OH\_HiTrace\_SetParentSpanId()

```c
void OH_HiTrace_SetParentSpanId(HiTraceId *id, uint64_t parentSpanId)
```

**描述**

设置[HiTraceId](capi-hitrace-hitraceid.md)结构的parentSpanId字段。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTraceId](capi-hitrace-hitraceid.md) \*id | 需要设置父分支ID的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| uint64\_t parentSpanId | 需要设置的父分支ID。 |

### OH\_HiTrace\_IdToBytes()

```c
int OH_HiTrace_IdToBytes(const HiTraceId* id, uint8_t* pIdArray, int len)
```

**描述**

将[HiTraceId](capi-hitrace-hitraceid.md)序列化为大端序字节数组，支持本地缓存及跨设备传输。

接口内部统一输出大端序数据，在大小端架构不一致的设备间同步HiTraceId时，可屏蔽字节序的差异，保证跨端数据解析正确。

本接口需与[OH\_HiTrace\_IdFromBytes](capi-trace-h.md#oh_hitrace_idfrombytes)配套使用，用于将序列化后的大端序数据还原为HiTraceId。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const HiTraceId](capi-hitrace-hitraceid.md)\* id | 需要转换的[HiTraceId](capi-hitrace-hitraceid.md)。 |
| uint8\_t\* pIdArray | 用于存放序列化数据的字节数组指针，目标的数组长度至少应为16Byte。 |
| int len | 存放序列化数据的字节数组的可用长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 转换后的字节数组长度，当传入参数无效时返回0。 |

### OH\_HiTrace\_StartTrace()

```c
void OH_HiTrace_StartTrace(const char *name)
```

**描述**

标记一个同步跟踪耗时任务的开始。

同步跟踪打点接口[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)和[OH\_HiTrace\_FinishTrace](capi-trace-h.md#oh_hitrace_finishtrace)必须配对使用。

[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)和[OH\_HiTrace\_FinishTrace](capi-trace-h.md#oh_hitrace_finishtrace)函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

从API version 19开始，建议使用[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)接口，以便分级控制跟踪输出。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 跟踪的名字。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name的长度不要超过420Byte。 |

### OH\_HiTrace\_FinishTrace()

```c
void OH_HiTrace_FinishTrace(void)
```

**描述**

标记一个同步跟踪耗时任务的结束。

必须和[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)配对使用。跟踪解析时，和其前执行流程中最近的[OH\_HiTrace\_StartTrace](capi-trace-h.md#oh_hitrace_starttrace)进行匹配。

从API version 19开始，建议使用[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)接口，以便分级控制跟踪输出。

**起始版本：** 10

### OH\_HiTrace\_StartAsyncTrace()

```c
void OH_HiTrace_StartAsyncTrace(const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的开始。

用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

必须和[OH\_HiTrace\_FinishAsyncTrace](capi-trace-h.md#oh_hitrace_finishasynctrace)配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

如果具有相同name的任务是串行执行的，则taskId可以相同。

从API version 19开始，建议使用[OH\_HiTrace\_StartAsyncTraceEx](capi-trace-h.md#oh_hitrace_startasynctraceex)接口，以便分级控制跟踪输出与跟踪聚类。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 异步跟踪任务的名字，用于标识要测量的异步操作，需与对应的结束接口的name参数相同。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name的长度不要超过420Byte。 |
| int32\_t taskId | 异步跟踪的ID。 异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。 |

### OH\_HiTrace\_FinishAsyncTrace()

```c
void OH_HiTrace_FinishAsyncTrace(const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的结束。

在异步操作完成后如回调函数中调用，进行结束打点。

和[OH\_HiTrace\_StartAsyncTrace](capi-trace-h.md#oh_hitrace_startasynctrace)配对使用，参数name和taskId必须与异步跟踪的开始打点接口的对应参数值保持一致。

从API version 19开始，建议使用[OH\_HiTrace\_FinishAsyncTraceEx](capi-trace-h.md#oh_hitrace_finishasynctraceex)接口，以便分级控制跟踪输出。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 异步跟踪任务的名字，需与对应的开始接口的name参数保持一致，用于匹配对应的异步跟踪任务。 |
| int32\_t taskId | 异步跟踪的ID。异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。 |

### OH\_HiTrace\_CountTrace()

```c
void OH_HiTrace_CountTrace(const char *name, int64_t count)
```

**描述**

用于跟踪给定整数变量名和整数值。

多次执行该接口可以跟踪给定整数变量在不同时刻的数值变化。

从API version 19开始，建议使用[OH\_HiTrace\_CountTraceEx](capi-trace-h.md#oh_hitrace_counttraceex)接口，以便分级控制跟踪输出。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 整数变量跟踪的名字，不必与真实变量名相同。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name的长度不要超过420Byte。 |
| int64\_t count | 要记录的整数值，用于跟踪该变量在不同时刻的数值变化。 |

### OH\_HiTrace\_StartTraceEx()

```c
void OH_HiTrace_StartTraceEx(HiTrace_Output_Level level, const char *name, const char *customArgs)
```

**描述**

标记一个同步跟踪耗时任务的开始，分级控制跟踪输出。

同步跟踪打点接口[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)和[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)必须配对使用。

[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)和[OH\_HiTrace\_FinishTraceEx](capi-trace-h.md#oh_hitrace_finishtraceex)函数对可以嵌套使用，跟踪解析时使用栈式数据结构进行匹配。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) level | 跟踪输出级别。低于系统跟踪输出级别阈值的打点将不会生效。  log版本阈值为[HITRACE\_LEVEL\_INFO](capi-trace-h.md#hitrace_output_level)；nolog版本阈值为[HITRACE\_LEVEL\_COMMERCIAL](capi-trace-h.md#hitrace_output_level)。 |
| const char \*name | 同步跟踪的名字。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name和customArgs的长度之和不要超过420Byte。 |
| const char \*customArgs | 自定义键值对参数，用于附加额外的跟踪信息，多个键值对使用逗号分隔，例"key1=value1,key2=value2"。这些参数可以在性能分析时帮助过滤或标记特定的跟踪点。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name和customArgs的长度之和不要超过420Byte。 |

### OH\_HiTrace\_FinishTraceEx()

```c
void OH_HiTrace_FinishTraceEx(HiTrace_Output_Level level)
```

**描述**

标记一个同步跟踪耗时任务的结束，分级控制跟踪输出。

必须和[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)配对使用，参数level必须与同步跟踪的开始打点接口[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)的对应参数值一致。

跟踪数据解析时，和其前执行流程中最近的[OH\_HiTrace\_StartTraceEx](capi-trace-h.md#oh_hitrace_starttraceex)进行匹配。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) level | 跟踪输出级别。 |

### OH\_HiTrace\_StartAsyncTraceEx()

```c
void OH_HiTrace_StartAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId, const char *customCategory, const char *customArgs)
```

**描述**

标记一个异步跟踪耗时任务的开始，分级控制跟踪输出。

用于在异步操作执行前进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。

和[OH\_HiTrace\_FinishAsyncTraceEx](capi-trace-h.md#oh_hitrace_finishasynctraceex)配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

如果有多个相同name的任务需要跟踪或者对同一个任务跟踪多次，并且任务同时被执行，则每次调用的taskId需不相同。

如果具有相同name的任务是串行执行的，则taskId可以相同。

不同进程的taskId不会相互干扰。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) level | 跟踪输出级别。 |
| const char \*name | 异步跟踪的名字。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name、customCategory和customArgs的长度之和不要超过420Byte。 |
| int32\_t taskId | 异步跟踪的ID。异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。 |
| const char \*customCategory | 自定义聚类名称，用于聚合同一类异步跟踪打点。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name、customCategory和customArgs的长度之和不要超过420Byte。 |
| const char \*customArgs | 键值对，多个键值对使用逗号分隔，例"key1=value1,key2=value2"。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name、customCategory和customArgs的长度之和不要超过420Byte。 |

### OH\_HiTrace\_FinishAsyncTraceEx()

```c
void OH_HiTrace_FinishAsyncTraceEx(HiTrace_Output_Level level, const char *name, int32_t taskId)
```

**描述**

标记一个异步跟踪耗时任务的结束，分级控制跟踪输出。

用于在异步操作完成后进行结束打点，例如在回调函数中调用。

和[OH\_HiTrace\_StartAsyncTraceEx](capi-trace-h.md#oh_hitrace_startasynctraceex)配对使用，参数level、name和taskId必须与异步跟踪开始打点接口的对应参数值保持一致。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) level | 跟踪输出级别。 |
| const char \*name | 异步跟踪的名字。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name的长度不要超过420Byte。 |
| int32\_t taskId | 异步跟踪的ID。异步跟踪开始和结束由于不是顺序发生的，所以需要通过name和每次执行唯一的taskId进行开始和结束的匹配。 |

### OH\_HiTrace\_CountTraceEx()

```c
void OH_HiTrace_CountTraceEx(HiTrace_Output_Level level, const char *name, int64_t count)
```

**描述**

标记一个跟踪的整数变量，分级控制跟踪输出。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [HiTrace\_Output\_Level](capi-trace-h.md#hitrace_output_level) level | 跟踪输出级别。 |
| const char \*name | 整数变量的名称，不必与实际变量名相同。  由于单条trace记录的总长度限制为512Byte，超出部分将被截断，建议name的长度不要超过420Byte。 |
| int64\_t count | 要记录的整数值，用于跟踪该变量在不同时刻的数值变化。 |

### OH\_HiTrace\_IsTraceEnabled()

```c
bool OH_HiTrace_IsTraceEnabled(void)
```

**描述**

判断当前是否开启应用trace捕获。

**起始版本：** 19

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 使用hitrace命令行工具等方式开启采集时返回true。  未开启采集或停止采集后返回false，此时调用HiTraceMeter性能跟踪打点接口无效。 |

### OH\_HiTrace\_RegisterTraceListener()

```c
int32_t OH_HiTrace_RegisterTraceListener(OH_HiTrace_TraceEventListener callback)
```

**描述**

注册应用trace捕获开关通知回调，使用callback异步回调。

注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。回调函数保存在应用进程内，一个进程最多可以注册10个回调函数。

若注册的回调包含耗时操作，当回调被执行时，注册或注销行为会被阻塞（等待回调执行完成）。因此，建议不要在应用主线程中注册或注销包含耗时操作的回调，避免发生应用冻屏。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_HiTrace\_TraceEventListener](capi-trace-h.md#oh_hitrace_traceeventlistener) callback | 注册的回调函数。应避免耗时操作，否则会阻塞注册或注销操作；建议不在主线程注册或注销含耗时操作的回调，避免应用冻屏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 回调注册状态。  >= 0：注册成功，返回用于注销的回调索引，索引范围0到9；  -1：已达到最大回调函数注册数量；  -2：无效参数，参数非[OH\_HiTrace\_TraceEventListener](capi-trace-h.md#oh_hitrace_traceeventlistener)类型。 |

### OH\_HiTrace\_UnregisterTraceListener()

```c
int32_t OH_HiTrace_UnregisterTraceListener(int32_t index)
```

**描述**

注销应用trace捕获开关通知回调。

使用[OH\_HiTrace\_RegisterTraceListener](capi-trace-h.md#oh_hitrace_registertracelistener)返回的回调索引，注销该索引关联的回调函数。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t index | 已注册回调函数索引，有效取值范围为0到9。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 回调注销状态。  0：注销成功；  -1：目标索引的回调函数未注册；  -2：无效索引，参数index值不在0到9的范围内。 |
