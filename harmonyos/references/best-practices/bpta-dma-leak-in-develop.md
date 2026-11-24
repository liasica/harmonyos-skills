---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dma-leak-in-develop
title: 开发态快速定位DMA泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位DMA泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:599ee13ff8486204a94a02ae952bf967d49b16bf69354dde61f9d3a373f8ab95
---

## 概述

在HarmonyOS中，DMA内存是指由DMA驱动分配的、支持多进程和多硬件之间共享访问的RAM内存（特别说明，DMA内存与ION内存是同一概念）。应用一般通过系统开放的ArkUI、图形和媒体的相关接口间接使用DMA内存。例如ArkUI中的XComponent、Image和Web组件，图形相关的ImageNative和NativeBuffer，以及AvCodec的编解码，图片的PixelMap接口等。当应用占用的DMA内存超过阈值时，即认为应用发生DMA内存泄漏。

本文将通过高频泄漏场景和DMA内存泄漏分析案例快速定位应用DMA泄漏的问题。

## 常见泄漏场景

应用通常通过系统提供的ArkUI、图形和媒体接口间接使用DMA内存（详见：[应用DMA内存泄漏故障模式说明](bpta-stability-app-dmaleak-fault-mode.md)），常见场景包括：

* **Image控件泄漏或缓存过多**

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

1. 复现与日志获取：使用DevEco Studio Profiler的Allocation模板开启统计模式录制泄漏场景，重复3-5次操作疑似泄漏场景以复现问题。

2. 识别泄漏点：点击All Anonymous VM中的VM:ION子泳道，在下方详情Call Tree标签页中选择Created & Existing，查看内存占比较高的调用栈。

3. 分析调用栈：优先在调用栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。

4.代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。

* 业务逻辑未发现异常：参考[附录：查看进程中DMA内存信息](bpta-dma-leak-in-develop.md#section53218913389)并结合DMA内存信息分析。
* 业务逻辑存在异常：修改相关代码。

5.修复与验证：修改代码后，重复步骤1，确认内存曲线回归平稳。

标准化排查流程整体流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/z49wkJ9HQn-GYgKCaTFpZw/zh-cn_image_0000002675100563.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F5ED2E85A3E8FC241CE164B5302F2668F2174B7D063950A8643C0101E96A816 "点击放大")

## DMA内存泄漏分析案例

### 案例背景

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Graph内存占用呈现“阶梯式持续增长”趋势。

**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Graph曲线，呈现出典型的“阶梯式增长”，确认存在DMA内存泄漏。

* **Graph子泳道**：应用使用的DMA内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/LN1QW10TRpyhoszENdwy5g/zh-cn_image_0000002675020711.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EA5C576B31BB9CC58FD3198B651C738487FDC18F3EFE724E1B655ED809D8F0C "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/sxYygJ0QRymr29K9UAdFHA/zh-cn_image_0000002645100760.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE586238251CB390B1ABEA4D57047BB4CB7ED42A3033B7AED47B19A1EDDFC34E "点击放大")

### 分析流程

1. **通过Allocation录制泄漏场景**

   1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息以及调用栈信息。堆内存信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/gM4a-k-xSOCM6lA1LcFbuw/zh-cn_image_0000002644940858.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBAF9F062A0482A6226B1831DF95407A29D94EB6654669F9356B4507C7D13A5A)

   2. 开启统计模式，可以打开JS栈记录和异步栈记录开关。由于DMA内存的分配频率相比于NativeHeap的Malloc更低，因此可关闭Malloc采集，减少对DMA内存分析的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/tFCZ-VdkQJi_HEf2feegOw/zh-cn_image_0000002675100565.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4B6A7DB1976C2FB321E4D13CEC02CFC9BC46DAF9CF0E6888C55D094BB98087B "点击放大")

   3. 点击按钮启动录制并复现问题场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/JXf4N1IQQBCnLKueCwomPw/zh-cn_image_0000002675020713.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=51DC5185B60ED07B327189C7C64258C22359DF91E5AEF0B46AC69323D47EBCA9 "点击放大")
2. **查看DMA内存调用栈**

   1. 框选All Anonymous VM中的VM:ION子泳道。

   * VM:ION子泳道：用于显示DMA内存分配数据。

   2. 在下方详情区的“Statistics”页签中选择Created & Existing。

   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/G8znRbiAQziqf9LoPSmTqA/zh-cn_image_0000002645100762.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFFEC12F2870359D64BAF2280F60019A818987774F2D48C29DD8F0C21EFB17CA "点击放大")

   3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/ekeBQO81TXGx-HPDrqbeNA/zh-cn_image_0000002644940860.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=011157DF6707BBCA78D7E5CDEEF869D80FF4A6C6A30A6C76ED8B4BB911D66B2B "点击放大")
3. **分析DMA内存调用栈**

   优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码中缓存了PixelMap，但未调用release()方法释放内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/iwmif9bmTUebjdmwf-92XQ/zh-cn_image_0000002675100567.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1C309C8DDB3E23191D8E5B701525A4E1FC38580B0279B7D108C90FF6864250F "点击放大")

### 优化修复

1. 修改代码，增加image.PixelMap的release()方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复3-5次操作泄漏场景。
4. 验证结果：
   * 每次页面退出后，内存曲线回落至基线。
   * 泄漏问题已修复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/TEmaFFWtRJacmcf3F1iP4Q/zh-cn_image_0000002675020715.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE474C394BA2626806116180A3F97ED8A728D9EB8C5725DC18E7A96152763EB9 "点击放大")

## 附录：查看进程中DMA内存信息

1. 查找进程pid。启动应用进程，选择Profiler工具 → 选择设备与应用进程，即可看到进程pid。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/3Fn8D37-QySiuF7SyvIuig/zh-cn_image_0000002645100764.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C300E0A820EF8D4AF9526AAEDE98523CC208E11AC0F61AC4C330E4BD48B24710 "点击放大")

2. 获取到pid后，在终端中执行hdc shell，然后执行命令hidumper --mem pid --show-dmabuf（[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)）对比出现DMA泄漏前和DMA泄漏后的DMA内存数据。根据buf\_name和leak\_type排查相关组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ejoA1qhTQgeZriSi0LD84w/zh-cn_image_0000002644940862.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8D8AE24C9B6D4ECC2C2F99BBBA2A7E75D4FB57073D319E7420331D2DC396317 "点击放大")

获取指定pid的DMA内存详细信息，开发者可以根据DMA内存信息中的buf\_name、leak\_type等列定位可疑泄漏组件。
