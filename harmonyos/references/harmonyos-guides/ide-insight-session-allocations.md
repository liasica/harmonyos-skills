---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations
title: 基础内存：Allocation分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e1c60d0275e5b7737b3a73d4e5e4d5ea8e0427038a7a27e6d191d8239622a7ae
---

## 功能介绍

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

Allocation模板支持的泳道包括：Memory、ArkTS Allocation、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory、Native Leaks。同时，Allocation模板支持离线符号解析能力，相关能力介绍请参考[离线符号解析](ide-insight-session-time.md#section186881175012)。

**说明** 

任务分析前，需创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

* **[内存分析介绍](ide-insight-session-allocations-memory.md)**
* **[内存分析数据筛选](ide-insight-session-allocations-data-filtering.md)**
* **[启动时内存分析](ide-insight-session-boot-memory.md)**
* **[案例：Native内存泄漏分析](ide-native-allocation-case.md)**
