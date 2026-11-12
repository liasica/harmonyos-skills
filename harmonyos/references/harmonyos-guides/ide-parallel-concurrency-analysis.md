---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3c7fc3c323d2fc5e5f47028b5260c2b9f6ed753e7d8549f9d40c6240643a758a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ccr1lEe0T9mC3ZTckH6JCQ/zh-cn_image_0000002779567228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4020F8EFAFF39E57E43F90BDD1C12A4AE2585D22D9550D76518AE08DD259F11E "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/jeQmdtqbQWuhtxLqnZ0f1w/zh-cn_image_0000002808886897.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E94827CB6C98E051F40C00900BFE78B4D2BE757785A4ECD25B11B180398A8E45 "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/MLjP_JhWQByltqtyaBLPog/zh-cn_image_0000002808886891.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=52058F1A553C31DB63F4F41140AD150482745EAFF2F5B47688C901B90E9F9A8F)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/V9ETJQi5RUupeSFHOwNfWw/zh-cn_image_0000002808766813.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C620D6663645889FE5BBF568DC8EF109860B3CB7617E363C0852579A8B54DC34 "点击放大")
4. 展开**Async ArkTS**泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ye2n08MDQFuWwqMlGKmNyw/zh-cn_image_0000002779567234.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0375EE83B5403762C6A9286398E0EB7511768A5977A1DFE94EA33CCC0BF9FDC "点击放大")
5. 展开**Async NAPI**泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/yp1euzuSSUq8l4bIPd85vQ/zh-cn_image_0000002779407252.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD69CB287BC19A8CFB9345A2F7329470ECF5CD6A4D1E9D64DDD5FA8077FBF4AC "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，**Details**详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/bzKOVEcQSB2-hozVbVJZDQ/zh-cn_image_0000002808766811.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AED2E17CCAF6D913F28238D927AE5758D0950815B73D681FE612EED2E3CA9E02 "点击放大")
