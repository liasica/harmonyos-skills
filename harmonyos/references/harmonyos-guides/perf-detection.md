---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/perf-detection
title: 性能检测
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 性能检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6706b4a69bc23fa5bb38f6854cd9711bc34c03f0d7f3fab607a8f454d380cd5e
---

## 启动耗时事件检测

## 简介

启动耗时事件是用于度量应用启动过程在系统可感知阶段耗时的事件，主要是针对用户可感知的应用启动过程进行性能度量，包括桌面启动、状态栏启动、最近任务列表启动等场景。开发者订阅此事件可以获取到启动过程中关键阶段耗时。

### 实现原理

启动事件统计时间起点为用户点击屏幕，默认结束点为启动动效完成，使用者可调用[reportDrawCompleted](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#reportdrawncompleted10)接口根据实际情况传入定制结束时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/KUi04y5dT5qXZq7cWxec3A/zh-cn_image_0000002589244801.png?HW-CC-KV=V1&HW-CC-Date=20260429T053353Z&HW-CC-Expire=86400&HW-CC-Sign=19B0B7003407F5E0EDD9C80EE83BC55781554F7642FF08278184080A0D4ACE8E)

icon\_input\_time：用户点击屏幕时间点。

animation\_finish\_time：系统定义的启动耗时，开发者无法干预，该时间为手指离开屏幕到启动动效结束的时间。

extend\_time：开发者定制的启动耗时，该时间为手指离开屏幕到开发者调用[reportDrawnCompleted](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md#reportdrawncompleted12)接口的时间。开发者可以根据业务需要在合适的时机调用reportDrawnCompleted接口，不调用或手指离开屏幕后5s未调用则该指标大小为0。

### 约束与限制

1. 启动事件是指用户操作的应用启动，不包括进程自动重启等情况。
2. 启动时间为行为类事件，触发后即上报不受阈值限制。

### 事件获取方式

可以通过订阅HiAppEvent获取启动耗时事件及其相关信息，详见[HiAppEvent介绍](hiappevent-intro.md)。参考[订阅启动耗时事件（ArkTS）](hiappevent-watcher-app-launch-arkts.md)完成启动耗时事件订阅。

## 滑动事件检测

## 简介

滑动丢帧事件用于检测列表滑动过程中产生的卡顿，订阅此事件后，会在列表滑动中出现超过50ms的卡顿时上报故障事件。

### 实现原理

1. 计算方法：

   当列表滑动过程中应用主线程或者RenderService绘制流程中出现卡顿时上报此事件。

   其中滑动过程从手势识别为滑动开始到页面滑动停止结束。从应用主线程和RenderService绘制分别计算卡顿时长。
2. 上报阈值：

   最大单帧耗时超过50ms则为滑动丢帧，具体规则为max\_render\_frametime或max\_app\_frametime超过50ms时 会触发该事件上报。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/HohAJ-OGTZ-b5c5KVAL0Dw/zh-cn_image_0000002558764996.png?HW-CC-KV=V1&HW-CC-Date=20260429T053353Z&HW-CC-Expire=86400&HW-CC-Sign=65311A27B03C47DD434929D7BD4023EE0BBA3FC11AB234718EAFCBA8C62EEC15)

### 约束与限制

滑动单帧耗时不超过50ms时不会触发上报。

## 滑动丢帧日志采集机制

滑动丢帧事件会触发主线程的调用栈采集。

1. 启动时间

   滑动丢帧的采样栈功能仅在滑动过程中开启。
2. 采栈时间

   在滑动过程中，如果应用主线程出现了达到上报阈值的卡顿，则触发采栈。

## 滑动丢帧事件日志规格

1. 日志老化规格

   一般情况，栈文件的大小为7-10KB。应用沙箱内的watchdog目录最大保存10M内容，超出后，需要用户手动清 理文件。目录地址：/data/storage/el2/log/watchdog/。

   若用户未主动清理，系统会触发清理。
2. 事件里如何获取日志

   从external\_logs中获取日志路径。
3. 采样栈的格式

   抓栈功能目前只支持ARM64架构，抓栈结果为解析后的混合栈信息，包含native帧和JS帧。此日志为避免过度消耗系统资源，一个进程一天至多采集一次。

抓栈结果部分示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/2BroqMtSR_GoSWyBoVtrFA/zh-cn_image_0000002558605340.png?HW-CC-KV=V1&HW-CC-Date=20260429T053353Z&HW-CC-Expire=86400&HW-CC-Sign=ACF602D15FACF795713E5F1D18F2F19583A2A522E5C4E2EAA04DE7BA54BEF956)

此采样栈包含在滑动出现超过50ms卡顿时应用主线程调用信息，由于一般滑动卡顿过程较短，因此在出现问题时采集了一次调用栈。可根据同一场景卡顿上报的采样栈数据进行聚类，以判断该场景下滑动卡顿的具体根因。采样栈具体解析方法详见[主线程超时调用栈日志规格](apptask-timeout-guidelines.md#日志规格)。

### 日志获取方式

HiAppEvent给开发者提供了故障订阅接口，详见[HiAppEvent介绍](hiappevent-intro.md)。参考[订阅滑动丢帧事件（ArkTS）](hiappevent-watcher-scroll-jank-arkts.md)完成滑动丢帧事件订阅。
