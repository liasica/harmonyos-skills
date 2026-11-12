---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu
title: GPU活动分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > GPU活动分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:000e4071d22085ee6f8f044c6fbe15ea5c7a2448d2fd952972616f0890bc0eea
---

## 功能介绍

从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

GPU模板支持的泳道包括：Counters、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍Counters泳道，其他泳道的详细信息请参考对应模板内容。

* ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* CPU Core、Process泳道的介绍请参考[CPU活动分析](ide-insight-session-cpu.md)。

## 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 仅支持Phone设备。

## 操作步骤

1. 创建GPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。

   GPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/xCEIlZRmRGy6p7R5ZCD8cQ/zh-cn_image_0000002779406850.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B28DD89B661D609759F403AD2CA5232AA672CAE2F017AC9BBF6521A0B15D0A5 "点击放大")指定要录制的泳道。单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/AC-wc4IwS9mvBqFvaqrG0Q/zh-cn_image_0000002808766409.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=04FC94111CECBFDB6C3571FD4D32E8A95E4BB07680F358C8B4847BDB007EB29D "点击放大")按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
2. **Counters**泳道显示当前设备GPU的使用率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/3t6YLPzJRSSkAXmhD1asCg/zh-cn_image_0000002779566824.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB93A18972748BA15990E513C8C3C39189F90128C0566B955D58A51ECB1C5958 "点击放大")
3. 将**Counters**泳道展开，**子泳道**显示GPU各项活动信息，包括counters\_gather、GPU执行命令的频率、GPU执行命令的持续时间等。除counters\_gather外，其他子泳道信息可参考[GPU Counters](../Tools-Guides/gpu-counters-0000001886127538.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/PSLp4QyDScCZoLPr_mAlEw/zh-cn_image_0000002808886489.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC3BE05A98FDB534875075811918D35908D3DF3E8D6ADF111BA00FFE8BB053D7 "点击放大")
4. **counters\_gather**子泳道显示线程对各CPU核心的占用情况。单击运行状态的时间片段，显示线程在该时间片段的起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态，并且支持跳转到上个或者下个线程运行状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/g_edu6MYQLWnFjnfI_6oOg/zh-cn_image_0000002779566828.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=564923EB1242C232492AFF331C986E1F9A2C6BB62F14F53420B97CCB476C4117 "点击放大")
5. 框选**counters\_gather**子泳道，可查看此时间段内的统计信息，包括线程状态统计信息、CPU单线程使用情况、线程中的中载重载数据统计。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/tsXiMxqWTB2DCpmkJrNVkg/zh-cn_image_0000002808886491.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=04C54FF2617C5AE026220ED9A5EF3ED8CB7AC375D566DEA02C4AE99AC46C230A "点击放大")
