---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-layout
title: 界面布局
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 界面布局
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:24+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:bba50fb6ef75b8e4aa6dff96fbb367586978b50fb7dafe79506b7d71009dea7f
---

DevEco Profiler工具的首页分为两大区域：

①[会话区](ide-hmos-profiler-session.md)：负责调优会话的管理。会话区提供了性能实时监控工具来帮助开发者先明确问题场景，完成问题的发现和初步定界。开发者可以在会话区选择待调优的设备、应用及当前应用进程，当前已创建的调优分析任务将在下方以列表的形式展示。

每个会话是一份独立完整的性能数据单位，是由开发者通过一次录制得到的，同一个会话中的各种数据经过工具的处理可以互相关联，而不同会话间的数据，由于来自不同时间段的录制，不会具备关联关系。实时监控本质上也是一种会话，是由实时监控这个场景模板创建的。录制会话时需要注意，确保场景复现完整后再结束该次会话的录制。

②[数据区](ide-hmos-profiler-data.md)：负责性能数据的可视化呈现。包含工具控制栏、时间轴、泳道区域、详情区域，通过不同泳道展示，直观展示调优详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/XUrmEwn-TDG1-hWeVy1LGA/zh-cn_image_0000002750009760.png "点击放大")
