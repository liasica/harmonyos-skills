---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-launch-case
title: 案例：应用冷启动首帧完成时延问题分析
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > 案例：应用冷启动首帧完成时延问题分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:33+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:6f7887f85218af843d81356b87fe2b08534aec8ce5ab868faf86ebf49a5fb73d
---

应用冷启动首帧完成时延是指从用户点击桌面应用图标离手开始，到应用进程首帧绘制结束的时间。本案例介绍如何找到应用冷启动首帧完成时延起止点，以及如何通过调用栈和trace信息分析应用运行逻辑，定位应用冷启动首帧完成时延超预期的原因。

应用冷启动分析基础功能请参考[Launch模板基本操作](ide-insight-session-launch.md)。

## 分析步骤

分析冷启动首帧完成时延类问题步骤如下：

1. 确认应用冷启动首帧完成时延起止点。
2. 框选应用冷启动首帧完成时延起止点位置，查看耗时是否超预期。
3. 若超过预期，根据调用栈和trace信息进一步确认问题点。

## 录制Launch模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Launch**模板，点击**Create Session**或双击Launch图标即可创建一个Launch的录制模板。
2. 创建模板后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/BqjKePLKQUmaM9tvi4w3LA/zh-cn_image_0000002530753108.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=4E33CD1E4A6CD0CC94BB604215567BDF90C50EB77D7CDECEE122A34009E1E314)切换启动模式为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/q9uGHb_DTz2dXXc7f3f2yA/zh-cn_image_0000002530913132.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=779BF62701EF84F48D0FB7E5842FC3EAAAE2F41AD48DC73CA3E9010AAE20B391)手动启动。
3. 在工具控制栏中点击齿轮图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/cfDhx70uQLqMKALgN1DQYw/zh-cn_image_0000002561833043.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=FD2F58DB3071C77E4A6D9DB42DC9856B66A44D57ADF4BDB4C2CE65290D1F1B85)后勾选Hitrace > multimodalinput。用于采集多模子系统的trace信息，这部分信息会包含硬件传递过来的离屏信号，即多模子系统收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/d4K0iTTBRAir-ROF67Ba8w/zh-cn_image_0000002561753021.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=E5A022B497FAC83EF338D0219EDC35903728B76EE71140F1C837259F2440D360 "点击放大")
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/uqsrt7a5S6OKb31gKVJ0bg/zh-cn_image_0000002561753025.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=06491F9207CB523A16C54FCC39871EB2D34725101E906D7799C346F6DA9595BD)即开始录制。等待界面出现弹窗提示启动应用后，需要手动点击设备上的应用图标启动应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/vuBc8QkURNCnFcKC6SFCxw/zh-cn_image_0000002530753100.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=1273DA1CB4E5D6F03C71879E932C286B738CD7CF4217BF9242CD07A94D44CAC1 "点击放大")
5. 待右侧泳道全部显示recording则表明正在录制中，等待应用冷启动结束后可以点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/21GLCihETKOAa3j9nGloNw/zh-cn_image_0000002561753045.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=0CEF107168FDA3047CEA2C79310DFC0B91737FD92954E6B787C07DB9C02D27F3 "点击放大")

## 分析Launch数据

### 确认首帧完成时延起止点

**冷启动首帧完成时延起点确认：**

首帧完成时延起点是用户点击桌面应用图标离手的时刻，即多模子系统收到硬件传递过来的离屏信号的时刻。

由于离屏信号对应的trace点耗时较短且不方便记忆。因此，需要优先找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）来辅助定位首帧完成时延的起点位置。具体步骤如下：

