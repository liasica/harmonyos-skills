---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy
title: 能耗诊断：Energy分析
breadcrumb: 指南 > 优化应用性能 > 能耗诊断：Energy分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26c7ddd7c9062f6a7c542cf11688aa763d879ccfddf8ded5975f7e64647c9527
---

从DevEco Studio 5.1.0 Release版本开始，DevEco Profiler提供Energy模板，帮助用户在应用运行过程中查看能耗信息，包括不同器件的能耗、整机温度以及能耗异常帧，从而方便用户对能耗问题进行调优。此外，Energy模板还集成了Frame、Time、CPU场景分析任务的功能，方便开发者在分析能耗问题的同时同步对比同一时段的其他资源占用情况。

说明

TV设备暂不支持使用Energy模板进行应用性能分析。

## 定位能耗问题

1. 创建Energy模板任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。
2. 录制结束等待处理数据完成。默认包含Energy Anomaly、Temperature以及Energy三条能耗相关泳道：
   * Energy Anomaly泳道：展示能耗相关的异常帧信息。该泳道暂不支持在Wearable设备上进行应用性能分析；
   * Temperature泳道：展示整机的温度信息。该泳道暂不支持在2in1设备上进行应用性能分析；
   * Energy泳道：展示各器件的能耗信息及整机电流信息。
3. 点击Temperature泳道，鼠标悬浮于泳道上可以查看对应时间范围的温度以及温度等级，帮助用户明确温度是否有明显上升，从而进行进一步的能耗定位。观察下方Detail区域，可以看到所选范围内的平均温度、最大温度以及最小温度。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Nx2npZi-TDS2aCX6jXHTVQ/zh-cn_image_0000002561832923.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=4A2F877522B36F2211816C062C84AA4D45A03271DAD7F61773BB888B4A001D01 "点击放大")
4. 点击Energy泳道，可在下方数据区查看录制范围内具体器件消耗的电量，器件包含：CPU、\*Display（屏幕显示耗电量）、GPU、Location（定位模块耗电量）、Camera（相机耗电量）、Bluetooth（蓝牙功能耗电量）、Flashlight（闪光灯功能耗电量）、Audio（声音模块耗电量）、Wifi（无线功能耗电量）、Modem（信号模块耗电量）。\*Device表示整机电流消耗情况。

   框选Energy泳道数据，Energy Detail中呈现框选时间段内的详情信息。根据不同器件的消耗可结合Callstack泳道的调用栈信息进行进一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/baUQrKNGTpiqN9-AJj1pGw/zh-cn_image_0000002530752996.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=3D3F6E9BE85F24C5437EC16D404953C5AA1AC355CF67D91F90EE951DDB89C052 "点击放大")
5. 点击Energy Anomaly泳道，鼠标悬浮于泳道上，可以查看空跑的渲染帧数（RS Empty Run）、不能正常调用动态系统合成器（DSS）合成而直接使用GPU进行渲染导致能耗恶化的帧的次数（GPU Consumption）、UI空跑次数（UI Empty Run）以及CPU高负载异常次数（High CPU Load）。观察下方Details区域，可以看到所选范围内的能耗异常详情，包括能耗异常类型、开始时间、结束时间、能耗异常信息、能耗异常原因、能耗异常数量。

   说明

   * 从DevEco Studio 6.1.0 Beta1版本开始，支持查看能耗异常原因、能耗异常数量。
   * 2in1设备暂不支持查看RS Empty Run和GPU Consumption。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/8u7kvpXiTk2HvVFDMFrQaw/zh-cn_image_0000002561832917.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=ADE8005C7E49692E8D910B05DB4AF5308ED38D472FCFFE110B9955E5EC23535B "点击放大")
6. 点击对应的异常类型数据（RS Empty Run、UI Empty Run和GPU Consumption），右侧More区域展示该异常帧信息，包括帧编号、RS VsyncId、帧持续时间。点击右侧跳转按钮可以跳转到Frame泳道中对应的具体帧，可以根据[查看指定Frame页面布局信息](ide-insight-session-frame.md#section58691959194312)详细查看页面组件的布局情况，以及识别存在能耗问题的组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/oXRuAEOoThm6fEnhXKCnOg/zh-cn_image_0000002530753000.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=36DA47F3C084C3E16D2C7632ED41F62A4BAA2F65D9311E09E3A0EDF953AAC3E4 "点击放大")
7. 点击CPU高负载异常数据，右侧More区域展示该异常帧信息，包括进程ID、线程ID、负载值。点击右侧跳转按钮可以跳转到对应线程调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/fFiptgOlRhC8e0Xr86g7Hw/zh-cn_image_0000002561832913.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=C6347C7D263A625EE9C9909513E459B937560638643B433358CE5E10A0CC6018 "点击放大")
