---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-79
title: 如何收集应用崩溃信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何收集应用崩溃信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:28766b1483ae31acc6587fa55c200155e4affd97c0bd7ab7343743e4172ea6e6
---

## 问题现象

有哪些收集HarmonyOS应用崩溃信息的方式？各个方式之间有什么区别？

## 背景知识

为了更好的帮助开发者定位HarmonyOS应用问题，HarmonyOS提供[ErrorManager](../harmonyos-references/js-apis-app-ability-errormanager.md)、[HiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)和[FaultLogger](../harmonyos-references/js-apis-faultlogger.md)三种崩溃收集方式采集日志分析。

相较于前三种系统侧提供的开发接口外，也可以使用[APMS](../app/agc-help-apms-introduction-0000002236333914.md)（应用性能检测服务）和[DevEco Service](https://devecoservice.harmonyos.com/documentCenter)（智能分析平台）这两种现成的应用质量监测方案。

## 解决方案

Performance Analysis Kit、APMS和智能分析平台三种崩溃信息收集方式，有以下区别：

| 方式 | 故障检测范围 | 集成方式 | 成本 | 使用场景 |
| --- | --- | --- | --- | --- |
| Performance Analysis Kit | JS崩溃、C++崩溃、Freeze无响应 | 通过集成系统提供的开发接口 | 需要一定的开发成本 | 业务定制化信息采集 |
| APMS | JS崩溃、C++崩溃、Freeze无响应 | 在AGC上直接开启相关服务 | 零成本快速使用 | 专业数据化分析场景下使用 |
| 智能分析平台 | JS崩溃、C++崩溃、Freeze无响应 | 直接登入分析平台使用 | 零成本快速使用 | 应用异常分析 |

1. Performance Analysis Kit提供了FaultLogger、ErrorManager和HiAppEvent三种崩溃收集方式差异分析，主要从作用范围、触发机制、使用场景和崩溃表现上有以下四方面区分：

   | 方式 | 作用范围 | 触发方式 | 场景 | 崩溃表现 |
   | --- | --- | --- | --- | --- |
   | ErrorManager | JS崩溃、应用冻结 | 主动查询 | 错误通知（进程内处理） | 抛出错误信息，进程不退出 |
   | FaultLogger | JS崩溃、C++崩溃、应用冻结 | 观察者模式回调 | 主动查询近期故障日志（可实时） | 抛出错误日志，进程不退出 |
   | HiAppEvent | JS崩溃、C++崩溃、应用冻结 | 观察者模式回调 | 事件记录和监听（下次启动处理） | 进程退出，下次进入应用时处理崩溃信息 |

   * 三种崩溃日志的收集方式，主要是通过系统提供的接口来采集崩溃时的自定义日志信息。ErrorManager通过注册错误观测器[errorManager.on('error')](../harmonyos-references/js-apis-app-ability-errormanager.md#errormanageronerror)捕获到应用产生的crash；FaultLogger则是通过主动查询[FaultLogger.query(faultType, callback)](../harmonyos-references/js-apis-faultlogger.md#faultloggerquery9)，再由回调函数的方式获取故障信息；而HiAppEvent则是通过[hiAppEvent.addWatcher(watcher)](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)添加事件观察者订阅崩溃事件信息。
   * ErrorManager主要观测应用发生JS Crash和AppFreeze等崩溃，而HiAppEvent和FaultLogger主要观测JS Crash、Cpp Crash、应用冻结等崩溃。同时需要注意的是FaultLogger相关接口从API 18开始不再维护，建议使用HiAppEvent订阅崩溃事件（[ArkTS](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md)、[C/C++](../harmonyos-guides/hiappevent-watcher-crash-events-ndk.md)）。

2. 应用性能监测服务（Application Performance Management Service，简称APMS）是AppGallery Connect（简称AGC）向开发者提供的一个现网质量监测解决方案。智能分析平台是一站式问题智能定位分析工具，平台支持对卡顿、崩溃、启动慢、资源泄漏等问题类型进行专家级的分析。
   * 这两种方案都能快速开通一键使用，快速具备应用质量检测能力。而两者的差异在于，APMS侧重正式版本的质量问题检测以及异常数据采集上报多视角展示，智能分析平台则是倾向于应用异常分析。
   * 开通[APMS开通服务](../app/agc-help-apms-faq-0000002271373129.md)后，APMS可以采集性能指标，帮助快速界定问题范围：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/13HqbQsSQJW8gbdP7x8nnw/zh-cn_image_0000002680658384.png "点击放大")
   * [智能分析平台启动即接入](https://devecoservice.harmonyos.com/activateservice)，数据来源于系统侧上报，无需接入SDK，即可分析查看应用异常：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/zzLCFVt3S8mIOEMQUonBsg/zh-cn_image_0000002680498518.png "点击放大")

## 常见FAQ

Q：通过eventInfo.params['threads']获取到的代码行不准确。

A：因为编写的代码是基于ets文件，但是返回的堆栈是ts文件的堆栈，ts文件是编译器基于ets文件编译生成的，可以根据现有ts堆栈解析。可使用分析工具：[堆栈轨迹分析](../harmonyos-guides/ide-release-app-stack-analysis.md)。

Q：关于[errorManager.on('error')](../harmonyos-references/js-apis-app-ability-errormanager.md#errormanageronerror)与[hiAppEvent.event](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)中hiAppEvent.event.APP\_CRASH的区别与使用建议，两者是否有冲突或重复？

A：关于errorManager.on('error')：属于ArkUI错误管理机制，用于捕获运行时错误（如JS崩溃）。关于hiAppEvent.event.APP\_CRASH：属于HiAppEvent的崩溃监控能力，专用于捕获应用崩溃事件（包括JS崩溃）。

1. errorManager.on('error')其核心特点是：

* 应用不会退出：捕获错误后，应用可继续运行，适合调试或非致命错误处理。
* 实时性高：错误发生时立即触发回调，便于实时记录或修复。

2. hiAppEvent.event.APP\_CRASH其特点是：

* 崩溃退出机制：触发后应用会终止运行，需下次启动时上报崩溃数据。
* 适用于事后日志收集和分析，无法在崩溃发生时实时干预。

两者功能不重复，ErrorManager是开发阶段的错误拦截工具（防崩溃），APP\_CRASH是线上崩溃监控方案（崩溃后上报）。

两者无冲突，两者独立工作，ErrorManager捕获错误不影响APP\_CRASH触发崩溃事件。

Q：从API Version 26开始，通过errorManager监听可捕获异常后，HiAppEvent无法订阅JsCrash崩溃事件，如何获取崩溃日志？

A：从API版本26.0.0开始，如果已经通过[errorManager](../harmonyos-references/js-apis-app-ability-errormanager.md)接口监听了可捕获异常，则HiAppEvent将无法订阅JsCrash崩溃问题，两者相互互斥。使用errorManager后，开发者可以自行选择是否退出应用。如果不退出，应用的表现不是崩溃，但上报JsCrash和投递对应事件会推高应用的崩溃指标，导致指标不准。建议在errorManager的回调中增加同步退出操作，相关异常信息已通过回调带给开发者，可参考[errorManager使用指导](../harmonyos-guides/errormanager-guidelines.md)。
