---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-arkweb
title: 加载丢帧：ArkWeb分析
breadcrumb: 指南 > 优化应用性能 > 加载丢帧：ArkWeb分析
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:49461c261cc9e74268019cd239606d55d8a1498930894bb54e2f248ce298cf7a
---

## 功能介绍

应用开发过程中，会通过在App中嵌入WebView以提高开发效率，可能面临ArkWeb加载和丢帧等问题。DevEco Profiler提供ArkWeb分析模板，可以结合ArkWeb执行流程的关键trace点来定位问题发生的阶段。如果问题发生在渲染阶段，可以结合H:RosenWeb数据，线程运行状态以及帧渲染流程打点数据，进一步分析丢帧问题。

ArkWeb模板支持的泳道包括：ArkWeb、User Events、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍ArkWeb泳道，其他泳道的详细信息请参考对应模板内容。

* User Events泳道的介绍请参考[Frame分析](ide-insight-session-frame.md)。

* ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* CPU Core、Process泳道的介绍请参考[CPU活动分析](ide-insight-session-cpu.md)。

**说明** 

任务分析前，需创建ArkWeb模板，完成一次录制，录制期间触发Web相关场景，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## ArkWeb加载问题分析

根据Web页面加载过程中的关键trace点，划分了五个阶段，分别是：点击事件（Click Event）， 组件初始化（Component Initialization），主资源下载（Primary Resource Download），子资源下载（Sub-resource Download），渲染输出（Render And Output）。

框选**ArkWeb**泳道，可以查看耗时阶段划分的关键trace点，并可以根据trace信息，关联到所在线程信息。

**Details**区域可以跳转关键trace所在泳道，进一步分析加载问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/AVklbFCbRSS0Wer1zPGWCg/zh-cn_image_0000002701663768.png "点击放大")

## ArkWeb丢帧问题分析

1. **ArkWeb**子泳道聚合了Web相关线程的trace信息，通过分析Web渲染过程的关键函数的trace点，可以分析出每一帧的执行流程。聚合的Web线程信息如下：
   * H:RosenWeb：用于记录准备提交给Render Service进行统一渲染的数据量。
   * Compositor：合成线程，负责图层CPU指令合成，承载动态效果。
   * CompositorGpuTh：用于从GPU获取渲染结果和将合成的buffer送至图形子系统执行渲染。
   * Chrome\_InProcGpu：光栅化。
   * VsyncGenerator：图形侧vsync信号，用于定时生成vsync信号，通知渲染线程或动画线程准备下一帧的渲染。
   * VSync-webview：用于接收图形侧发送的vsync信号，并根据信号触发WebView页面的渲染或重绘。
   * VizCompositorTh：绘制信号监听线程，向图形请求Web本身的vsync信号，触发系统Web相关绘制或执行。
   * Web应用Render线程：以 :render 结尾的线程，主要用于图形渲染任务，包括html、css解析，进行分层布局绘制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/JxCuYCCvQjSUQjAKkTQqRw/zh-cn_image_0000002701823692.png "点击放大")
2. 一般结合**H:RosenWeb**泳道和**PresentFence**泳道来分析是否存在丢帧。

   H:RosenWeb上标识有待提交给渲染服务的数据量。正常情况下，每个数据量都会提交给硬件进行上屏，即PresentFence泳道上的H:Waiting for PresentFence trace点。如果某个数据量在PresentFence泳道上没有该trace点，那么很可能是存在丢帧问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Jlr4wrjtSDucuJ7DpQJ9wQ/zh-cn_image_0000002701663766.png "点击放大")

3. 在ArkWeb的子泳道中，Web应用Render线程提供了分析子资源加载各阶段具体耗时的能力。切换到 **Sub Resource**区域，可查看详细信息。

   包括统一资源定位符、缓存类型、是否为本地资源替换、请求资源时间（ns）、队列时间（ns）、停滞时间（ms）、dns解析时间（ms）、连接耗时（ms）、ssl连接时间（ms）、服务器响应耗时（ms）、下载耗时（ms）、传输时间（ms）、请求方法、状态码、编码前资源大小、编码后资源大小以及HTTP版本。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/S0jTSYtkSEOM6HWXtb2loA/zh-cn_image_0000002701823690.png "点击放大")
4. 点选某一行，可以查看该URL对应的缓存信息。包括缓存存在时长、最后修改时刻、过期时刻、缓存指令、资源的唯一标识符以及资源是否过期。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/dhnUXJgiQbCj4zgklWXg4g/zh-cn_image_0000002701663770.png "点击放大")
