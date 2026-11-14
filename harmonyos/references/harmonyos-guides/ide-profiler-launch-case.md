---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-launch-case
title: 案例：应用冷启动首帧完成时延问题分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 冷启动：Launch分析 > 案例：应用冷启动首帧完成时延问题分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:961ac42366854ff4c7037b8fa237835a2582ac051774159cb33da9c678b10c08
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
2. 创建模板后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/aHmjHOGLRSSmbguLGz08rw/zh-cn_image_0000002808766695.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE2F183D1C2E4E66104B62D81D20D6CD80FCCE1C3BD5CCE0DBBD44BB37947E86 "点击放大")切换启动模式为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/9vMDz6heSrqPRlUCRGI9GQ/zh-cn_image_0000002779567130.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=9205747A9116F32175487770AA399BB0425CF716EF4E2A370D5F2F4A71BBA4DC "点击放大")手动启动。
3. 在工具控制栏中点击齿轮图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Al5950I5Rt62ZjB5iIvXKg/zh-cn_image_0000002779407146.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1DF4E7BD3C60EBD8FB7E2F22EA10C05ED9568FF3A7F5322E5EE2DA417918994 "点击放大")后勾选Hitrace > multimodalinput。用于采集多模子系统的trace信息，这部分信息会包含硬件传递过来的离屏信号，即多模子系统收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/tgSqFADJSK2sAQKDQzvfDA/zh-cn_image_0000002779567126.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=82C7FED08297514AC199E58C4D5C720FD06AC4B6202CB88B63F8F2C1550D2F08 "点击放大")
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/qdbzsD46RpWWX28e0yWd0A/zh-cn_image_0000002779407122.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC68E17C5061DF3332DD543E18ED9EA368A3298262336C6EE92545ABA3F3462F "点击放大")即开始录制。等待界面出现弹窗提示启动应用后，需要手动点击设备上的应用图标启动应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/O-0zz92KSjC5HuLKk5xJlQ/zh-cn_image_0000002779407152.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC38AA29248CE47B1488052E80BFEC30AF784E6CDB7E7AF76B5EBB2E1CE0067A "点击放大")
5. 待右侧泳道全部显示recording则表明正在录制中，等待应用冷启动结束后可以点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/bTNWqokgRjynfbNTwZyC7g/zh-cn_image_0000002779567098.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A85691816760EEA7CD024DBC1060855D7C58D44C2972EA609D0E054C4D1603 "点击放大")

## 分析Launch数据

### 确认首帧完成时延起止点

**冷启动首帧完成时延起点确认：**

首帧完成时延起点是用户点击桌面应用图标离手的时刻，即多模子系统收到硬件传递过来的离屏信号的时刻。

由于离屏信号对应的trace点耗时较短且不方便记忆。因此，需要优先找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）来辅助定位首帧完成时延的起点位置。具体步骤如下：

1. 找到桌面进程收到点击离手事件的trace点（H:DispatchTouchEvent）。在Profiler面板点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在搜索框中输入H:DispatchTouchEvent后回车，通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/O0J3F2RtTTKfL5D5-5Fx6g/zh-cn_image_0000002808766701.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=85F923CD0E56E3E4838424B986C17274548EE1E91B90A00A68F1387329F314B7 "点击放大")或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/-eEtaHSpSvyr4x8iximHfQ/zh-cn_image_0000002779567124.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C6E5E4BFE83AAE2B019F3BCACE86A1E68037D4BCEE59FE6CE287E3DF43282B1 "点击放大")按钮切换搜索结果，找到桌面进程泳道（ohos.sceneboard）中type=1（0：手指按下；1：手指抬起；2：滑动）的H:DispatchTouchEvent点并添加标记，为方便后续查找，可以通过双击标记，在弹出的标记属性框中修改标记描述为点击离手事件。该trace点就代表桌面进程收到点击离手事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/GV22By-vSzuIGN21ZGctAQ/zh-cn_image_0000002779567116.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BDAAD998529ECC904CC7F381ADD5BE0DD506771EBF7E52D0D7EFF1256DC4C57 "点击放大")
2. 搜索多模子系统泳道（mmi\_service）。点击搜索框选项区选择**Search Units搜索泳道**，在输入框中输入mmi\_service后回车，该泳道可能有多条，需要通过点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/URhzHF08QeCUlzSCJEld1g/zh-cn_image_0000002779407144.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB827644E01ED91AE69B797A976E81896BA8ECFE0D410FEFB1258BC46814E5F9 "点击放大")或者![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/kiTLIPsUTFe9MHJDX-qujQ/zh-cn_image_0000002808766703.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3201462393F93C3E23D4307ED6369F673050D436D8D7E3632AF43E1450B45F0 "点击放大")按钮切换搜索结果，找到包含trace片段的mmi\_service泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/joZlqzhqQqa14MhxH9WA2A/zh-cn_image_0000002779407154.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=680BDA3966DA6242E8EF11337DC6C60FB720B26673A2F3F386AC04EDD8DE396B "点击放大")
3. 借助桌面进程收到点击离手事件trace点，继续定位多模子系统收到点击离手事件的trace点。

   在mmi\_service泳道中找到位于点击离手事件标记位置前方的CPU Running条块（此段时间表示多模子系统正在运行），在该条块下方找到H:service report touchId:{id}, type: up（或H:service report pointerId:{id}, type: button-up）的trace点并添加标记，然后修改标记描述为首帧完成时延起点。该trace点代表的是多模子系统收到点击离手事件，即冷启动首帧完成时延的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/gdzCzz8PQDm6mvB2It-u9Q/zh-cn_image_0000002779567104.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D3F3EABBDD6C466576072B1D3DF38B60429D2FB652E3BA230BDFD5A924AAF11 "点击放大")

