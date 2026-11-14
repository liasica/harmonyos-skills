---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6a5d4073e3642de8c6a2dd673e11e4d094287814d730a18283b50d2f06c759a6
---

## 功能介绍

[任务池（TaskPool）](../harmonyos-references/js-apis-taskpool.md)是为应用程序提供一个多线程的运行环境，降低整体资源的消耗和提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息。

Concurrency模板支持的泳道包括：FFRT、TaskPool、Async NAPI、Async ArkTS、ArkTS Callstack、Callstack、Process。本文介绍FFRT、TaskPool、Async NAPI、Async ArkTS泳道，其他泳道的详细信息请参考对应模板内容。

* ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* Process泳道的介绍请参考[CPU活动分析](ide-insight-session-cpu.md)。

**说明** 

任务分析前，需创建Concurrency分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看Task统计信息

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/LwuXJfloTNO__Hk3s-iV0w/zh-cn_image_0000002779567228.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF3CDAD430FF323F55B722C640E58896D2EFE6758A3F8E8BEAD71C227801FE51 "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/B3pelu7KS0ySe4PoaAAZug/zh-cn_image_0000002808886897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FF2D97F7BE7CEEBDDFAA2A2E2BE0ED30B83FD258D0F1063F6215D1464B4E0AA "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Q3z2ZL-VRqO6MnkGtlxfiQ/zh-cn_image_0000002808886891.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BB57119AD10E134EB39666204CACB1FBCCDA2FD438CCDADAE41B8125FDA29CF)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/AkLoK8lxRxKCZ83ojMh1HQ/zh-cn_image_0000002808766813.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2F57E4C12C20C0E23F3A390DADEDC242C0BE8359110BBD1B4E80A4D69B698C6 "点击放大")
4. 展开**Async ArkTS**泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4QVR-YfhTEKRyPzRVBOylw/zh-cn_image_0000002779567234.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=F51EF3A8377EA9D39A145136567A031D49660C964E2AC7EB76B3EC25AFF466DB "点击放大")
5. 展开**Async NAPI**泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/34T-6nY4T5m81OHnIA6Gow/zh-cn_image_0000002779407252.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=40E209DE765F2FA35C4A673F2ED3CB9F1017E9391E71833B389CC9B5F2865484 "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，**Details**详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/vw4ieG5tS-CA0NbzYSInxw/zh-cn_image_0000002808766811.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9CB7A86A44FB1E41B533E89153E29CFED32DC45450EE1A0A3B6F6BC8FF544C1 "点击放大")
