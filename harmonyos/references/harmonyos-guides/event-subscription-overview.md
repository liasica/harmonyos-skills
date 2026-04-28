---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/event-subscription-overview
title: 事件订阅简介
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 事件订阅简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68f819046a323d19ba4f2c22278738fc698affaef926a1ca9afcd6ac55e08e9d
---

## 事件介绍

HiAppEvent能够订阅应用事件和系统事件。

### 应用事件

应用事件由开发者自行定义，例如点击按钮。应用事件的事件参数对象params包含的字段来源于应用，由开发者通过打点接口[write](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventwrite-1)自定义配置。具体字段含义根据开发者需求确定。

### 系统事件

系统事件是指应用运行期间发生的性能、功耗、稳定性等问题。系统事件的事件参数对象params包含的字段来源于系统服务，已由系统服务定义。此外，系统事件中的崩溃事件和应用冻屏事件还支持开发者通过[setEventParam](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventseteventparam12)接口向事件参数对象params中添加自定义参数。

已支持的系统事件介绍、检测原理及事件参数对象params包含的字段说明，请查阅各系统事件介绍的详细文档。

[崩溃事件介绍](hiappevent-watcher-crash-events.md)

[应用冻屏事件介绍](hiappevent-watcher-freeze-events.md)

[资源泄漏事件介绍](hiappevent-watcher-resourceleak-events.md)

[地址越界事件介绍](hiappevent-watcher-address-sanitizer-events.md)

[主线程超时事件介绍](hiappevent-watcher-mainthreadjank-events.md)

[任务执行超时事件介绍](hiappevent-watcher-apphicollie-events.md)

[应用终止事件介绍](hiappevent-watcher-app-killed-events.md)

[ArkWeb抛滑丢帧事件介绍](hiappevent-watcher-web-fling-jank-events.md)

[启动耗时事件介绍](hiappevent-watcher-app-launch-event.md)

[滑动丢帧事件介绍](hiappevent-watcher-scroll-jank-event.md)

[CPU高负载事件介绍](hiappevent-watcher-cpu-usage-high-event.md)

[24h功耗器件分解统计事件介绍](hiappevent-watcher-battery-usage-event.md)

[音频卡顿事件介绍](hiappevent-watcher-audio-jank-event.md)

## 事件订阅的三种方式

HiAppEvent通过[addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)接口提供系统事件的订阅功能，支持三种订阅方式。

方式一：设置回调条件triggerCondition，实现onTrigger()回调。当满足回调条件时，系统将自动触发回调。

方式二：未设置回调条件参数，使用事件订阅返回的holder对象主动获取监听的事件。

说明

主动获取监听的事件时，如果事件未生成或者日志信息未捕获完成，查询结果可能为空。此时，建议多次调用查询接口。

方式三：实现onReceive()回调，当监听的事件发生后实时触发回调。

ArkTS接口事件订阅参考[hiAppEvent.addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)；C/C++接口事件订阅只支持方式一和方式三，参考[事件订阅](hiappevent-watcher-app-events-ndk.md#步骤二订阅事件)。
