---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-frame
title: Frame分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:26652d48d056c9babd8e557b3fe0377eeaf92745af1aee7e4866f2852f677228
---

## 功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Frame、Callstack、CPU Core、Process。本文介绍Frame、CPU Core、Process泳道，Callstack泳道的介绍请参考[基础耗时分析：Time分析](ide-hmos-insight-session-time.md)。

**说明** 

卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在会话区点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Okst0bKhQ4CEKxJ9OXqb9Q/zh-cn_image_0000002781311220.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=488CCF3CC1189B4EE6BF5F82EF9A0532D986AB22CECF90EC8358F8220CC1C763)图标，导入历史数据。

## 查看GPU使用情况

**Frame**泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有**RS Frame**和**App Frame**标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

**说明** 

* 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
* 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Jo5BCXniQOSTqjHf4WYm4w/zh-cn_image_0000002781471160.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B926D201F313E6F00A58789AA012D540BE23B486E9197976624DE91EB75EC4E "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选**Frame**主泳道。

   窗口下方的**Statistics**区域中会以进程为维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/gF4iaq8bRQm9YGA4qdAOnQ/zh-cn_image_0000002810630711.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B1DB9395F98D764D441420221D1A4F20097664B2E99FA535E828FF1C8FB7EB6 "点击放大")
3. 点击**Statistics**列表中任一进程的跳转按钮，在**Frame List**区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/JCGk6Y_OSSyTHlcqeuJnLA/zh-cn_image_0000002781471170.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=18132F5F8C419E3EE3A3DECD2C3DFA10600B0017932FAB979EC76563762A7868 "点击放大")
4. 单击**Frame List**列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/5ZWpt2gjSVarPkTuC6E2mw/zh-cn_image_0000002810750807.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6CA267F0CC0B9AEC2F841E63526D59CD2B7C4564C70280C234A65D8ECC57AC1)跳转至关联的切片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/LcJWT331S7i8vx1iW1CnUA/zh-cn_image_0000002781471164.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6778D59F8B505626D0A4C362D06D4A804217A9F0A93A02437D0E664F2BCBE71 "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 展开**Frame**主泳道，选择要观察的带**App Frame**或带**RS Frame**标签的子泳道。

   窗口下方的**Details**区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/WysW7_g3QdC4bssC6hckpQ/zh-cn_image_0000002781311238.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0C1396C26EA88AB1A9179F82C9BBD307B6689F3A353A09E31A08AB129CDCAD6 "点击放大")
3. 单击列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/JjaWs9OuRvKO6qToFfrF5A/zh-cn_image_0000002810630727.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=48AE9ECC62382FF514E3D8C3BFFA8215E9FDE5A5E1D00F6E0E2A209A1A7AD583 "点击放大")跳转至关联的切片。

## 查看指定Frame信息

展开**Frame**主泳道，选择带**App Frame**或带**RS Fram****e**标签的子泳道，该泳道图区域上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Zf96gZZKRmaRaMbPUVrFjA/zh-cn_image_0000002781471150.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD23B7201FCA1A12C2538D794DB9C64B452C71A77F0935B1977FFA6071371C3E "点击放大")

窗口下方的**Frame**区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。在带**App Frame**标签的子泳道中，**Non UI**区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

**说明** 

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/okrBpgvdTZ-2qGh7A2GGMQ/zh-cn_image_0000002781311232.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0B76A80D5315E00F3BD4DAFB88F4F4955840581961F8CF16FFB8099213F3D15 "点击放大")

## 查看帧率统计信息

1. 展开**Frame**泳道，框选一段数据。
2. 带**App Frame**和**RS Frame**标签的子泳道会出现FPS标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/3C5jfG6tTVGQeEjxPOB98w/zh-cn_image_0000002781311242.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=172595F37501BEECC09411FC17958A327538AC125D3F2E5CB09FCB39AA94951A "点击放大")
3. 在带**RS Frame**标签的子泳道中打开**筛选出ArkWeb数据**开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/1UQF7j9vTJSsb8cc0-JJKg/zh-cn_image_0000002781311228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5078015CA29B794A59A37F544A884E76E1149FFE569C122E77A85718C77ADBE "点击放大")

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/nj2ytXHXTUiEMxN_FQfJpg/zh-cn_image_0000002810630709.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3527BF897D69320913764CDDAC16ADBE4209C9420E5A5DD7F0F1A825713BBC2F)图标下拉列表中选择显示内容：
   * **Slice and Frequency**：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * **Usage and Frequency**：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/yQXGjxDrQhCryxXc2CyGsQ/zh-cn_image_0000002781311230.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=05861E8A6C2576631A82A9C0236377C5ACBFF54E56D2FB08CCAD8CA4881411B0 "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/MhKz3-IsR9qPrIUs-Vo6rQ/zh-cn_image_0000002781311236.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8037A199534AF2F6376760BAB5205C32966F1FB59077618DCDB3677E57058D41 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/eXFN3qIpTP-n-ucrTS-qVw/zh-cn_image_0000002781311216.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F252838D14ED10B1EF59CAFB09BD4B5DF35B4FC25568FF2D7DBA5E9AB242678 "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/myvcuLz9TfiGTJjeYb86RA/zh-cn_image_0000002810750833.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F80025A2DE1DA109679B22C7BE8B72F7F49D83F2AC7576AEECE005B49AB8B23E "点击放大")
   * 开启**查看完整调度链**后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/08JZ3170QoieP5AhrQIxaQ/zh-cn_image_0000002810630725.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A650FF38B12B9EB7E15B847A451612178D5289B1CF52C2990EC1F16F525EE47A "点击放大")

## 查询进程详情

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、所属进程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/wNwdptpKQBWcb2Z4CaN0tg/zh-cn_image_0000002810750827.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FCEB99E2F0E342BB696DC49B624CF2B139845B1BA4C2786F88A0DDEC72F26A7 "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/7xmmEW-oQJ6w_56D0I4z5w/zh-cn_image_0000002781471152.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=043977D36A469BD36D6517F908F95BFD05FA62B0797AFE477EB0128510ED316D "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程数并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/KPU_Mo7nSYSqv65dk8Ymtg/zh-cn_image_0000002810750821.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA90F00DF87DA844CACC8B82A9C487220894C942F06D1AC450D0C795CF7D5B60 "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xHrTxFS7Ra2n8ND2MMHmrQ/zh-cn_image_0000002781311222.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=301C3232F879B2AF6CC292F4BFBC01071F84EE889A8635226CE314F581A0C684 "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/oPcWuNqeSKWbXlua0yNtvQ/zh-cn_image_0000002781471172.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A235B3DD58876F12C02EC58768212AAA153DEF4538133CFF5C1E42F76FF6355 "点击放大")
