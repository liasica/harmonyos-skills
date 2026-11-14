---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-frame
title: Frame分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2c9786c5cc384c9c8ef08fa728228fa1a9eb29fd7c51c4b1b7195ea2f6f78706
---

## 功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Frame、Callstack、CPU Core、Process。本文介绍Frame、CPU Core、Process泳道，Callstack泳道的介绍请参考[基础耗时分析：Time分析](ide-hmos-insight-session-time.md)。

**说明** 

卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在会话区点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/uXGdfINDQR6QOE6w_Ga7pA/zh-cn_image_0000002781311220.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=F91FA4FD8D2F75A8B62055892EF7F79A09DEF74F0122A69D86BDF3D02500F185)图标，导入历史数据。

## 查看GPU使用情况

**Frame**泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有**RS Frame**和**App Frame**标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

**说明** 

* 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
* 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Ik-RmNMDRYWrlOX6kkhnYg/zh-cn_image_0000002781471160.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=7522525BBAF06521F70CE89D3CFD8026ED3E36E5E6E32033B71BC1D871AA90E1 "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选**Frame**主泳道。

   窗口下方的**Statistics**区域中会以进程为维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/OGVNDw_MSUu2_zahw2FLWA/zh-cn_image_0000002810630711.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=84C1824BE69958CB72298A350CFC2B2FD79012910DBD6A2EA9F69E4BBF896C25 "点击放大")
3. 点击**Statistics**列表中任一进程的跳转按钮，在**Frame List**区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/GkdlDVz7T3-PoxsdrKfM-w/zh-cn_image_0000002781471170.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=8853A7711645D66E2B2AF987E340DDBAA9435A75B80BA30F03D6F192E93F9AE2 "点击放大")
4. 单击**Frame List**列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/9spC_DNyTKWUfdlmYCfotA/zh-cn_image_0000002810750807.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0483F6C63F4C832329E32FB7924D3FF20BB7AFB7640BFCEE536CCBB45ADB4BC)跳转至关联的切片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/9zMtlprfTfy8jVyz9cVLPg/zh-cn_image_0000002781471164.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB922FCBEC7AC332629DA65B213FADCEB88662C2E127E09FDF83BD3BD3CFE1F9 "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 展开**Frame**主泳道，选择要观察的带**App Frame**或带**RS Frame**标签的子泳道。

   窗口下方的**Details**区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/RzQAQEs6Rj2VPQrLdyngfQ/zh-cn_image_0000002781311238.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B11F21B0C1C5C98093D56542A4C5FE75265C993758A6989391EB4287C3663DD "点击放大")
3. 单击列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/jn_zy0SuR9yP-mF4kIsimQ/zh-cn_image_0000002810630727.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ABE12894DCE35C6FD5EF9CE45058FDEFA87BC011638C5B7D4F6FAD6A70D4EF0 "点击放大")跳转至关联的切片。

## 查看指定Frame信息

展开**Frame**主泳道，选择带**App Frame**或带**RS Fram****e**标签的子泳道，该泳道图区域上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/rQ-G6NmQQKOf_9IffZWYFw/zh-cn_image_0000002781471150.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=26A8C2C63974B71CA298F65B16CCD3142F7E51C73AB445F04469E00D0F2DCC94 "点击放大")

窗口下方的**Frame**区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。在带**App Frame**标签的子泳道中，**Non UI**区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

**说明** 

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CkvH4XWyR8GEuEqQnVRdcg/zh-cn_image_0000002781311232.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=6069D62D5483CB23C7022FAA3832201281231C4CDFDBC834528CBF294CE98EE1 "点击放大")

## 查看帧率统计信息

1. 展开**Frame**泳道，框选一段数据。
2. 带**App Frame**和**RS Frame**标签的子泳道会出现FPS标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/v-jB-65xTnG1MgkJDqdKvw/zh-cn_image_0000002781311242.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6CB3E26DA09105178C9BAE41802958A7D11F71ED4025283D9F99FBA49D2C66F "点击放大")
3. 在带**RS Frame**标签的子泳道中打开**筛选出ArkWeb数据**开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/3le3jYbxQTGrnFFc_IkIzg/zh-cn_image_0000002781311228.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A7229C5AE769BCCFA4A3F913645AABCE92DDDCB05CD264A95FE06105C04D830 "点击放大")

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/QyGNdlN6SUCfmcTGbwKkkg/zh-cn_image_0000002810630709.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=69F330EE8ACE8C59311BF15A5411A75C7D94619A60E4D52D71B90045E8299D7F)图标下拉列表中选择显示内容：
   * **Slice and Frequency**：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * **Usage and Frequency**：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/zIkoObTsSSqpmcDrvoamsQ/zh-cn_image_0000002781311230.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=56AC9B45FF2933CE3C31F65E81E4F389AF68B1B5161675E515F05C6CB2E5AB8B "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/6mQcxO1GS5eDYNsxDDGZaw/zh-cn_image_0000002781311236.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA9F61468F34BC09F28CF9BAB93B3BB2E6716DE024E1B9EB5715A860923C4790 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/glMo3zRjSoe8bX7SgJ2UNA/zh-cn_image_0000002781311216.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E1D38068CDC96335977BC00A1CAEA3DCC3119C8096B2CEA7AC89F9912FBF0E9 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/N4FhhgbVT8OcJpQDbF_Gfw/zh-cn_image_0000002810750833.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=E484EA1345831A411F1775A8DF75E625A395E64A5FC60F5B9B0A6251A40CA96A "点击放大")
   * 开启**查看完整调度链**后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/OSZEpjapSBGwCaPFkWvHAQ/zh-cn_image_0000002810630725.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E5CBD7DB96722D35A27A01A9413E3C5978C1BECEDDC9248D8422BF9111A31D8 "点击放大")

## 查询进程详情

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、所属进程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Kharg4A8TBaV2lbcTLHp4A/zh-cn_image_0000002810750827.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C103E6D6541534BFAA816F7ADFDC532B3930B33D6198A1F98C50EFB5D1A5198 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Ov3XFEbJRqCWXcoyCTwuUw/zh-cn_image_0000002781471152.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFBD4E41CEDE3AFCDCAC31BFF0A714DDBC861F280BE66C95131AB30ED74F82A0 "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程数并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/uxFW_DpJQ7qVFgZPvcdSug/zh-cn_image_0000002810750821.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF40F7B8A5E182564E2435C27FEC9D79D2911CC8355FF09571CFA62A6D8F971D "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/j3lxM8AJRTyj-9Hni0STrA/zh-cn_image_0000002781311222.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=F65BED0B1DDFE561263B3FBBD23D29A8535DDDDE4D3B9CF500A28B84D5663BBA "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/ycwpKc14SuWPfu70wMvmRg/zh-cn_image_0000002781471172.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FB6F8630A8E47A833A46596D86A52679C57B9437B9CC29A4C12A2476FB56F71 "点击放大")
