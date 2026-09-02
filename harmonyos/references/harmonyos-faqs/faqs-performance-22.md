---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-22
title: 滑动翻页时动效卡顿不流畅
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 滑动翻页时动效卡顿不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9eea1e3b440e70d84f393cf16072812c215e0ad44f1b0439b64584c1c71236c8
---

## 问题现象

阅读文档场景下，左右滑动翻页时丢帧，帧率低。

## 背景知识

* 屏幕刷新率：每秒钟屏幕会刷新的次数，120Hz是一秒内刷新120次，平均一次耗时8.33ms。
* Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
* 渲染流程：下图为90Hz刷新率的渲染流程，首先应用侧收到Vsync信号后会响应用户的屏幕点击等输入事件，确定UI元素的位置、大小、资源、动效属性等，然后提交绘制指令给渲染服务(Render Service)，渲染服务会根据绘制指令进行相应的图形计算和渲染操作，将渲染结果写入到帧缓冲区（存储用于显示器输出的图像数据）中，将数据送到屏幕上显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/_kERsKymShmj3bX-pOrFPw/zh-cn_image_0000002658914379.png "点击放大")

  按上述流程中，应用侧和Render Service侧都可能因为处理时间较长，超过了Vsync信号周期，导致界面送显的频率低于屏幕刷新率，出现卡顿丢帧的情况。前者可能是应用业务逻辑、组件复杂，执行耗时逻辑等导致，后者可能是界面结构过于复杂、GPU负载过大等导致。

  1. 应用卡顿导致丢帧的故障模型：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SKnXnWH7TMGJaA9L9ZjqJA/zh-cn_image_0000002658794421.png "点击放大")
  2. Render Service卡顿导致丢帧的故障模型：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/WkLnyNPzSkWYyrj5xlojBg/zh-cn_image_0000002628555058.png "点击放大")
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  常见Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:touchEventDispatch | 屏幕触摸事件 |
  | H:FrameNode[组件名][id:组件ID]::RenderTask | 执行单个组件的绘制任务 |
  | H:ReceiveVsync | 应用接收Vsync信号 |

## 问题定位

1. 使用DevEco Profiler Frame模板抓取滑动翻页过程的Trace信息，根据User Events（用户交互事件）和应用接收Vsync信号处理的Trace关键字H:ReceiveVsync确定左右滑动翻页的大致范围，查看render\_service泳道中的H:PreferredFrameRate可知当前屏幕刷新率为120Hz，通过Present Fence可看到左右翻页时页面变化的帧率接近20fps，帧率过低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/9EQnneNNTA-0DvMRgc8gtw/zh-cn_image_0000002628395154.png "点击放大")
2. 查看该主线程范围内的Trace信息，在Slice List中通过RenderTask关键字过滤可看到有应用有执行Canvas组件的绘制任务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/kIQYKNM5SkGvRc0rZ5okxw/zh-cn_image_0000002658914381.png "点击放大")
3. 使用ArkUI Inspector查看应用布局，应用采用Canvas组件来显示文档，而左右滑动翻页时会触发Canvas绘制，因此查看主线程执行Canvas组件的绘制任务的频率，确认是否是频率过低导致滑动翻页掉帧。
4. 根据ArkUI Inspector获取的Canvas组件id号，在Profiler中搜索H:FrameNode[Canvas][id:2321]::RenderTask，确认应用两次执行Canvas组件绘制任务的时间间隔为50ms左右，正好是20fps，因此可知是应用侧Canvas组件绘制的频率较低，导致翻页掉帧问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Z_e6Fd9RRJCYU1YCuirT6w/zh-cn_image_0000002658794423.png "点击放大")

## 分析结论

阅读文档、左右滑动翻页时，应用组件绘制的频率过低，小于屏幕刷新率，导致丢帧问题。

## 修改建议

优化组件绘制的相关业务逻辑，提高组件绘制的频率，可参考[Drawing自绘制性能提升](../best-practices/bpta-drawing-capability-improve-performance.md)。
