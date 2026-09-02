---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain
title: "@ohos.hiTraceChain (分布式跟踪)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiTraceChain (分布式跟踪)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a98941c4bab9c87941119070bc2b101677032eb231639c592bbe19bd4fe7a349
---

本模块提供了端侧业务流程调用链跟踪的打点能力，包括业务流程跟踪的启动、结束、信息埋点等能力。

使用场景：

* 分布式跨设备业务调用链追踪与分析。
* 性能问题定位与瓶颈分析。
* 业务流程调试与故障排查。
* 异步调用链路监控。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { hiTraceChain } from '@kit.PerformanceAnalysisKit';
```

## HiTraceFlag

跟踪标志组合类型枚举。用于控制分布式跟踪的行为模式，例如在需要跟踪异步调用的业务流程中使用INCLUDE\_ASYNC标志，在不需要详细分支信息的简单业务流程中使用DONOT\_CREATE\_SPAN标志，在需要调试埋点信息的场景中使用TP\_INFO标志。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认标志。 |
| INCLUDE\_ASYNC | 1 | 异步调用标志。  设置该标志，同时跟踪同步和异步调用；默认只跟踪同步调用。 |
| DONOT\_CREATE\_SPAN | 1 << 1 | 无分支标志。  设置该标志，不创建分支信息；默认创建分支信息。 |
| TP\_INFO | 1 << 2 | 埋点标志。  设置该标志后，调用[tracepoint()](js-apis-hitracechain.md#hitracechaintracepoint)接口时会打印埋点信息hilog；默认不打印埋点信息hilog日志。 |
| NO\_BE\_INFO | 1 << 3 | 无开始结束信息标志。  调试场景下设置该标志，调用开始跟踪接口[begin()](js-apis-hitracechain.md#hitracechainbegin)和结束跟踪接口[end()](js-apis-hitracechain.md#hitracechainend)时，分别会打印开始、结束跟踪信息hilog日志；默认不打印开始、结束跟踪信息hilog日志。 |
| DISABLE\_LOG | 1 << 4 | 日志关联标志。  设置该标志，不会在hilog日志中附加HiTraceId信息；默认会在hilog日志中附加HiTraceId信息。 |
| FAILURE\_TRIGGER | 1 << 5 | 故障触发标志。预置标志，暂未启用。 |
| D2D\_TP\_INFO | 1 << 6 | 设备间埋点标志，为TP\_INFO的子集，用于调试场景。  已设置TP\_INFO时，D2D\_TP\_INFO不生效；  未设置TP\_INFO时，D2D\_TP\_INFO生效，调用信息埋点接口[tracepoint()](js-apis-hitracechain.md#hitracechaintracepoint)仅在mode参数为DEVICE时打印埋点信息hilog日志。 |

## HiTraceTracepointType

跟踪埋点类型枚举。用于标识业务流程中的关键节点，例如CS和CR用于标记客户端请求的发送和接收，SS和SR用于标记服务端请求的接收和发送，GENERAL用于标记无法归入上述四种场景的其他关键节点。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CS | 0 | 客户端发送(Client Send)。 |
| CR | 1 | 客户端接收(Client Receive)。 |
| SS | 2 | 服务端发送(Server Send)。 |
| SR | 3 | 服务端接收(Server Receive)。 |
| GENERAL | 4 | 通用类型，标识CS、CR、SS、SR四种场景之外的埋点。 |

## HiTraceCommunicationMode

跟踪通信类型枚举。用于标识通信发生的层级，例如THREAD用于标记同一应用内线程间通信，PROCESS用于标记同一设备内进程间通信，DEVICE用于标记跨设备的分布式通信。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 缺省通信类型。 |
| THREAD | 1 | 线程间通信。 |
| PROCESS | 2 | 进程间通信。 |
| DEVICE | 3 | 设备间通信。 |

## HiTraceId

此接口为HiTraceId对象接口。用于标识分布式跟踪链中的唯一节点，在需要跨线程、跨进程、跨设备跟踪业务流程的场景中使用，例如电商下单流程、支付流程、分布式服务调用链等。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| chainId | bigint | 否 | 否 | 跟踪链标识。 |
| spanId | number | 否 | 是 | 分支标识，默认值为0。 |
| parentSpanId | number | 否 | 是 | 父分支标识，默认值为0。 |
| flags | number | 否 | 是 | 跟踪标志位，默认值为0。 |

## hiTraceChain.begin

begin(name: string, flags?: number): HiTraceId

开始跟踪，同步接口。用于在业务流程的起始节点启动分布式跟踪，例如在用户点击按钮发起请求、服务端收到请求开始处理、启动后台任务等场景。

**说明** 

* 当前线程TLS（Thread Local Storage，线程本地存储）中不存在有效的HiTraceId时，生成有效的HiTraceId并设置到当前线程TLS中，返回该HiTraceId。
* 当前线程TLS中已存在有效的HiTraceId时，不会开始新的跟踪，返回各属性值均为0的无效HiTraceId。
* begin()必须与end()方法配对使用，调用begin()后，应在业务逻辑完成后调用end()结束跟踪，未调用end()可能导致跟踪链无法正常结束，影响跟踪数据的完整性。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 跟踪业务名。  该参数的长度不超过63Byte，超出部分将被截断。 |
| flags | number | 否 | 跟踪标志组合，具体可参考[HiTraceFlag](js-apis-hitracechain.md#hitraceflag)。当需要跟踪异步调用时设置INCLUDE\_ASYNC，不创建分支信息时设置DONOT\_CREATE\_SPAN，调试场景下设置TP\_INFO可打印埋点信息。默认值为0，表示只跟踪同步调用、创建分支信息、不打印日志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](js-apis-hitracechain.md#hitraceid) | 当前线程TLS中的HiTraceId实例。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.end

end(id: HiTraceId): void

结束跟踪，同步接口。用于在业务流程的结束节点终止分布式跟踪，例如在请求处理完成返回结果、用户操作流程结束、后台任务执行完毕等场景。

**说明** 

* 若给定的HiTraceId有效，且等于当前线程TLS中的HiTraceId，结束跟踪并将当前线程TLS中的HiTraceId设置为无效。若给定的HiTraceId无效，或不等于当前线程TLS中的HiTraceId，结束跟踪失败，打印结束跟踪失败hilog日志。
* end()必须与begin()方法配对使用，且需要传入begin()方法返回的HiTraceId，用于结束由begin()启动的跟踪链，释放相关资源。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | HiTraceId实例。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.getId

getId(): HiTraceId

获取跟踪标识，同步接口。用于在需要传递当前跟踪标识的场景，例如将跟踪标识传递给子线程、传递给其他进程、或者在日志中记录当前跟踪标识。

**说明** 

* 获取当前线程TLS中的HiTraceId。若当前线程TLS中不存在有效的HiTraceId，返回各属性值均为0的无效HiTraceId。
* 应在调用begin()方法之后使用此方法，用于在同一线程的业务逻辑间获取跟踪标识后进行传递。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](js-apis-hitracechain.md#hitraceid) | 当前线程TLS中的HiTraceId实例。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，获取当前跟踪标识。
let curTraceId = hiTraceChain.getId();
// 同一跟踪链获取的跟踪标识的chainId一定相同。
if (curTraceId.chainId != traceId.chainId) {
// 基于异常场景的处理逻辑。
}
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.setId

setId(id: HiTraceId): void

设置跟踪标识，同步接口。用于在需要将外部跟踪标识设置到当前线程的场景，例如从父线程继承跟踪标识、从其他进程接收跟踪标识、从设备间通信获取跟踪标识。

**说明** 

将给定的HiTraceId设置到当前线程TLS中。若给定的HiTraceId无效，则不执行任何操作。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | HiTraceId实例。 |

**示例：**

```ts
// 获取当前跟踪链中的跟踪标识。
let traceId = hiTraceChain.getId();
// 将获取的跟踪标识设置为当前traceId。
hiTraceChain.setId(traceId);
```

## hiTraceChain.clearId

clearId(): void

清除跟踪标识，同步接口。用于在需要切断当前跟踪链的场景，例如业务逻辑分支不再需要跟踪、任务完成后清理跟踪标识、或者在开始新的跟踪前清理旧的跟踪标识。

**说明** 

将当前线程TLS中的HiTraceId设置为无效。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**示例：**

```ts
// 业务开始前，尝试清除跟踪标识。
hiTraceChain.clearId();
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.createSpan

