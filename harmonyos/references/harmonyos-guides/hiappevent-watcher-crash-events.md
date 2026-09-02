---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events
title: 崩溃事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 崩溃事件 > 崩溃事件介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ee3863e455492737ef08eca0bc5348cfd4295c130247bc24a8f160c547a034ae
---

## 简介

崩溃是指应用进程非预期退出，以下两种场景会生成崩溃事件：

1. Native代码未处理[崩溃信号](cppcrash-guidelines.md#系统处理的崩溃信号)时，会生成NativeCrash类型崩溃事件。
2. ArkTS/JS代码未处理异常时，会生成JsError类型崩溃事件。

本文面向开发者介绍崩溃事件检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅系统崩溃事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅崩溃事件（ArkTS）](hiappevent-watcher-crash-events-arkts.md)。
* [订阅崩溃事件（C/C++）](hiappevent-watcher-crash-events-ndk.md)。

**说明** 

崩溃事件支持在[应用分身](app-clone.md)和元服务场景下使用HiAppEvent进行订阅。从API version 22开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用HiAppEvent进行订阅。

## 检测原理

### NativeCrash崩溃类型检测原理

系统的进程崩溃检测能力主要基于POSIX信号机制，当进程崩溃后收到崩溃信号，进入系统注册信号处理流程，进行崩溃信息收集、事件生成、事件上报等操作，最终将崩溃事件发布给应用进程的崩溃事件订阅者。

系统检测进程崩溃的详细流程如下：

1. 进程运行时崩溃后收到来自内核发送的崩溃信号，由进程在启动时注册的信号处理模块进行处理。
2. 进程接收到崩溃信号后，保存当前进程上下文并fork出子进程执行ProcessDump二进制抓取崩溃信息。
3. ProcessDump进程收集完崩溃信息后，上报给Hiview进程。Hiview进程将事件信息存储到[应用沙箱目录](app-sandbox-directory.md)。
4. HiAppEvent注册的崩溃事件观察者监听到应用沙箱目录的文件变化，将事件回调给应用进程。

### JsError崩溃类型检测原理

在ArkTS中，JsError崩溃类型检测主要通过全局异常捕获错误，收集完错误对象的类型（如 Error、TypeError、ReferenceError） 上报给Hiview进程。Hiview进程将事件信息存储到[应用沙箱目录](app-sandbox-directory.md)，HiAppEvent注册的崩溃事件观察者监听到应用沙箱目录的文件变化，将事件回调给应用进程，帮助开发者快速定位和修复问题。

## 自定义规格设置

### setEventConfig接口说明

从**API version 20**开始支持设置崩溃日志规格自定义设置。

系统提供通用的NativeCrash崩溃日志生成功能，同时给应用提供设置崩溃日志配置参数功能，以满足其对日志内容的个性化需求。

| 接口名 | 描述 |
| --- | --- |
| setEventConfig(name: string, config: Record<string, ParamType>): Promise<void> | 设置崩溃日志配置参数，name需设置为崩溃事件名称常量hiappevent.event.APP\_CRASH。**仅支持NativeCrash类型崩溃。** |

### setEventConfig接口参数设置说明

开发者可以使用上述HiAppEvent提供的接口，在Record<string, ParamType>中配置崩溃日志打印规格的参数。具体参数说明如下：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extend\_pc\_lr\_printing | boolean | 否 | true：64位系统打印pc和lr寄存器地址向前248字节、向后256字节范围的内存值。32位系统打印pc和lr寄存器地址向前124字节、向后128字节范围的内存值。  false：64位系统打印pc和lr寄存器地址向前16字节、向后232字节范围的内存值。32位系统打印pc和lr寄存器地址向前8字节、向后116字节范围的内存值。  缺省时默认为false。 |
| log\_file\_cutoff\_sz\_bytes | number | 否 | 单位为byte，取值范围为[0, 5242880]。  如果设置，按设置的参数值截断崩溃日志大小。  如果不设置，默认值取0表示不截断崩溃日志。 |
| simplify\_vma\_printing | boolean | 否 | true：只打印崩溃日志中出现的地址所属的VMA（Virtual Memory Area，进程地址空间中的区域）映射信息，即崩溃日志中Maps，以减小日志大小。  false：打印所有VMA映射信息。  缺省时默认为false。 |

