---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-layout
title: 界面布局
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 界面布局
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a57dd6383d705e3c58e612740168b8734528910efcd3920995f25e151df9a80e
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/ppo9_cMOQyStBCWleu-JuA/zh-cn_image_0000002561833119.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=FCCD70D52A6D60B2891D6DDAF1152E69ACF3876002D0A653E6A8D3FADED4B978 "点击放大")

DevEco Profiler工具的界面分为两大区域：

①[会话区](ide-profiler-session.md)：负责调优会话的管理。会话区提供了性能实时监控工具Realtime Monitor来帮助开发者先明确问题场景，完成问题的发现和初步定界。开发者可以在会话区选择待调优的设备、应用及当前应用进程，当前已创建的调优分析任务将在下方以列表的形式展示。

每个会话是一份独立完整的性能数据单位，是由开发者通过一次录制得到的，同一个会话中的各种数据经过工具的处理可以互相关联，而不同会话间的数据，由于来自不同时间段的录制，不会具备关联关系。实时监控本质上也是一种会话，是由实时监控这个场景模板创建的。录制会话时需要注意，确保场景复现完整后再结束该次会话的录制。

同时会话区提供Frame、Launch等一系列场景化分析任务类型，帮助开发者有针对性的采集并展示更多更详细的数据，这些数据将会还原对应场景下的应用运行状况。

②[数据区](ide-profiler-data.md)：负责性能数据的可视化呈现。包含工具控制栏、时间轴、泳道区域、详情区域，通过不同泳道展示，直观展示调优详情。
