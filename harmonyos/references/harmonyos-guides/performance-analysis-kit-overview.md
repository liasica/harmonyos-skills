---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit-overview
title: Performance Analysis Kit简介
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > Performance Analysis Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:10+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:2cf66eee481a2173f9fc2e0ce83e24a1c25ff2d0d3efd07a84d6b2eed36c2b12
---

Performance Analysis Kit（性能分析服务）为开发者提供应用事件、日志、跟踪分析工具，可观测应用运行时状态，用于行为分析、故障分析、安全分析、统计分析，帮助开发者持续改进应用体验。

Performance Analysis Kit承载着HarmonyOS DFX子系统面向应用开发者提供的提升应用质量能力集合，详见[应用质量概览](../best-practices/bpta-quality-overview.md)。

## 使用场景

* 应用调试：提供流水日志功能，帮助开发者记录和获取日志，以便进行问题分析。
* 问题定位：提供各类场景的故障现场，包含可靠性、性能、功耗、分布式故障相关的日志、事件、跟踪。
* 线上监控：提供应用构建线上观测所需的日志、事件、跟踪接口，方便开发者记录和分析应用的线上运行情况。
* 灰度采集：与云侧配合，选取少量设备开启全量故障日志采集并上传云侧，提供更详细的故障信息帮助开发者更好地定位故障。

## 能力范围

* [故障检测](fault-detection-overview.md)，提供开发者检测应用稳定性故障的能力，包括崩溃检测、地址越界检测、应用冻屏检测、资源泄漏检测、任务超时检测等。
* [功耗检测](power-detection.md)，提供开发者检测应用功耗异常的能力，如CPU高负载检测。
* [性能检测](perf-detection.md)，提供开发者检测应用性能异常的能力，如应用启动耗时检测、滑动丢帧检测等。
* [日志打印](hilog-guidelines-arkts.md)，提供开发者记录和获取流水日志的能力。
* [事件订阅](hiappevent-intro.md)，提供开发者记录故障、行为、安全、统计事件的能力，并订阅系统事件，设置数据处理者以完成数据上传。
* [性能跟踪](hitracemeter-intro.md)与[分布式调用链跟踪](hitracechain-intro.md)，提供开发者通过进行性能追踪和跨线程、跨进程的分布式跟踪能力。
* [检测模式](hichecker-guidelines-arkts.md)，提供开发者检测应用线程耗时调用、元能力资源泄漏等问题的能力。
* [系统调试信息获取](hidebug-guidelines.md)，提供开发者获取应用和系统资源使用情况的能力。
* [业务线程超时检测](hicollie-guidelines-ndk.md)，提供开发者检测业务线程任务执行超时并上报超时事件的能力。
* [错误管理](errormanager-guidelines.md)与[应用恢复](apprecovery-guidelines.md)，提供开发者捕获应用运行时异常能力，以及应用非预期退出后启动状态和数据的自恢复能力。
* [应用灰度采集](hiretrieval-intro.md)，提供开发者应用灰度采集能力，可以选取少量设备打开全量日志采集获取更详细的故障日志，帮助开发者更好的定位故障。
* 调试命令提供包含[hdc](hdc.md)、[hilog](hilog.md)、[hidumper](hidumper.md)、[hitrace](hitrace.md)、[hiperf](hiperf.md)等工具用于调试系统和应用。

## 亮点/特征

**便捷地构建APM系统**

* 提供接口（[HiDebug](hidebug-guidelines.md)、[HiAppEvent](hiappevent-intro.md)、[HiLog](hilog-guidelines-arkts.md)），可用于自建端侧APM（Application Performance Management，应用性能管理平台）SDK，与厂商自研APM对接。
* 基于[HiAppEvent系统事件](event-subscription-overview.md#系统事件)和[HiAppEvent应用事件](event-subscription-overview.md#应用事件)，订阅应用运行过程中所触发的事件（如崩溃、应用冻屏），快捷地记录、收集运维和运营所需的事件信息。

**强大的故障检测与异常处理机制**

* 提供全方位的应用质量检测能力，涵盖[故障检测](fault-detection-overview.md)、[性能检测](perf-detection.md)与[功耗检测](power-detection.md)。
* 提供精简、标准且完备的异常日志，支持精准记录异常传播路径。
* 全面的异常检测机制，实时感知异常，通知应用，自动拉起恢复。
* 提供灰度采集能力，选取少量设备针对特定故障精准采集全量故障日志，兼顾应用性能表现和故障定位需求。

**全面的基础维测能力**

* 日志提供分级分类功能，支持多语言，隐私处理和流量控制。
* 提供完备的事件框架和事件打点、记录、上报机制。
* 支持追踪进程轨迹，进行程序性能分析。

## 模拟器支持情况

本Kit部分能力支持模拟器，且与真机存在能力差异，具体差异如下。

* 故障检测中的Cpp Crash（进程崩溃）检测日志规格存在差异，x86模拟器不支持采集JS混合栈，且不包含提交者线程栈字段信息。
* 不支持故障检测中的Resource Leak（资源泄漏）检测、AddrSanitizer（地址越界）检测。
* 不支持功耗检测、性能检测。
* 事件订阅不支持对启动耗时事件、滑动丢帧事件、CPU高负载事件、24h功耗器件分解统计事件、音频卡顿事件的订阅。
* 命令行工具hdc不支持USB调试和无线调试。
* 命令行工具hilogtool不支持。
* 命令行工具hiperf仅支部分事件类型的性能采集，支持的事件类型可通过hiperf list sw和hiperf list tp命令查询。
* 命令行工具hiprofiler不支持。
* 通用差异：请参见[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)。
