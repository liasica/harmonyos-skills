---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-frame
title: Frame分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:53+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9af14ee5fc5d55011bf23776699b27554fa8747f25e54bd44f91d7f1e7bb53e0
---

## 功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Frame、Callstack、CPU Core、Process。本文介绍Frame、CPU Core、Process泳道，Callstack泳道的介绍请参考[基础耗时分析：Time分析](ide-hmos-insight-session-time.md)。

**说明** 

卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在会话区点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/pVvio9GBQ16Rfq-Wo31a6A/zh-cn_image_0000002750169678.png)图标，导入历史数据。

## 查看GPU使用情况

**Frame**泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有**RS Frame**和**App Frame**标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

**说明** 

* 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
* 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/sGZo2AeCS36bZT0TjM6G1Q/zh-cn_image_0000002750169684.png "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选**Frame**主泳道。

   窗口下方的**Statistics**区域中会以进程为维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/z7VAfnhWRO6nQxRp3pLhUQ/zh-cn_image_0000002779728857.png "点击放大")
3. 点击**Statistics**列表中任一进程的跳转按钮，在**Frame List**区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mC8RmKVMQV-VTzbmHOBysQ/zh-cn_image_0000002750009804.png "点击放大")
4. 单击**Frame List**列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/nCyOmLKGQnee77Qp_3hb1A/zh-cn_image_0000002779728849.png)跳转至关联的切片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Gv10eK8ETAa0humvKIQ3IA/zh-cn_image_0000002750009802.png "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 展开**Frame**主泳道，选择要观察的带**App Frame**或带**RS Frame**标签的子泳道。

   窗口下方的**Details**区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/grF0o2OvRvS91ta1B51dDw/zh-cn_image_0000002779728867.png "点击放大")
3. 单击列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/85BKUmcJRhWfqYXBH1uIfA/zh-cn_image_0000002750169696.png "点击放大")跳转至关联的切片。

## 查看指定Frame信息

展开**Frame**主泳道，选择带**App Frame**或带**RS Fram****e**标签的子泳道，该泳道图区域上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/elQjG3DeQ7yc7_X5dNj_4w/zh-cn_image_0000002779728851.png "点击放大")

窗口下方的**Frame**区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。在带**App Frame**标签的子泳道中，**Non UI**区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

**说明** 

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/69abJVQ4T1iYom04omT-4Q/zh-cn_image_0000002779728865.png "点击放大")

## 查看帧率统计信息

1. 展开**Frame**泳道，框选一段数据。
2. 带**App Frame**和**RS Frame**标签的子泳道会出现FPS标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Dg9AuwyxSPmTicjh1HagGg/zh-cn_image_0000002779728871.png "点击放大")
3. 在带**RS Frame**标签的子泳道中打开**筛选出ArkWeb数据**开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/0PifIGbeQcyxt0HcBg_vTA/zh-cn_image_0000002779608711.png "点击放大")

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/j7G3OumFSCKa7-WYuQ56WQ/zh-cn_image_0000002750169682.png)图标下拉列表中选择显示内容：
   * **Slice and Frequency**：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * **Usage and Frequency**：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/GSBe52ffTXeNyAi84aIz3A/zh-cn_image_0000002779608713.png "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/-L7CJ3MvRFyrYtL8Sj5QZQ/zh-cn_image_0000002750169692.png "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/WX4_MGatQFKSc-nhljxEIw/zh-cn_image_0000002750169676.png "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/1dJgaH9NT0WZYXI0dG-GyQ/zh-cn_image_0000002779728869.png "点击放大")
   * 开启**查看完整调度链**后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/d9B60ciiShG0fE0PMD6n9Q/zh-cn_image_0000002750169694.png "点击放大")

## 查询进程详情

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、所属进程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/iEk6wxXiRZaApS7daJhZTA/zh-cn_image_0000002779608715.png "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/X18KUbm-Q9SDGQXK0gW9jA/zh-cn_image_0000002779728853.png "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程数并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Ix2zE69eSrG01-75EtJz2A/zh-cn_image_0000002750009800.png "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/B0j_u5QBTJuKpgmt7w7exg/zh-cn_image_0000002750009794.png "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/fALor9MtRuiz1keNmhfAXA/zh-cn_image_0000002779608717.png "点击放大")
