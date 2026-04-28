---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu
title: GPU活动分析
breadcrumb: 指南 > 优化应用性能 > GPU活动分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6a01c1f516911caf272304376fdc5884b51adb4e69811646703f91070e5e5ba7
---

从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

## 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 仅支持Phone设备。

## 操作步骤

1. 创建GPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。

   GPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KIq0QxD0SWWSpFqcuOnpFQ/zh-cn_image_0000002561753031.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=79F74235DDA6FC276E3961D171A02338DF2594E7B110690BD390D444FF529618)指定要录制的泳道。单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/pXQ3HL1cQ5SFBYaqf1pMsg/zh-cn_image_0000002530913086.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=312E67F3992DD0C5F222D0B3D177DC53044851547D7DFA341FB305420DC84E14)按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
2. “Counters”泳道显示当前设备GPU的使用率，“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息请参考[基础耗时：Time分析](ide-insight-session-time.md)和[CPU活动分析](ide-insight-session-cpu.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/UKAZKhOTSd2mGlWJm-IUfA/zh-cn_image_0000002530753088.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=96127B0945340DD0B2B149AB692F4437F69DC7DB56739820630F4C3895294846 "点击放大")
3. 将“Counters”泳道展开，子泳道显示GPU各项活动信息，包括counters\_gather、GPU执行命令的频率、GPU执行命令的持续时间等。除counters\_gather外，其他子泳道信息可参考[GPU Counters](../Tools-Guides/gpu-counters-0000001886127538.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/c6SwFIirTpOYMD4eLdbQcQ/zh-cn_image_0000002530913084.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=3F4B38AC25B768958F8A73A8E2B4C1AF0AC2F0B217474D1D260C3F618349E9CC "点击放大")
4. counters\_gather泳道显示线程对各CPU核心的占用情况。单击运行状态的时间片段，显示线程在该时间片段的起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态，并且支持跳转到上个或者下个线程运行状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/3tpyMNcRTW6PFHZRIqRC1A/zh-cn_image_0000002561833021.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=4BAF370CC3DFB6CB9146DEFC2DAD25185701C57706B881CB1CC8CBBED455EB00 "点击放大")
5. 框选counters\_gather泳道，可查看此时间段内的统计信息，包括线程状态统计信息、CPU单线程使用情况、线程中的中载重载数据统计。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/pt4rzBxcSZ64p9CJK3wTLA/zh-cn_image_0000002561753035.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=7ABF01E07E0B83A3C13CD034B13A604630065CE4F735B0984B094A0F7921F7F0 "点击放大")
