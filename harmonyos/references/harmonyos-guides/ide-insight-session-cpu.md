---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5376ec83e2f333dac131f70112598719f085215d859c56dfa61dd266689be3d8
---

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

## 查看各CPU使用情况

1. 创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。

   CPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/CGuM-vLQRiOxg-1M6ZKXsw/zh-cn_image_0000002530753316.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=F7187B1F05E09BBC94AB934455E9E87272AF4B3F31137AC46CFB5B07681546A0)指定要录制的泳道。
2. “CPU Core”泳道显示当前选择调优应用或元服务的CPU的使用率。

   可在“CPU Core”右侧的下拉列表中选择显示内容：

   * Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/wHh9LfZbSyOrYI0j9DNafA/zh-cn_image_0000002530913304.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=9216C23B47F59206D66ACE6472B84A28CF6F4A9BD40DC75662A1BBC13EE9D831 "点击放大")
3. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   说明

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/mMt3G1UnQkikVSmzMVFlWw/zh-cn_image_0000002530753302.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=ADE40A7B4C38BC70BF14177B2EEF40049EE2196600D9CDC5BB9B1AB8DDE8DEF6 "点击放大")
4. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/GcKT6XSOQQOuSquyz4ciLw/zh-cn_image_0000002561833239.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=025500EAEB1E8CD521F22E891CC9D7E264937560C23C5A29B20477067072F508 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/wNFoDAj0SuK4ZxE4MSDBfw/zh-cn_image_0000002530913306.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=591A43C3DD856E1D16F0C6B583121BF21100D0D48168057E181ACED24EBFC6BA "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KFY_GtIhTE2bhrccZ5zQnQ/zh-cn_image_0000002561833231.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=5FABAA3BD67C6F8E0FCEB69A9724BC644EE915F9FBC6E90BF6DD419A26EEE639 "点击放大")

说明

* 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
* 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
* 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
* 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
* 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
* CPU分析支持能耗分析，请参见[能耗诊断：Energy分析](ide-profiler-energy.md)。

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/pbvX8P9vS3mnjqXY0ZFA7w/zh-cn_image_0000002561833243.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=C6EAFB71F731376C685897CF584D8885FB53FCE02DE8EF6923A482D7CCB906A9)按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/7FdwfrjnSD2mT8p_LePA1A/zh-cn_image_0000002561753251.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=E5AAA15DCEB164C9E445D5458B2954ADB0E0887461BEA1E7EF4A44EC9C13A1C3 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/VpDfrCbKQB24YeSmR4x8UQ/zh-cn_image_0000002561753245.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=9BF01DA90B964657AF195770506C8BD4559B338F995E95AB24F03F7231E51B15 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  说明

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/yhb-4w-nTtSj5pHDJgPsdA/zh-cn_image_0000002561753259.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=09DCDFBF2A3B5B8F52AC388D902C555E0BD8F5AC07699CF29C7EED420BE39729 "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  说明

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/qS1usp0sT_a2BpMYBUmseQ/zh-cn_image_0000002561833237.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=DB585EA32DF9459BF4C9CEA58C90A3D970F6A8A96C9266CFDF914ADBF7F6A2C2 "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  说明

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/OHU_ix7kS3KYX6A6Tri79g/zh-cn_image_0000002561833225.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=AF6083E435DF708FEAC829D0707D6DBCCDBF78FC6B21D7D3F47E16F213CA5DAE "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fo0bPEu-RbatdGYv-sZO7w/zh-cn_image_0000002561833221.png?HW-CC-KV=V1&HW-CC-Date=20260429T054745Z&HW-CC-Expire=86400&HW-CC-Sign=E525E8D8C4AEC9AB977ACAE616C44D36D5DBEAD0173FAEF87C9AE8486265F417 "点击放大")
