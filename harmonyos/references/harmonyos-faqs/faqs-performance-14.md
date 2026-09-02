---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-14
title: ArkUI页面点击响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面点击响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:313223495d7f80fbcdb509e47428663d78360d87457188e8c1cb1a810981dfc1
---

## 问题现象

点击页面内容后需要等待一段时间才进入新页面，有延迟。

## 背景知识

* 点击响应时延是用户使用移动设备时，从手指触摸屏幕（如点击按钮）到屏幕上有反应（如按钮呈现被按下的效果）的时间间隔。
* 点击响应慢问题是因为点击响应时延超出了预期的响应时延，响应慢的问题通常会分为性能测试上的响应慢和用户体验上的响应慢，这两类情况有不同的预期点击响应时延。
  + 在性能测试中，针对特定场景有相应的测试指标，对于不同级别有不同的时延基线，应用内点击操作响应时延不能超出以下时间。

    | 指标分级 | 时延 |
    | --- | --- |
    | S标 | 100ms |
    | A标 | 150ms |
    | B标 | 250ms |
  + 用户体验上点击响应慢和性能测试上会有所差异，对点击响应时延的感知在秒级，通常延迟1秒、2秒甚至几秒的时候才会觉得慢。
* 点击应用页面内容到屏幕上有反应过程，设备整体处理流程大致如下：
  1. 多模输入服务mmi\_service线程收到用户触摸屏幕的相关事件（比如按下、滑动、离开屏幕），根据窗口的触摸热区判定分发给应用。
  2. 应用侧在收到Vsync信号后会响应用户的屏幕点击等输入事件，执行相关的业务流程，如跳转到新页面、显示按钮被按下的效果等，提交绘制指令给渲染服务render\_service。
  3. 渲染服务会根据绘制指令进行相应的图形计算和渲染操作，将渲染结果写入到帧缓冲区（存储用于显示器输出的图像数据）中，将数据送到屏幕上显示。
* Trace文件是一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况。查看Trace文件可使用[Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host/tree/master/smartperf_host)工具。

  点击操作响应慢问题相关Trace关键字如下：

  | 关键字 | 线程/泳道 | 说明 | 备注 |
  | --- | --- | --- | --- |
  | H:originEventHandle code:501 | mmi\_service | 点击应用页面内容离手点 | 多模输入起点 |
  | H:DispatchTouchEvent id:N, pointX=XXX pointY=XXX type=1 | 应用包名 | 应用收到点击离手的事件 | 多模输入终点，应用模块处理起点 |
  | H:SendCommands | 应用包名 | 应用发送渲染请求，下方H:MarshRSTransactionData表示提交绘制相关数据给渲染服务，transactionFlag中包含了应用进程号和序号 | 应用模块处理终点 |
  | H:ABILITY\_OR\_PAGE\_SWITCH | H:ABILITY\_OR\_PAGE\_SWITCH | 页面切换过程 |  |
  | H:RSMainThread::ProcessCommandUni[应用进程号，序号] | render\_service | 渲染服务处理渲染请求，在接收Vsync信号时执行，应用进程号、序号与应用发送渲染请求的transactionFlag相同 | 渲染服务处理起点 |
  | H:RSHardwareThread::CommitAndReleaseLayers rate: 帧率，now：时间戳 | RSHardwareThread | 将GPU处理的渲染结果提交到显示硬件，now与H:RSMainThread::ProcessCommandUni上方的H:ReceiveVsync中的now字段一一对应 | 渲染服务处理终点 |
* DevEco Profiler目前是集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码，更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  借助DevEco Profiler Time工具可以查看应用执行的ArkTS代码以及相应耗时，如下图所示，更多详细内容可看[基础耗时分析：Time分析](../harmonyos-guides/ide-insight-session-time.md)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/4oU9EZBiSQ27YsUUs8_Jlg/zh-cn_image_0000002658914331.png "点击放大")

## 问题定位

以点击某应用首页跳转到详情页，点击响应慢问题为例，按整体流程拆分总耗时，确定各模块耗时，具体如下：

1. 多模输入模块耗时为手指离开屏幕到应用收到该事件的时间。用SmartPerf打开Trace文件，在上方搜索框中输入H:originEventHandle code:501找到手指离开屏幕的地方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/ewRBu1brSlW0Dxk7Sj_lhg/zh-cn_image_0000002658794377.png "点击放大")

   接着以该点为起始点，在应用包名泳道中往后查看几ms范围内的Trace关键字H:DispatchTouchEvent XXX type=1，找到应用收到该事件的地方，得到该部分耗时为1.5ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/PEZkwEAOQeqpNaifm-mNPw/zh-cn_image_0000002628555012.png "点击放大")
