---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-quality-overview
title: 应用质量概览
breadcrumb: 最佳实践 > 应用质量概览 > 应用质量概览
category: best-practices
scraped_at: 2026-09-16T06:55:06+08:00
doc_updated_at: 2026-09-15
content_hash: sha256:637c8cef677b3e87ed6e7b732f8390ed777913d00e09e492339f81073b224f0c
---

DFX（Design For eXcellence）是指产品的非功能性设计的总称，其中X代表产品的某个特性或产品生命周期的某个阶段。HarmonyOS DFX子系统提供了一系列DFX功能，帮助开发者创建高质量的应用和游戏。这些功能包括：

* DFR（Design For Reliability）可靠性设计：提供应用崩溃、卡死、资源泄漏、地址越界等故障的检测与恢复功能。
* DFT（Design For Testability）可测试性设计：提供日志、跟踪、调试信息、命令行工具等，以支持应用的观测与调试。
* DFP（Design For Performance）性能设计：提供应用启动慢、卡顿、丢帧等性能问题的检测功能，以及hitrace、hiperf等分析工具，帮助开发者优化性能。

这些DFX功能涵盖了故障管理、问题上报、问题分析等多个方面，具体能力分类详见下方表格：

## 基础能力

| **场景** | **子场景** | **组件或工具** |
| --- | --- | --- |
| 故障管理 | 稳定性检测 | [崩溃检测](../harmonyos-guides/crash-detection.md) |
| [Resource Leak（资源泄漏）检测](../harmonyos-guides/resource-leak-guidelines.md) |
| [AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md) |
| [AddrSanitizer（地址越界）检测](../harmonyos-guides/address-sanitizer-guidelines.md) |
| [任务超时检测](../harmonyos-guides/apptask-timeout-guidelines.md) |
| 性能检测 | [性能检测](../harmonyos-guides/perf-detection.md) |
| 功耗检测 | [功耗检测](../harmonyos-guides/power-detection.md) |
| 错误管理 | [错误管理开发指导](../harmonyos-guides/errormanager-guidelines.md) |
| 故障恢复 | [应用恢复开发指导](../harmonyos-guides/apprecovery-guidelines.md) |
| 问题上报 | 事件订阅 | [事件订阅](../harmonyos-guides/hiappevent.md) |
| 问题分析 | 日志 | [日志打印](../harmonyos-guides/hilog-dev.md) |
| 跟踪 | [性能跟踪](../harmonyos-guides/hitracemeter.md) |
| [分布式调用链跟踪](../harmonyos-guides/hitracechain.md) |
| 调试信息 | [系统调试信息获取](../harmonyos-guides/hidebug.md) |
| 命令行工具 | [hdc](../harmonyos-guides/hdc.md) |
| [hilog](../harmonyos-guides/hilog.md) |
| [hilogtool](../harmonyos-guides/hilog-tool.md) |
| [hidumper](../harmonyos-guides/hidumper.md) |
| [hitrace](../harmonyos-guides/hitrace.md) |
| [hiperf](../harmonyos-guides/hiperf.md) |
| [调试命令](../harmonyos-guides/debugging-commands.md) |
| 界面化工具 | [Smartperf-Host](https://gitcode.com/openharmony-sig/smartperf)，[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) |

## 场景化知识地图

在开发及运维过程中，如果遇到稳定性、性能、功耗相关的问题，可以参考如下场景化知识地图进行分析和解决。

| **场景** | **二级场景** | **开发态检测** | **运行态检测** | **分析**方法 | 案例 |
| --- | --- | --- | --- | --- | --- |
| 稳定性 | 地址越界 | * [地址越界检测工具原理](bpta-stability-address-sanitizer-principle.md) * [使用ASan检测内存错误](bpta-stability-asan-detection.md) * [使用HWASan检测内存错误](bpta-stability-hwasan-detection.md) * [使用GWP-ASan检测内存错误](bpta-stability-gwpasan-detection.md) | * [地址越界类问题检测方法](bpta-stability-runtime-address-sanitizer-detection.md) | * [地址越界类问题分析方法](bpta-stability-address-illegal-way.md) * [地址越界问题类型](bpta-stability-address-sanitizer-category.md) | * [地址越界类问题案例](bpta-scenario-stability-address-sanitizer.md) |
| 资源泄漏 | * [开发态资源泄漏类问题检测](bpta-stability-leak-detection.md) | * [运行态资源泄漏类问题检测方法](bpta-stability-runtime-leak-detection.md) | * [内存泄漏分析方法](bpta-stability-leak-way.md#section728319329442) * [句柄泄漏分析方法](bpta-stability-leak-way.md#section9594173320417) * [线程泄漏分析方法](bpta-stability-leak-way.md#section282262074411) | * [内存泄漏-JS内存泄漏类案例](bpta-scenario-stability-leak.md#section433214716396) * [内存泄漏-native jemalloc泄漏类案例](bpta-scenario-stability-leak.md#section10929163884819) * [内存泄漏-内核内存泄漏类案例](bpta-scenario-stability-leak.md#section189600384502) * [句柄泄漏-文件句柄泄漏案例](bpta-scenario-stability-leak.md#section5313162915382) * [线程泄漏案例](bpta-scenario-stability-leak.md#section107128486383) |
| 应用冻屏 | - | * [THREAD\_BLOCK\_6S应用主线程卡死超时](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时) * [APP\_INPUT\_BLOCK用户输入响应超时](../harmonyos-guides/appfreeze-guidelines.md#app_input_block用户输入响应超时) | * [应用冻屏类问题分析](bpta-analysis-of-app-freeze-in-develop.md) | * [应用冻屏类问题案例](bpta-scenario-stability-app-freeze.md) |
| 应用异常退出 | * [使用TSan检测线程问题](bpta-stability-tsan-detection.md) * [使用UBSan检测未定义行为](bpta-stability-ubsan-detection.md) | * [JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md) * [Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md) * [应用被查杀问题检测](bpta-stability-runtime-appkilled-detection.md) | * [JS Crash类问题分析方法](bpta-stability-app-crash-js-way.md) * [CppCrash类问题分析方法](bpta-stability-app-crash-cpp-way.md) * [应用被查杀类问题分析方法](bpta-stability-app-killed-way.md) | * [应用异常退出类问题案例](bpta-scenario-stability-exception-exit.md) |
| 性能 | 应用启动慢 | * [Code Linter](bpta-performance-detection.md#section145453441571) * [AppAnalyzer](bpta-performance-detection.md#section135451444171) | * [启动耗时类问题检测方法](bpta-performance-startup-time-detection.md) * [主线程超时类问题检测方法](bpta-performance-mainthread-consumption-detection.md) | - | - |
| 应用卡顿、丢帧 | * [滑动丢帧类问题检测方法](bpta-performance-sliding-frame-drop-detection.md) | * [点击响应时延分析](bpta-click-to-click-response-optimization.md) * [点击完成时延分析](bpta-click-to-complete-delay-analysis.md) * [Web点击响应时延分析](bpta-web-click-response-delay-analysis.md) * [Web加载完成时延分析](bpta-web-completion-delay-analysis.md) * [跨线程序列化耗时问题分析](bpta-threads-serialization-timeout-analysis.md) * [帧率问题分析](bpta-zhenlv.md) * [内存基础知识](bpta-memory-basic-knowledge.md) | * [Web加载性能优化](bpta-web-develop-optimization.md) * [应用冷启动时延优化](bpta-application-cold-start-optimization.md) * [长列表加载丢帧优化](bpta-best-practices-long-list.md) * [瀑布流加载丢帧优化](bpta-waterflow-performance-optimization.md) * [性能场景优化案例](bpta-scenario-performance-optimization.md) |
| 功耗 | 应用异常耗电 | * [HiSmartPerf功耗检测](bpta-application-power-test.md#section1701321935) * [Profiler功耗检测](bpta-application-power-test.md#section2779154791312) | [运行态功耗检测](bpta-power-consumption-runtime-analysis.md) | * [CPU 高负载分析](bpta-high-cpu-load-analysis.md) * [前台不可见动效问题分析](bpta-frontend-invisible-animation-analysis.md) | * [Vsync低功耗优化](bpta-vsync-power-optimization.md) * [Buffer低功耗优化](bpta-buffer-power-optimization.md) |

对于开发态检测，除上表提到的检测方法外，还可以使用专业的测试工具[DevEco Testing](https://developer.huawei.com/consumer/cn/next/deveco-testing/)对应用进行质量测试。

## 常用术语

下表列出了一些常见的应用质量相关术语方便开发者进行查阅，更多的术语可查看[Performance Analysis Kit术语](../harmonyos-guides/performance-analysis-kit-terminology.md)。

| 场景 | 常用术语 |
| --- | --- |
| 通用 | [log版本](../harmonyos-guides/performance-analysis-kit-terminology.md#log版本)，[nolog版本](../harmonyos-guides/performance-analysis-kit-terminology.md#nolog版本)，[debug版本应用](../harmonyos-guides/performance-analysis-kit-terminology.md#debug版本应用)，[release版本应用](../harmonyos-guides/performance-analysis-kit-terminology.md#release版本应用) |
| 稳定性 | [CPP Crash](../harmonyos-guides/performance-analysis-kit-terminology.md#cpp-crash)，[JS Crash](../harmonyos-guides/performance-analysis-kit-terminology.md#js-crash)，[AppFreeze](../harmonyos-guides/performance-analysis-kit-terminology.md#appfreeze)，[ASan](../harmonyos-guides/performance-analysis-kit-terminology.md#asan)，[HWASan](../harmonyos-guides/performance-analysis-kit-terminology.md#hwasan)，[GWP-ASan](../harmonyos-guides/performance-analysis-kit-terminology.md#gwp-asan)，[TSan](../harmonyos-guides/performance-analysis-kit-terminology.md#tsan)，[UBSan](../harmonyos-guides/performance-analysis-kit-terminology.md#ubsan) |
| 性能 | [丢帧](../harmonyos-guides/performance-analysis-kit-terminology.md#丢帧) |
| 功耗 | [前台任务](../harmonyos-guides/performance-analysis-kit-terminology.md#前台任务)，[后台任务](../harmonyos-guides/performance-analysis-kit-terminology.md#后台任务)，[帧率](../harmonyos-guides/performance-analysis-kit-terminology.md#帧率)，[LTPO](../harmonyos-guides/performance-analysis-kit-terminology.md#ltpo)，[冗余绘制](../harmonyos-guides/performance-analysis-kit-terminology.md#冗余绘制)，[不可见动效](../harmonyos-guides/performance-analysis-kit-terminology.md#不可见动效)，[HWC](../harmonyos-guides/performance-analysis-kit-terminology.md#hwc) |
| 内存 | [VSS](../harmonyos-guides/performance-analysis-kit-terminology.md#vss)，[PSS](../harmonyos-guides/performance-analysis-kit-terminology.md#pss)，[RSS](../harmonyos-guides/performance-analysis-kit-terminology.md#rss)，[脏页](../harmonyos-guides/performance-analysis-kit-terminology.md#脏页)，[干净页](../harmonyos-guides/performance-analysis-kit-terminology.md#干净页)，[匿名页](../harmonyos-guides/performance-analysis-kit-terminology.md#匿名页)，[文件页](../harmonyos-guides/performance-analysis-kit-terminology.md#文件页) |

## 相关主题

* [Performance Analysis Kit（性能分析服务）](../harmonyos-guides/performance-analysis-kit.md)指南
* [Performance Analysis Kit（性能分析服务）](../harmonyos-references/performance-analysis-api.md)API参考
* [运维](../harmonyos-faqs/faqs-performance-analysis-kit.md)
* [HarmonyOS应用DFX能力介绍](https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101705113085386097?pathId=101667550095504391)
