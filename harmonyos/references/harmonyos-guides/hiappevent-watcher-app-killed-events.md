---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events
title: 应用终止事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用终止事件 > 应用终止事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:68eed57866d62d92ef07111e14e03e6de63ec19868bb45e957f9335739779504
---

## 概述

从API version 20开始，HiAppEvent提供接口用于订阅应用终止事件。

应用终止是指应用程序被系统强制退出的一种现象。与应用崩溃不同，终止并非源于应用自身业务代码的异常，而是主要归因于系统基于资源管控策略而对应用实施的终止行为。

HiAppEvent提供接口用于订阅应用终止事件。

* [订阅应用终止事件（ArkTS）](hiappevent-watcher-app-killed-events-arkts.md)
* [订阅应用终止事件（C/C++）](hiappevent-watcher-app-killed-events-ndk.md)

说明

应用终止事件支持在[应用分身](app-clone.md)场景下使用 HiAppEvent 进行订阅，支持在元服务场景下使用 HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用 HiAppEvent 进行订阅。

应用终止事件信息中params属性的详细描述如下：

## 事件字段说明

### params字段说明

终止事件信息中params属性的详细描述如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位为ms。 |
| reason | string | 终止原因，原因范围详见[reason字段说明](hiappevent-watcher-app-killed-events.md#reason字段说明)。 |
| foreground | boolean | 应用是否处于前台状态。true表示应用处于前台；false表示应用处于后台。 |

### reason字段说明

| 类型 | 说明 |
| --- | --- |
| IllegalAudioRendererBySuspend | 应用未申请合理的后台任务，但是后台有大量音频播放。 |
| LowMemoryKill | 整机低内存。 |
| OomKiller | 整机内存耗尽，无法继续分配。 |
| PowerSaveClean | 整机切换到省电模式或应急模式。 |
| ResourceLeak(AshmemLeak) | 应用Ashmem内存占用超标。 |
| ResourceLeak(GpuLeak) | 应用GPU内存占用超标。 |
| ResourceLeak(GpuRsLeak) | 应用在Render Service进程内的GPU内存占用超标。 |
| ResourceLeak(IonLeak) | 应用的Ion内存占用超标。 |
| RssThresholdKiller | 应用的RSS（Resident Size Set）占用超标。 |
| SwapFull | 整机Swap空间耗尽。 |
