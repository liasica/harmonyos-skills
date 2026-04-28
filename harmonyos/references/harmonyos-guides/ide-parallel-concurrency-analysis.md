---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis
title: 并行并发：Concurrency分析
breadcrumb: 指南 > 优化应用性能 > 并行并发：Concurrency分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a53441ed311a22320b8a19d18bc7d7518e7672c811a817f6b36331e3e82607d
---

任务池（TaskPool）（详细信息请参考[@ohos.taskpool（启动任务池）](../harmonyos-references/js-apis-taskpool.md)）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗和提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。

## 查看Task统计信息

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/H6BSZEmgShKbKlWkW7b6qQ/zh-cn_image_0000002561753355.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=FEBCB7390162A318A73DFF501802B41F855867E4830FE0CFB3395183E201D013 "点击放大")
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/PJ4-CQQeRZmJhzSn-esZDA/zh-cn_image_0000002561753367.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=03508DBDB943836FF4797C33D4D25A1A404632476A1067EEB7719710C1BE2627 "点击放大")

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/PMGVrLWxSziEDrvF_76n-Q/zh-cn_image_0000002561833335.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=56B7B0EFFE1AC0F96257F73576BB28620EDF24FF4B4CB0C066DDBA0D5F948E05)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/P6mVjBPfTV290i3LnNSelQ/zh-cn_image_0000002530753424.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=A8C9A1EA7E1E1DC421C9D4745E005112F83EA78333C65C0CCCD0CCA7F7B96AA7 "点击放大")
4. 展开Async ArkTS泳道，可单独查看ArkTS异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/vJPCK1-xSaG9gcCE1tTyqQ/zh-cn_image_0000002561833343.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=7156B21A0FA3FE85BB9440230846E7A26F863323F983212D45585912D4646860 "点击放大")
5. 展开Async NAPI泳道，单独查看NAPI异步调用任务详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/pQpD5kAvT-SkHD_bN3pWTg/zh-cn_image_0000002530913414.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=39EA02DCA8C6A912F9E52795D18D2A2CF6C7C3F68A870AD4DFCDF0D7E6861E86 "点击放大")

## 查看Task的某个状态

点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/S2H0aNXcSMWwhqjwmrNYBQ/zh-cn_image_0000002561753359.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=9562750456AEEF0B9C6E75EB24A810CA0E6D3EB528F644E85AF1D0D5DBC77899 "点击放大")
