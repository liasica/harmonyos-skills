---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame
title: Frame分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > Frame分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0960322009a50037749ce1862d592e8aaa50bcc69374c4fde54916ec941b150
---

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因。此外，Frame任务窗口还集成了Time、CPU、Network场景分析任务的功能，方便开发者在分析丢帧数据时同步对比同一时段的其他资源占用情况。

说明

* 在任务分析窗口中，可通过[快捷键](ide-shortcut-key.md)缩放时间轴、移动时间轴、添加时间标签等。
* Frame分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
* Frame分析支持Energy泳道，请参见[定位能耗问题](ide-profiler-energy.md#section889733410010)。

## 查看GPU使用情况

1. 创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。
2. “Frame”泳道显示当前设备的GPU的使用率，将其展开，子泳道显示Render Service侧帧数据和App侧帧数据。

   说明

   * 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
   * 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。
   * 在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * 除“RS Frame”和“App Frame”泳道外的“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息，请参考[基础耗时：Time分析](ide-insight-session-time.md)、[CPU活动分析](ide-insight-session-cpu.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Q5-Fr3WnTV-OL8kpU5WZrQ/zh-cn_image_0000002530752902.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=5DB28CB2707D9C30B2AADC309449BEADE3B27F3E4196BE3FECBE775B27E07597 "点击放大")

## 查看指定时间段内所有进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选Frame主泳道。

   窗口下方的“Statistics”区域中会以进程维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/J5xDJnTxQbCmLk1A85Xe5w/zh-cn_image_0000002561832811.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=E3FF9C6C14613FE77A739F6D70F443EBF145F521DC006FDA520AF03B26137986 "点击放大")
3. 点击“Statistics”列表中任一进程的跳转按钮，在“Frame List”区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/y5CGHMBnSwmN5vMEh4bl5w/zh-cn_image_0000002561752841.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=652DFFA781351775982089352EA639AAAE1CE9966B0478D9340959D7A80E6445 "点击放大")
4. 单击“Frame List”列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/IQQhgFXgQnOOxqfQHlqiaQ/zh-cn_image_0000002530912912.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=B886053E7FF2F0E3A879D4B3C08C0572A055FFCF56043112D5BF2E0E823CE444)跳转至关联的切片。

## 查看指定Frame页面布局信息

从DevEco Studio 5.1.0 Release版本开始，支持查看最新录制的Session中指定的Frame页面布局信息。

从DevEco Studio 6.1.0 Beta1版本开始，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/WMNXsk_ZThyZzx9F27WMMg/zh-cn_image_0000002530912910.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=F616EFD8E55B9F6FAAF8323160A814AF64530DA17735A7FD74A8C21E45713606)按钮中新增Frame Layout开关，开发者可自行设置开关状态。开关关闭时，不支持查看最新录制的Session中指定的Frame页面布局信息，默认关闭。

暂不支持在Wearable设备上查看指定Frame页面布局信息。

1. 单击RS Frame泳道或APP Frame泳道中任意一帧，“Details”区域中会展示该帧具体信息。点击**Open Layout**按钮，将在ArkUI Inspector中直接打开相应arkli文件；点击**Download Layout**将arkli文件下载到指定目录，之后可手动导入[ArkUI Inspector](ide-arkui-inspector.md)查看页面布局信息。

   说明

   单击“Download Layout”或 “Open Layout”前，需应用进程置于前台，才能正确回放全量渲染数据，获取arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/kfgPVKh0SyerptIJ-ebtRA/zh-cn_image_0000002530912882.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=A3B77B89DBC07B32DE16868259B559CE8F39BEB1983390203375CDF3B9DD659B "点击放大")
2. 在ArkUI Inspector中可查看组件树和组件属性信息，当前支持BackgroundFilter、nodeGroup、nodeGroupReuseCache组件。
   * BackgroundFilter：背景滤波器。
   * nodeGroup：节点组类型，0表示非节点组节点，1表示被动画标记的节点组，2表示被UI标记的节点组，4表示被用户标记的节点组，8表示被前景滤波器标记的节点组。
   * nodeGroupReuseCache： 0表示在生成缓存或无需缓存，1表示在重用缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/a678ar7qTwW8nJ8z14TNDA/zh-cn_image_0000002530752900.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=8010774866AF6D893A1D6EC86EC7604512CDC2BEA1C5572271866DE38688C5AC "点击放大")

## 查看指定时间段内指定进程的Frame数据统计信息

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 选择要观察的子泳道（例如带“RS Frame”标签的泳道）。

   窗口下方的“Details”区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/qKQCYjJgTrCLv3UPk8Axzw/zh-cn_image_0000002561832831.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=DF30B348E3CDD6892504E80F8F9642CD48BF17A0FA081E2B1045C227C6E1AB39 "点击放大")
3. 单击列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/bFw8G2zyRzGYZ5WT_uKA7w/zh-cn_image_0000002561752835.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=4022CC6D6E7FF92FE10A1FDA3C28C0F04C6E0EDBB5DE8D2A9F21BE273D5E80C9)跳转至关联的切片。

## 查看指定Frame信息

