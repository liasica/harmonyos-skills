---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-description
title: 性能调优工具简介
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 性能调优工具简介
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1c0fa8f7c4d233440132458018313be4653074f23173f2ba9880bfe43e0bc308
---

应用或元服务运行期间可能出现响应速度慢、动画播放不流畅、列表拖动卡顿、应用崩溃或耗电量过高、发烫、交互延迟等现象，这些现象表明应用或元服务可能存在性能问题。造成性能问题的原因可能是业务逻辑、应用代码对系统API的误用、对ArkTS对象的不合理持有导致内存泄漏等，引起对系统资源不合理使用，包括对CPU、内存、网络、文件、GPU以及其他外设器件的冗余占用，进而引发性能问题。

通常，进行性能优化主要围绕关键点“降负载”来入手，这包括：

* 永久降负载。即将原本不合理的冗余处理进行彻底清理；
* 临时降负载。即避免在关键时间段内扎堆产生负载。可以考虑采用懒加载等延迟处理机制，错峰运行。

在遇到这些问题时，首先需要对应用的运行情况以及设备的资源消耗进行监测，以初步确定可能存在的性能问题以及问题出现的位置，进而有针对性地降低负载。

**[CodeLinter](ide-hmos-code-linter.md)**提供静态代码扫描能力，通过[性能规则](ide-hmos-codelinter-rule.md)检查代码是否存在性能问题，帮助开发者分析和修改性能问题。

**[DevEco Profiler](ide-hmos-profiler.md)**提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖CPU占用、内存占用、实时帧率、GPU使用率等多个维度的数据，自顶向下逐层展开分析，明确不合理的负载出现位置，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率。

优化应用性能章节集中介绍DevEco Profiler工具，CodeLinter请根据链接进行参考。
