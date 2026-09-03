---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-dmaleak-fault-mode
title: 应用DMA内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > DMA内存泄漏故障模式说明 > 应用DMA内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:f875ba34b402f8754e1c6cfbcdeef58cd9ddb60caf37cce62c7fc2ec1b56bc85
---

## 概述

应用进程因为不正确使用Image组件、ArkWeb组件等原因，导致DMA内存过高，系统会判定此应用发生DMA内存泄漏，并管控此应用，导致应用闪退等故障。本文旨在为开发者介绍应用DMA内存泄漏的几种常见根因，并基于案例介绍开发态与运维态的问题分析思路。

### 根因分布

DMA内存资源通常与图像显示等业务有关，一些常见的DMA内存泄漏的根因如下：

* 媒体播放器帧监听未注销：使用AVPlayer或AVRecorder的帧数据输出时，页面退出仅释放播放器实例，未调用off('audioFrameAvailable')等接口注销监听，导致内部缓冲队列无法释放。
* XComponent关联的Native对象未销毁：在ArkUI侧销毁XComponent时，没有同步在napi\_init注册的销毁回调中，调用[OH\_NativeImage\_Release()](../harmonyos-references/capi-native-image-h.md#oh_nativeimage_release)或释放关联的EGLImage/GraphicBuffer。
* 离屏渲染/截图后PixelMap未及时释放：高频调用截图或图片编辑API后，每次产生的新PixelMap对象未调用release()，造成DMA内存积压。
* 组件级Surface创建与销毁不配对：动态创建用于视频预览或扫码的Surface或XComponent时，只创建不销毁，或销毁时机不当。

## 问题分析思路

### 运维态问题分析思路

开发者可以根据[运维态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section10889164472315)对日志中的DMA内存维测信息进行分析，定位至本次DMA内存泄漏的可疑业务或泄漏点。

### 开发态问题分析思路

如果开发者定位后确认是应用DMA内存发生了泄漏，可以按照[开发态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section796854014215)使用DevEco Studio中Profiler工具的Allocation功能来监控应用的内存占用情况和内存占用分布并抓取内存分配栈，以定位DMA内存泄漏的泄漏点。

## 案例分析

为直观展示DMA内存泄漏的问题定位方法，下文结合Image组件缓存过大导致内存泄漏、ArkWeb组件使用不当导致内存泄漏两个负向案例介绍了开发态与运维态下的问题分析过程。

### 案例一：Image组件缓存过大导致内存泄漏

此负向案例为应用创建超大Image资源不释放，系统检测到应用发生DMA内存泄漏后在前台管控此应用，最终造成应用闪退故障。

**运维态问题分析：**

如果开发者在运维态遇到此问题，可以按照如下步骤进行分析：

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，在沙箱中接收到DMA内存泄漏相关的故障日志。
2. 在故障日志中找到关键字“LOGGER\_MEMCHECK\_PROC\_INFO”，并读取数据如下：

   ```screen
   LOGGER_MEMCHECK_PROC_INFO
   MM_DMABUF_INFO
   realtime:	2026/05/23 12:00:37
   Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
   xample.dfx_test	28812   	67      	130965504	7899    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	69      	130965504	5397    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	71      	130965504	7900    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	73      	130965504	7901    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	76      	147456  	7902    	28812   	xample.dfx_test	srcImageSize-192x192-pixelMapSize-192x192-streamsize-5386-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	  	
   xample.dfx_test	28812   	90      	131563520	13452   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	92      	131563520	14509   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	96      	131563520	13453   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   ......
   ************ endl ************
   ```
3. 排查发现当前内存维测中存在大量重复size为“130965504”和“131563520”的DMA内存，并且这些size的内存块共占用超过5GB，因此可以确定这些内存出现泄漏：

   ```screen
   Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
   xample.dfx_test	28812   	69      	130965504	5397    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   xample.dfx_test	28812   	77      	131563520	5398    	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
   ```
4. 根据这些DMA内存的“buf\_name”和“leak\_type”可以确定为PixelMap出现了泄漏，根据规则对“buf\_name”进行匹配，可以确定是[使用ImageSource完成图片解码](../harmonyos-guides/image-decoding.md)功能时发生了泄漏。
5. 仅通过DMA内存标签无法直接定位到具体泄漏点，因此推荐开发者通过[内存栈日志获取方法](bpta-stability-dmaleak-fault-mode-overreview.md#section2689241446)获取DMA内存栈日志后，将内存栈日志导入DevEco Studio参考[内存栈日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section94641340515)定位到DMA内存调用栈如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/qw79YJ02Qk-_O3Za7IBNHA/zh-cn_image_0000002699731888.png "点击放大")
6. 结合代码分析，发现当前应用通过createImageSource()函数申请了超大DMA内存但是未释放，最终导致DMA内存泄漏问题。内存调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/uzRFs7AmQQSYP_SsP8_Q4A/zh-cn_image_0000002729491143.png "点击放大")

**开发态问题分析：**

对于开发态存在的问题，开发者大致能够推断出当前出现DMA内存泄漏的场景，那么可以参考[开发态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section796854014215)抓取DMA内存调用栈如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/17xErXJSQRSzoalp95ibMw/zh-cn_image_0000002729611103.png "点击放大")