1. 找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）。在Profiler面板点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在搜索框中输入H:DispatchTouchEvent后回车，通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/elMKFTzvT2aZD527nSQ2sA/zh-cn_image_0000002530913104.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=065B7A4036A06974282EF810DE214853ADB9471C13F3476D5B4E7E5774919170)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tdyrr7BcSmaCR7kDWO57Kw/zh-cn_image_0000002530913114.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=7F6D349D77C43A46C5083C18E22189A48D1A94EDF57154B1915166F4FBC1A6B3)按钮切换搜索结果，找到桌面进程泳道（ohos.sceneboard）中type=1（0：手指按下；1：手指抬起；2：滑动）的H:DispatchTouchEvent点并添加标记，为方便后续查找，可以通过双击标记，在弹出的标记属性框中修改标记描述为点击离手事件。该trace点就代表桌面进程收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/1QdKF9ymRNy7eCS6K4uOBw/zh-cn_image_0000002530753132.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=B133DDC7B879E316A97EF1B7D12C59126B4FE2E8CCBFBDE8D5F8226D1EBED5C5 "点击放大")
2. 搜索多模子系统泳道（mmi\_service）。点击搜索框选项区选择**Search Units搜索泳道**，在输入框中输入mmi\_service后回车，该泳道可能有多条，需要通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/rRFZr9tbR8uJsKVPI7dJRw/zh-cn_image_0000002561833037.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=0DACAC0F5C6F96921E262D38B493E0142F7520ED17847C8188391B7F892838D1)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/MgF6uaHiSPW733dhsuSP9w/zh-cn_image_0000002530753116.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=99DF9E91A056337FDF92E35BFEE2F2ED996EE17A27817D69763E0E644E94FFD6)按钮切换搜索结果，找到包含trace片段的mmi\_service泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/dZYJ9nfCTb-nloDIR0hy0A/zh-cn_image_0000002530913124.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=13B317D9840462A3F029C10E878B760DD8E515DD2D553380DE0785BA38A269B2 "点击放大")
3. 借助桌面进程收到点击离手事件trace点，继续定位多模子系统收到点击离手事件的trace点。

   在mmi\_service泳道中找到位于点击离手事件标记位置前方的CPU Running条块（此段时间表示多模子系统正在运行），在该条块下方找到H:service report touchId:{id}, type: up（或H:service report pointerId:{id}, type: button-up）的trace点并添加标记，然后修改标记描述为首帧完成时延起点。该trace点代表的是多模子系统收到点击离手事件，即冷启动首帧完成时延的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/8PQJqpb6QQazWYR2IpMaXA/zh-cn_image_0000002561753061.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=8F4FE2DD9CC36FAB78E45C3AD963F3C60C118E558E7E939C8A006FD200735041 "点击放大")

**冷启动****首帧完成****时延止点确认：**

首帧完成时延止点是应用进程启动后收到的首个硬件垂直同步信号的时间点，即Render Service（统一渲染服务进程）将应用首帧渲染结果呈现到屏幕上的结束点。定位首帧完成时延止点具体步骤如下：

1. 找到应用进程启动后的首个垂直同步信号trace点H:ReceiveVsync，这个trace点代表应用的首帧开始绘制。选择应用进程子泳道，点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在输入框中输入H:ReceiveVsync后回车，找到第一个H:ReceiveVsync点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/pKRktaWyQcilmVHZpDME5A/zh-cn_image_0000002561833023.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=A5E10021FAAD64818282C65D9C77E91A2871337031BE0BFD9EE1A691E106A5AA "点击放大")
2. 应用进程启动后收到首个垂直同步信号时，会通知Render Service进程进行图形渲染，因此需要优先找到应用进程通知Render Service进程进行图形渲染的三个trace（H:FlushMessages > H:SendCommands > H:MarshRSTransactionData）。由于这三个trace耗时较短，不便查看，因此需要使用搜索功能来确定。框选H:ReceiveVsync trace点，点击搜索框选项区选择**Search Units Data**搜索泳道数据，在输入框中输入FlushMessages后回车。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/CPoI4SAESYe_CEVaLRBPhg/zh-cn_image_0000002530753134.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=8BB3F5D583136B945CE41E73900A38238EC0DD57CB6B85DCEC2E821B1482C363 "点击放大")
3. 找到trace点H:FlushMessages（代表绘制消息） 后，继续在该trace点下方逐层分析，先找到trace点H:SendCommands（代表发送绘制指令给Render Service进程进行图形渲染），在下方再找到trace点H:MarshRSTransactionData（代表发送了绘制指令），这3个trace点就代表应用进程通知Render Service进程进行图形渲染的流程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ThS2RRNJTAyiLFESyYsx3A/zh-cn_image_0000002561753071.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=09563DACA87E41D2F58BB65E43084D88BC34AD3AEFD7958D603B133987C01F6A "点击放大")
4. 接着需要找Render Service进程收到应用进程首帧渲染通知的trace点，点击H:MarshRSTransactionData条块，“Slice Detail”区域可以查看该trace详情，包括trace名称、所属进程等。点击“Slice Detail”区域中Name后方跳转按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/9bCpLw-gRFyTU7AzU0yHPQ/zh-cn_image_0000002561753049.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=A5328D9A260371EED15F7C74910050CB6CF916674DEAA1D23611864451EA565B)跳转到render\_service泳道的H:RSMainThread::ProcessCommandUni trace点并添加标记，然后修改标记描述为收到渲染通知。该trace点就代表Render Service进程收到应用进程首帧渲染通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/7vlQuGJcQmG9KRfYKj-Mag/zh-cn_image_0000002530913120.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=F6E9AE1D90FCE19190493A94256254867AED13184DEF9C04EF43D9988A150B79 "点击放大")
5. 接着找到Render Service将应用首帧提交硬件上屏的trace点，该操作在Render Service送显线程（RSHardwareThrea）中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入RSHardwareThrea后回车，查找位于收到渲染通知标记位置后方的第一个H:CommitLayers并添加标记，然后修改标记描述为提交硬件上屏。该trace点代表Render Service将应用首帧提交硬件上屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/DzNVuzrWQa-5FX3ZEp1IrQ/zh-cn_image_0000002561833013.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=D170F21C8EA296F94CCCEA79287B9818026D898BA57BD3D1E465AE6A14BD4120 "点击放大")
6. 最后找到Render Service将应用首帧渲染结果呈现到屏幕上的trace点，该操作在Present Fence中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入Present Fence后回车，查找位于提交硬件上屏标记位置后方的第一个H:Waiting for Present Fence，该trace点代表Render Service将应用首帧渲染结果呈现到屏幕上，trace点的结束位置就是冷启动首帧完成时延的止点，在此处添加标记并修改标记描述为首帧完成时延止点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/2eYsTDCzSwGMk3q0ZLL0eA/zh-cn_image_0000002561833011.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=6E95EA208D263EB943CB90A55B2B1CA2800519F69BF8692B2E392E8F93178D6F "点击放大")