**冷启动****首帧完成****时延止点确认：**

首帧完成时延止点是应用进程启动后收到的首个硬件垂直同步信号的时间点，即Render Service（统一渲染服务进程）将应用首帧渲染结果呈现到屏幕上的结束点。定位首帧完成时延止点具体步骤如下：

1. 找到应用进程启动后的首个垂直同步信号trace点H:ReceiveVsync，这个trace点代表应用的首帧开始绘制。选择应用进程子泳道，点击搜索框选项区选择**Search Unit Data**搜索泳道数据，在输入框中输入H:ReceiveVsync后回车，找到第一个H:ReceiveVsync点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/4aFSl55gSau1VM1iBlN50Q/zh-cn_image_0000002779567102.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BE2C72B5D89B67F9EC457B86843046F9DCCBBC383057964373B314D6D31236C "点击放大")
2. 应用进程启动后收到首个垂直同步信号时，会通知Render Service进程进行图形渲染，因此需要优先找到应用进程通知Render Service进程进行图形渲染的三个trace（H:FlushMessages > H:SendCommands > H:MarshRSTransactionData）。由于这三个trace耗时较短，不便查看，因此需要使用搜索功能来确定。框选H:ReceiveVsync trace点，点击搜索框选项区选择**Search Units Data**搜索泳道数据，在输入框中输入FlushMessages后回车。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/nN-x-AGaQfOhkqv6C61-pg/zh-cn_image_0000002808886779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=999074E466EEB643EE2B71583DB64DB21D67B354B5F1B256E7E336D67C546897 "点击放大")
3. 找到trace点H:FlushMessages（代表绘制消息） 后，继续在该trace点下方逐层分析，先找到trace点H:SendCommands（代表发送绘制指令给Render Service进程进行图形渲染），在下方再找到trace点H:MarshRSTransactionData（代表发送了绘制指令），这3个trace点就代表应用进程通知Render Service进程进行图形渲染的流程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/wt6p2Tr7QVyZXZ44xjSAMw/zh-cn_image_0000002808886785.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC11CCB7B93E0A7CC7BDFC3C2BCFD55CD6F85F268C04609140DE9BB1B599BB30 "点击放大")
4. 接着需要找Render Service进程收到应用进程首帧渲染通知的trace点，点击H:MarshRSTransactionData条块，“Slice Detail”区域可以查看该trace详情，包括trace名称、所属进程等。点击“Slice Detail”区域中Name后方跳转按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/dCwZID04T12wY5rNB3n1bw/zh-cn_image_0000002779567122.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D76EAEF189DB0BCAFC8370405C5FFF7C6BE9F635621A25CDF588247B76A7853)跳转到render\_service泳道的H:RSMainThread::ProcessCommandUni trace点并添加标记，然后修改标记描述为收到渲染通知。该trace点就代表Render Service进程收到应用进程首帧渲染通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/mGxIm1ZXTreC2M8QuNQc5Q/zh-cn_image_0000002779407134.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=7343D9D65619B849EFA585031999B9A91C844718C4A60286AEA2B3105E401F7F "点击放大")
5. 接着找到Render Service将应用首帧提交硬件上屏的trace点，该操作在Render Service送显线程（CompThread）中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入CompThread后回车，查找位于收到渲染通知标记位置后方的第一个H:CommitLayers并添加标记，然后修改标记描述为提交硬件上屏。该trace点代表Render Service将应用首帧提交硬件上屏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/DNZje0K8Q6OfO7svNBggNQ/zh-cn_image_0000002779407124.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=32AA181B804245375AA557F3A326FE9DE5A2240BAB094518A41579EDDC4FFFC2 "点击放大")
6. 最后找到Render Service将应用首帧渲染结果呈现到屏幕上的trace点，该操作在PresentFence中完成。点击搜索框选项区选择**Search Units**搜索泳道，在输入框中输入PresentFence后回车，查找位于提交硬件上屏标记位置后方的第一个H:Waiting for PresentFence，该trace点代表Render Service将应用首帧渲染结果呈现到屏幕上，trace点的结束位置就是冷启动首帧完成时延的止点，在此处添加标记并修改标记描述为首帧完成时延止点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/YrOyaZd0SOKQxJRHI36BAQ/zh-cn_image_0000002808886767.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBE714F644B03E19B39B804DCDDDE955E011D716ABD5A53DBBF1E04D4C97520E "点击放大")

