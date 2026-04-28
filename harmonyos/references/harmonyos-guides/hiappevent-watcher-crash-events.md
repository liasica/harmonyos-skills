---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events
title: 崩溃事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 崩溃事件 > 崩溃事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c66bbe6f91a07f62e09edaf790e55f6cfbb970a56d470e7cec0a814f0617620c
---

## 简介

崩溃是指应用进程非预期退出，以下两种场景会生成崩溃事件：

1. Native代码未处理[崩溃信号](cppcrash-guidelines.md#系统处理的崩溃信号)时，会生成NativeCrash类型崩溃事件。
2. ArkTS/JS代码未处理异常时，会生成JsError类型崩溃事件。

本文面向开发者介绍崩溃事件检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅系统崩溃事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅崩溃事件（ArkTS）](hiappevent-watcher-crash-events-arkts.md)。
* [订阅崩溃事件（C/C++）](hiappevent-watcher-crash-events-ndk.md)。

说明

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

## 崩溃日志规格自定义参数设置

从**API version 20**开始支持设置崩溃日志规格自定义设置。

系统提供通用的NativeCrash崩溃日志生成功能，同时给应用提供设置崩溃日志配置参数功能，以满足其对日志内容的个性化需求。

### **接口说明**

| 接口名 | 描述 |
| --- | --- |
| setEventConfig(name: string, config: Record<string, ParamType>): Promise<void> | 设置崩溃日志配置参数，name需设置为崩溃事件名称常量hiappevent.event.APP\_CRASH。**仅支持NativeCrash类型崩溃。** |

### **参数设置说明**

开发者可以使用上述HiAppEvent提供的接口，在Record<string, ParamType>中配置崩溃日志打印规格的参数。具体参数说明如下：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extend\_pc\_lr\_printing | boolean | 否 | true：64位系统打印pc和lr寄存器地址向前248字节、向后256字节范围的内存值。32位系统打印pc和lr寄存器地址向前124字节、向后128字节范围的内存值。  false：64位系统打印pc和lr寄存器地址向前16字节、向后232字节范围的内存值。32位系统打印pc和lr寄存器地址向前8字节、向后116字节范围的内存值。  缺省时默认为false。 |
| log\_file\_cutoff\_sz\_bytes | number | 否 | 单位为byte，取值范围为[0-5242880]。  如果设置，按设置的参数值截断崩溃日志大小。  如果不设置，默认值取0表示不截断崩溃日志。 |
| simplify\_vma\_printing | boolean | 否 | true：只打印崩溃日志中出现的地址所属的VMA（Virtual Memory Area，进程地址空间中的区域）映射信息，即崩溃日志中Maps，以减小日志大小。  false：打印所有VMA映射信息。  缺省时默认为false。 |

参数配置示例如下:

```
1. let configParams: Record<string, hiAppEvent.ParamType> = {
2. "extend_pc_lr_printing": true, // 使能扩展打印pc和lr寄存器附近的内存值
3. "log_file_cutoff_sz_bytes": 102400, // 截断崩溃日志到100KB
4. "simplify_vma_printing": true // 使能精简打印maps
5. };
```

以32位系统为例，参考[订阅崩溃事件（ArkTS）开发步骤](hiappevent-watcher-crash-events-arkts.md#开发步骤)完成崩溃事件订阅和日志配置参数设置，然后通过[external\_log](hiappevent-watcher-crash-events.md#params字段说明)字段获取NativeCrash类型崩溃日志内容。日志中打印如下使能的配置参数列表：

```
1. ...
2. Build info:HarmonyOS 6.0.0.33
3. Enabled app log configs:    <- 使能的配置参数列表，只打印不是默认值的配置参数
4. Extend pc lr printing:true  <- extend_pc_lr_printing参数设置为true
5. Log cut off size:102400B    <- 崩溃日志大小截断到100KB
6. Simplify maps printing:true <- simplify_vma_printing参数设置为true
7. Timestamp:2025-05-17 19:17:07.000
8. ...
```

崩溃日志详细说明见[应用通过HiAppEvent设置崩溃日志配置参数场景日志规格](cppcrash-guidelines.md#应用通过hiappevent设置崩溃日志配置参数场景日志规格)。

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
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| pid | number | 应用的进程ID。 |
| uid | number | 应用的用户ID。 |
| uuid | string | 根据故障信息生成的故障特征码，用于标识特征相同的崩溃故障。 |
| exception | object | 异常信息, 详见[exception字段说明](hiappevent-watcher-crash-events.md#exception字段说明)。包含故障简要信息，全量故障信息见external\_log文件。 |
| hilog | string[] | 日志信息，最多显示100行hilog日志。更多日志见故障日志文件。 |
| process\_life\_time | number | 故障进程存活时间，单位为s。  **说明**：从API version 22开始支持。 |
| memory | object | 内存信息，详见[memory字段说明](hiappevent-watcher-crash-events.md#memory字段说明)。  **说明**：从API version 22开始支持。 |
| threads | object[] | 全量线程调用栈，详见[thread字段说明](hiappevent-watcher-crash-events.md#thread字段说明)。仅在NativeCrash类型的崩溃事件提供。 |
| external\_log | string[] | 故障日志文件[应用沙箱路径](app-sandbox-directory.md)。开发者可通过路径读取故障日志文件内容。**为避免目录空间超限导致新生成的日志文件写入失败，日志文件处理完后请及时删除，超限规格请参考log\_over\_limit字段。** |
| log\_over\_limit | boolean | 生成的与已存在的故障日志文件的大小总和是否超过5M上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
| process\_name | string | 故障进程名。  **说明**：从API version 21开始支持。 |

### exception字段说明

**JsError类型exception字段说明**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 异常类型。 |
| message | string | 异常原因。 |
| stack | string | 异常调用栈。 |
| thread\_name | string | 线程名称。  **说明**：从API version 21开始支持。 |

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
| buildId | string | 文件唯一标识。**文件可能没有buildId**。 |
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
