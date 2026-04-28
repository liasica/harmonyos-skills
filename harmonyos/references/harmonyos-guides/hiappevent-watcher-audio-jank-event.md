---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event
title: 音频卡顿事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 音频卡顿事件 > 音频卡顿事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea01ad06daa898565620d15aa9554f494d77860b33c47e1c97f80be3ef09c1a9
---

## 简介

从API version 21开始，支持订阅音频卡顿事件。音频卡顿事件是指音频流卡顿导致的音频播放不流畅，音频卡顿发生场景可以分为应用进程问题卡顿、系统问题卡顿。当出现音频长时间无数据时被定义为音频卡顿事件，并生成HiAppEvent日志，供应用开发者分析。如何使用HiAppEvent订阅音频卡顿事件可参见以下文档：

* [订阅音频卡顿事件（ArkTS）](hiappevent-watcher-audio-jank-event-arkts.md)
* [订阅音频卡顿事件（C/C++）](hiappevent-watcher-audio-jank-event-c.md)

说明

音频卡顿事件不支持在[应用分身场景](app-clone.md)、[输入法应用场景](inputmethod-application-guide.md)或[元服务场景](agc-harmonyos-create-faproject.md)下使用HiAppEvent进行订阅。

## 检测原理

* **应用卡顿**：通过检测应用将音频数据写入音频引擎的共享缓冲区超时异常，来判断是否为**应用进程问题导致卡顿**。当应用在120ms内未传入音频数据时，将触发上报音频卡顿事件。
* **系统卡顿：** 通过检测音频引擎周期性处理数据超时异常，来判断是否为**系统进程问题导致卡顿**。当单次音频引擎处理时长达到200ms时触发上报音频卡顿事件。

## params字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 音频卡顿事件生成时间，单位为ms。 |
| bundle\_version | string | 音频卡顿应用版本名称。 |
| bundle\_name | string | 音频卡顿应用包名。 |
| max | number | 音频卡顿丢帧时长，单位为ms。 |
| happen\_time | number | 音频卡顿丢帧开始时间，单位为ms。 |
| fault\_type | string | 故障类型。  “application”表示应用卡顿；  “system” 表示系统卡顿。 |
