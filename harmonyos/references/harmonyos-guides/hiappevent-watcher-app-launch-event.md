---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-event
title: 启动耗时事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 启动耗时事件 > 启动耗时事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:69807aad2adff44f745f46c0342f678991453f38309a282746505773351cf014
---

## 简介

用户在使用应用时，如果出现点击应用后启动缓慢的情况，并且整个过程超过了一定的时间，就会被定义为启动耗时事件。系统会采集相关流程耗时，并生成HiappEvent事件，供应用开发者分析。

如何使用HiAppEvent提供订阅启动耗时事件的接口可参见以下文档：

* [订阅启动耗时事件（ArkTS）](hiappevent-watcher-app-launch-arkts.md)

说明

启动耗时事件支持在[元服务场景](agc-harmonyos-create-faproject.md)下使用HiAppEvent进行订阅。不支持在[应用分身场景](app-clone.md)或[输入法应用场景](inputmethod-application-guide.md)下使用HiAppEvent进行订阅。

## 事件检测原理

检测原理可参考[启动耗时事件检测](perf-detection.md)。

## 约束与限制

1. 系统在监控应用启动时，依赖多个系统内部事件的打点记录。若这些事件在完成应用启动的5秒内全部完成打点上报，系统将立即生成启动耗时事件，并通过回调函数将事件内容传递给应用；若非关键事件存在缺失，系统将在5秒后根据实际接收到的事件生成启动耗时事件。
2. 单设备上的所有应用在每个自然日内最多可以累计上报2000次启动耗时事件，系统会在每日 0 点重置统计计数。若在一次启动流程中，涉及多个同一依赖事件的触发（如在启动过程中调用多次[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-1)），会导致实际可上报的启动耗时事件数量少于理论上限。
3. 启动完成前（如应用[首帧绘制](ide-profiler-launch-case.md)前）终止启动不会生成启动耗时事件。

## 启动耗时优化指导

启动耗时优化方法可参看[优化应用冷启动时延问题](../best-practices/bpta-application-cold-start-optimization.md)。

## 事件params属性描述

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件生成时间，单位为ms。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| process\_name | string | 应用进程名称。 |
| start\_type | number | 启动类型。0：[冷启动](../best-practices/bpta-application-cold-start-optimization.md#section1235404851116)，1：[热启动](../best-practices/bpta-application-cold-start-optimization.md#section1235404851116)，4：温启动（[预加载](preload-application.md)后启动应用）。 |
| icon\_input\_time | number | 点击桌面应用图标离手时间戳，若无法获取（如语音唤醒）则表示系统开始启动应用的时间戳，单位为ms。 |
| animation\_finish\_time | number | 动效完成耗时，单位为ms。  在无法获取点击离手时间戳或依赖的系统内部事件打点次数超限时，该值为 0。 |
| extend\_time | number | 手指离开屏幕到开发者调用[reportDrawnCompleted](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md#reportdrawncompleted12)接口时间，单位为ms。  若用户不调用或手指离开屏幕后5s未调用reportDrawnCompleted接口，该值为0。 |
| response\_latency | number | 手指离开屏幕到动效开始的耗时，单位为ms。  在无法获取点击离手时间戳或依赖的系统内部事件打点次数超限时，该值为 0。从API version 22开始提供。 |
| laun\_to\_start\_ability\_dur | number | 手指离开屏幕到系统开始启动Ability的耗时，单位为ms。  在无法获取点击离手时间戳或依赖的系统内部事件打点次数超限时，该值为 0。从API version 22开始提供。 |
| startability\_processstart\_dur | number | [冷启动过程](../best-practices/bpta-application-cold-start-optimization.md#section196451814101216)中系统开始启动Ability到完成应用进程创建的耗时，单位为ms。  仅在冷启动中存在该值，若依赖的系统内部事件打点次数超限或在非冷启动类型中，该值为 0。从API version 22开始提供。 |
| processstart\_to\_appattach\_dur | number | 冷启动过程中应用进程初始化的耗时，单位为ms。  仅在冷启动中存在该值，若依赖的系统内部事件打点次数超限或在非冷启动类型中，该值为 0。从API version 22开始提供。 |
| appattach\_to\_appforeground\_dur | number | 冷启动过程中完成应用进程初始化到应用切换到前台的耗时，单位为ms。  该阶段包括资源加载、虚拟机创建、Application&Ability 对象的创建与初始化、依赖模块加载等。  仅在冷启动中存在该值，若依赖的系统内部事件打点次数超限或在非冷启动类型中，该值为 0。从API version 22开始提供。 |
| startability\_appforeground\_dur | number | 启动过程中系统开始启动Ability到应用切换到前台状态的耗时，单位为ms。  在冷启动中，该值为startability\_processstart\_dur、processstart\_to\_appattach\_dur和appattach\_to\_appforeground\_dur三者之和；其余启动类型中，该过程包括系统启动Ability和应用切换到前台。从API version 22开始提供。 |
| appforegr\_abilityonforegr\_dur | number | 应用切换到前台状态到[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)切换至前台（系统触发[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)回调）的耗时，单位为ms。从API version 22开始提供。 |
| abilityonforeg\_startwindow\_dur | number | 系统完成创建应用窗口[WindowStage](application-window-stage.md)（系统触发[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调）到UIAbility切换到前台的耗时，单位为ms。  仅在冷启动和预加载启动中存在该值，若依赖的系统内部事件打点次数超限或在热启动类型中，该值为0。从API version 22开始提供。 |
