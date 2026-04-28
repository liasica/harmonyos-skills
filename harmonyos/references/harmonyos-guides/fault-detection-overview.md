---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-detection-overview
title: 简介
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > 简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d6752c115286326accf3b156963683ebdd6f45b756928703747199885a1aeb41
---

基于 Performance Analysis Kit（性能分析服务），为开发者提供了完善的故障检测、异常处理等能力。由于故障种类繁多，产品和软件业务不同，故障的原因和表现也千差万别，从而导致应用的稳定性发生劣化，严重影响应用开发效率、交付成本以及用户体验。因此需要开发者通过开发态和运行态的故障管理设计来提升版本质量，包括故障检测、故障分析、定位、恢复、质量度量等。

为了帮助开发者更好更快的定位和解决应用故障，本章节将介绍进程崩溃、地址越界、应用冻屏、资源泄漏、任务执行超时、应用终止等故障的检测原理、日志规格、日志获取方法、约束限制等内容。

注意

如下故障场景会造成应用或者系统进程非预期退出：

1. Native代码未处理崩溃异常信号时会生成CppCrash日志，详见[Cpp Crash（进程崩溃）检测](cppcrash-guidelines.md)。
2. JS/ArkTS代码未处理异常时会生成JsCrash日志，详见[JS Crash（进程崩溃）检测](jscrash-guidelines.md)。
3. 应用卡死后生成AppFreeze日志并被强制终止退出，详见[AppFreeze（应用冻屏）检测](appfreeze-guidelines.md)。
4. 应用进程被系统终止造成其非预期退出，详见[App Killed（应用终止）检测](appkilled-guidelines.md)。
