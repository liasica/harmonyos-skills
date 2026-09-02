---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-28
title: 滑动地图卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 滑动地图卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e550a2868f104c1a3fcf4cbfcc075f7219acc7bcf36216eae84ed4fc81c68ac6
---

## 问题现象

左右滑动地图查看地图信息时存在卡顿的现象。

## 背景知识

* 屏幕刷新率：每秒钟屏幕会刷新的次数，120Hz是一秒内刷新120次，平均一次耗时8.33ms。
* Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
* 在HarmonyOS中，图形系统采用统一渲染模式，遵循典型流水线模式。在渲染流程中，应用侧首先响应消费者的屏幕点击等输入事件，处理完成后提交给Render Service。Render Service协调GPU等资源处理，最终将图像送到屏幕上显示，整个流程应用侧和Render Service侧都可能出现卡顿，导致最终用户观察到丢帧，具体可看[渲染流程](../best-practices/bpta-optimization-overview.md#section1625893416218)。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能。更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。常见Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:FrameNode[组件名][id:组件ID]::RenderTask | 执行单个组件的绘制任务 |
  | H:ReceiveVsync | 应用接收Vsync信号 |
  | H:ViewPU.viewPropertyHasChanged 组件名 状态变量名 N | 某个组件状态变量发生更新，N表示该状态变量更新后影响的组件数量。需要在应用启动前运行hdc shell param set persist.ace.debug.enabled 1命令才可以看到该Trace关键字 |

## 问题定位

1. 运行hdc shell param set persist.ace.debug.enabled 1命令、重启应用，使用DevEco Profiler Frame分析工具抓取滑动地图过程的Trace信息。User Events（用户交互）泳道中的Touch为触摸事件类型，其等同于滑动地图的过程，然后查看Frame泳道中的Display子泳道发现屏幕刷新率为120Hz，但应用侧绘制帧率只有17.7FPS，绘制帧率较低。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Y6qrA_VZSd-iQT5cyojRmQ/zh-cn_image_0000002658794435.png "点击放大")
2. 查看应用主线程两次接收Vsync信号处理的时间间隔，从下图中可看到为67.4ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ik4Zoh3tQYKXNgCPFc2H4A/zh-cn_image_0000002628555072.png "点击放大")
3. 分析该部分Trace信息可看到耗时主要集中在应用Canvas组件绘制（33ms）和状态变量更新（21ms）。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/exPbRkx6SZ6yBLYWzN-3gg/zh-cn_image_0000002628395166.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/b7ha7Ll1SjKD33c5sVPGeA/zh-cn_image_0000002658914395.png "点击放大")
4. 在该过程应用长时间处于Running状态，可知应用在执行耗时操作，导致滑动地图卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ft28fmYrQiCtenso8ndnIA/zh-cn_image_0000002658794437.png "点击放大")

## 分析结论

滑动地图过程中，组件渲染绘制和状态变量更新时执行耗时操作，导致卡顿。

## 修改建议

优化组件渲染绘制的耗时逻辑；参考[状态管理最佳实践](../best-practices/bpta-status-management.md)，在滑动过程中避免不必要的状态变量更新。
