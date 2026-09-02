---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-3
title: 应用在页面跳转时发生卡顿的现象
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用在页面跳转时发生卡顿的现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a70572ba077b810cd5014e12be8cdd570f64e875e0991ce51ace3037da9de7b2
---

## 问题现象

当用户点击应用页面上的内容（比如按钮），从一个页面进入到另一页面过程，出现卡顿的情况。

## 背景知识

* 屏幕刷新率：显示设备每秒钟更新屏幕内容的次数，其决定了Vsync信号周期，120Hz对应8.33ms，90Hz对应11.11ms，60Hz对应16.67ms。
* Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
* 在HarmonyOS中，图形系统采用统一渲染模式，遵循典型流水线模式。在渲染流程中，应用侧首先响应消费者的屏幕点击等输入事件，处理完成后提交给Render Service。Render Service协调GPU等资源处理，最终将图像送到屏幕上显示，整个流程应用侧和Render Service侧都可能出现卡顿，导致最终用户观察到丢帧，具体可看[渲染流程](../best-practices/bpta-optimization-overview.md#section1625893416218)。

* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码，更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  页面切换关键Trace点如下：

  | 关键字 | 所处线程 | 描述 |
  | --- | --- | --- |
  | H:ABILITY\_OR\_PAGE\_SWITCH | 应用主线程 | 页面切换。 |
  | H:PostAndWait | render\_service | 渲染服务提交绘制任务并等待绘制完成。 |
  | H:RSSurfaceRenderNodeDrawable::OnDraw[窗口名] | RSUniRenderThread | 窗口绘制。 |
  | H:onCreateTexture | RSUniRenderThread | 创建纹理。 |

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。

* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，常用于在应用中显示图片。Image组件在显示大图（分辨率大于512x512）时，会将图片资源解码后放入到共享内存中，在绘制前会进行纹理上传，将数据从CPU拷贝到GPU，该过程会导致绘制耗时多的问题。

  当前对于分辨率在512x512~8192x8192范围的大图，系统采用DMA（直接内存访问）策略解决从CPU拷贝数据到GPU的耗时问题，而对于分辨率大于8192x8192的大图，进行纹理上传。

## 问题定位

以某应用页面切换卡顿为例，相关定位过程如下：

1. 使用DevEco Profiler Frame模板抓取应用页面切换的Trace信息，根据Trace关键字H:ABILITY\_OR\_PAGE\_SWITCH确定页面切换的过程，查看该过程应用主线程Trace信息，发现主线程在该过程并没有多次触发绘制送显，因此推测不是应用主线程卡顿导致的页面切换卡顿，而是Render Service卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/k2oBThmgTxWJVDbT9BMrSQ/zh-cn_image_0000002628554944.png "点击放大")
2. 查看render\_service线程，发现渲染服务线程在接收Vsync信号处理时，长时间处于PostAndWait阶段（175ms左右），在等待RsUniRenderThread子线程唤醒。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/JdZGqM7LRFeBnd7-Vx1WrA/zh-cn_image_0000002628395044.png "点击放大")

   而RsUniRenderThread子线程在执行绘制时，应用窗口的绘制时长时间处于Running状态，时长达到了179ms，同时有创建8191x7176大小的纹理，推测是页面负载过高，并且与图片有关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/gto1GmpdSWSRFpugNtFxbw/zh-cn_image_0000002658914263.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/aETLCKj1RWmZxgZaUjBfQA/zh-cn_image_0000002658794311.png "点击放大")
3. 使用ArkUI Inspector抓取页面的布局，发现页面层级不深、布局不复杂，Image组件的图片为http图片资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/D512BV-3S_C3KPPcLxBUHw/zh-cn_image_0000002628554946.png "点击放大")

   将图片下载后查看得知该图片的分辨率达到了10800\*7176，图片分辨率较大，超出了Image组件DMA策略生效的图片大小范围，在绘制时会出现纹理上传，导致渲染服务绘制耗时，出现卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/kFT7KhVAQzCIC1SEgmlcfw/zh-cn_image_0000002628395046.png "点击放大")

## 分析结论

应用页面的资源图分辨率过大，在绘制时会进行纹理上传，绘制耗时多，导致页面切换卡顿。

## 修改建议

* 调整大图的宽度、高度像素点在8192范围内。
* [设置图片解码尺寸](../harmonyos-guides/arkts-graphics-display.md#设置图片解码尺寸)降低图片的分辨率。
