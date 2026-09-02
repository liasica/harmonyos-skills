---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-appfreeze-fault-detection-mechanism
title: 应用冻屏故障检测机制及规格说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 应用冻屏故障模式说明 > 应用冻屏故障检测机制及规格说明
category: best-practices
scraped_at: 2026-09-02T14:53:46+08:00
doc_updated_at: 2026-08-17
content_hash: sha256:47fdc7bc0854e250d88cdd77d480e4d2545b15387a9bdfa4ff369b27e6979549
---

## 概述

用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用冻屏（AppFreeze），即应用无响应。系统会检测应用无响应，并生成AppFreeze日志，供应用开发者分析。

## 故障检测机制

应用冻屏检测从主线程任务队列、用户输入事件及UIAbility生命周期三个维度出发，依据各自设定的时间阈值进行超时判定。一旦触发超时，即进入冻屏故障处理流程，依次完成信息收集、事件生成与上报，并将冻屏事件分发给应用进程内已注册的订阅者。同时，为保障应用可恢复性，系统将强制终止该应用进程。

应用冻屏检测事件和说明：

| 事件类型 | 说明 | 所属故障类型 |
| --- | --- | --- |
| THREAD\_BLOCK\_3S | 应用冻屏告警事件，应用主线程执行任务超过3s时触发。  **说明**：从API版本26.0.0开始，支持该类型。 | [THREAD\_BLOCK\_6S应用主线程卡死超时](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时) |
| THREAD\_BLOCK\_6S | 应用冻屏事件，应用主线程执行任务超过6s时触发。 | [THREAD\_BLOCK\_6S应用主线程卡死超时](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时) |
| APP\_INPUT\_BLOCK | 应用冻屏事件，用户输入响应超时。 | [APP\_INPUT\_BLOCK用户输入响应超时](../harmonyos-guides/appfreeze-guidelines.md#app_input_block用户输入响应超时) |
| LIFECYCLE\_HALF\_TIMEOUT | 应用冻屏告警事件， UIAbility生命周期切换过程中，超过半生命周期阈值时触发。  **说明**：从API版本26.0.0开始，支持该类型。 | [LIFECYCLE\_TIMEOUT生命周期切换超时](../harmonyos-guides/appfreeze-guidelines.md#lifecycle_timeout生命周期切换超时) |
| LIFECYCLE\_TIMEOUT | 应用冻屏事件，UIAbility生命周期切换超时。  **说明**：从API版本26.0.0开始，支持该类型。 | [LIFECYCLE\_TIMEOUT生命周期切换超时](../harmonyos-guides/appfreeze-guidelines.md#lifecycle_timeout生命周期切换超时) |

根据应用冻屏触发的原因，系统将应用冻屏划分为4类二级根因，以及17类三级根因，如下表所示：

| 一级根因 | 二级根因 | 三级根因 |
| --- | --- | --- |
| 应用冻屏 | 应用主线程阻塞 | [等锁](bpta-app-main-thread-block.md#section138261239153915) |
| [同步Binder接口调用阻塞](bpta-app-main-thread-block.md#section715018255107) |
| [对端Binder线程满](bpta-app-main-thread-block.md#section46121838121717) |
| [同步耗时I/O操作](bpta-app-main-thread-block.md#section128357941815) |
| [触发长时间GC](bpta-app-main-thread-block.md#section192572721819) |
| [触发长时间抓取内存快照](bpta-app-main-thread-block.md#section763875871819) |
| [执行耗时操作](bpta-app-main-thread-block.md#section1137920772012) |
| 应用主线程繁忙 | [频繁等锁](bpta-app-main-thread-busy.md#section15741142111511) |
| [频繁调用Binder接口](bpta-app-main-thread-busy.md#section1249193810202) |
| [频繁执行I/O操作](bpta-app-main-thread-busy.md#section711018112112) |
| [频繁执行UI操作](bpta-app-main-thread-busy.md#section6164181919215) |
| [频繁执行特定业务](bpta-app-main-thread-busy.md#section5769184718215) |
| [执行耗时操作](bpta-app-main-thread-busy.md#section9745134227) |
| ArkWeb GPU进程卡死 | [I/O阻塞](bpta-arkweb-gpu-freeze.md#section119813221081) |
| [等锁](bpta-arkweb-gpu-freeze.md#section156717367109) |
| ArkWeb Render进程卡死 | [线程执行繁忙](bpta-arkweb-render-freeze.md#section5119151212336) |
| [执行耗时JS](bpta-arkweb-render-freeze.md#section7907171716331) |

## 日志规格

HarmonyOS系统在应用冻屏之后，采集到的冻屏现场信息会生成应用冻屏日志，应用冻屏日志中包含进程基本信息、堆栈信息、对端信息、CPU信息、内存信息等结构化字段，详见[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。

掌握日志规格是问题定位的前提，开发者需要熟悉各字段的语义，才能从日志关键段落中快速定位问题。

## 日志获取方式

HarmonyOS提供多种方式获取应用冻屏日志，包括开发态和运维态，开发者可根据当前所处的开发阶段选择对应方式，详见[日志获取](../harmonyos-guides/appfreeze-guidelines.md#日志获取)。

## 订阅应用冻屏事件

详见[应用冻屏事件介绍](../harmonyos-guides/hiappevent-watcher-freeze-events.md)。

## 聚类规则

详见[AppFreeze聚类](../harmonyos-guides/appfreeze-guidelines.md#appfreeze聚类)。