2. 应用模块耗时起点为应用收到手指离开屏幕的事件，终点为应用从当前页面开始跳转到新页面时第一次发送绘制请求的结束点。

   手指离开屏幕事件的地方为上述多模输入模块耗时的结束点。应用第一次发送绘制请求的地方可以通过应用收到手指离开屏幕的事件后第一次接收Vsync信号（Trace关键字为H:ReceiveVsync）中发送绘制请求（关键字为H:SendCommands）的结束点来确定，同时该点会在页面切换Trace关键字H:ABILITY\_OR\_PAGE\_SWITCH的起始点附近。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/0VLFc1xLTRqkGP78dCmFcg/zh-cn_image_0000002628395112.png "点击放大")

   计算应用收到手指离开屏幕的事件和该点之后应用第一次提交绘制请求的时间可确定应用模块处理耗时142.5ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/W4qjvXmCQtyounEl8VghSA/zh-cn_image_0000002658914333.png "点击放大")
3. 渲染服务模块耗时为渲染服务处理应用发送的渲染请求到将GPU处理的渲染结果提交到显示硬件的时间。

   渲染服务处理应用发送的渲染请求可以通过应用模块耗时的结束点来确定。在应用包名泳道上方有个Actual Timeline泳道，在应用接收Vsync信号、提交绘制请求处会有对应的一段Trace点（以数字呈现），点击后在下方显示框中点击render\_service右侧的跳转箭头可以找到渲染服务处理页面有变化第一帧数据的地方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/_4YRdDqjTNKTHPvXjVMw5w/zh-cn_image_0000002658794379.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/8qjHXZiuRo2SW-J0bkyCNQ/zh-cn_image_0000002628555014.png "点击放大")

   然后以render\_service这次处理Vsync信号为起点，根据now（时间戳），在RSHardwareThread泳道中找到render\_service将该帧GPU处理的渲染结果提交到显示硬件的地方，最终得到渲染服务模块耗时15.7ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/BDfY16x3Ty-2XcTiSvxDtw/zh-cn_image_0000002628395114.png "点击放大")

   最终得到如下耗时拆分结果，耗时主要集中在应用模块。

   | 多模输入模块 | 应用 | 应用->渲染服务（应用结束点到渲染服务起始点） | 渲染服务 | 总和 |
   | --- | --- | --- | --- | --- |
   | 1.5ms | 142.5ms | 6.0ms | 15.7ms | 165.7ms |
4. 分析耗时占比较多的模块，按上述步骤分析，耗时最多的部分在应用，应用侧耗时场景可能有：
   * 场景一：执行业务代码耗时：

     框选Trace中应用主进程该阶段的运行状态，发现耗时主要在Running部分，查看该阶段的Trace信息，得知其中一部分是加载NewsPage页面，还有另一部分没有Trace点，无法看到在执行什么业务流程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Rt3rMezmRE2J_n1_Nw19Bg/zh-cn_image_0000002658914335.png "点击放大")

     使用Profiler工具抓取该过程的Trace信息，发现应用在执行dispatchJson方法，该方法耗时占比较多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/yglEGHYwSLOH9ZJNIYLAbA/zh-cn_image_0000002658794381.png "点击放大")
   * 场景二：http请求耗时：

     查看该阶段应用包名泳道Trace，发现耗时主要在http请求部分。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ZDwZU8aZSwerbzYjscXOWA/zh-cn_image_0000002628555016.png "点击放大")

     结合问题发生时的Hilog日志，根据Trace信息中的TaskID可以看到问题发生时http请求总耗时7.237秒，因此点击响应慢。

     ```txt
     06-26 10:37:48.275 21779 26289 I C015B0/应用包名/NETSTACK: [http_exec.cpp:418] taskid=-2147483646, size:89, dns:0.073, connect:0.000, tls:0.000, firstSend:0.219, firstRecv:0.000, total:7236.370, redirect:0.000, errCode:0, RespCode:200, httpVer:2, method:POST, osErr:0
     ```

## 分析结论

1. 应用主线程在收到点击事件响应处理时，执行较耗时的业务代码，导致点击响应慢的问题。
2. 应用通过http请求获取资源，请求耗时过久导致整体响应慢。

## 修改建议

1. 可将耗时操作迁移到异步任务中处理，避免阻塞主线程，提升应用的响应速度，参考[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)。
2. 优化服务侧性能或采用[预加载](../harmonyos-guides/cloudfoundation-prefetch-service.md)服务提前请求资源，提升响应速度。
