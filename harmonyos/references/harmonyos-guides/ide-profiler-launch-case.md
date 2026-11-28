---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-launch-case
title: 案例：应用冷启动首帧完成时延问题分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 冷启动：Launch分析 > 案例：应用冷启动首帧完成时延问题分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:d17149ca705ea57bdee8b333e2ac6234b74809344988bc648deae17dbd0834c8
---

应用冷启动首帧完成时延是指从用户点击桌面应用图标离手开始，到应用进程首帧绘制结束的时间。本案例介绍如何找到应用冷启动首帧完成时延起止点，以及如何通过调用栈和trace信息分析应用运行逻辑，定位应用冷启动首帧完成时延超预期的原因。

应用冷启动分析基础功能请参考[Launch模板基本操作](ide-insight-session-launch.md)。

## 分析步骤

分析冷启动首帧完成时延类问题步骤如下：

1. 确认应用冷启动首帧完成时延起止点。
2. 框选应用冷启动首帧完成时延起止点位置，查看耗时是否超预期。
3. 若超过预期，根据调用栈和trace信息进一步确认问题点。

## 录制Launch模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Launch**模板，点击**Create Session**或双击Launch图标即可创建一个Launch录制模板。
2. 创建模板后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3gTv5nY0QXCffmQybyn_LQ/zh-cn_image_0000002808766695.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=37874CA88C0A306DA474FDAE8D857F56C3B40E85F0B3BF5D75D35DD495ED40C4 "点击放大")切换启动模式为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/9-91bEDoSrSrs_VcugObig/zh-cn_image_0000002779567130.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=F352095AEFF337AC535B86C0DD8A509500E6FD00066ECA966F21E42FCB05BA14 "点击放大")手动启动。
3. 在工具控制栏中点击齿轮图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/AR97wpibQLiWGKOgqrodzQ/zh-cn_image_0000002779407146.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3F6756B9ADE6D27C2FB32F4BFFAD23D6FFBBE449D24055FADDC6AF3737FF360 "点击放大")后勾选Hitrace > multimodalinput。用于采集多模子系统的trace信息，这部分信息会包含硬件传递过来的离屏信号，即多模子系统收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/u8RVpoyKR4m4LqYrcit93A/zh-cn_image_0000002779567126.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B3F5FA6B8CCD026427731200E5537D9545CDF8B4A002D7F3A613CF01ABC4507 "点击放大")
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/PhoFnELQTX2J6iTd0AX_2Q/zh-cn_image_0000002779407122.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=7988C60F5BFE5C578078339C8460D2BFDE620FC611091EC71E03CAC8D146F8C4 "点击放大")即开始录制。等待界面出现弹窗提示启动应用后，需要手动点击设备上的应用图标启动应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/T3V1wNKhRbuHu7CgyJ22rA/zh-cn_image_0000002779407152.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=36AC66D3A9DE6C104B82DF2FF6854F5F77AC4D25FB626259344CC40C4C257E4E "点击放大")
5. 待右侧泳道全部显示recording则表明正在录制中，等待应用冷启动结束后可以点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/cXPM6-ouR1WsGX7PeaBX_Q/zh-cn_image_0000002779567098.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4482D46C87B2E3F6C34431DCE66CE4BC36F74FB3A6B67DE682579BD71AB46F35 "点击放大")

## 分析Launch数据

### 确认首帧完成时延起止点

**冷启动首帧完成时延起点确认：**

首帧完成时延起点是用户点击桌面应用图标离手的时刻，即多模子系统收到硬件传递过来的离屏信号的时刻。

由于离屏信号对应的trace点耗时较短且不方便记忆。因此，需要优先找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）来辅助定位首帧完成时延的起点位置。具体步骤如下：