参数配置示例如下：

```text
let configParams: Record<string, hiAppEvent.ParamType> = {
    "extend_pc_lr_printing": true, // 使能扩展打印pc和lr寄存器附近的内存值
    "log_file_cutoff_sz_bytes": 102400, // 截断崩溃日志到100KB
    "simplify_vma_printing": true // 使能精简打印maps
};
```

以64位系统为例，参考[订阅崩溃事件（ArkTS）开发步骤](hiappevent-watcher-crash-events-arkts.md#开发步骤)完成崩溃事件订阅和日志配置参数设置，然后通过[external\_log](hiappevent-watcher-crash-events.md#params字段说明)字段获取NativeCrash类型崩溃日志内容。日志中打印如下使能的配置参数列表：

```text
...
Build info:HarmonyOS 6.0.0.33
Enabled app log configs:    <- 使能的配置参数列表，只打印不是默认值的配置参数
Extend pc lr printing:true  <- extend_pc_lr_printing参数设置为true
Log cut off size:102400B    <- 崩溃日志大小截断到100KB
Simplify maps printing:true <- simplify_vma_printing参数设置为true
Timestamp:2025-05-17 19:17:07.000
...
```

崩溃日志详细说明见[应用通过HiAppEvent设置崩溃日志配置参数场景日志规格](cppcrash-guidelines.md#应用通过hiappevent设置崩溃日志配置参数场景日志规格)。

### OH\_HiAppEvent\_SetEventConfig接口说明

从**API version 24**开始支持崩溃日志规格自定义设置，如打印PC和LR寄存器扩展字节范围的内存内容、截断崩溃日志、打印崩溃日志中出现的地址所属的VMA、拼接应用日志。当应用发生崩溃故障时，系统可以按设置的崩溃日志规格收集并上报崩溃日志，帮助开发者定位问题。

从**API version 26.0.0**开始支持使能[minidump](performance-analysis-kit-terminology.md#minidump)。

| 接口名 | 描述 |
| --- | --- |
| int [OH\_HiAppEvent\_SetEventConfig](../harmonyos-references/capi-hiappevent-h.md#oh_hiappevent_seteventconfig)(const char\* name, HiAppEvent\_Config\* config) | 崩溃日志规格自定义设置，拼接应用日志功能接口。**仅支持NativeCrash类型崩溃。** |

### OH\_HiAppEvent\_SetEventConfig接口参数设置说明

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | const char\* | 是 | 应用崩溃事件名称，此处为宏**EVENT\_APP\_CRASH**。 |
| config | HiAppEvent\_Config\* | 是 | 应用崩溃事件配置参数，可使用[OH\_HiAppEvent\_SetConfigItem](../harmonyos-references/capi-hiappevent-h.md#oh_hiappevent_setconfigitem)函数设置config参数的配置项。 |

| 配置项名称 | 类型 | 必须配置 | 说明 |
| --- | --- | --- | --- |
| 宏：OH\_APP\_CRASH\_PARAM\_EXTEND\_PC\_LR\_PRINTING  字符串：extend\_pc\_lr\_printing | const char\* | 否 | 是否打印PC和LR寄存器扩展字节范围的内存内容。  "true"：64位系统打印pc和lr寄存器地址向前248字节、向后256字节范围的内存值。32位系统打印pc和lr寄存器地址向前124字节、向后128字节范围的内存值。  "false"：64位系统打印pc和lr寄存器地址向前16字节、向后232字节范围的内存值。32位系统打印pc和lr寄存器地址向前8字节、向后116字节范围的内存值。  缺省时默认为"false"。  **说明**：从API version 24开始支持该参数。 |
| 宏：OH\_APP\_CRASH\_PARAM\_LOG\_FILE\_CUTOFF\_SZ\_BYTES  字符串：log\_file\_cutoff\_sz\_bytes | const char\* | 否 | 是否截断崩溃日志（CPP\_CRASH日志、minidump），单位为Byte，取值范围为[0, 5242880]。  如果设置，按设置的参数值截断崩溃日志大小。  如果不设置，默认值取0表示不截断崩溃日志。  **说明**：从API version 24开始支持该参数。 |
| 宏：OH\_APP\_CRASH\_PARAM\_SIMPLIFY\_VMA\_PRINTING  字符串：simplify\_vma\_printing | const char\* | 否 | 是否打印崩溃日志中出现的地址所属的VMA（Virtual Memory Area，虚拟内存空间）映射信息。  "true"：只打印崩溃日志中出现的地址所属的VMA映射信息，即崩溃日志中Maps，以减小日志大小。  "false"：打印所有VMA映射信息。  缺省时默认为"false"。  **说明**：从API version 24开始支持该参数。 |
| 宏：OH\_APP\_CRASH\_PARAM\_MERGE\_CPPCRASH\_APP\_LOG  字符串：merge\_cppcrash\_app\_log | const char\* | 否 | 是否拼接应用沙箱的日志。  "true"：在 Native Crash 场景拼接应用日志。  "false"：不拼接应用生成日志。  框架读取的应用日志路径为：沙箱路径 + 应用包名 + \_CppCrash\_AppMerge.log，例如：/data/storage/el2/log/com.samples.eventsub\_CppCrash\_AppMerge.log  如果开发者选择在信号处理函数中生成拼接日志，最长生成时间不超过5s，超过5s无法拼接应用生成的日志。  **注意**：沙箱路径下必须有应用生成的拼接日志。  **说明**：从API version 24开始支持该参数。 |
| 宏：OH\_APP\_CRASH\_PARAM\_COLLECT\_MINIDUMP  字符串：collect\_minidump | const char\* | 否 | 是否使能minidump，默认值为"false"。  "true"：在Native Crash场景同时生成minidump。  "false"：在Native Crash场景不生成minidump。  生成minidump日志文件以.dmp结尾，跟随APP\_CRASH事件一起返回，保存在external\_log字段中。  **说明**：该配置项为持久化配置，应用未重新设置前，值不变。  从API version 26.0.0开始支持该参数。 |

参数设置示例如下：

OH\_HiAppEvent\_SetEventConfig配置参考[订阅崩溃事件（C/C++）开发步骤](hiappevent-watcher-crash-events-ndk.md#开发步骤)完成崩溃事件订阅和日志配置参数设置，然后通过[external\_log](hiappevent-watcher-crash-events.md#params字段说明)字段获取崩溃日志文件路径。

### configEventPolicy接口说明

从**API version 24**开始支持页面切换日志配置。当应用发生崩溃时，系统可以收集并上报页面切换日志，帮助开发者定位问题。

从**API version 26.0.0**开始支持崩溃日志规格自定义设置。系统提供通用的NativeCrash崩溃日志生成功能，同时给应用提供设置崩溃日志配置参数功能，以满足其对日志内容的个性化需求。

| 接口名 | 描述 |
| --- | --- |
| [configEventPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventconfigeventpolicy22) (policy: EventPolicy): Promise<void> | 设置崩溃事件策略参数接口，支持开启崩溃事件的页面切换日志采集，支持设置崩溃日志配置参数。 |

### configEventPolicy接口参数设置说明

开发者可以通过设置[EventPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#eventpolicy22) 的参数来设置崩溃日志配置参数和开启崩溃事件的页面切换日志采集。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appCrashPolicy | [AppCrashPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#appcrashpolicy24) | 否 | 是 | 崩溃事件配置策略。 |

参数设置示例如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

let policy: hiAppEvent.EventPolicy = {
    appCrashPolicy: {
      pageSwitchLogEnable: true, // 启用页面切换日志。从API version 24开始支持该参数
      extendPcLrPrinting: true, // 使能扩展打印pc和lr寄存器附近的内存值。从API版本26.0.0开始支持该参数
      logFileCutoffSzBytes: 102400, // 截断崩溃日志到100KB。从API版本26.0.0开始支持该参数
      simplifyVmaPrinting: true, // 使能精简打印maps。从API版本26.0.0开始支持该参数
      collectMinidump: true // native崩溃场景，使能minidump。从API版本26.0.0开始支持该参数
    }
};
hiAppEvent.configEventPolicy(policy).then(() => {
    hilog.info(0x0000, 'hiAppEvent', `Set crash config policy successfully.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'hiAppEvent', `Failed to set crash config policy. code: ${err.code}, message: ${err.message}`);
});
```

## 事件字段说明

### params字段说明

params是[AppEventInfo](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#appeventinfo)中事件参数对象，包含每个事件参数的参数名和参数值。

系统事件中params包含的字段已由各系统事件定义。

崩溃事件信息中系统预定义的通用信息如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位为ms。 |
| crash\_type | string | 崩溃类型，支持NativeCrash（native代码异常）和JsError（js代码异常）两种类型。检测方法请参见[CppCrash（NativeCrash）检测](cppcrash-guidelines.md)和[Js Crash（JsError）检测](jscrash-guidelines.md)。 |
| foreground | boolean | 应用是否处于前台状态。true表示应用处于前台状态；false表示应用处于后台状态。 |
| release\_type | string | 应用的版本类型。release表示应用为[release版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)，debug表示应用为[debug版本应用](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。  **说明**：从API version 23开始支持。 |
| cpu\_abi | string | 二进制接口类型。  **说明**：从API version 23开始支持。 |
| app\_running\_unique\_id | string | 应用运行时唯一关联的id。  **说明**：从API version 24开始支持该参数。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| pid | number | 应用的进程ID。 |
| uid | number | 应用的用户ID。 |
| uuid | string | 根据故障信息生成的故障特征码，用于标识特征相同的崩溃故障。 |
| exception | object | 异常信息，详见[exception字段说明](hiappevent-watcher-crash-events.md#exception字段说明)。包含故障简要信息，全量故障信息见external\_log文件。 |
| hilog | string[] | 日志信息，最多显示100行hilog日志。更多日志见故障日志文件。 |
| process\_life\_time | number | 故障进程存活时间，单位为s。  **说明**：从API version 22开始支持。 |
| memory | object | 内存信息，详见[memory字段说明](hiappevent-watcher-crash-events.md#memory字段说明)。  **说明**：从API version 22开始支持。 |
| threads | object[] | 全量线程调用栈，详见[thread字段说明](hiappevent-watcher-crash-events.md#thread字段说明)。仅在NativeCrash类型的崩溃事件提供。 |
| external\_log | string[] | [应用沙箱目录](app-sandbox-directory.md)下的故障日志文件路径。开发者可通过路径读取故障日志文件内容。**为避免目录空间超限导致新生成的日志文件写入失败，日志文件处理完后请及时删除，超限规格请参考log\_over\_limit字段。** |
| log\_over\_limit | boolean | 生成的与已存在的故障日志文件的大小总和是否超过5MB上限。true表示超过上限，日志写入失败；false表示未超过上限。  启用[minidump](performance-analysis-kit-terminology.md#minidump)时，上限调整至35MB；关闭minidump时，上限恢复到5MB。 |
| process\_name | string | 故障进程名。  **说明**：从API version 21开始支持。 |
| page\_switch\_log | string | 页面切换日志路径，日志介绍详见[页面切换日志](pageswitch-log.md)。  **说明**：从API version 24开始支持。 |

### exception字段说明

**JsError类型exception字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 异常类型。 |
| message | string | 异常原因。 |
| stack | string | 异常调用栈。 |
| thread\_name | string | 线程名称。  **说明**：从API version 21开始支持。 |
| caught\_by\_errormanager | boolean | 是否注册异常管理捕获。true：已注册异常管理捕获；false：未注册异常管理捕获。  **说明**：从API版本26.0.0开始，支持该字段。 |
| uncatchable\_fault | boolean | 是否为不可捕获的异常类型，当前仅包含OutOfMemoryError。true：不可捕获的异常类型；false：可捕获的异常类型。  **说明**：从API版本26.0.0开始，支持该字段。 |

**NativeCrash类型exception字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 异常原因。 |
| signal | object | 信号信息，详见[signal字段说明](hiappevent-watcher-crash-events.md#signal字段说明)。 |
| thread\_name | string | 线程名称。 |
| tid | number | 线程ID。 |
| frames | object[] | 线程调用栈，详见[frame字段说明](hiappevent-watcher-crash-events.md#frame字段说明)。 |

### signal字段说明

具体内容请参考[CppCrash（进程崩溃）检测实现原理](cppcrash-guidelines.md#实现原理)。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| signo | number | 信号值。 |
| code | number | 信号二级分类。 |
| address | string | 访问出错的地址。 |

### thread字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| thread\_name | string | 线程名称。 |
| tid | number | 线程ID。 |
| frames | object[] | 线程调用栈，详见[frame字段说明](hiappevent-watcher-crash-events.md#frame字段说明)。 |

### frame字段说明

**Native frame字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| file | string | 文件名称。 |
| symbol | string | 函数名称。symbol为空可能是由于以下两种原因：  **1. 二进制文件中没有保存该函数名信息。**  **2. 函数名称长度超过256字节时将被全部删除，以防止超长字符串引起未知问题。** |
| buildId | string | 来源于elf中.note.gnu.build-id。 |
| pc | string | 程序执行的指令在文件内的偏移十六进制字节数。 |
| offset | number | 程序执行的指令在函数内偏移字节数。 |

详细说明请参见[调用栈帧内容说明](cppcrash-guidelines.md#一般故障场景日志规格)。

**Js frame字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| file | string | 文件名。 |
| packageName | string | 模块的包名。 |
| symbol | string | 函数名称。 |
| line | number | 代码行号。 |
| column | number | 代码列号。 |

详细说明请参见[JS混合栈帧内容说明](cppcrash-guidelines.md#一般故障场景日志规格)。

### memory字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| rss | number | 进程实际占用内存大小，单位KB。对应[cppcrash日志](cppcrash-guidelines.md#日志规格)或[jscrash日志](jscrash-guidelines.md#日志规格)中Process Memory字段。 |
| sys\_free\_mem | number | 空闲内存大小，单位KB。对应[cppcrash日志](cppcrash-guidelines.md#日志规格)或[jscrash日志](jscrash-guidelines.md#日志规格)中Device Memory字段的Free。 |
| sys\_avail\_mem | number | 可用内存大小，单位KB。对应[cppcrash日志](cppcrash-guidelines.md#日志规格)或[jscrash日志](jscrash-guidelines.md#日志规格)中Device Memory字段的Available。 |
| sys\_total\_mem | number | 总内存大小，单位KB。对应[cppcrash日志](cppcrash-guidelines.md#日志规格)或[jscrash日志](jscrash-guidelines.md#日志规格)中Device Memory字段的Total。 |

## 崩溃事件自定义参数设置

当前崩溃事件上报系统通用崩溃信息，可能无法满足开发者的个性化需求，因此提供事件setEventParam方法，自定义事件上报信息。

### 自定义参数设置接口

| 接口名 | 描述 |
| --- | --- |
| setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void> | 事件自定义参数设置方法。 |
