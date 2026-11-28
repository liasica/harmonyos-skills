---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2bd4eedb3727e1565c6c611dda5697f31fb3a2937d2fe79f668cc8d29bcf2b99
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/XEXjeGAoSpix5rLBDyHIHQ/zh-cn_image_0000002808766625.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3629C8D84F6A7C62E116769DB6414E791346F088F4D7731CC9534F2B6E44A02 "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/W436Tnf1TRGTVYGkB5I_SQ/zh-cn_image_0000002779567040.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D35744C813360D008899247A58AEBC1D4D5DC793CBD3C8BA7186EDC888AA5DE9 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/HWeL8fMkT3uQlFfNHKsXlg/zh-cn_image_0000002779407068.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=55CA086D2EFD3CC92B7F816C6F1FEA550F795243864A9489C31FE22DE3081E12 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/5EHVP-UyTqG1qhaSjy_qXg/zh-cn_image_0000002808886707.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=A260508DE6A5E434D0EABDE1318C2373D557B53E0960CA0F4FBAF5F4A32240B9 "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/LEbKvbzkQwGTNJP5gzw-Fw/zh-cn_image_0000002808886705.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AE256838ED892AC4863BE8B10CACD413E1FA080D54CB6C4A0E3A31EF87D15F7 "点击放大")

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Tmn_d7DZT3Svg-wLhCV2yw/zh-cn_image_0000002808766629.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D39A13E2795459DD17FFA24C0A5CB83BD96C8AC5BED8839CCBD5768613F9B4B0 "点击放大")按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/NIC-DpxNSLCL3Jb5Ab-8nw/zh-cn_image_0000002808886709.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=87FE364C80CF6BDD1F819326C758E7100A8DB560D15B85DDA5344F0A2B23669D "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/j0bXjboJQoCNflUOTelsyA/zh-cn_image_0000002808766623.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9FEE5C42D540788A815FF424ACA35382FFA4D5D3E340AEBD8E8ED9ABDCA286F "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/xLTBF7HTRYG3lsRnlg3NtQ/zh-cn_image_0000002779567048.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC7392E995D63F261D530536C9D20577D1038EBD66B256810338AFE11535FE6B "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/akW1YoimSd6P8d-Fo-QU7w/zh-cn_image_0000002808766627.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=441B8882EAC2A4AD8F0FF4513A4A9D50D63AF285C9829D07A3C68755A076A2CA "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/95UzE_dWSmKtaZkRnoV-VQ/zh-cn_image_0000002808886703.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=44A92F8E60FDC29569517BF567EA5D62CEF7B0FDC6261A18CF6ED88DA818E5B2 "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/8YI-XbmzQuW7VtX8oNV5SQ/zh-cn_image_0000002808766621.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=42B6429DAAF494CE5CC15166D2D87810249E7EF770D5F331B71434DD36BCB744 "点击放大")
