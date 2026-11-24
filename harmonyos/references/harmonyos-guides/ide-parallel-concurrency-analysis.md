---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7511e7591e25db7a809361bdd3fb9a05910d01644156d2eaf44a8e7443ff0f43
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/FbI3-_TCRO-jAPE8iamqYA/zh-cn_image_0000002779567228.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=80EE5C1323619405437A10D2A6E863F1A62F7F2FDB90BA590A646906B471C2F5 "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/cyPEu0ZmSzqOAvS1thCqCQ/zh-cn_image_0000002808886897.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A13F29C23EC579F4F93E8C41B8EA9E1886DA91FC057A9BA9E0998E30FAD1B6B "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/UtDbsNEmS3SPmFNxUnZMEw/zh-cn_image_0000002808886891.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A3EA665B3BB0E27EA4BA445B597E51295F95A6A761A504E33683AD2910F7277)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/fJSAIhhPRI-1WYifMbePYg/zh-cn_image_0000002808766813.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF919B34580B8FB4DE4136B73CF55D6160E190709C0DA4CD47C0FD951F187DB0 "点击放大")
4. 展开**Async ArkTS**泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/OFlJOleESiaR2jVHJX_CnA/zh-cn_image_0000002779567234.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD9C9C2239A03ECEAEC654B203E5AEF71D0A72DCC7F467BF311C40A6088CF9BE "点击放大")
5. 展开**Async NAPI**泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/V1_L0rs5QVOsROHa3a1ywg/zh-cn_image_0000002779407252.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=436C142FC07B5448FE517D52F2FE99B95DB316A7FF39B1D031E0B1ED2AA7A214 "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，**Details**详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/pQgQqeVyQTy8lCde8dgg3w/zh-cn_image_0000002808766811.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C234FF36E5FA6E0DD83B327B2E360D64CEC7C11B2DB12272D36699698E35609 "点击放大")
