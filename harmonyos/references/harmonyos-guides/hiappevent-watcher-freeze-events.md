---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events
title: 应用冻屏事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏事件 > 应用冻屏事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a58352fb61877762f6c8a244137fe7362f5ddfb20b08f77c33d042bb6f808c2a
---

## 简介

用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用冻屏，也被称为应用无响应。为了应对应用冻屏问题，系统会提供应用冻屏检测、维测日志抓取、日志上报的能力，为开发者提供详细的维测日志以辅助故障定位。

本文面向开发者介绍AppFreeze（应用冻屏）检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅应用冻屏事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅应用冻屏事件（ArkTS）](hiappevent-watcher-freeze-events-arkts.md)。
* [订阅应用冻屏事件（C/C++）](hiappevent-watcher-freeze-events-ndk.md)。

说明

应用冻屏事件支持在[应用分身](app-clone.md)场景下使用 HiAppEvent 进行订阅，支持在元服务场景下使用HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用 HiAppEvent 进行订阅。

## 检测原理

详见[AppFreeze（应用冻屏）检测原理](appfreeze-guidelines.md#检测原理)。

## 事件字段说明

### params字段说明

应用无响应事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位为ms。 |
| foreground | boolean | 应用是否处于前台状态。true表示应用处于前台；false表示应用处于后台。 |
| release\_type | string | 应用的版本类型。release表示应用为[release版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)，debug表示应用为[debug版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。  **说明**：从API version 23开始支持 |
| cpu\_abi | string | 二进制接口类型。  **说明**：从API version 23开始支持。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| process\_name | string | 应用的进程名称。 |
| pid | number | 应用的进程ID。 |
| uid | number | 应用的用户ID。 |
| uuid | string | 根据故障信息生成的故障特征码，用于标识特征相同的崩溃故障。 |
| exception | object | 异常信息，详见exception属性。 |
| hilog | string[] | 日志信息。当生成应用无响应事件日志时，从hilog缓冲区中获取最多100行故障进程日志信息。 |
| event\_handler | string[] | 主线程未处理消息。 |
| event\_handler\_size\_3s | string | [THREAD\_BLOCK\_6S事件](appfreeze-guidelines.md#thread_block_6s-应用主线程卡死超时)（仅在应用无响应事件生效）中3s时任务栈中任务数量。 |
| event\_handler\_size\_6s | string | [THREAD\_BLOCK\_6S事件](appfreeze-guidelines.md#thread_block_6s-应用主线程卡死超时)（仅在应用无响应事件生效）中6s时任务栈中任务数量。 |
| peer\_binder | string[] | binder调用信息。 |
| threads | object[] | 全量线程调用栈，详见thread属性。 |
| memory | object | 内存信息，详见memory属性。 |
| external\_log12+ | string[] | 故障日志文件路径。**为避免目录空间超限（参考log\_over\_limit），导致新生成的日志文件写入失败，日志文件处理完后请及时删除。** |
| log\_over\_limit12+ | boolean | 生成的故障日志文件与已存在的日志文件总大小是否超过5M上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
| process\_life\_time | number | 故障进程存活时间。  **说明**：从API 22开始支持。 |

### exception字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 异常类型 |
| message | string | 异常原因 |

### thread字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| thread\_name | string | 线程名。 |
| tid | number | 线程id。 |
| frames | object[] | 线程调用栈，详见frame属性。 |
| state | string | 线程运行状态。读取自/proc/pid/stat的state的值。  **说明**：从API version 23开始支持。 |
| utime | number | 线程在用户态下消耗的CPU的嘀嗒数。读取自/proc/pid/stat的utime的值。  **说明**：从API version 23开始支持。 |
| stime | number | 线程在内核态下消耗的CPU的嘀嗒数。读取自/proc/pid/stat的stime的值。  **说明**：从API version 23开始支持。 |
| priority | number | 实时优先级。读取自/proc/pid/stat的priority的值。  **说明**：从API version 23开始支持。 |
| nice | number | 静态优先级。读取自/proc/pid/stat的nice的值。  **说明**：从API version 23开始支持。 |
| clk | number | 每秒的时钟嘀嗒次数。使用sysconf(\_SC\_CLK\_TCK)获取，获取失败时使用默认值100。通过嘀嗒数除以该值可以计算得到运行时间（单位：秒）。  **说明**：从API version 23开始支持。 |

### frame字段说明

**Native帧frame字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| symbol | string | 函数名称。**名称长度超过256字节时将被删除，防止超长字符串引起未知问题。** |
| file | string | 文件名。 |
| buildId | string | 文件唯一标识。**文件可能没有buildId**。 |
| pc | string | 程序执行的指令在文件内的偏移十六进制字节数。 |
| offset | number | 程序执行的指令在函数内偏移字节数。 |

详细说明请参见[调用栈帧内容说明](cppcrash-guidelines.md#一般故障场景日志规格)。

**Js帧frame字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| file | string | 文件名 |
| packageName | string | 模块的包名 |
| symbol | string | 函数名称 |
| line | number | 代码行号 |
| column | number | 代码列号 |

详细说明请参见[JS混合栈帧内容说明](cppcrash-guidelines.md#一般故障场景日志规格)。

### memory字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| rss | number | 进程实际占用内存大小，单位KB。对应[Appfreeze日志](appfreeze-guidelines.md#日志头部信息)中Process Memory(kB)字段。 |
| vss | number | 进程向系统申请的虚拟内存大小，单位KB。 |
| pss | number | 进程实际使用的物理内存大小，单位KB。 |
| sys\_free\_mem | number | 空闲内存大小，单位KB。对应[Appfreeze日志](appfreeze-guidelines.md#日志头部信息)中Device Memory(kB)字段的Free。 |
| sys\_avail\_mem | number | 可用内存大小，单位KB。对应[Appfreeze日志](appfreeze-guidelines.md#日志头部信息)中Device Memory(kB)字段的Available。 |
| sys\_total\_mem | number | 总内存大小，单位KB。对应[Appfreeze日志](appfreeze-guidelines.md#日志头部信息)中Device Memory(kB)字段的Total。 |
| vm\_heap\_total\_size | number | 主虚拟机总堆内存大小，单位KB。  **说明**：从API 22开始支持。 |
| vm\_heap\_used\_size | number | 主虚拟机的生命周期过程中，持续统计存活对象的大小，单位KB。  **说明**：从API 22开始支持。 |

## 应用冻屏规格自定义参数设置

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void> | **应用冻屏事件自定义参数设置方法。** |

### 参数设置说明

开发者可以通过该接口订阅name为hiAppEvent.event.APP\_FREEZE的应用冻屏事件，具体使用详见[setEventParam使用](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventseteventparam12)。
