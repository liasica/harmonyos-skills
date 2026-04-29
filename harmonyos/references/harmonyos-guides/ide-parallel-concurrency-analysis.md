---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbd9369fbe4e74a29b2b169b8b3b3728c1bade56f13df04bc49502112a5bb71f
---

任务池（TaskPool）（详细信息请参考[@ohos.taskpool（启动任务池）](../harmonyos-references/js-apis-taskpool.md)）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗和提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。

## 查看Task统计信息

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ZWhzcg7_TKulfkuZnKBCIw/zh-cn_image_0000002561753355.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=EA48969BA07F42990A48DADB8854FF66FA97148A53FDC61622B6E45EB4A28877 "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/IVbwiY7HS--B4dC00DHo5A/zh-cn_image_0000002561753367.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=7459327A58865D0607306BC4FF5A39E67C3D586F8A71D999A7E0A1D21DD73C70 "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/TGXv_3L1SbGRpCL08N_wEw/zh-cn_image_0000002561833335.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=7E881480C99C2F855C42AABAE543BEE2FF4D779630E8750C38C3D6376FDA7D7E)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/d2uBFKjDQA64RtdWh_rIEg/zh-cn_image_0000002530753424.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=78C6461F8EDFE85ABEDEE89EFE99718585710ECC13DD0D9920DAF310B63FA943 "点击放大")
4. 展开Async ArkTS泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/P4tHbskwRxKubbcJOyUnzQ/zh-cn_image_0000002561833343.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=788E175227B3E83E6FDE4EEFEA171CCEFE3347D83B0DF3D9F80F25300DB86878 "点击放大")
5. 展开Async NAPI泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/QDYlUE2uQNKMJnlpPSGhfg/zh-cn_image_0000002530913414.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=0AD4914A6099788240DF7D9312BD91083D4B524F3C4BD8F1935C70135FF2B7D9 "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/baZQTm_3T4GTV0FqCJxFBA/zh-cn_image_0000002561753359.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=0966BFB808FD8F193ED5DADD205E527590A23C6713E402FC03C38460EE4F4522 "点击放大")
