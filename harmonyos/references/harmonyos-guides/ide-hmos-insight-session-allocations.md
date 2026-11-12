---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations
title: 基础内存分析：Allocation分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:46987f054b5397b7168aa520a86436f706c418c4d461600bc8698092c618535f
---

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

Allocation模板支持的泳道包括：Memory、Native Allocation。

**说明** 

任务分析前，需创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在[会话区](ide-hmos-profiler-session.md)点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Wxj_w9cvQQKimdnTxTIJiQ/zh-cn_image_0000002781471112.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D91FEC51A701ABDAC0DF34F6696D442A36791BA9AB955497FD29D5056D22ECD4)图标，导入历史数据。

* **[内存分析介绍](ide-hmos-insight-session-allocations-memory.md)**
* **[内存分析数据筛选](ide-hmos-insight-session-allocations-data-filtering.md)**