结合代码分析，发现当前应用通过createImageSource()函数申请了超大DMA内存但是未释放，最终导致DMA内存泄漏问题。内存调用栈指向的代码段如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/PhYID3HqTwa6cQqjx2Q5Jw/zh-cn_image_0000002699891776.png "点击放大")

### 案例二：ArkWeb组件使用不当导致内存泄漏

此负向案例为应用通过ArkWeb组件渲染时，持续申请超大尺寸图形buffer并循环导入Surface组件，导致DMA内存持续占用无法回收。系统检测到应用发生DMA内存泄漏后在前台管控此应用，最终造成应用闪退故障。

**运维态问题分析：**

如果开发者在运维态遇到此问题，可以按照如下步骤进行分析：

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到DMA内存泄漏相关的故障日志。
2. 在故障日志中找到关键字“LOGGER\_MEMCHECK\_PROC\_INFO”，并读取数据如下：

   ```screen
   *****************************
   LOGGER_MEMCHECK_PROC_INFO
   MM_DMABUF_INFO
   realtime:	2026/06/02 21:31:39
   Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
   xample.dfx_test	52223   	70      	101122048	24041   	51660   	allocator_host	NULL    	mm_heap_helpers	xcomponent	xcomponent-s-surfaceView	1520    	0       	0       	
   xample.dfx_test	52223   	72      	101122048	22100   	51660   	allocator_host	NULL    	mm_heap_helpers	xcomponent	xcomponent-s-surfaceView	1520    	0       	0       	
   xample.dfx_test	52223   	74      	101122048	23399   	51660   	allocator_host	NULL    	mm_heap_helpers	xcomponent	xcomponent-s-surfaceView	1520    	0       	0       	
   xample.dfx_test	52223   	76      	101122048	23400   	51660   	allocator_host	52223   	mm_heap_helpers	xcomponent	xcomponent-s-surfaceView	1520    	0       	0       	
   xample.dfx_test	52223   	551     	13418496	23460   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-391	1520    	0       	0       	
   xample.dfx_test	52223   	561     	13418496	23461   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-356	1520    	0       	0       	
   xample.dfx_test	52223   	563     	13418496	24098   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-365	1520    	0       	0       	
   xample.dfx_test	52223   	573     	13418496	24103   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-392	1520    	0       	0       	
   xample.dfx_test	52223   	575     	13418496	24104   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-390	1520    	0       	0       	
   xample.dfx_test	52223   	579     	13418496	23464   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-383	1520    	0       	0       	
   xample.dfx_test	52223   	595     	13418496	23465   	1301    	allocator_host	52223   	mm_heap_helpers	last_buffer	web-surface-401	1520    	0       	0       	
   xample.dfx_test	52223   	597     	13418496	23466   	1301    	allocator_host	NULL    	mm_heap_helpers	last_buffer	web-surface-329	1520    	0       	0       	
   ************ endl ************
   ```
