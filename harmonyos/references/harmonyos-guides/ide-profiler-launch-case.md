---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-launch-case
title: 案例：应用冷启动首帧完成时延问题分析
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > 案例：应用冷启动首帧完成时延问题分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:32+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:7c9652310f14c1272cf717a79f2be6b0f2cec3fae703235a16bdaa06dc0d067e
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
2. 创建模板后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/hlY68FmWS8iA812lO88MTA/zh-cn_image_0000002530753108.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=8A8CCC9D1CB84CDD463A3A818A8E0002BD3337BD0F24467BF4B39CD282F283C3)切换启动模式为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/NKmFeup7QI2v5Fbr_jJTHQ/zh-cn_image_0000002530913132.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=34A0D9B2D1A79C634C1CAD0F9916026CFC2874B4456797A63B37F8EA17EE7498)手动启动。
3. 在工具控制栏中点击齿轮图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/AhdlokDqQMCvcIYfDi5IQQ/zh-cn_image_0000002561833043.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=77DC895DDA3D6A7E252E39FABCF77061A2D1DD93D8293E75265E6AC6FECE94C9)后勾选Hitrace > multimodalinput。用于采集多模子系统的trace信息，这部分信息会包含硬件传递过来的离屏信号，即多模子系统收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/wBId5dAlQKGeC8MGsEyWbw/zh-cn_image_0000002561753021.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=C8A254B4AE9C33A76484D6A820065B71BE204BC4A240F82304554C54D0B5295C "点击放大")
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/VNCEJ-TbT9agScahDUyUuA/zh-cn_image_0000002561753025.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=793B66295F79538B09F9CF05BD848E31B1265BDA99A8FF8568AAA2F80C2A4B64)即开始录制。等待界面出现弹窗提示启动应用后，需要手动点击设备上的应用图标启动应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/aClE461tTKWcGHvi38Pz_A/zh-cn_image_0000002530753100.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=7955BA2DE7F49A82EA775C9E0DA9C1A552C4FF6CB773EE8A72F4C0B1D753E004 "点击放大")
5. 待右侧泳道全部显示recording则表明正在录制中，等待应用冷启动结束后可以点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/9Zy7EMblQd2GIPPoah0opg/zh-cn_image_0000002561753045.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=A5F836B90AB7F5D9A9EB9AA9B4B9B395DAB3E89B8E82C7B5C5468E12719C36E5 "点击放大")

## 分析Launch数据

### 确认首帧完成时延起止点

**冷启动首帧完成时延起点确认：**

首帧完成时延起点是用户点击桌面应用图标离手的时刻，即多模子系统收到硬件传递过来的离屏信号的时刻。

由于离屏信号对应的trace点耗时较短且不方便记忆。因此，需要优先找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）来辅助定位首帧完成时延的起点位置。具体步骤如下：

1. 找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）。在Profiler面板点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在搜索框中输入H:DispatchTouchEvent后回车，通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/6fshV1n1SpmC2vM0xuJbVw/zh-cn_image_0000002530913104.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=CB26B97B7DC4E1550E8EE733B777BDF2F72DF747CD3C5C1765AC40B7ABD91DCE)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/wVdQ4lhvTgW2W6fUOJKBOw/zh-cn_image_0000002530913114.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=9F56E4A1D0F39A124FBA17887D91E21A31FF3107C34E3324E63F79A93F1E9300)按钮切换搜索结果，找到桌面进程泳道（ohos.sceneboard）中type=1（0：手指按下；1：手指抬起；2：滑动）的H:DispatchTouchEvent点并添加标记，为方便后续查找，可以通过双击标记，在弹出的标记属性框中修改标记描述为点击离手事件。该trace点就代表桌面进程收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/vb1RJohiSLiW4AtohXaVDw/zh-cn_image_0000002530753132.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=6D8D72C87510738F634141E38BB2F67F42B274D212622FF28CE380C6366BF1E9 "点击放大")
2. 搜索多模子系统泳道（mmi\_service）。点击搜索框选项区选择**Search Units搜索泳道**，在输入框中输入mmi\_service后回车，该泳道可能有多条，需要通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/F5j4KdibSjy7T7SJO-Fj8Q/zh-cn_image_0000002561833037.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=7FB0783EF41736E3D7533B83E4C80A60748FEBAB7DFC0079B61D6A11F2E3CABA)或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/lCqyGBxHSrSQcUxAC9vLog/zh-cn_image_0000002530753116.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=5F8817A7688FBCB0173B8A7A72D161523ECB70ED8FA47F0690DCF681AEF53F0F)按钮切换搜索结果，找到包含trace片段的mmi\_service泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Al2Xt6W5RU6mVJVtb-GBqg/zh-cn_image_0000002530913124.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=EB62FFAA26A6382A24FFBDE0EB27C4626D98A2637C63ABFB522DBDF7B35BF817 "点击放大")
3. 借助桌面进程收到点击离手事件trace点，继续定位多模子系统收到点击离手事件的trace点。

   在mmi\_service泳道中找到位于点击离手事件标记位置前方的CPU Running条块（此段时间表示多模子系统正在运行），在该条块下方找到H:service report touchId:{id}, type: up（或H:service report pointerId:{id}, type: button-up）的trace点并添加标记，然后修改标记描述为首帧完成时延起点。该trace点代表的是多模子系统收到点击离手事件，即冷启动首帧完成时延的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/qLlVmUywSieTnZqeCCCD8g/zh-cn_image_0000002561753061.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=6EF0426D28B8203577FC7D3966D38CCE601F42D03F9675251674EAE5332C7706 "点击放大")

