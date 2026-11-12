---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:24ce8eba11495e7bbd41d12de60d317b5e310a6b280b5d14b34c19d5cc203992
---

## 功能介绍

开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景：

* Allocation：主要用于应用/元服务内存资源占用情况的分析，可深度采集内存相关数据，直观呈现不同分类的内存趋势，提供内存实例分配的调用栈记录，深入分析内存问题。
* Time：主要用于改进函数执行效率的分析，深度录制函数调用栈及每帧耗时等相关运行数据，并完整展现ArkTS到Native的跨语言调用栈，支撑Native API典型问题分析。
* Frame：主要用于深度分析应用/元服务的卡顿丢帧原因。

## 启动深度录制

可以通过实时监控（Realtime Monitor）检测各项资源使用情况，识别并界定潜在的性能瓶颈及热点区域后启动深度录制；也可以直接启动深度录制。

1. [使用USB连接方式](ide-hmos-run-device.md)完成设备连接，并启动您想要监测的应用。
2. 通过如下两种方式打开Profiler：

   方式一：在鸿蒙电脑DevEco Studio图标上右键，选择**调优**，打开DevEco Profiler。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/u_2EbZETS-21_aztLbUxyw/zh-cn_image_0000002810750933.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D35EB4C548DC9933BC5F49D1B62DAD91C77DA2FA1E78209003F34C79F2A85188 "点击放大")

   方式二：打开DevEco Studio后，在菜单栏点击**运行** > **调优**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/zIeKkywLSwSht0Cmi4i_wQ/zh-cn_image_0000002781471274.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F263427A791E5AE0664E7AC5F938E79A143F03C880A8FCFE4CFEF119FE00244 "点击放大")
3. 选择待调优的设备、应用或进程，以及选择实时监控的模板后，点击右下角**立即开始**录制，或点击**打开文件**，导入历史数据。

   录制时若设备不止有一个主进程，还存在Extension或者Render进程，那么您需要再手动选择一个您想要监控的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/sfDqAhxlQ-GCihJtEbtzMg/zh-cn_image_0000002810630825.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=99715D37E55C151E6D18BD9DF6BBA5C1BF3EBC9E1FA47C8602B51A59668058E5 "点击放大")
4. 配置并确认会话环境，录制前单击任务区域启动录制按钮右侧下拉三角可以配置录制参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/ZyzD2k29TRSPNByH0cQFCw/zh-cn_image_0000002810630829.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F690032C6A32DD4816922899A2672D043724108D3FC3FB14A60B1021021575B "点击放大")
5. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/NGm4VQr3QrmZTcAhN73JPQ/zh-cn_image_0000002810630823.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=25E70D444B2A5D82148DD0D6DD6AE5104FBDE1A2716BD9A9E11B94EF8B7B05D6)按钮启动录制，等待任务状态由**初始化**变为**录制中**，在调优设备上操作应用，执行要验证的操作，复现设备性能问题。

   录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板，可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Hu8fGY9USGK2anTcHGB7AQ/zh-cn_image_0000002781471278.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=806BDE01FC9C8258CEF334C86BBDCF8547C10BB720C587005FAA5531EFDCFF66 "点击放大")
6. 录制场景结束，停止录制。

   单击该任务的停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/vQrF8V4_QB2FLTiWFapXRQ/zh-cn_image_0000002810750937.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4287ED9DE840509BEB7E41837EFC08AE34B1B5213B142454CCFA1C3C8512A9D5)，进入数据解析阶段，所有泳道任务状态由**录制中**变为**解析****中**，解析结束后右侧区域会显示具体调优内容。解析过程可能包含大量的数据，需要等待一段时间，请耐心等待解析完成。