createSpan(): HiTraceId

创建跟踪分支，同步接口。用于在业务流程中标记重要的子流程，例如在请求处理过程中的关键步骤、服务端处理链中的各个阶段、或者需要重点关注的业务分支。

**说明** 

* 创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。
* 需要当前线程TLS中存在有效的HiTraceId（即已调用begin()且未调用clearId()），如果当前线程TLS中没有有效HiTraceId，将返回各属性值均为0的无效HiTraceId。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HiTraceId](js-apis-hitracechain.md#hitraceid) | HiTraceId实例。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// 若干业务逻辑完成后，创建跟踪分支。
let spanTraceId = hiTraceChain.createSpan();
// 同一跟踪链的跟踪标识的chainId一定相同。
if (spanTraceId.chainId != traceId.chainId) {
// 基于异常场景的处理逻辑。
}
// 业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.tracepoint

tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void

[@ohos.hiTraceMeter (性能打点)](js-apis-hitracemeter.md)跟踪信息埋点，同步接口。

**说明** 

本接口与HiTraceMeter模块协同工作，HiTraceChain负责跟踪链的管理，HiTraceMeter负责性能数据的采集和统计。当type为客户端发送CS且服务端接收到SR时，进行同步HiTraceMeter开始打点；当type为服务端发送SS且客户端接收到CR时，进行同步HiTraceMeter结束打点；CS和CR以及SR和SS的信息埋点需配套使用。否则，HiTraceMeter开始与结束打点无法正常匹配；当type为通用类型GENERAL时，不会进行HiTraceMeter打点。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [HiTraceCommunicationMode](js-apis-hitracechain.md#hitracecommunicationmode) | 是 | 信息埋点需要指定的跟踪通信模式，用于标识埋点发生的通信范围：THREAD表示线程间通信，PROCESS表示进程间通信，DEVICE表示设备间通信。 |
| type | [HiTraceTracepointType](js-apis-hitracechain.md#hitracetracepointtype) | 是 | 信息埋点需要指定的跟踪埋点类型。 |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | 实施信息埋点操作的HiTraceId实例。 |
| msg | string | 否 | HiTraceMeter打点操作传入的trace说明信息，用于在性能分析时标识打点位置。当需要在HiTraceMeter报告中区分不同打点位置时传入有意义的描述信息（如函数名、操作步骤等），不传入时使用空字符串，不影响基本打点功能。该参数的长度不超过63Byte，超出部分将被截断。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是INCLUDE_ASYNC与DONOT_CREATE_SPAN的并集。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC | hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 若干业务逻辑完成后，触发信息埋点操作。
hiTraceChain.tracepoint(hiTraceChain.HiTraceCommunicationMode.THREAD, hiTraceChain.HiTraceTracepointType.SS, traceId, "Just an example");
// 业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.isValid

isValid(id: HiTraceId): boolean

判断HiTraceId是否有效，同步接口。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | 需要判断是否有效的HiTraceId实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：HiTraceId有效；false：HiTraceId无效。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是DEFAULT。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.DEFAULT);
// traceIdIsvalid为true
let traceIdIsvalid = hiTraceChain.isValid(traceId);
if (traceIdIsvalid) {
// 基于跟踪标识合法性校验成功的场景的处理逻辑。
}
// 业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.isFlagEnabled

isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean

判断HiTraceId是否启用了跟踪标志flag，同步接口。用于在业务逻辑中根据跟踪标志进行不同处理，例如检查是否启用了INCLUDE\_ASYNC标志以决定是否等待异步操作完成、检查是否启用了TP\_INFO标志以决定是否打印调试信息。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | 需要判断指定跟踪标志是否启用的HiTraceId实例。 |
| flag | [HiTraceFlag](js-apis-hitracechain.md#hitraceflag) | 是 | 指定的跟踪标志。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true：HiTraceId已启用flag；false：HiTraceId未启用flag。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是INCLUDE_ASYNC。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
// enabledIncludeAsyncFlag为true。
let enabledIncludeAsyncFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
if (enabledIncludeAsyncFlag) {
// 基于INCLUDE_ASYNC跟踪标志已设置场景的处理逻辑。
}
// 业务结束，结束跟踪。
hiTraceChain.end(traceId);
```

## hiTraceChain.enableFlag

enableFlag(id: HiTraceId, flag: HiTraceFlag): void

启用HiTraceId中指定的跟踪标志，同步接口。用于在业务流程中动态调整跟踪行为，例如在调试时启用TP\_INFO标志以打印埋点信息、在需要跟踪异步调用时启用INCLUDE\_ASYNC标志、在需要禁用日志关联时启用DISABLE\_LOG标志。

**系统能力**：SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | [HiTraceId](js-apis-hitracechain.md#hitraceid) | 是 | 需要启用指定跟踪标志的HiTraceId实例。 |
| flag | [HiTraceFlag](js-apis-hitracechain.md#hitraceflag) | 是 | 指定的跟踪标志。 |

**示例：**

```ts
// 开始跟踪，跟踪标志是INCLUDE_ASYNC。
let traceId = hiTraceChain.begin("business", hiTraceChain.HiTraceFlag.INCLUDE_ASYNC);
// enabledDoNotCreateSpanFlag为false。
let enabledDoNotCreateSpanFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// 设置DONOT_CREATE_SPAN跟踪标志。
hiTraceChain.enableFlag(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
// enabledDoNotCreateSpanFlag为true。
enabledDoNotCreateSpanFlag = hiTraceChain.isFlagEnabled(traceId, hiTraceChain.HiTraceFlag.DONOT_CREATE_SPAN);
if (enabledDoNotCreateSpanFlag) {
// 基于DONOT_CREATE_SPAN跟踪标志已设置场景的处理逻辑。
}
// 业务结束，结束跟踪。
hiTraceChain.end(traceId);
```
