---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:52+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fbfd01ec3f5b0484879f6cce34cce3f831ab658bd7bbc7893b6ba8ec40728ef1
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/dB6spyiCQBWGCmclnpLMKg/zh-cn_image_0000002750169814.png "点击放大")

   方式二：打开DevEco Studio后，在菜单栏点击**运行** > **调优**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/lPUVhAIiShirOSCX1EEb8w/zh-cn_image_0000002750169816.png "点击放大")
3. 选择待调优的设备、应用或进程，以及选择实时监控的模板后，点击右下角**立即开始**录制，或点击**打开文件**，导入历史数据。

   录制时若设备不止有一个主进程，还存在Extension或者Render进程，那么您需要再手动选择一个您想要监控的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/49A1wpvVR8C0iFXA2H_tow/zh-cn_image_0000002779728983.png "点击放大")
4. 配置并确认会话环境，录制前单击任务区域启动录制按钮右侧下拉三角可以配置录制参数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/_hoE3J5xSxyxOyCtfJq1Zg/zh-cn_image_0000002750169818.png "点击放大")
5. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/S8qieXBiQdeShTdzNUJp8A/zh-cn_image_0000002750009918.png)按钮启动录制，等待任务状态由**初始化**变为**录制中**，在调优设备上操作应用，执行要验证的操作，复现设备性能问题。

   录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板，可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/KGRrokiaQ9aqe6G3gk4pbg/zh-cn_image_0000002750009924.png "点击放大")
6. 录制场景结束，停止录制。

   单击该任务的停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/0KapZWCcQ-KKI_jZtUErnw/zh-cn_image_0000002779728985.png)，进入数据解析阶段，所有泳道任务状态由**录制中**变为**解析****中**，解析结束后右侧区域会显示具体调优内容。解析过程可能包含大量的数据，需要等待一段时间，请耐心等待解析完成。