**冷启动****首帧完成****时延止点确认：**

首帧完成时延止点是应用进程启动后收到的首个硬件垂直同步信号的时间点，即Render Service（统一渲染服务进程）将应用首帧渲染结果呈现到屏幕上的结束点。定位首帧完成时延止点具体步骤如下：

1. 找到应用进程启动后的首个垂直同步信号trace点H:ReceiveVsync，这个trace点代表应用的首帧开始绘制。选择应用进程子泳道，点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在输入框中输入H:ReceiveVsync后回车，找到第一个H:ReceiveVsync点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/LlQ-tVvIS4OKTRTpZOn03A/zh-cn_image_0000002561833023.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=D0AEE45A19176F7A2DA38525E62EE6B78BF8D4D5864B5EEC9713EA675C5A7FD7 "点击放大")
2. 应用进程启动后收到首个垂直同步信号时，会通知Render Service进程进行图形渲染，因此需要优先找到应用进程通知Render Service进程进行图形渲染的三个trace（H:FlushMessages > H:SendCommands > H:MarshRSTransactionData）。由于这三个trace耗时较短，不便查看，因此需要使用搜索功能来确定。框选H:ReceiveVsync trace点，点击搜索框选项区选择**Search Units Data**搜索泳道数据，在输入框中输入FlushMessages后回车。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/rLZT99EeQ7mBo9wn5gwdOQ/zh-cn_image_0000002530753134.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=C3EE97254F3B13FC28085C1F103A2F65C12AC132A59A275168D11E8BC3DEB66D "点击放大")
3. 找到trace点H:FlushMessages（代表绘制消息） 后，继续在该trace点下方逐层分析，先找到trace点H:SendCommands（代表发送绘制指令给Render Service进程进行图形渲染），在下方再找到trace点H:MarshRSTransactionData（代表发送了绘制指令），这3个trace点就代表应用进程通知Render Service进程进行图形渲染的流程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/HvSBNMUXR5-bkNp931tzXA/zh-cn_image_0000002561753071.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=57EAF59DF83625DB0B39FAD3DD76ADAFA7FDA6B7A3FAE52055F2BF9296B94CED "点击放大")
4. 接着需要找Render Service进程收到应用进程首帧渲染通知的trace点，点击H:MarshRSTransactionData条块，“Slice Detail”区域可以查看该trace详情，包括trace名称、所属进程等。点击“Slice Detail”区域中Name后方跳转按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/wekEN4oYTL-pAzNAtwLL-w/zh-cn_image_0000002561753049.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=026D88672FB3B6617E43B900A8700A285628B84EDDBE5C25B2C6B9CC00296F59)跳转到render\_service泳道的H:RSMainThread::ProcessCommandUni trace点并添加标记，然后修改标记描述为收到渲染通知。该trace点就代表Render Service进程收到应用进程首帧渲染通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/fPl_dBv6Sx6cKRGo8OCR5Q/zh-cn_image_0000002530913120.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=4647C0F01A873DF2C9021C3271C74408FBFF041FF7714F5D974FB747AE33A60A "点击放大")
5. 接着找到Render Service将应用首帧提交硬件上屏的trace点，该操作在Render Service送显线程（RSHardwareThrea）中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入RSHardwareThrea后回车，查找位于收到渲染通知标记位置后方的第一个H:CommitLayers并添加标记，然后修改标记描述为提交硬件上屏。该trace点代表Render Service将应用首帧提交硬件上屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/kz98lOHESJKGFB8952iUOg/zh-cn_image_0000002561833013.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=2CE9E958CB50B5B06EE49437A663F4169674555764F5C3879A72F8254B3E3733 "点击放大")
6. 最后找到Render Service将应用首帧渲染结果呈现到屏幕上的trace点，该操作在Present Fence中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入Present Fence后回车，查找位于提交硬件上屏标记位置后方的第一个H:Waiting for Present Fence，该trace点代表Render Service将应用首帧渲染结果呈现到屏幕上，trace点的结束位置就是冷启动首帧完成时延的止点，在此处添加标记并修改标记描述为首帧完成时延止点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/l27JC6S9Qfq0F3_aMzP4lA/zh-cn_image_0000002561833011.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=F06E42F73AA17ADD6A952D08B9E7C0B493141699B8038EC11FF4271FDE442D93 "点击放大")

