---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-frame
title: Frame分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:49+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:62e200248fb1c6379092dace7594168126f68caed5ae717ae897ed49e0f60cf3
---

## 功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Frame、Callstack、CPU Core、Process。本文介绍Frame、CPU Core、Process泳道，Callstack泳道的介绍请参考[基础耗时分析：Time分析](ide-hmos-insight-session-time.md)。

**说明** 

卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在会话区点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/MhbMtbZ1TYiYtwydT5WeAw/zh-cn_image_0000002791841194.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=2394E174D7706FEC9296E399D61444820AE6790B7EE2F4A27BF67FD883D1018C)图标，导入历史数据。

## 查看GPU使用情况

**Frame**泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有**RS Frame**和**App Frame**标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

**说明** 

* 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
* 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ySAWnZT9SbWWXsx5zPOzig/zh-cn_image_0000002820721137.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0A5811ED31E543C6AC30191C6B5B0183DA0B09DF1D019E00401BA8CA289EED9 "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选**Frame**主泳道。

   窗口下方的**Statistics**区域中会以进程为维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Ioou0vpnSf2W3IrBmff6pw/zh-cn_image_0000002791841196.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DCFABC473C267534F4F5E0388AA2F3488258B1E87AC4E91F31974672712B56C "点击放大")
3. 点击**Statistics**列表中任一进程的跳转按钮，在**Frame List**区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/HJ28EViJTXW1kBo3nMV8Qg/zh-cn_image_0000002820681133.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCF60AB197CFEAA46D8B17D27BD0D176187964AA8EE337A2142C7CEC2B7C2AFB "点击放大")
4. 单击**Frame List**列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Lgoj4fdDQIer11lYqyv1Qw/zh-cn_image_0000002792001168.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFBE7F0226969B18B1A60BD7F50E367F8B4B637932E6E2E9D094D8E9EE613E8D)跳转至关联的切片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/0k4Lgo7ZSoek4BO9cTZTpw/zh-cn_image_0000002792001170.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BA51FD4B53B65E50A43265C07F82328894D703849CDCD8E3BDC7DA57D5EFB10 "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 展开**Frame**主泳道，选择要观察的带**App Frame**或带**RS Frame**标签的子泳道。

   窗口下方的**Details**区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/eFM2ZdmSSbW3pSo3kkDJDg/zh-cn_image_0000002820721125.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=B03CB9B91CEAD8D9ABB548BE66F8EB9BF0DA019D7C362F61A909C028A15D8DBE "点击放大")
3. 单击列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/RU7l6UnWRE6yrnpY_pqI2w/zh-cn_image_0000002820681127.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0190234B643B731FDF3D767E053FBFA22721F789A8218B4DB3E5EDA6BC9BAC8 "点击放大")跳转至关联的切片。

## 查看指定Frame信息

展开**Frame**主泳道，选择带**App Frame**或带**RS Fram****e**标签的子泳道，该泳道图区域上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/frZ1ob2JR8qIFxja74l9jg/zh-cn_image_0000002792001172.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A579FCAB8C1EC035D0E87783D38E4F4246FD121741FB951D5065F2E91F78497 "点击放大")

窗口下方的**Frame**区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。在带**App Frame**标签的子泳道中，**Non UI**区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

**说明** 

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Y1-BfG2-SwuKaE7sQHCYpg/zh-cn_image_0000002820681129.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFFD86CAC76354B1C6393AF88EEF8F74812D2C57FD2BA9E44139762F0219097C "点击放大")

## 查看帧率统计信息

1. 展开**Frame**泳道，框选一段数据。
2. 带**App Frame**和**RS Frame**标签的子泳道会出现FPS标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/DUU0XdPvT4uye1Od0t4yng/zh-cn_image_0000002820681131.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=D25B057BE257FF64E8222FE6CF6FE0C7B00E7597042CD757DEE2412BE14294AF "点击放大")
3. 在带**RS Frame**标签的子泳道中打开**筛选出ArkWeb数据**开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/9i7OXv-RQDqjIa9S9oOlrA/zh-cn_image_0000002791841184.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=107C818C39D338350BECFD2A4107188ACC076805CA6BFFE0B21E82F61457E5A4 "点击放大")

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/MEPirAaQRdus2a9MmCBzLA/zh-cn_image_0000002820681123.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=1704DE9B47C7E9FA2281F61E541F3131991C51276F06DE94A8361B6E78AC79CB)图标下拉列表中选择显示内容：
   * **Slice and Frequency**：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * **Usage and Frequency**：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/lbLiwLzqR1yrzt9nTiK9cg/zh-cn_image_0000002820721135.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=36B0F8AEE86ECC59E94A52E3DC82B2B85BA731488FEA03B46CABC68032EFBCAF "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/UeYSp0sgTlCSjoH7oklaow/zh-cn_image_0000002791841190.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCA7801F559F05DE95322DB1C23D339E2FA14707C628AE149CB5FB478BAC3147 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/qHj3B-RERCm2KXF_pZ8j8g/zh-cn_image_0000002791841188.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFA9EECF17D856BEE4B82D7EEB390EF817A5757B05505761BE5BF164B8946174 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/vzaouxoqRpitlU5JtktJcw/zh-cn_image_0000002820681125.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F6EF7AFDA31A7753B2685767F4EA5E9E393F55B0FD9B3543D779055B080148F "点击放大")
   * 开启**查看完整调度链**后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Mc2id9M8R0StD2XyfA1VRA/zh-cn_image_0000002820721133.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EC6007A97BA5F709F7A1691FAC4E1FB5AFA95B93EB5CBE42CBA9BE725BCE96A "点击放大")

## 查询进程详情

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、所属进程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/C8ah1jkISySumMPPr8skhA/zh-cn_image_0000002791841192.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=B978406C2CCE9174CF00B8E55C36F18400915221C8D5C61DD138CEFD6E0D9397 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/gFr80TSGQ16m6EcQJRaujQ/zh-cn_image_0000002820681137.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=33E7B07545CEC36D9394C10D85F8B9FA57AACEFBD15CEEB060C6E52494B8A334 "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程数并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/uOXp1kv1RCiq-ZlnmjfLuw/zh-cn_image_0000002792001158.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F9D03103C3DF5D7C648FB8F02A9E2A0210F938CBE6F2014D580E6C346DB4715 "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/C0ZK6x4YT3KUH4kDpHiyzg/zh-cn_image_0000002792001166.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=B71AB78693689CA791237B89A3F5A83098AC101284871C7B780A6A03B0B9CDD9 "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/tEHHHCPLRqqR_bDxOYmHGA/zh-cn_image_0000002820721139.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=E380A75557DF57FD59AEE49C9EFEB1A850DC6C065BEB892F06969CA8A47D6B6D "点击放大")
