---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-intro
title: HiAppEvent介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > HiAppEvent介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f00f08787dc3b1ed0811bdd974fa72e402d9ca1b047455dc962a10f07b3ae3ec
---

## 简介

HiAppEvent是系统为应用开发者提供的事件订阅和事件打点机制，支持记录应用运行过程中的故障、统计、安全和行为事件，帮助开发者定位问题、分析应用运行情况，统计访问量、用户活跃度、操作习惯以及其他影响用户使用产品的关键因素。

## 基本概念

**打点**：记录用户操作引起的变化，提供业务数据信息，供开发、产品、运维分析。

* 事件领域：标识事件的领域，建议设置为业务领域名称，以便于区分不同的业务领域。
* 事件名称：指定事件的名称，建议设置为具体的业务名称，以便于描述实际的业务意义。
* 事件类型：指定事件的类型，支持以下四种类型事件：

  + 行为事件：记录用户日常操作行为的事件，例如按钮点击、界面跳转等行为。
  + 故障事件：定位和分析应用故障的事件，例如界面卡顿、网络中断等故障。
  + 统计事件：统计和度量应用关键行为的事件，例如对使用时长、访问数等的统计。
  + 安全事件：记录涉及应用安全行为的事件，例如用户授权等行为。
* 事件参数：指定事件的参数，每个事件可以包含一组参数，建议设置为事件属性或事件发生的上下文信息，以便于描述事件的详细信息。

**事件订阅**：通过HiAppEvent的接口[addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)，开发者可以注册监听自己关注的系统事件或应用事件。目的是当订阅的事件发生后，接收事件的回调信息并进行处理。

## 实现原理

### 系统事件订阅机制

在当前系统应用沙箱机制下，应用进程仅可以直接访问自己的应用沙箱目录，参考[应用沙箱目录](app-sandbox-directory.md)。而系统事件信息的存放路径不在应用沙箱目录中，因此无法直接获取。

应用调用HiAppEvent的addWatcher接口订阅系统事件并创建共享目录。当应用进程发生故障时，DFX系统捕获相关信息，生成事件和日志，并写入到共享目录。HiAppEvent监听到事件后，将事件回调给应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/K4RqRo0LRmq943oVvUsTuA/zh-cn_image_0000002589324867.png?HW-CC-KV=V1&HW-CC-Date=20260429T053355Z&HW-CC-Expire=86400&HW-CC-Sign=42F8ADBA3B477622CC02511B0AF079110BFB58806BABB6D54A88C81AF0FD5636)

### 应用事件订阅机制

应用调用addWatcher接口订阅关注的应用事件后，还需在应用事件发生时，调用[write](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventwrite-1)接口进行打点，用来记录应用事件。

HiAppEvent通过事件领域和事件名称关联应用事件，并通过addWatcher接口设置的回调方式将事件回调给应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/GgSAEH4ISUaAH0zHsKLmSw/zh-cn_image_0000002589244803.png?HW-CC-KV=V1&HW-CC-Date=20260429T053355Z&HW-CC-Expire=86400&HW-CC-Sign=946D64F6F771D72EBDEC82D4F7A3857D61A0285F8A3CCE34CEED36861A20436E)

说明

若应用已订阅到相关事件，但在触发回调前应用退出，则未回调的事件会在应用下次启动调用addWatcher后进行回调。例如订阅崩溃事件场景，在应用崩溃退出后，下次启动调用addWatcher后执行事件回调。

## 约束与限制

* 订阅接口addWatcher是同步接口，涉及IO操作。对于性能有要求的模块，建议将接口的调用放到非主线程。
* 订阅接口addWatcher传入的名称name是唯一的，相同的name，后一次调用会覆盖前一次的订阅。
* 目前鸿蒙应用有普通应用、[应用分身](app-clone.md)、元服务、[输入法应用](inputmethod-application-guide.md)等多种类型，不同类型应用上，系统事件的订阅规格不同。从API version 22开始，HiAppEvent系统事件订阅能力支持输入法应用。具体规格可参见如下表格：

| 系统事件名称 | 是否支持应用分身订阅 | 是否支持元服务订阅 | 是否支持输入法应用订阅 |
| --- | --- | --- | --- |
| 崩溃事件 | 支持 | 支持 | 支持 |
| 应用冻屏事件 | 支持 | 支持 | 支持 |
| 资源泄漏事件 | 支持 | 支持 | 支持 |
| 地址越界事件 | 支持 | 不支持 | 支持 |
| 主线程超时事件 | 支持 | 支持 | 支持 |
| 任务执行超时事件 | 支持 | 不支持 | 支持 |
| 应用终止事件 | 支持 | 支持 | 支持 |
| 启动耗时事件 | 不支持 | 支持 | 不支持 |
| 滑动丢帧事件 | 不支持 | 支持 | 不支持 |
| CPU高负载事件 | 不支持 | 不支持 | 支持 |
| 24h功耗器件分解统计事件 | 不支持 | 不支持 | 支持 |
| 音频卡顿事件 | 不支持 | 不支持 | 不支持 |
| ArkWeb抛滑丢帧事件 | 支持 | 支持 | 支持 |