### 案例：应用首页加载耗时较长导致应用冷启动首帧完成时延不达标

说明

* 本案例基于应用进程启动过程中，在Ability的生命周期回调函数中做了耗时操作。
* 预期冷启动首帧完成时延不超过600ms。

框选应用冷启动首帧完成时延起止点位置，通过框选区间的时间长度看出，冷启动首帧完成时延超过800ms，比预期的600ms长。

切换到应用进程Process泳道，查看主线程（线程号与进程号一致）的trace。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/JBYlUaYaSKKwf4GeTpDssw/zh-cn_image_0000002530753098.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=D37EAFF838A7CA256BE2F3388EDACEBDE51C78855DDB0E685CCD1EF9450DB5AC "点击放大")

下方详情区展示Details信息，包括trace名称、起始时间、持续时长。将持续时间（Duration）降序排序，可以看到主要耗时在H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction，该阶段主要是AbilityStage/Ability的启动生命周期在执行相应的回调。从这里可以看出，是因为AbilityStage/Ability启动生命周期的回调执行时间较长。接下来需要分析调用栈，通过调用栈分析回调执行时间长的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/8VS6lYPAQOikR9v_Q8q33w/zh-cn_image_0000002530913096.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=60F328F9F9EC534CA7D738A6B9370355BE945044E109A9E96AF4A3EF9BA8FBD8 "点击放大")

接着切换到ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看线程号与进程号一致的ArkVM子泳道（该泳道为主线程调用栈），可以看到ArkTS侧一些方法的耗时。从下图中可以看到ArkTS侧无函数执行，需要切换到Callstack泳道看ArkTS和Native混合函数调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zYhM_Yc7RoOLm7LJQfk3WA/zh-cn_image_0000002561753039.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=64041342E7FECBDB50E1520CD2E1FE749CF8CE0C8ABB849334FAA6344246A402 "点击放大")

最后切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，查看下方Heaviest Stack区域，滑动观察权重占比最大的函数调用栈，定位到耗时主要是EntryAbility.ets文件下第79行代码引起，双击该栈帧可以直接跳转到源码文件的对应位置上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ntYHj1Z1T0GPuf_Ch0jAUw/zh-cn_image_0000002530753140.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=126BE0B585025D5299A276F61708B239FCFCCE4EC60F0827239EAD3961DD758B "点击放大")

结合业务代码查看，可以看到是因为在EntryAbility.ets文件下onCreate()中做了耗时操作。耗时操作建议通过异步任务延迟处理或者放到其他线程执行，以降低主线程负载，缩短应用冷启动首帧完成时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/O67uhP_3SYOq8SGqC-sqbg/zh-cn_image_0000002530753122.png?HW-CC-KV=V1&HW-CC-Date=20260427T235731Z&HW-CC-Expire=86400&HW-CC-Sign=DD299AA8AA81DBAEBEDC53AF7AB4A036FEF701A61A8F6D3C2387073627AECF52)

更多应用冷启动优化方案，请参考[应用冷启动时延优化](../best-practices/bpta-application-cold-start-optimization.md)。
