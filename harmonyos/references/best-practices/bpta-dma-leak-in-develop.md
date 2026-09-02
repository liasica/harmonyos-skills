---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dma-leak-in-develop
title: 开发态快速定位DMA泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位DMA泄漏
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:ca5d42e5c009049b3e4bb42797c28bb15098a8c8d0de714b4fe7fdc00bbec055
---

## 概述

在HarmonyOS中，DMA内存是指由DMA驱动分配的、支持多进程和多硬件之间共享访问的RAM内存（特别说明，DMA内存与ION内存是同一概念）。在HarmonyOS系统中，应用一般通过系统开放的ArkUI、图形和媒体的相关接口间接使用DMA内存。例如ArkUI中的XComponent、Image和Web组件，图形相关的ImageNative和NativeBuffer，AvCodec的编解码，图片的PixelMap接口等。当应用占用的DMA内存超过阈值时，即认为应用发生DMA内存泄漏。

本文将通过高频泄漏场景和DMA内存泄漏分析案例快速定位应用DMA泄漏的问题。

## 常见泄漏场景

应用通常通过系统提供的ArkUI、图形和媒体接口间接使用DMA内存，常见场景包括：

* **Image控件泄漏或者缓存过多导致内存泄漏**

  应用程序中的Image控件未正确释放DMA内存，引发DMA内存泄漏，最终引发系统图像服务异常或应用崩溃。
* **ArkWeb控件泄漏导致内存泄漏**

  应用程序中的ArkWeb控件未正确管理ArkWeb控件的生命周期或缓存策略，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
* **使用Surface的NDK接口分配内存未释放导致内存泄漏**

  应用程序中，Surface的NDK接口分配的DMA内存未释放，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
* **XComponent组件泄漏或者缓存过多导致内存泄漏**

  应用程序中的XComponent组件未正确释放DMA内存，或组件缓存无限增长，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
* **视频软硬编解码器API接口使用不当导致内存泄漏**

  应用程序中的视频软硬编解码器API接口使用不当导致视频解码/编码时分配的DMA内存未释放，引发DMA内存泄漏，最终引发系统异常或应用崩溃。

## 标准化排查流程

1. 复现与日志获取：使用DevEco Profiler的Allocation模板开启统计模式录制泄漏场景，重复3-5次操作疑似泄漏场景以复现问题。

2. 识别泄漏点： 点击All Anonymous VM中的VM:ION子泳道，在下方详情Call Tree标签页中选择Created&Existing，查看内存占比较高的调用栈。

3. 分析调用栈：优先在调用栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。

4.代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。

* 业务逻辑未发现异常：[查看进程中DMA内存信息](bpta-dma-leak-in-develop.md#section53218913389)并结合DMA内存信息分析。
* 业务逻辑存在异常：修改相关代码。

5.修复与验证：修改代码后，重复步骤1，确认内存曲线回归平稳。

标准化排查流程整体流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YBRj_pXKR3C952iGKg_4KA/zh-cn_image_0000002675100563.jpg "点击放大")

## DMA内存泄漏分析案例

### 案例背景

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Graph内存占用呈现“阶梯式持续增长”趋势。

**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Graph曲线，呈现出典型的“阶梯式增长”，确认存在DMA内存泄漏。

* **Graph子泳道**：应用使用的DMA内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/j2V48dCXTzKy4Oxj5R2hWQ/zh-cn_image_0000002675020711.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wTe5Ep_VTVu2TtNBrOUVew/zh-cn_image_0000002645100760.png "点击放大")

### 分析流程

1. **通过Allocation录制泄漏场景**

   1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息以及调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/DgMDizywRSerCGKa8dlgFQ/zh-cn_image_0000002644940858.png)

   2. 开启统计模式，可以打开JS栈记录和异步栈记录开关。由于DMA内存的分配频率相比于NativeHeap的Malloc更低，因此可关闭Malloc采集，减少对DMA内存分析的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/A5iqwMaeTua6Rp9LrufKnw/zh-cn_image_0000002675100565.png "点击放大")

   3. 点击按钮启动录制并复现问题场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/1y1Ylc7oSgeoQef9BYs4iA/zh-cn_image_0000002675020713.png "点击放大")
2. **查看DMA内存调用栈**

   1. 框选All Anonymous VM中的VM:ION子泳道。

   * VM:ION子泳道：用于显示DMA内存分配数据。

   2. 在下方详情区的“Statistics”页签中选择Created & Existing。

   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/vKH0RwwiQ2Som6OSi9zlag/zh-cn_image_0000002645100762.png "点击放大")

   3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/q8sHO3vBQGuABcgnLqPPJA/zh-cn_image_0000002644940860.png "点击放大")
3. **分析DMA内存调用栈**

   优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码中缓存了PixelMap，但未调用release()方法释放内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/kcejHaW7Q-SwDKo8O5MD0Q/zh-cn_image_0000002675100567.png "点击放大")

### 优化修复

1. 修改代码，增加image.PixelMap的release()方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复3-5次操作泄漏场景。
4. 验证结果：
   * 每次页面退出后，内存曲线回落至基线。
   * 泄漏问题已修复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/x2Zv1e_STxutZCdNfPnvkA/zh-cn_image_0000002675020715.png "点击放大")

## 附录：查看进程中DMA内存信息

1. 查找进程pid。启动应用进程，选择Profiler工具 → 选择设备与应用进程，即可看到进程pid。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/hONcX3YoTnG5Jn6SxqDjYw/zh-cn_image_0000002645100764.png "点击放大")

2. 获取到pid后，在终端中执行hdc shell，然后执行命令hidumper --mem pid --show-dmabuf（[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)）对比出现DMA泄漏前和DMA泄漏后的DMA内存数据。根据buf\_name和leak\_type排查相关组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ex12GNKDSL-tYWB1WWJZ4A/zh-cn_image_0000002644940862.png "点击放大")

获取指定pid的DMA内存详细信息，开发者可以根据DMA内存信息中的buf\_name、leak\_type等列定位可疑泄漏组件。
