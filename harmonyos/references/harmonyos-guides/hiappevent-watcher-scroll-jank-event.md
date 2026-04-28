---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-event
title: 滑动丢帧事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 滑动丢帧事件 > 滑动丢帧事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5435a8defab5efe3336469c8169f233a67b8e88e664615c928533a4e137090d
---

## 简介

用户在使用应用时，如果出现滑动列表丢帧的情况，并且持续时间超过一定限制，就会被定义为滑动卡顿，并生成HiAppEvent日志，供应用开发者分析。

如何使用HiAppEvent提供订阅滑动丢帧事件的接口可参见以下文档：

* [订阅滑动丢帧事件（ArkTS）](hiappevent-watcher-scroll-jank-arkts.md)

说明

滑动丢帧事件支持在[元服务场景](agc-harmonyos-create-faproject.md)下使用HiAppEvent进行订阅。不支持在[应用分身场景](app-clone.md)或[输入法应用场景](inputmethod-application-guide.md)下使用HiAppEvent进行订阅。

## 事件检测原理

具体检测原理可参见[滑动事件检测](perf-detection.md#section191899590502)章节。

## 事件params属性描述

**params属性：**

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件生成时间，单位为ms。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| process\_name | string | 应用进程名称。 |
| ability\_name | string | 应用界面名称。 |
| begin\_time | number | 滑动开始时间，单位为ms。 |
| duration | number | 持续时间，单位为ms。 |
| total\_app\_frames | number | 应用线程绘帧总数。 |
| total\_app\_missed\_frames | number | 应用线程丢帧总数。 |
| max\_app\_frametime | number | 应用线程最大单帧耗时，单位ms。 |
| max\_app\_seq\_frames | number | 应用线程最长连续丢帧。 |
| total\_render\_frames | number | 图形绘帧总数。 |
| total\_render\_missed\_frames | number | 图形丢帧总数。 |
| max\_render\_frametime | number | 图形最大单帧耗时，单位ms。 |
| max\_render\_seq\_frames | number | 图形线程最长连续丢帧。 |
| external\_log | string[] | 应用主线程调用栈文件路径，应用存续生命周期内，采集频次限制为每日一次（应用重启会重置采集计次限制）。**应用启动初始10s不会触发检测采集。为避免目录空间超限（限制参考log\_over\_limit），导致新生成的日志文件写入失败，日志文件处理完后请及时删除。** |
| log\_over\_limit | boolean | 生成的故障日志文件与已存在的日志文件总大小是否超过10M上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
