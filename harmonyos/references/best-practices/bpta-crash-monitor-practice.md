---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-crash-monitor-practice
title: 崩溃监测实践
breadcrumb: 最佳实践 > 稳定性 > 稳定性运维 > 崩溃监测实践
category: best-practices
scraped_at: 2026-04-28T08:23:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:85241b0e199d8344f99c7ba1d0643d70dc44a7aac6c681ab1e68835fe284698a
---

## 概述

崩溃（Crash）是指应用程序在运行过程中突然停止或因错误而无法继续执行。

崩溃率是衡量应用质量的关键指标。监测崩溃点并解决崩溃问题对维护应用稳定性具有重要意义：

* 用户体验：崩溃会直接影响用户体验，可能导致用户不再使用或卸载应用。
* 用户留存率：应用稳定性直接影响用户留存，低崩溃率是关键指标。
* 数据安全：应用崩溃可能导致数据丢失，影响数据完整性。在编辑类应用场景中，减少崩溃对用户数据的保护至关重要。

针对应用崩溃事件的监测，推荐以下两种方式：

1. HiAppEvent（[事件订阅](../harmonyos-guides/hiappevent.md)）

   HiAppEvent应用事件允许记录故障、行为、安全和统计等事件。应用可以使用HiAppEvent系统能力实现埋点数据采集。

   如果需要对Crash数据进行定制化处理，可以通过HiAppEvent收集数据并上传到指定服务器。
2. AGC崩溃服务（[业务介绍](../AppGallery-connect-Guides/agc-crash-introduction-0000001055732708.md)）

   订阅崩溃服务，获取崩溃提醒。应用崩溃时，及时接收通知并分析详细信息，有助于查找问题原因，快速修复，提升应用质量和用户体验。

在监听和采集Crash问题上，两种方式有以下相似和差异点：

|  | 相似点 | 差异点 |
| --- | --- | --- |
| HiAppEvent | 事件打点机制，可以订阅多种事件，包括崩溃；  属于系统自带API； | 结构化数据，可收集上传到指定服务器；  自行对数据进行分析处理操作； |
| AGC崩溃服务 | 实时监控服务，可以订阅崩溃提醒；  无需集成SDK； | 数据透明传输，基于AGC一站式服务；  无需代码开发，查看可视化数据报告； |

说明

在语言层面，二者都支持ArkTS和C/C++的运行时崩溃监测，针对C/C++的崩溃故障问题，可参考[CppCrash类问题分析方法](bpta-stability-app-crash-cpp-way.md)。

## HiAppEvent订阅崩溃事件

## HiAppEvent简介

HiAppEvent 是一种系统层面的事件打点机制，为应用开发者提供故障信息、统计信息、安全信息和用户行为信息的记录功能，帮助开发者分析应用运行情况，支持访问数、用户活跃数量、操作习惯等关键因素的统计分析。

HiAppEvent的接口设计由系统决定回调时机。在回调执行时，开发者可以获取已订阅事件的结构化数据。

### 场景与事件选型

应用在运行态，通常需要关注以下质量问题：

1. APP\_CRASH 应用崩溃事件
2. APP\_FREEZE 应用卡死事件
3. RESOURCE\_OVERLIMIT 应用资源泄露事件
4. ADDRESS\_SANITIZER 应用踩内存事件
5. MAIN\_THREAD\_JANK 应用主线程超时事件

目前HiAppEvent在这些问题上都具备相应的事件记录能力，更多事件选型参考[hiAppEvent.event()](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventevent)。通过订阅相关事件，可以获取相应日志，进行问题定位分析。

本文重点介绍崩溃故障场景，具体是指在应用发生APP\_CRASH或APP\_FREEZE后，监听并处理相应的崩溃信息。

使用HiAppEvent监听应用崩溃。应用崩溃后，用户重新进入应用处理崩溃信息。

### 详细步骤

HiAppEvent订阅崩溃事件的开发流程可分别参考[订阅崩溃事件（ArkTS）](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md)与[订阅系统崩溃事件（C/C++）](../harmonyos-guides/hiappevent-watcher-crash-events-ndk.md)。

## 使用AGC崩溃服务

### AGC简介

AppGallery Connect（AGC）提供一站式服务，涵盖应用的创意、开发、分发、运营和经营，构建全场景智慧应用生态。AGC整合多项服务，降低开发运维难度，提高版本质量，帮助开发者获得用户并增长收入。

AGC崩溃服务帮助开发者快速发现、定位、解决应用崩溃问题，使用简便，无需编写代码即可实时查看可视化数据报告。

### 详细步骤

AGC崩溃服务的开发使用流程如下：

**创建项目与应用**

1. 需要[注册华为开发者账号](../app/agc-help-getstarted-0000001100316670.md#section27844983310)，并完成实名认证。
2. 项目是AGC资源的组织实体，开发者可以将一个应用的不同平台版本添加到同一个项目中。登录AGC后，在”我的项目”中点击”添加项目”。可参考[创建项目-操作步骤](../app/agc-help-createproject-0000001100334664.md#section1734611188612)。
3. 要使用AGC提供的各类服务，还需要创建应用，在已创建的项目页面中点击”添加应用”，注意应用包名要与DevEco Studio项目中包名一致。具体可参考[创建HarmonyOS应用/元服务](../app/agc-help-createharmonyapp-0000001945392297.md)。

**开通崩溃服务**

1. 登录AGC，找到已创建的项目，选择需要启用崩溃服务的应用。
2. 选择“质量 > APMS > 异常管理”，进入异常管理页面，点击"立即开通"。

**测试崩溃服务**

配置完成后，需测试崩溃服务是否正常运行。手动制造一次崩溃，然后在AGC上查看上报情况。

1. 参照示例，手动触发一次崩溃。

   ```
   1. let test:string = "{name:'xiaoming' age:10}";
   2. let result:object = JSON.parse(test);
   ```
2. 前往AGC崩溃服务查看崩溃数据，分析问题。

**分析崩溃问题**

1. 登录AGC，点击“我的项目”。
2. 在项目列表中找到对应项目，然后在该项目的应用列表中找到对应应用。
3. 点击“质量 > APMS > 异常管理”，进入异常管理页面。
4. 点击不同类型的崩溃页签，可以查看相应的崩溃事件，例如CPP\_CRASH、JS\_ERROR、OOM和PROCESS\_KILL。
5. 在具体页签中的“异常崩溃列表”区域，可以查看崩溃的详细信息。其中，崩溃服务提取了应用崩溃堆栈日志中的关键帧，并自动将崩溃代码出现位置相同的崩溃聚合成一类崩溃事件。借助服务提供的一系列数据，开发者可以分析崩溃发生的原因，具体数据指标及使用见[分析崩溃问题](../app/agc-help-apms-crash-analyse-0000002271413041.md)。

说明

运行在HarmonyOS ROM版本 ≥ 3.0.0.25的ArkTS应用无需集成SDK，创建应用并开通服务即可。
