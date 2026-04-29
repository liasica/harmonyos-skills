---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu
title: GPU活动分析
breadcrumb: 指南 > 优化应用性能 > GPU活动分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:45+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1014240ea049165ab9c4a5566d42e2ee2ea86d8c78b674b554df38a040b7db8b
---

从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

## 约束与限制

* 该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
* 仅支持Phone设备。

## 操作步骤

1. 创建GPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。

   GPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/IcCbDh_CSaatVFaKZ_hv8Q/zh-cn_image_0000002561753031.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=A4EB0D9174C5E4CA594D094350B4C603916FEBD2F4C1B6DE1721C16A557C02EA)指定要录制的泳道。单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/b4LFT-fQQZ6mZApTBHJW-Q/zh-cn_image_0000002530913086.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=A85CB242DF9AD70AF9BA6EA27AA54B448BB33F0156CA547D41D0043F91757DC4)按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
2. “Counters”泳道显示当前设备GPU的使用率，“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息请参考[基础耗时：Time分析](ide-insight-session-time.md)和[CPU活动分析](ide-insight-session-cpu.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/4kA5t2jYQ8OfGh-wOJG1Pw/zh-cn_image_0000002530753088.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=AF8F6A2D5C822FEDD2722660666405BC8AC6A8B07D6C4FF2E74759F8A178D083 "点击放大")
3. 将“Counters”泳道展开，子泳道显示GPU各项活动信息，包括counters\_gather、GPU执行命令的频率、GPU执行命令的持续时间等。除counters\_gather外，其他子泳道信息可参考[GPU Counters](../Tools-Guides/gpu-counters-0000001886127538.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/UxuZi4Q2SKayu_CWB_UslA/zh-cn_image_0000002530913084.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=4FCF39799D841101C973553280F052228A8D743636982463B1DAF002D2F75BD6 "点击放大")
4. counters\_gather泳道显示线程对各CPU核心的占用情况。单击运行状态的时间片段，显示线程在该时间片段的起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态，并且支持跳转到上个或者下个线程运行状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/4-sDoW_CSfOF0gYZ5GpGkg/zh-cn_image_0000002561833021.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=3176ABD80588656604AC71BC71D8B37436A8A5C759966A03A2A60943EE74F882 "点击放大")
5. 框选counters\_gather泳道，可查看此时间段内的统计信息，包括线程状态统计信息、CPU单线程使用情况、线程中的中载重载数据统计。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/UhXyyp6pRe-BgtA-orvQfg/zh-cn_image_0000002561753035.png?HW-CC-KV=V1&HW-CC-Date=20260429T054744Z&HW-CC-Expire=86400&HW-CC-Sign=0C1EAA0E4A776798155B48D772AC1B289D38B72B19FD301C01D7AF266DF7A645 "点击放大")
