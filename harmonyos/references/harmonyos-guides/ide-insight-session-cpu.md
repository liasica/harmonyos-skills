---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:88cae13b9b3be18720bce5678bf301c0b94f26ad18e532ce16b9d78b5f2ff5bc
---

## 功能介绍

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

CPU模板支持的泳道包括：Energy、CPU Core、Process。本文介绍CPU Core、Process泳道，Energy泳道的详细信息请参考[能耗诊断：Energy分析](ide-profiler-energy.md)。

**说明** 

任务分析前，需创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧**options**下拉列表中选择显示内容：
   * Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/IpJJdJc2RQ2MVxDyVFlQiQ/zh-cn_image_0000002808766625.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C155D90FF04A6A6E8B9F1BE5B10850F8E34CA601AD112F4E4E96A686F6F48BBD "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/tu2aL99SSxuYsTNBjmD66Q/zh-cn_image_0000002779567040.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=88E99FA0649A17C3D83EC62A900CBFEC534B69DAC72534B0772DC800FF06DEF0 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Bm_0GKIOTrGNgTdra0PdGw/zh-cn_image_0000002779407068.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A6A141EA006A6C079D39AD12A077033831CE14DACD87AFDBA03A04F5A27E5C2 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/NgZOc6J5Sk-Q8_iIaRzq1Q/zh-cn_image_0000002808886707.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC15FAEB7C6BC3DFAC3DBC3AB338E579F911A8802CB4F7C5D2A551C2F14B3558 "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/93M9JHW2TcG5IVm6AyfGNQ/zh-cn_image_0000002808886705.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7B16319FD434BB8D6A5678B0C5CDC4295F24BFB34C80D42F7138D926FE8F790 "点击放大")

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/ZvqjHBX7RHir3lgPUo8l8w/zh-cn_image_0000002808766629.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8301BDD16D2F4DAE720BBD9AFED74218D68C5C8AE3AE795771073B616D18DAA5 "点击放大")按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/zkAJvOYWQkCTq21HUfRHNQ/zh-cn_image_0000002808886709.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3C193DA7125D38484DBA92E53CB32786C522C238376404876267DB127665A08 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/e_yMfqFeSLiQRFpJC3rxsQ/zh-cn_image_0000002808766623.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=75A0E59600319C2DD55ADFD2834CF0D1BEDD85D1436EC00EE438FA66C26EBCC7 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Afjx56RXRjaMlnyw1ATm9A/zh-cn_image_0000002779567048.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=53EB79DBA609679AE9420E8119D99CD46BCFA4EA2E3A105C27FDB7BD96DBB7DA "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NJHXQsToT6CUn24wHNsE1w/zh-cn_image_0000002808766627.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=06E706B1CA79A977DE2740BB0CF1B5FCBA83BE795EF45F4AB78E87370782381D "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/OsRNAdnjR5OK0TQzhsxBdg/zh-cn_image_0000002808886703.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=66579EBE0E72E9751F47888CEDA79D324F8C3FCB3E83E9ABBD87B0EE3E0F410C "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/L4ssqFeMRwuGZHP08f3Obg/zh-cn_image_0000002808766621.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD83CAAA0D5C436A6A0120C0FAF14FC5023C5300E405B5F65BDDE5C4AEBE35F1 "点击放大")