在子泳道（例如带“APP Frame”标签的泳道）中选中要查看的Frame，该泳道上方是耗时最长的非UI函数，下方是UI主线程泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/MjD1OlHxQaiPpdTFQ2ggxg/zh-cn_image_0000002561752857.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=ECD632239A18044DEF9DEA67F7B8FC280AB6FD3A748BC90C2EB33E98444140E8 "点击放大")

窗口下方的“Frame”区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。“Non UI”区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

说明

* 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
* 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
* 将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。
* 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/X2_IRULxQ12oC_ufyvmqhA/zh-cn_image_0000002561752829.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=AA07CF8FDD25A354A779F83765EF4B1C2430CD387F9F110A3C2EF2FA27B41BBD "点击放大")

## 查看屏幕帧率动态变化场景下丢帧和卡顿信息

Frame泳道下新增Lost Frames和Hitch Time两类子泳道，用于识别和优化卡顿和丢帧现象。

* Hitch Time：展示当前时间段内卡顿时长。计算方式为渲染前后两帧的间隔减去单帧耗时，若计算结果大于单帧耗时\*70%，则视为出现卡顿现象。
* Lost Frames：展示当前时间段内丢帧数。Lost Frames计算出的结果，六舍七入统计取整。

1. 创建Frame模板并录制会话，如存在卡顿和丢帧现象，会在Lost Frames和Hitch Time泳道对应时间显示矩形图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/f_pVpC5DQGizdQD9gnYsKA/zh-cn_image_0000002561752821.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=DAC182B5FA79782DCA6DE632DC1752AA60379E25BEABBF56AC2920CC501742DB "点击放大")
2. 鼠标点选某一时间点，提示信息会显示该点所属时间段内的丢帧数以及卡顿时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/aeeNUOzxQWe1JpnmbBGT6Q/zh-cn_image_0000002561832845.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=C9065D20A1C7283784254B8320D99306204445E7D00041CDB7BD0175AB4B3489 "点击放大")

## 支持动效场景调优

开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。

鼠标放置在某个动效上，显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。

说明

* 响应时延：<=85ms 绿色，85ms~150ms 浅绿色，150ms ~250ms 浅红色，>250ms深红色。
* 期望帧率：当前系统运行满帧帧率，如60HZ、90HZ、120HZ。智能刷新率模式下，不展示期望帧率。
* 动效持续时间：根据帧率展示颜色，FPS大于达标帧率即为绿色，小于则为深红色。智能刷新率模式下，帧率可变，颜色为灰色。达标帧率与期望帧率的大小有关，一般情况下期望帧率为60HZ，则达标帧率= 60HZ \* 91.7%。
* 完成时延：响应时延和动效持续时间只要有一个为深红色，完成时延为深红色。
* Launch模板中Frame泳道点击detail区启动动效详情信息，more区域展示动效帧Animation Data List信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/OpbN9lAOSzG-Go7xxNDiAA/zh-cn_image_0000002530912924.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=BE51745AC30AD0ABF7BB34D79DB81F60D48926EDE35C93665B5847FDE7C7EF7D "点击放大")

## 查看组件动画信息

从DevEco Studio 6.0.0.828版本开始，Frame泳道下新增Component Animation子泳道，用于从组件的角度展示应用中包含的各种动画类型，包括属性动画 (animation)、显式动画 (animateTo)、关键帧动画 (keyframeAnimateTo)以及页面间转场 (pageTransition)。

在Details页签中，可以查看每个动画的详细信息，包括起止时间、帧率、动画曲线类型以及影响的组件属性等。

单击列表中任意一动画，右侧的“More”区域会中显示该动画所影响的组件属性的具体变化过程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/PlIqct64TxO1CXr4WNvndw/zh-cn_image_0000002561832843.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=A76AB7012A053EC315D581E518295159C0C9530701364D8536DA5337A588067B "点击放大")

## 查看组件帧率信息

Frame泳道下新增两类子泳道，分别为Display Vsync与DisplaySync\_cb(tid)，用于对可变帧率的检测调优。

* Display Vsync：该泳道显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计。区分“<=30HZ”、“30~60HZ”、“60~90HZ”、“>90HZ”。统计值包括框选时间段内各区间的分布比率、最小/最大/平均时长以及平均HZ。如果某场景满足了帧率改变的要求，当底层系统根据机制进行变帧，相应的情况会展现在对应的泳道，帮助开发者了解vsync的变化情况是否符合预期。该泳道仅支持在配备硬件屏幕的设备上进行数据采集。
* DisplaySync\_cb(tid)：该泳道显示对应组件的帧率，如DisplaySync、XComponent两类接口组件动画对应的帧率。调测时，不同场景下由于帧率可变，系统实际表现是否符合预期，需要有实际的检测手段。尤其是由于DisplaySync的渲染均在UI主线程执行，当存在多个需要渲染的组件需要同时执行时，只能在UI主线程排队，此时任何一个组件的延迟都会对其他组件的渲染产生影响，导致UI卡顿。

  如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/pr2a3KZmQ0SE8zsi7W3yUw/zh-cn_image_0000002561832795.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=F963A4514491C49F5A1979D83345C67AF5935C87FE0394922FBCE650A5847FB9 "点击放大")

