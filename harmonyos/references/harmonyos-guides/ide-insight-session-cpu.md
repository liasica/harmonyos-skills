---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46299f65bbc71177254235f054e5ff803398a83df9c389cd0c193947334286fa
---

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

## 查看各CPU使用情况

1. 创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。

   CPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Hp4dCcMWT2uhxDQp85Q6Rg/zh-cn_image_0000002530753316.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=8560E0E22AC2AE0A93B0964BDA12BBF88CF1209092346D07A6818702F8B420A4)指定要录制的泳道。
2. “CPU Core”泳道显示当前选择调优应用或元服务的CPU的使用率。

   可在“CPU Core”右侧的下拉列表中选择显示内容：

   * Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/exBb00xUTmi79XcIs6qBcg/zh-cn_image_0000002530913304.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=9BBF32AA83C0796B2D92619934DE216122037ED445791FF4E82ECB1E2EEC6496 "点击放大")
3. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   说明

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/yTcRPBIfTB-bly2d176Bsw/zh-cn_image_0000002530753302.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=846AE436305E5E659A35C6E080F99EF5271CD0DD0CB01E455816B4FE2796CA8C "点击放大")
4. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/h5EDK43cQXCl_XWV7YxTyQ/zh-cn_image_0000002561833239.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=005E8B8486E49766C480434099D618A6AD0DDFB63F81E5E005892F33422F22E3 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Rhkc5FhHTUe3fw_rcDJsvw/zh-cn_image_0000002530913306.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=E5525FE9B7846403E7D58D6CEEFF5362685EF247B3494E29AEFA9C268F9EF0D8 "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/7Eczugo8SSCDM4skyqMUpg/zh-cn_image_0000002561833231.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=835750DF21A4C829433C1BB8225966473327487DCD6EF1D7F1B67874F767FB75 "点击放大")

说明

* 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
* 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
* 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
* 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
* 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
* CPU分析支持能耗分析，请参见[能耗诊断：Energy分析](ide-profiler-energy.md)。

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/UUtrrmztQyqS5jAd6GIPhQ/zh-cn_image_0000002561833243.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=D9FC2AE35A303F890C3F5617B4224E52853F0E657767AB9A1DA744EF7532062F)按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/9KUSGJs9RMaccSB1_MUMOA/zh-cn_image_0000002561753251.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=B29A85D745256A875DCB3470195A5F8DF42D6335DBECA4CA5696115875311909 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/amfg8TvtQDKvBAizDCoFxg/zh-cn_image_0000002561753245.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=0D46B68CC18E0E2CF9053BE47671CDC0F7F7FEC9F18CB6D69F985958D91AD760 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  说明

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/AcwYtE_hS5mf2YY5vw0ggQ/zh-cn_image_0000002561753259.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=339CBC948E412C41E11600DD88CDE316F4E2F98BC6B4E32139D17B8777EB4E4E "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  说明

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/9zevXl2gQkuSpjkpNRocmg/zh-cn_image_0000002561833237.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=BD8F5F4A7460CDB29F130D4B1AC1F3C71273AFDFD3C2CDB95C0DECDF8FCD491F "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  说明

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/5e4TP1kNQLWOrc-nxbv00A/zh-cn_image_0000002561833225.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=AB9F27B7768CD63FCDEBA2B8C8A273F93641E43C242F9B6ED8F8BAC68FE1FE45 "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Ngc7IMLfQXCZQyAWfCB0Gg/zh-cn_image_0000002561833221.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=B6E9524E44B84CD083A8C5135CF484B7E4AA4C2948E59BA30F0C91BD9821D927 "点击放大")