3. 排查发现当前内存维测中存在大量重复size为“101122048”和“13418496”的DMA内存，并且这些size的内存块共占用超过2.5GB，因此可以确定这些内存出现泄漏：

   ```screen
   Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
   xample.dfx_test	52223   	102     	101122048	5702    	51660   	allocator_host	NULL    	mm_heap_helpers	xcomponent	xcomponent-s-surfaceView	1520    	0       	0  	
   xample.dfx_test	52223   	597     	13418496	23466   	1301    	allocator_host	NULL    	mm_heap_helpers	last_buffer	web-surface-329	1520    	0       	0    	
   ```
4. 根据这些DMA内存的“buf\_name”和“leak\_type”与DMA命名规则进行匹配，确定是ArkWeb组件发生了泄漏。开发者后续可以通过排查使用ArkWeb组件的业务，找到DMA内存泄漏点。
5. 通过[内存栈日志获取方法](bpta-stability-dmaleak-fault-mode-overreview.md#section2689241446)获取内存调用栈后，按照[内存栈日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section94641340515)找到可疑内存块及其调用栈如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/M7-WMStrS5qeDL77-HMsTA/zh-cn_image_0000002699731890.png "点击放大")
6. 结合代码分析，发现应用通过RequestBufferBySurfaceId()函数拿到JS层下发的ArkWeb组件相关的SurfaceId，并申请了5个尺寸为5000×5000的超大buffer并循环导入到Surface组件中进行渲染，最终导致应用整体DMA内存冲高无法回落。内存调用栈指向的代码段如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/HK-Pndl4QJesNccdD9YTSg/zh-cn_image_0000002729491145.png "点击放大")

**开发态问题分析：**

对于开发态存在的问题，如果开发者大致能够推断出泄漏问题发生的场景，并且在问题复现过程中，发现当前allocation中DMA内存增长趋势最快，那么可以参考[开发态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section796854014215)抓取DMA内存调用栈如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/p2oxsp9XTTaw88jC4hj-Fw/zh-cn_image_0000002729611105.png "点击放大")

结合代码分析，发现应用通过RequestBufferBySurfaceId()函数拿到JS层下发的ArkWeb组件相关的SurfaceId，申请了5个尺寸为5000×5000的超大buffer并循环导入到Surface组件中进行渲染，最终导致应用整体DMA内存冲高无法回落。内存调用栈指向的代码段如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/S1T1wMEwQxW1XNdsfCWz4w/zh-cn_image_0000002699891778.png "点击放大")

## 修复建议

### Image组件泄漏或者缓存过多

1. 确保图片资源对象显式释放。
2. 图片切换前先解绑旧资源。
3. 实现有上限的图片缓存策略。
4. 避免静态/长生命周期对象持有图片。

### ArkWeb组件泄漏

1. 避免全局变量/全局Map/单例容器直接存ArkWeb实例，推荐使用WeakRef弱引用存储。
2. 如果Web注册了事件回调，要在销毁前统一解绑监听，闭包会隐性持有Web对象，阻断GC回收与内核析构。
3. 路由/页面缓存列表及时清理废弃Web引用，不长期挂在页面栈中。

### 直接使用Surface的NDK接口分配内存没有释放

如下接口务必配对使用：

1. [OH\_NativeWindow\_NativeWindowRequestBuffer()](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_nativewindowrequestbuffer)与[OH\_NativeWindow\_NativeWindowFlushBuffer()](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer)配对。
2. 当[OH\_NativeWindow\_NativeWindowFlushBuffer()](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_nativewindowflushbuffer)执行失败时，可在异常处理流程中使用[OH\_NativeWindow\_NativeWindowAbortBuffer()](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_nativewindowabortbuffer)归还请求的Buffer到Buffer队列。
3. [OH\_NativeBuffer\_Alloc()](../harmonyos-references/capi-native-buffer-h.md#oh_nativebuffer_alloc)与[OH\_NativeBuffer\_Unreference()](../harmonyos-references/capi-native-buffer-h.md#oh_nativebuffer_unreference)配对。