### 案例：应用首页加载耗时较长导致应用冷启动首帧完成时延不达标

**说明** 

* 本案例基于应用进程启动过程中，在Ability的生命周期回调函数中做了耗时操作。
* 预期冷启动首帧完成时延不超过600ms。

框选应用冷启动首帧完成时延起止点位置，通过框选区间的时间长度看出，冷启动首帧完成时延超过800ms，比预期的600ms长。

切换到应用进程Process泳道，查看主线程（线程号与进程号一致）的trace。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EzNp0TTXRzK9yxDWFqqbsA/zh-cn_image_0000002808886787.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=678CA26D1A564BEEB117CF7FE7D128CB4A20B84F7623FE3C8AAE13347C132AA7 "点击放大")

下方详情区展示Details信息，包括trace名称、起始时间、持续时长。将持续时间（Duration）降序排序，可以看到主要耗时在H:void OHOS::AbilityRuntime::UIAbilityThread::HandleAbilityTransaction，该阶段主要是AbilityStage/Ability的启动生命周期在执行相应的回调。从这里可以看出，是因为AbilityStage/Ability启动生命周期的回调执行时间较长。接下来需要分析调用栈，通过调用栈分析回调执行时间长的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/oNJG16bDRIixfOW6jSU_yQ/zh-cn_image_0000002779407128.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAB5BD870E940A7A800769E892839721812AFA4B558F9E74AB2266FBC0AA3034 "点击放大")

接着切换到ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看线程号与进程号一致的ArkVM子泳道（该泳道为主线程调用栈），可以看到ArkTS侧一些方法的耗时。从下图中可以看到ArkTS侧无函数执行，需要切换到Callstack泳道看ArkTS和Native混合函数调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/SoNy_i60QOO23OAYhOwV5g/zh-cn_image_0000002779567110.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=F121D7F99616AD4A72936BA5FA69EC224A9E8ACC90DE4C895B9BB1C7A3F9F3D1 "点击放大")

最后切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，查看下方Heaviest Stack区域，滑动观察权重占比最大的函数调用栈，定位到耗时主要是EntryAbility.ets文件下第79行代码引起，双击该栈帧可以直接跳转到源码文件的对应位置上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/z2xny1XzQEKRrUPnfdUMGA/zh-cn_image_0000002779567134.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A899BB6414C42F8CE1E18FA5F198BA1C1899CBD8113D79B8461E8461C582FEA "点击放大")

结合业务代码查看，可以看到是因为在EntryAbility.ets文件下onCreate()中做了耗时操作。耗时操作建议通过异步任务延迟处理或者放到其他线程执行，以降低主线程负载，缩短应用冷启动首帧完成时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Q1KfM4PYRq-HWojlJdnZ4Q/zh-cn_image_0000002808766709.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=49B5516EE6D5F0E4B04EA64F4028066277FAD3930D5D7307480E7DB1B6FAC701)

更多应用冷启动优化方案，请参考[应用冷启动时延优化](../best-practices/bpta-application-cold-start-optimization.md)。