1. 选择Display Vsync泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区显示当前时间段的屏幕刷新率，当前帧最大持续时间、最小持续时间、平均持续时间以及该时间段内平均帧数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/MyawMDCZTa20JraC5bVrYw/zh-cn_image_0000002561752849.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=9DDBE025E0B92A20D1D93FC9F5CAD160E897E3B9E150AD255D094C26B1EA62A7 "点击放大")
3. 点选Display Vsync泳道，可以查看当前帧的耗时和帧率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/j9zDkfI3RmuU2jKDaTzQOw/zh-cn_image_0000002561832803.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=251409EB811F29FE142ED38FC48D3194B230FF30316CF7F8003B9F487E4804FB "点击放大")
4. 框选DisplaySync\_cb泳道，可以查看应用侧对应组件的帧率，渲染时间等信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/wdQ6NBK9TmCLYjla7zw6ZQ/zh-cn_image_0000002530912902.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=F9E388C25A1EE3DB39BB65BA3FEDE3EF20507237B0B45B8B0D0205E7357A79C0 "点击放大")
5. 同时如果组件有可能的掉帧情况，DisplaySync\_cb泳道显示对应的掉帧情况并标红展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/E-d_7Y3IQ92plRmt5mh5wg/zh-cn_image_0000002561752871.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=B5CC1AEC7FCD7116C46D5B58F794A3849B003B1CD93B65E06F1661FF45D2EEDB "点击放大")

## 查看帧率统计信息

Frame泳道中的App Frame泳道和RS Frame泳道在框选时新增fps标记。RS泳道新增过滤按钮，用于过滤ArkWeb数据。

1. 展开Frame泳道，框选一段数据。
2. 泳道出现fps标记，展示当前框选范围内的帧率统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/zuq8P0KSTKqyvHXkFPVOkw/zh-cn_image_0000002530752908.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=77AF0222E8AB21877613427FE3B71C73556AD8C026DEE8083A3E2713796927CA "点击放大")
3. 打开Only ArkWeb data开关，筛选过滤出包含ArkWeb帧的数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/mKwxFegRRAiJH7zRR4UJcg/zh-cn_image_0000002530752888.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=213CA7FF5710401FF6AC0BFC7DE8BF9865F31A2D643E4C508B5C0FD7677DC000 "点击放大")

## Anomaly泳道：查看解码过度耗时和超过阈值的序列化、反序列化操作

如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。

如果应用中使用了worker, Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。

1. 在时间轴上拖拽鼠标选定出现告警的时间段。当耗时超过VSync周期的50%时，将在Anomaly泳道中出现红色告警，提示“Image decoding has exceeded 50% of the VSync time”。
2. 详情区给出录制时段内解码过度耗时的统计情况，包括类型，图片名，计数，总耗时，最小耗时、平均耗时、最大耗时，耗时标准差、 图源尺寸大小，目标尺寸大小等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/fGQ8OmS-Rris3ENAxNbZIQ/zh-cn_image_0000002561832799.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=5820EC06F9BA7C2C0F21B8ABE83FDCBC0A704B8B58B965F13270235640D1FE6D "点击放大")
3. 对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警。其中可以通过泳道启动配置按钮配置检测阈值，默认配置阈值为8ms。
4. 详情区给出录制时段内序列化、反序列化耗时情况统计信息，包括类型、计数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差等。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/5Gi89PjbTJGJvGYi6JlHww/zh-cn_image_0000002530912896.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=64D536C6707D0767A8289A57C14A52A9B30042227B5357D4C42CEE85A063003B "点击放大")

   说明

   已上架应用市场的应用不支持录制Anomaly泳道。

## User Events泳道：查看用户事件耗时

开发者在卡顿丢帧场景可通过User Event用户事件，查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。

1. 选择User Event泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区列表给出录制时间段内用户事件详情，包括用户事件ID、事件开始时间Input Time、应用开始处理时间Processing Start、应用处理耗时Duration和事件类型User Event Type。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/CKqMszwCRXG9w-InSL2lmQ/zh-cn_image_0000002561752833.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=BDB0DF1297CAE0796C8223F22EAF044708646EB33F2C9DDA9BED213DBEFFACA3 "点击放大")
3. 点选User Event泳道中的条块，Slice详情区展示该事件的详情信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/IEhEJcG4SeK1hbJSVw5Ohg/zh-cn_image_0000002561832853.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=32E6EFF4D332502DCB623813DCD7073768DBA5E8FDAFA74AB2C76C6049D591EE "点击放大")

更多性能调优最佳实践，请参考[点击响应时延分析](../best-practices/bpta-click-to-click-response-optimization.md)、[点击完成时延分析](../best-practices/bpta-click-to-complete-delay-analysis.md)、[帧率问题分析](../best-practices/bpta-zhenlv.md)、[Web点击响应时延分析](../best-practices/bpta-web-click-response-delay-analysis.md)、[Web加载完成时延分析](../best-practices/bpta-web-completion-delay-analysis.md)。