### 案例：应用首页加载耗时较长导致应用冷启动首帧完成时延不达标

说明

* 本案例基于应用进程启动过程中，在Ability的生命周期回调函数中做了耗时操作。
* 预期冷启动首帧完成时延不超过600ms。

框选应用冷启动首帧完成时延起止点位置，通过框选区间的时间长度看出，冷启动首帧完成时延超过800ms，比预期的600ms长。

切换到应用进程Process泳道，查看主线程（线程号与进程号一致）的trace。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/zBMaV0ubS4ev_RzTBsmncA/zh-cn_image_0000002530753098.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=36868A00C6F8C9AEEBF3D4238FDC63DB3490042B2DC3F1DDFEBE5743FE85D24C "点击放大")

下方详情区展示Details信息，包括trace名称、起始时间、持续时长。将持续时间（Duration）降序排序，可以看到主要耗时在H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction，该阶段主要是AbilityStage/Ability的启动生命周期在执行相应的回调。从这里可以看出，是因为AbilityStage/Ability启动生命周期的回调执行时间较长。接下来需要分析调用栈，通过调用栈分析回调执行时间长的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/bFlK_sRISEiUpEz4GxK0zQ/zh-cn_image_0000002530913096.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=D8139DE70E45742C664E18689012EE094A0DF74C2898B8EF64D983323C16CCBA "点击放大")

接着切换到ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看线程号与进程号一致的ArkVM子泳道（该泳道为主线程调用栈），可以看到ArkTS侧一些方法的耗时。从下图中可以看到ArkTS侧无函数执行，需要切换到Callstack泳道看ArkTS和Native混合函数调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/pl7wr_njSoeBmisa7LC4PA/zh-cn_image_0000002561753039.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=0050CD4EEBB5BE81089666C143EAB4D2441B97F5317C731163B3943F34D13227 "点击放大")

最后切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，查看下方Heaviest Stack区域，滑动观察权重占比最大的函数调用栈，定位到耗时主要是EntryAbility.ets文件下第79行代码引起，双击该栈帧可以直接跳转到源码文件的对应位置上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/gs8bJ3uNSTOAosq7yhWAtw/zh-cn_image_0000002530753140.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=F003654A8C18A4802A462F3752284FB9DCD726A3701D118A6D19B04C7B4DA5AB "点击放大")

结合业务代码查看，可以看到是因为在EntryAbility.ets文件下onCreate()中做了耗时操作。耗时操作建议通过异步任务延迟处理或者放到其他线程执行，以降低主线程负载，缩短应用冷启动首帧完成时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/IzwBfrzQTSuL5bwu8WLhKg/zh-cn_image_0000002530753122.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=D52B1C2CD3191F952FB9B928A52A352C9384272553FA8F43CA79132EE8AB1C5C)

更多应用冷启动优化方案，请参考[应用冷启动时延优化](../best-practices/bpta-application-cold-start-optimization.md)。
