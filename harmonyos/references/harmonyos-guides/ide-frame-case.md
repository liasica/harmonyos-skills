---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-frame-case
title: 案例：使用Frame模板分析应用卡顿问题
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 卡顿丢帧分析 > 案例：使用Frame模板分析应用卡顿问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:da3c10c4883866bda9ea2be1f17e585fa852dc1e70695e10dc0d78a9bdc5a30a
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/EO6cCTZtThSTvdvP4EH27Q/zh-cn_image_0000002779407210.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7C8B80AA614556A66407937328EC3A3B93C01D81200F4005BD0BDCF760552FD "点击放大")
2. 找到**Statistics**区域中存在卡顿帧的进程，点击进程名称后方跳转按钮，跳转到**Frame List**区域。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ppPcm5QfR3WF5YK8OhAWwg/zh-cn_image_0000002808766765.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=A172EFD35F7F841BA1F6743BAA6982694F9BE9D08AD9A81E332E38C4D02C3441 "点击放大")
3. Frame List区域会展现该进程对应的Frame列表。在Frame List区域中对卡顿丢帧类型（Jank Type）进行升序排序，单击Frame List页签中任意一卡顿帧，直接跳转到该帧且泳道上该帧被反选。

   **说明** 

   * 在带**RS Frame**和**App Frame**标签的子泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * AppDeadlineMissed：App侧的卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/oYEyXVKqREaCNIwOnpwPzw/zh-cn_image_0000002808886845.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=2555379251376228F2E2A03C794C0C707F6A7AD434C7CD443B503C56EA895DAE "点击放大")
4. 点选该卡顿帧，窗口下方的**Details**区域中显示卡顿帧的关键信息。右侧应用进程前方跳转按钮可以跳转到应用进程Trace。
   * Expected Duration：一帧绘制的期望耗时。与fps的大小有关，如fps为120，对应的Vsync周期为8.3ms，即App侧/Render Service侧的帧耗时，一般需要在8.3ms以内。
   * Actual Duration：一帧绘制的实际耗时。

   如下图，可以看到该帧的期望耗时为8ms 330μs，实际耗时为44ms54μs，远远超过了期望耗时，因此被识别为卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/8wmBgN8dTweY7uB8RCsLsg/zh-cn_image_0000002808886843.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BFC908FA489D2C151585028D310AB8ABF422D11C3D847A818ADDB0C280F0E22 "点击放大")
5. 框选该异常帧时间范围，结合**ArkTS Callstack**泳道、**Callstack**泳道和**Trace**等信息进一步分析异常点。

### 案例：分析应用卡顿原因

1. 找到并框选要分析的异常帧，查看**ArkTS Callstack**泳道分析ArkTS侧耗时函数。优先查看主线程调用栈，即线程号与进程号一致的ArkVM子泳道。可以看到ArkTS侧一些方法的耗时。
2. 查看下图调用栈，除(program)外，其他调用栈耗时小于一帧绘制的期望耗时8.3ms（被调优的设备fps为120），因此该卡顿帧主要分析调用栈(program)的耗时。

   (program)代表程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或者Native调用ArkTS情况，一般很难通过这里分析出有效的信息，需要切换到Callstack泳道看具体的调用栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/7enAyPTqQGOz0JS25N9x2Q/zh-cn_image_0000002808766761.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DBE49E7CE06702B096453269BB6D34523D465AABBE1E222FD72548FAFCF292C "点击放大")
3. 切换到**Callstack**泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，滑动观察下方Heaviest Stack区域“%”列中占比最大的函数调用栈，Category中亮色代表开发者调用栈，灰色代表系统调用栈，可以看出下图中耗时主要在系统侧的so，无法识别具体异常原因，接下来进一步分析应用进程Trace。

   **说明** 

   也可通过底部的“Call Trees”选择框来隐藏系统调用栈，减少干扰信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/aahg0uJiQJ6D8foGozrY-g/zh-cn_image_0000002808886853.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=3037765AC22160EAF2C337855919449C649F7116E04A4B11C85D06848B643665 "点击放大")
4. 切换到应用进程Process泳道，查看主线程（线程号与进程号一致）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/vrPlyjW0S9W0o-O1lRz9Bw/zh-cn_image_0000002779407200.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1102D9EE1F01421451E867320F56545066638ED6B03FD6D92AF66320333FE7A "点击放大")
5. 窗口下方详情区可查看到Trace统计信息列表，逐层展开耗时最长的Trace，定位到主要耗时是在3次H:CreateImagePixelMap。接下来进一步分析这3次H:CreateImagePixelMap耗时的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/kwIbrTPoTU6qWjIruxving/zh-cn_image_0000002779407208.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=589D313FC0AA784027FA4E12CABFF14805BEA43DDA8572FB1190260A0A82194C "点击放大")
6. H:CreateImagePixelMap和图片加载相关，再结合业务代码查看，可以看到是因为同步加载网络图片，建议修改为异步加载。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/wH_4IIFFS0yQB0QJxXHKOw/zh-cn_image_0000002779567188.png?HW-CC-KV=V1&HW-CC-Date=20261114T004905Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D6CA41168AA75DA412D21130E195EBD7F38C4664D2F77554831DA53D1F46A08 "点击放大")

   **说明** 

   一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。不建议图片加载较长时间时使用同步加载。