1. 找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）。在Profiler面板点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在搜索框中输入H:DispatchTouchEvent后回车，通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/EyJbgogeTWaBFe9UoVqDpQ/zh-cn_image_0000002808766701.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=37CCB272B9EA7BBD4B0F6D31AD9E4D831D137D1FF84BFB78952750EEFB257D51 "点击放大")或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/FYtob3xCTf-9UzQ13gHLCw/zh-cn_image_0000002779567124.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=5495839BF8F25EE12217A6F828F715343FC8D05AC117CC59358890A8AC0C3B0D "点击放大")按钮切换搜索结果，找到桌面进程泳道（ohos.sceneboard）中type=1（0：手指按下；1：手指抬起；2：滑动）的H:DispatchTouchEvent点并添加标记，为方便后续查找，可以通过双击标记，在弹出的标记属性框中修改标记描述为点击离手事件。该trace点就代表桌面进程收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/r10F5dzKSNm10aBpA4Bx4Q/zh-cn_image_0000002779567116.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4549F5ED69BC36CA283B4924D22901DA6C8CBC26F768093990CB00C7528C04AA "点击放大")
2. 搜索多模子系统泳道（mmi\_service）。点击搜索框选项区选择**Search Units搜索泳道**，在输入框中输入mmi\_service后回车，该泳道可能有多条，需要通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0WPNLxt4SOiz53-lTGgNyA/zh-cn_image_0000002779407144.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=45490FCA3B739269D3C3ED7CE7B4E60909A72B5596159276E01F6BFD4D119C5A "点击放大")或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/RBKU97PNQlSHG0HUjxVLNA/zh-cn_image_0000002808766703.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D4B65824AFA41071F11D44EBBE78DAC19479F44A1A92F87CC24F09E49CDE6E6 "点击放大")按钮切换搜索结果，找到包含trace片段的mmi\_service泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/qqQE1rEBTlSuEcy4my-XbA/zh-cn_image_0000002779407154.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=0181C895FEB2AE69BB937587BBDA4E635DA2FAC4142CFC31675E2C49446AF088 "点击放大")
3. 借助桌面进程收到点击离手事件trace点，继续定位多模子系统收到点击离手事件的trace点。

   在mmi\_service泳道中找到位于点击离手事件标记位置前方的CPU Running条块（此段时间表示多模子系统正在运行），在该条块下方找到H:service report touchId:{id}, type: up（或H:service report pointerId:{id}, type: button-up）的trace点并添加标记，然后修改标记描述为首帧完成时延起点。该trace点代表的是多模子系统收到点击离手事件，即冷启动首帧完成时延的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/FsfeDsBnT2S-R73SeM45Lg/zh-cn_image_0000002779567104.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A7BCAAC2D5828F6B20D20F73A4E8106035218231D7D49CA50E865B0F3427029 "点击放大")

**冷启动****首帧完成****时延止点确认：**

首帧完成时延止点是应用进程启动后收到的首个硬件垂直同步信号的时间点，即Render Service（统一渲染服务进程）将应用首帧渲染结果呈现到屏幕上的结束点。定位首帧完成时延止点具体步骤如下：

1. 找到应用进程启动后的首个垂直同步信号trace点H:ReceiveVsync，这个trace点代表应用的首帧开始绘制。选择应用进程子泳道，点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在输入框中输入H:ReceiveVsync后回车，找到第一个H:ReceiveVsync点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/mPsqcXcCRZqyRb6akWW83w/zh-cn_image_0000002779567102.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=E85014D061FBEAFAE250B7B33B2FB3B1CCC985960E7CCDFEE88D786AA1BBB893 "点击放大")
2. 应用进程启动后收到首个垂直同步信号时，会通知Render Service进程进行图形渲染，因此需要优先找到应用进程通知Render Service进程进行图形渲染的三个trace（H:FlushMessages > H:SendCommands > H:MarshRSTransactionData）。由于这三个trace耗时较短，不便查看，因此需要使用搜索功能来确定。框选H:ReceiveVsync trace点，点击搜索框选项区选择**Search Units Data**搜索泳道数据，在输入框中输入FlushMessages后回车。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/LjBG3tsUSK2LvgVhqB3tow/zh-cn_image_0000002808886779.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC5578121A680E7D25B9410254FD2428C03B9B0780BC09B4D09396A761305DA2 "点击放大")
3. 找到trace点H:FlushMessages（代表绘制消息） 后，继续在该trace点下方逐层分析，先找到trace点H:SendCommands（代表发送绘制指令给Render Service进程进行图形渲染），在下方再找到trace点H:MarshRSTransactionData（代表发送了绘制指令），这3个trace点就代表应用进程通知Render Service进程进行图形渲染的流程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/m_WNVj0VSMWKfIf4zg72tA/zh-cn_image_0000002808886785.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6CA5C10A05D657588B599BA358F53A0EEA4E06529EBA52CD8F54CD395FE5194 "点击放大")
4. 接着需要找Render Service进程收到应用进程首帧渲染通知的trace点，点击H:MarshRSTransactionData条块，“Slice Detail”区域可以查看该trace详情，包括trace名称、所属进程等。点击“Slice Detail”区域中Name后方跳转按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/28ZiQYCkRvOWzwtTsheXjQ/zh-cn_image_0000002779567122.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1E33967EFD1E7E1D0067BB2500A311CA5E961770F8B1C01C026154BBFAC905F)跳转到render\_service泳道的H:RSMainThread::ProcessCommandUni trace点并添加标记，然后修改标记描述为收到渲染通知。该trace点就代表Render Service进程收到应用进程首帧渲染通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/TweIX1y2Rr6Gqh87tBtswg/zh-cn_image_0000002779407134.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A56A87583B508B82FB40749EA28DEE84323A1E218707535E0ECDEAD0D623A23 "点击放大")
5. 接着找到Render Service将应用首帧提交硬件上屏的trace点，该操作在Render Service送显线程（CompThread）中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入CompThread后回车，查找位于收到渲染通知标记位置后方的第一个H:CommitLayers并添加标记，然后修改标记描述为提交硬件上屏。该trace点代表Render Service将应用首帧提交硬件上屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/I7gBi8VESaexV1rORlwtuA/zh-cn_image_0000002779407124.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB66160F3B3CB1A3003A6C71BE32872C18D0A86B2AB998D2FA3B2CFD72C152B1 "点击放大")
6. 最后找到Render Service将应用首帧渲染结果呈现到屏幕上的trace点，该操作在PresentFence中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入PresentFence后回车，查找位于提交硬件上屏标记位置后方的第一个H:Waiting for PresentFence，该trace点代表Render Service将应用首帧渲染结果呈现到屏幕上，trace点的结束位置就是冷启动首帧完成时延的止点，在此处添加标记并修改标记描述为首帧完成时延止点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/DOuU2GM1RS2bSm64vf9qxw/zh-cn_image_0000002808886767.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CDD6C39777F8A9BD19726B9310E318B2B0C764B08135DACC9C2825D32A6061A "点击放大")

