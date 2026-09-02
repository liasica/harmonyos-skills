---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-36
title: 动态变化的页面卡住一段时间无变化
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 动态变化的页面卡住一段时间无变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:667fbc2e3ce9220bf2313fe19b2b8f31ada2d4061300653daeb822cd0d8745b0
---

## 问题现象

动态更新的页面在渲染过程中出现卡顿，页面内容长时间无响应或未及时刷新问题，如何定位？

## 背景知识

* [XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)：一种渲染组件，可作为EGL/OpenGLES和媒体数据写入，通常用于满足应用较为复杂的自定义渲染需求，例如相机预览流的显示和游戏画面的渲染。XComponent持有一个Surface，应用能通过调用[NativeWindow](../harmonyos-guides/native-window-guidelines.md)等接口（比如OH\_NativeWindow\_NativeWindowFlushBuffer）将自绘制内容传送至该Surface。XComponent负责将此Surface整合进UI界面，其中展示的内容正是应用传送的自绘制内容。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

## 问题定位

1. 使用ArkUI Inspector抓取该页面布局，发现该动态变化的页面使用XComponent组件来完成渲染绘制。
2. 使用DevEco Profiler Frame工具抓取该过程的Trace信息，在上方搜索框中输入H:NativeWindowFlushBuffer找到应用将自绘制内容传送到XComponent组件的Surface的相关线程。从下图中可看到该线程为应用的44780子线程，同时有持续1.6s左右未将自绘制内容传送到XComponent组件的Surface。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/cq0_ofBxSAicGiCh9KBPhA/zh-cn_image_0000002658914493.png "点击放大")

   在过程该线程大部分时间处于Running状态，在执行耗时操作。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/wReRxbCGRoqU97gPvYgSXQ/zh-cn_image_0000002628395264.png "点击放大")
3. 通过查看Callstack泳道中的XXX[44780]子泳道，可看到耗时主要集中在libxxx.so文件的函数中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Cuq-S5IRSpamuqtGj7vr9g/zh-cn_image_0000002658794539.png "点击放大")

## 分析结论

应用线程在执行耗时操作，未将自绘制内容传送到XComponent组件的Surface，导致动态变化的页面卡住一段时间无变化。

## 修改建议

[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)将耗时操作移到子线程中处理。
