---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events
title: 任务执行超时事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 任务执行超时事件 > 任务执行超时事件介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:33733d8e38a37fd31002664289331edf2ef4782c4edc96a221e43264cbc0d952
---

## 简介

任务执行超时指要监控的业务代码逻辑执行时长超过业务逻辑预期时间。为了更好地定位和分析问题，开发者可以利用[任务执行超时检测](apptask-timeout-guidelines.md#任务执行超时检测)机制，根据生成的[日志规格](apptask-timeout-guidelines.md#日志规格)，主动分析任务执行超时的执行情况。

本文面向开发者介绍任务执行超时检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅任务执行超时事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅任务执行超时事件（ArkTS）](hiappevent-watcher-apphicollie-events-arkts.md)。
* [订阅任务执行超时事件（C/C++）](hiappevent-watcher-apphicollie-events-ndk.md)。

**说明** 

任务执行超时事件支持在[应用分身](app-clone.md)场景下使用 HiAppEvent 进行订阅，不支持在元服务场景下使用HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用 HiAppEvent 进行订阅。

## 检测原理

详见[任务执行超时检测原理](apptask-timeout-guidelines.md#任务执行超时检测)。

## 事件字段说明

### params字段说明

任务执行超时事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位为ms。 |
| foreground | boolean | 应用是否处于前台状态。true表示应用处于前台；false表示应用处于后台。 |
| bundle\_version | string | 应用版本。 |
| process\_name | string | 应用的进程名称。 |
| pid | number | 应用的进程ID。 |
| uid | number | 应用的用户ID。 |
| uuid | string | 根据故障信息生成的故障特征码，用于标识特征相同的崩溃故障。 |
| exception | object | 异常信息，详见[exception字段说明](hiappevent-watcher-apphicollie-events.md#exception字段说明)。 |
| hilog | string[] | 日志信息。 |
| peer\_binder | string[] | binder调用信息，binder调用链及相关抓栈信息。 |
| memory | object | 内存信息，详见[memory字段说明](hiappevent-watcher-apphicollie-events.md#memory字段说明)。 |
| external\_log | string[] | 故障日志文件路径。**为避免目录空间超限（限制参考log\_over\_limit），导致新生成的日志文件写入失败，日志文件处理完后请及时删除。** |
| log\_over\_limit | boolean | 生成的故障日志文件与已存在的日志文件总大小是否超过5MB上限。true表示超过上限，日志写入失败；false表示未超过上限。  启用[minidump](performance-analysis-kit-terminology.md#minidump)时，上限调整至35MB；关闭minidump时，上限恢复到5MB。 |
| external\_callback\_log | string | 自定义回调日志信息，可通过[OH\_HiCollie\_SetFreezeCallback](../harmonyos-references/capi-hicollie-h.md#oh_hicollie_setfreezecallback)写入。  **说明**：从API version 24开始支持。 |

### exception字段说明

exception属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 异常类型。 |
| message | string | 异常原因。 |

### memory字段说明

memory属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| rss | number | 进程实际占用内存大小，单位KB。 |
| vss | number | 进程向系统申请的虚拟内存大小，单位KB。 |
| pss | number | 进程实际使用的物理内存大小，单位KB。 |
| sys\_free\_mem | number | 空闲内存大小，单位KB。 |
| sys\_avail\_mem | number | 可用内存大小，单位KB。 |
| sys\_total\_mem | number | 总内存大小，单位KB。 |