### 案例：应用首页加载耗时较长导致应用冷启动首帧完成时延不达标

**说明** 

* 本案例基于应用进程启动过程中，在Ability的生命周期回调函数中做了耗时操作。
* 预期冷启动首帧完成时延不超过600ms。

框选应用冷启动首帧完成时延起止点位置，通过框选区间的时间长度看出，冷启动首帧完成时延超过800ms，比预期的600ms长。

切换到应用进程Process泳道，查看主线程（线程号与进程号一致）的trace。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/GXUfe88yQm-QhFKfAEHgpw/zh-cn_image_0000002808886787.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=339888FB6BBCCB02A1112E427C8D79BB90632531AEF54B0C9251559F99D786E1 "点击放大")

下方详情区展示Details信息，包括trace名称、起始时间、持续时长。将持续时间（Duration）降序排序，可以看到主要耗时在H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction，该阶段主要是AbilityStage/Ability的启动生命周期在执行相应的回调。从这里可以看出，是因为AbilityStage/Ability启动生命周期的回调执行时间较长。接下来需要分析调用栈，通过调用栈分析回调执行时间长的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/kwJiMpt0TEuO3ccC01QxaQ/zh-cn_image_0000002779407128.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2E865E80DBBD2F4196A69EA6F62C9189D7BE875F039B34A29066FA45E6C3C69 "点击放大")

接着切换到ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看线程号与进程号一致的ArkVM子泳道（该泳道为主线程调用栈），可以看到ArkTS侧一些方法的耗时。从下图中可以看到ArkTS侧无函数执行，需要切换到Callstack泳道看ArkTS和Native混合函数调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/OQ98viY_RYS8qordipHXLg/zh-cn_image_0000002779567110.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=64619DDA6EC2E376E32E9A3C25597FC83754AE82F307A0FB7BA7F8B9C748DA46 "点击放大")

最后切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，查看下方Heaviest Stack区域，滑动观察权重占比最大的函数调用栈，定位到耗时主要是EntryAbility.ets文件下第79行代码引起，双击该栈帧可以直接跳转到源码文件的对应位置上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/vQcGbU_qTWCWr27bMkX_cQ/zh-cn_image_0000002779567134.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2CCF4560BD421D016D34DC9110224BE467156F1D44EF9A4A69FE63A01EEEA1E "点击放大")

结合业务代码查看，可以看到是因为在EntryAbility.ets文件下onCreate()中做了耗时操作。耗时操作建议通过异步任务延迟处理或者放到其他线程执行，以降低主线程负载，缩短应用冷启动首帧完成时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HOXc_7yRSs-IVpkjr0hgaw/zh-cn_image_0000002808766709.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=275544D37EDCC3653FF4B7F27F957A4A763964223DA541B908791FE2BB2CC300)

更多应用冷启动优化方案，请参考[应用冷启动时延优化](../best-practices/bpta-application-cold-start-optimization.md)。
