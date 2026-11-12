---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-frame-case
title: 案例：使用Frame模板分析应用卡顿问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 卡顿丢帧分析 > 案例：使用Frame模板分析应用卡顿问题
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a41c004cf8eedb2f0b3e3f8a325c8a36b9c3b82d874cfd072f501eb3400611b9
---

本案例介绍如何判断应用存在卡顿帧，再通过调用栈和Trace信息分析应用运行逻辑，找出应用卡顿的原因。

应用卡顿分析基础功能请参考[Frame分析](ide-insight-session-frame.md)。

## 分析步骤

分析应用卡顿类问题步骤如下：

1. 确认是否存在卡顿帧。
2. 若存在卡顿帧，根据调用栈和Trace等信息进一步确定问题点。

## 分析Frame数据

### 分析应用是否存在卡顿

1. 框选Frame泳道，窗口下方的**Statistics**区域中会以进程维度对选定时间段内的Frame信息进行统计，当Jank Count大于0时，说明存在卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/VCyDVWz8QMWFfU1V9qZELg/zh-cn_image_0000002779407210.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=58B18CCB445E4CA181FCFF74270185F46011C6701CE74E5A2C4F74D044D9A858 "点击放大")
2. 找到**Statistics**区域中存在卡顿帧的进程，点击进程名称后方跳转按钮，跳转到**Frame List**区域。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/cgRbceolTr6DM7BcJ8R0AQ/zh-cn_image_0000002808766765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAF5D707E4D883CBD5135C6580563BDEA5BC000EE73DF0A0FEC68F6F4F296F66 "点击放大")
3. Frame List区域会展现该进程对应的Frame列表。在Frame List区域中对卡顿丢帧类型（Jank Type）进行升序排序，单击Frame List页签中任意一卡顿帧，直接跳转到该帧且泳道上该帧被反选。

   **说明** 

   * 在带**RS Frame**和**App Frame**标签的子泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * AppDeadlineMissed：App侧的卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/FAr1U9FATEOghE00knGtJg/zh-cn_image_0000002808886845.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D74B973F08AD767ED5A763E101C91749A16FB98D79D13E49C0513804CA6B780B "点击放大")
4. 点选该卡顿帧，窗口下方的**Details**区域中显示卡顿帧的关键信息。右侧应用进程前方跳转按钮可以跳转到应用进程Trace。
   * Expected Duration：一帧绘制的期望耗时。与fps的大小有关，如fps为120，对应的Vsync周期为8.3ms，即App侧/Render Service侧的帧耗时，一般需要在8.3ms以内。
   * Actual Duration：一帧绘制的实际耗时。

   如下图，可以看到该帧的期望耗时为8ms 330μs，实际耗时为44ms54μs，远远超过了期望耗时，因此被识别为卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/n6hWHH8lQtqwRQE_RqStmQ/zh-cn_image_0000002808886843.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=65C27198D1C5D8FA94204FE6ACF0D6FD2C3E5625C55B98E870A88420A5081354 "点击放大")
5. 框选该异常帧时间范围，结合**ArkTS Callstack**泳道、**Callstack**泳道和**Trace**等信息进一步分析异常点。

### 案例：分析应用卡顿原因

1. 找到并框选要分析的异常帧，查看**ArkTS Callstack**泳道分析ArkTS侧耗时函数。优先查看主线程调用栈，即线程号与进程号一致的ArkVM子泳道。可以看到ArkTS侧一些方法的耗时。
2. 查看下图调用栈，除(program)外，其他调用栈耗时小于一帧绘制的期望耗时8.3ms（被调优的设备fps为120），因此该卡顿帧主要分析调用栈(program)的耗时。

   (program)代表程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或者Native调用ArkTS情况，一般很难通过这里分析出有效的信息，需要切换到Callstack泳道看具体的调用栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/N1Neduy3QeSe00dYcsWkNA/zh-cn_image_0000002808766761.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF6B9C81E7C0E8ED4263B5BBB43D3322EBCCF2D5DD8074192E1E9F3F8EFFE140 "点击放大")
3. 切换到**Callstack**泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，滑动观察下方Heaviest Stack区域“%”列中占比最大的函数调用栈，Category中亮色代表开发者调用栈，灰色代表系统调用栈，可以看出下图中耗时主要在系统侧的so，无法识别具体异常原因，接下来进一步分析应用进程Trace。

   **说明** 

   也可通过底部的“Call Trees”选择框来隐藏系统调用栈，减少干扰信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Y6HT1DCQQuauUPVe4kvZPQ/zh-cn_image_0000002808886853.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D82581238DADA843960BE151C9A4A913DFD478EE66EA8C706D66AC7297DFDCB6 "点击放大")
4. 切换到应用进程Process泳道，查看主线程（线程号与进程号一致）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/j9QwM-j0TfSMMwK90cgb8g/zh-cn_image_0000002779407200.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=99793A018580D3A85295E1768AD7CEC780DCDE0FCD285F35FC7111B49708189C "点击放大")
5. 窗口下方详情区可查看到Trace统计信息列表，逐层展开耗时最长的Trace，定位到主要耗时是在3次H:CreateImagePixelMap。接下来进一步分析这3次H:CreateImagePixelMap耗时的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/wlFh26SzR4Kb7ReGfXty0Q/zh-cn_image_0000002779407208.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C93E05214D323770C0E16FBC850A73B544CC1BAE88BCC4E69F7E8AFC56667F9 "点击放大")
6. H:CreateImagePixelMap和图片加载相关，再结合业务代码查看，可以看到是因为同步加载网络图片，建议修改为异步加载。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/ToC7ovUxTtWNG8TPlzN1gA/zh-cn_image_0000002779567188.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=41DB6D594FA3A5877A70201B469DE419417CC3BCAAB276E1C0327AA5E6082F81 "点击放大")

   **说明** 

   一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。不建议图片加载较长时间时使用同步加载。
