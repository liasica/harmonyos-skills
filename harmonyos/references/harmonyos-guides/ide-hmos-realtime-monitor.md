---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-realtime-monitor
title: 性能问题定界：实时监控
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定界：实时监控
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:58+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:425e67d478949c6770b2c3b0e288821032ed25495a7a39a62ad4b1912d03bdbe
---

## 功能介绍

解决性能问题，首先对当前应用的运行情况以及设备的资源消耗进行监测，以初步确定可能存在的性能问题以及问题出现的位置。

DevEco Profiler提供实时监控（Realtime Monitor）能力，可以实时监控CPU占用、内存占用、实时帧率、GPU使用率，帮助开发者了解到当前应用具体运行情况和可能出现性能问题的热点区域。

## 实时监控面板和泳道介绍

### 面板整体介绍

整个实时监控页面从上到下，依次展示CPU占用、Memory（内存占用）、FPS（帧率）、GPU使用率等各个维度的数据，帮助您从多个维度来对比识别当前应用的性能热区。

界面左侧为实时数据展示区域，该区域的数据显示了每一项监测内容的瞬时值，并通过饼图或者仪表盘的形式让您更加直观地观察到各项数据的使用占比以及具体数值。界面右侧则是各项数据随着时间推移的变化趋势，通过不同的图像形式（直方图、柱状图、折线图等）来更加清晰的展示某一项资源在一段时间范围内的变化趋势，以帮助您快速判断性能热点区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/e39HQhBkRDSOwZpcZu7bvw/zh-cn_image_0000002792001038.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=329479C45ECCCBFC435DF549F661BECEA7189468B8783C6FCE080773FB6FC801 "点击放大")

### 泳道介绍

* CPU泳道：左侧饼图展示了当前时刻应用/元服务的CPU使用率、其他进程的CPU使用率以及空闲情况。右侧的泳道图则展示了时间窗内的整体CPU使用情况，其中绿色的部分代表系统中其他进程的CPU占用，蓝色部分则展示了当前应用/元服务的CPU占用情况。
* Memory泳道：左侧饼图展示了当前时刻应用/元服务的内存占用、其他进程的内存占用以及未使用的内存。右侧的泳道图则展示了时间窗内的整体内存使用情况，其中绿色的部分代表系统中其他进程的内存占用，蓝色部分则展示了当前应用/元服务的内存占用情况。
* FPS泳道：左侧仪表盘展示了当前设备屏幕的帧率瞬时值，红色、黄色、绿色区域则代表当前屏幕帧率是否达标理想状态。右侧柱状图则展示了每一次采集设备帧率时的数值。
* GPU泳道：左侧仪表盘展示了当前设备GPU使用率的瞬时值，右侧泳道则展示了时间窗内的整体GPU使用率。

## 实时监控常用操作

实时监控页面除了展示各个维度数据的瞬时值以及时间窗内的变化趋势之外，还提供了多种交互方式协助您更加便捷、快速、细致地分析您的数据。

* 启停控制

  点击会话区实时监控页面上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Fl2ID-ntTnWUYNikfUmH3w/zh-cn_image_0000002820680999.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD66DB154EB0C0C36DB5703CA66F993C797D75F3910E64B394EFC88D93CD785B)、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/eTGUZbx8TGGucbAYomPX3A/zh-cn_image_0000002820721007.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2EA36C556C365CF01A9C09687AA39A292EB07A422FE6EEB93C2EB4562008030)按钮来即时控制实时监控界面的录制状态。
* 详细数据展示

  将鼠标悬浮于所关心的泳道数据上时，界面上会出现当前时间点的时间标线以及含有当前时间点上泳道详细数据的Tooltips。更进一步，当您将鼠标悬浮于时间轴之上时，实时监控页面内的所有泳道均会以Tooltips展示出该时刻的数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/E-IDSL84TySYdqEyOcu2sg/zh-cn_image_0000002820681003.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAFC3EC10EE0CCAC9697DACC7DDF434FB9707F8291EFF42FFBE755DE84B073B5 "点击放大")

* 图例选择

  实时监控界面部分泳道内的图例均支持选择/反选来增加/去除泳道内这一数据的展示，内容改变后泳道内的数据会自动缩放以适应泳道的高度，能够更加专注地分析所关心的数据。

## 启动实时监控录制

1. [使用USB连接方式](ide-hmos-run-device.md)完成设备连接，并启动您想要监测的应用。
2. 通过如下两种方式打开Profiler：

   方式一：在鸿蒙电脑DevEco Studio图标右键，选择**调优**打开DevEco Profiler。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/xyH4rVKWQG2LCtaZ8T9hJw/zh-cn_image_0000002791841064.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB61233BCC664741A933996C441AE028BDFA6673955770E752DC1DB87CDBCC5D "点击放大")

   方式二：打开DevEco Studio后，在菜单栏点击**运行** > **调优**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9dfQC2V9RTaRp20ltypKxg/zh-cn_image_0000002820721011.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=96700F04C4D1E46DF88AD1E9491724E7B8E4810B1130E8C82154186383943DC9 "点击放大")
3. 选择待调优的设备、应用或进程，以及选择实时监控的模板后，点击右下角**立即开始**录制，或点击**打开文件**，导入历史数据。

   录制时若设备不止有一个主进程，还存在Extension或者Render进程，那么您需要再手动选择一个您想要监控的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/G1CfEfB4Qli5874l4OGH6Q/zh-cn_image_0000002792001040.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9E4F9539F635EF4EB0DFA5742AEA7649745CDDC0E3839659A5962312CE8D8EC "点击放大")
4. 在[数据区](ide-hmos-profiler-data.md#section8296319104115)点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/zbTBey3ZQCylKpzGTVh--g/zh-cn_image_0000002791841068.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BCF639E78510A4EDF6933C79526A46EBDCFF260F01711FF9C4F92810B0CC82E)、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/FAv34V-ASfeYgospixkdZA/zh-cn_image_0000002791841066.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=C564946EAF03FF563C3A8AC976691AFAD8174AB7591E7D6C47A01B4F1E243473)，开启/停止会话录制。
