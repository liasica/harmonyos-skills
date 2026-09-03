---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-dmaleak-fault-mode-overreview
title: DMA内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > DMA内存泄漏故障模式说明 > DMA内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:480fdd04720cff33ff3c753f45ec18adf98e9c9aa126f55ee2a81385f2e39d3e
---

## 概述

系统会对应用DMA内存进行监控，如果应用DMA内存使用超过阈值，并且整机处于低内存状态时，系统会抓取DMA内存基础维测日志并管控此应用。本文旨在为开发者介绍系统的DMA内存泄漏检测机制，并提供开发态与运维态的问题分析思路。此外，本文还提供了DMA内存泄漏问题分析与定位实践系列文章，旨在系统梳理泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [DMA内存泄漏故障模式说明](bpta-stability-app-dmaleak-fault-mode.md)：在应用开发中，Image与ArkWeb等组件的误用易引发DMA内存持续攀升，系统认定应用发生内存泄漏后将触发管控机制，最终导致应用闪退等稳定性问题。此文为开发者介绍了DMA内存泄漏的几种可能根因，并结合应用进行Image、ArkWeb等组件使用不当导致DMA内存泄漏的案例展示了DMA内存泄漏的开发态和运维态分析思路。

## DMA内存泄漏基本概念与故障检测机制

### DMA内存及泄漏概念介绍

在HarmonyOS上，DMA内存是指DMA驱动分配的，支持在多进程、多硬件之间共享访问的RAM内存。应用一般通过系统开放的ArkUI、图形和媒体的相关接口间接使用DMA内存，一些常见的组件与接口如下：

* ArkUI：[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)、[Image](../harmonyos-references/ts-basic-components-image.md#image-1)、[ArkWeb（方舟Web）](../harmonyos-guides/arkweb.md)。
* 图形：[Image Kit（图片处理服务）](../harmonyos-references/image-api.md)、[ArkGraphics 2D（方舟2D图形服务）](../harmonyos-guides/arkgraphics-2d.md)。
* 媒体：[AVCodec Kit（音视频编解码服务）](../harmonyos-guides/avcodec-kit.md)。

如果驱动或应用层未正确释放引用计数或未解除映射，系统则无法回收或重新利用DMA内存。系统检测到应用DMA内存值大于一定阈值时，会判定应用进程发生了DMA内存泄漏故障，上报DMA内存泄漏事件。

**说明** 

在HarmonyOS上，DMA内存与ION内存都代表同一种类型的内存，不做专门区分。

### DMA内存大小获取方式

开发者可以通过[GraphicsMemorySummary()](../harmonyos-references/js-apis-hidebug.md#graphicsmemorysummary21)接口读取当前应用进程的DMA内存占用，和预期DMA内存占用比较，判断应用自身是否发生了DMA内存泄漏故障。

### DMA内存泄漏检测原理

系统通过周期轮询和关键操作（如DMA内存分配）触发两种方式，实时监控整机DMA内存的总使用量。

当整机DMA内存占用超过预设的系统阈值时，系统会启动内存泄漏排查流程，对当前所有持有DMA内存的应用进程进行分析。若某一应用的DMA内存占用超出其单应用阈值，系统则判定其发生内存泄漏。

对于已确认泄漏的问题应用，系统将采取主动管控策略。该策略的触发需同时满足以下两个前置条件：

1. 应用自身泄漏：目标应用的DMA内存占用已超过其合理使用上限（即单应用阈值）。
2. 整机资源紧张：整机进入低内存状态。

只有在上述条件均成立时，系统才会管控此问题应用，以保障整机稳定性，避免因资源耗尽导致重启、冻屏等严重故障。

**说明** 

1. 低端设备的内存总量较小，更容易进入低内存状态。

2. 整机压力影响因素较多，应用需要关注自身内存是否超阈值，是否超出合理使用范围，只要超出或接近阈值，就需要进行相关优化，提升应用保活成功率，保证用户使用体验。

## 故障感知

如果需要感知应用是否发生过DMA内存泄漏故障，开发者可以订阅以下故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，资源泄漏故障事件中包含应用申请的DMA内存大小等内存信息，同时会附带DMA内存基础维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，如果应用发生了DMA内存泄漏故障，那么应用终止事件的终止原因为ResourceLeak(IonLeak)或者DmaKiller。开发者可以通过监听此事件，快速判断本次发生的故障类型，也可以与其他应用终止事件汇总分析此类故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)感知应用的DMA内存泄漏问题，当泄漏类型为ion\_memory时，表明应用进程发生了DMA内存泄漏。开发者也可通过此事件的external\_log字段获取到DMA内存泄漏的维测日志路径，并根据[运维态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section10889164472315)对获取的维测日志进行分析。

以下为发生了DMA内存泄漏故障后，应用收到的资源泄漏事件回调示例：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"616930575450354120","bundle_name":"com.example.lk","bundle_version":"1.0.0","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1779972816408_31230.log"],"level":"warning","log_over_limit":false,"memory":{"gpu":0,"ion":3913456,"pss":45747,"rss":103992,"sys_avail_mem":3894272,"sys_free_mem":1106888,"sys_total_mem":11892820,"vss":45468472},"page_switch_log":"[\"/data/storage/el2/log/page_switch/snapshot/page_switch-com.example.lk-1-1-20260528205336400.log\",\"/data/storage/el2/log/page_switch/snapshot/page_switch-com.example.lk-1-2-20260528205336400.log\"]","pid":31230,"resource_type":"ion_memory","time":1779972816400,"uid":20020198}}
```

其中，resource\_type字段的值为ion\_memory，说明本次发生的资源泄漏问题属于DMA内存泄漏问题。external\_log字段的值为/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_1779972816408\_31230.log，开发者可以通过此路径找到DMA内存泄漏故障日志。

### 订阅应用终止事件

开发者可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因。如果终止原因为ResourceLeak(IonLeak)或DmaKiller，说明应用发生了DMA内存泄漏故障。根据不同的管控原因，开发者可以判断本次内存泄漏的严重程度，管控原因的描述与影响如下表所示：

| Reason | 描述 |
| --- | --- |
| DmaKiller | 应用申请DMA内存超过系统前台管控阈值，并且导致整机进入低内存状态时触发的系统管控，通常表现为应用前台闪退。 |
| ResourceLeak(IonLeak) | 应用申请DMA内存超过系统周期检测阈值触发的系统管控，通常表现为应用后台冷启。 |

以ResourceLeak(IonLeak)管控原因为例，应用会收到应用终止事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"616930575450354120","bundle_version":"1.0.1","foreground":false,"reason":"ResourceLeak(IonLeak)","time":1777877700534}}
```

其中，reason字段为ResourceLeak(IonLeak)，foreground字段为false，说明此次应用终止是因为系统周期检测发现应用DMA内存占用超过单应用阈值，触发了系统后台管控。

**说明** 

如果应用在同一个生命周期内触发多个故障，那么这几次故障事件会持有相同的app\_running\_unique\_id，开发者可以根据app\_running\_unique\_id对应用发生的多个故障进行关联。

## 日志规格与日志获取

系统检测到应用发生DMA内存泄漏后，会通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径，并根据[运维态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section10889164472315)对获取的维测日志进行分析。

### 日志规格

对于DMA内存泄漏故障，开发者可以结合以下几种维测日志进行问题分析：

* DMA内存基础维测日志，记录了应用申请DMA内存的详细分布，详细信息可参考[ASHMEM/DMA/GPU/GPU\_RS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)中DMA内存泄漏维测信息。
* DMA内存栈，记录了抓栈期间进程申请的DMA内存的调用栈，详细信息可参考[内存栈](../harmonyos-guides/resource-leak-guidelines.md#内存栈-1)。

### 内存栈日志获取方法

DMA内存泄漏的运维态维测仅包含DMA内存基础维测日志，如果需要进一步定位至代码行，可以使用DevEco Studio获取内存栈日志：通过用户描述、资源泄漏事件中的页面切换信息或流水日志等信息推测故障复现路径，参考[开发态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section796854014215)使用DevEco Studio的Profiler调优功能抓取相关内存栈日志。

## 运维态问题分析方法

开发者可以结合故障日志，对DMA内存泄漏问题进行定界和定位。建议开发者先参考[DMA内存基础日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section170311436201)将问题定界到具体的组件和业务，再通过[内存栈日志获取方法](bpta-stability-dmaleak-fault-mode-overreview.md#section2689241446)抓取内存栈日志并参考[内存栈日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section94641340515)定位至内存泄漏点。

### DMA内存基础日志分析方法

在出现DMA内存泄漏的场景下，开发者可通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)获取DMA内存基础维测日志，并以LOGGER\_MEMCHECK\_PROC\_INFO为关键字检索，得到如下维测日志：

```screen
LOGGER_MEMCHECK_PROC_INFO
MM_DMABUF_INFO
realtime:	2026/05/23 12:00:37
Process 	pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	                                                                exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
xample.dfx_test	28812   	67      	130965504	7899    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	69      	130965504	5397    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	71      	130965504	7900    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	73      	130965504	7901    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	76      	147456  	7902    	28812   	xample.dfx_test	srcImageSize-192x192-pixelMapSize-192x192-streamsize-5386-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	77      	131563520	5398    	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	80      	130965504	8829    	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	82      	130965504	12035   	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	84      	131563520	13450   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	85      	131563520	14508   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	87      	130965504	12037   	37152   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-32188836-mimetype-png	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	90      	131563520	13452   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	92      	131563520	14509   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
xample.dfx_test	28812   	96      	131563520	13453   	1428    	allocator_host	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0       	
......
************ endl ************
```

**说明** 

DMA内存维测中，一行代表申请的一个DMA内存的句柄，ino是dma\_buf唯一的标识。如果遇到两行dma\_buf的ino一致，说明两个DMA句柄指向了同一块dma\_buf，在计算总内存占用的时候要做去重处理。

开发者可以先排查size\_bytes较大或者存在大量重复size\_bytes的DMA内存，筛选出可疑的内存块。系统会按既定规则为每块DMA内存打上内存名（buf\_name）和内存类型（leak\_type）标签，开发者参照下表即可确定可疑内存块与组件的对应关系。为进一步缩短问题定位路径，建议开发者通过相关接口自定义内存名称或类型，并将其与具体的文件、页面或显示组件关联，以便在应用发生泄漏时快速追溯至对应的业务模块。

|  |  |  |  |
| --- | --- | --- | --- |
| **组件/特性** | **内存名（buf\_name）** | **内存类型（leak\_type）** | **应用自定义方法** |
| [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md) | / | xcomponent-type-id  注：type取s(surface)、t(texture)，id取xcomponent id  示例：  xcomponent-s-nodeId\_237  xcomponent-t-nodeId\_238 | [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent10)自定义参数：  示例：在文件file1中，有页面page1，其中组件component1使用了XComponent   ```screen XComponent(value: {id: 'file1_page1_component1', type: XComponentType.SURFACE, libraryname?: 'libxx.so', controller?: ctrl}) ```   则leak\_type显示为xcomponent-s-file1\_page1\_component1 |
| [Image](../harmonyos-references/ts-basic-components-image.md#image-1) | 宽x高-url  覆盖如下三种图片路径：  本地 file://data/xxx/xxxxxx/xxx.png  网络 https://xxxx/xxxxx.png  资源 resource://xxxxxxx.png  示例：  72x72-resource://xxx.webp  72x72-https://xxx.png | pixelmap | 使用Image组件的id自定义：  示例：在文件file1中，有页面page1，其中组件component1使用了Image   ```screen Image(pixelmapDesc).id('file1_page1_component1') ```   则buf\_name显示为id:file1\_page1\_component1。 |
| Web（详见[ArkWeb简介](../harmonyos-guides/web-component-overview.md)） | / | web-type-组件id  注：type为surface和texture、组件id默认为内部的nodeid  示例：  web-surface-1  web-texture-2 | 使用Web组件的id自定义：  示例：在文件file1中，有页面page1，其中组件component1使用了Web   ```screen Web({ src: 'https://xxx/', controller: ctrl }).id('file1_page1_component1') ```   则buf\_name显示为web-surface-file1\_page1\_component1。 |
| ImageSource（详见[图片解码](../harmonyos-guides/image-decoding-arts.md)） | 原图-宽x高-解码后-宽x高-原图文件大小[B]-原图图片类型  注：B代表单位-字节  示例：  srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp  各字段含义解释：  srcImageSize-宽x高：原图分辨率 宽x高  pixelMapSize-宽x高：原图解码后的分辨率 宽x高  streamSize-文件大小：原图文件大小（单位：B）  mimetype-图片类型：原图图片类型（png/webp/jpg/...） | pixelmap | 使用ImageSource解码后的Pixelmap的Arkts接口（[setMemoryNameSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)）和Native接口（[OH\_PixelmapNative\_SetMemoryName()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)）。  示例：  Arkts 在文件file1中，有页面page1，其中组件component1使用了ImageSource：   ```screen pixelmap.setMemoryNameSync('file1_page1_component1') ```   native 在文件file1中，有页面page1，其中组件component1使用了ImageSource：   ```screen char* name = "file1_page1_component1"; OH_PixelmapNative_SetMemoryName(pixelmap, name, strlen(name)); ```   则buf\_name显示为file1\_page1\_component1。 |
| 视频编解码 | 宽x高-协议类型-实例id  注：宽x高是指视频的分辨率，协议类型取值hevc、avc、vvc，实例id为内部生成 | hw-video-编解码类型  注：硬件编解码，编解码类型取值encoder、decoder    sw-video-编解码类型  注：软件编解码，编解码类型取值encoder（手机不支持）、decoder | 暂不支持应用通过API自定义标签。 |
| NativeImage（详见[NativeImage开发指导 (C/C++)](../harmonyos-guides/native-image-guidelines.md)） | / | external |
| NativeBuffer（详见[NativeBuffer开发指导 (C/C++)](../harmonyos-guides/native-buffer-guidelines.md)） |
| NativeWindow（详见[NativeWindow开发指导 (C/C++)](../harmonyos-guides/native-window-guidelines.md)） |

以一份DMA内存为例：

```screen
Process 	      pid     	fd      	size_bytes	ino     	exp_pid 	exp_task_comm	buf_name	                                                                exp_name	buf_type	leak_type	ahost-cpid	ahost-iova	ahost-usage	
com.example.dfx_test  28812   	67      	130965504	7899    	28812   	xample.dfx_test	srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg	mm_heap_helpers	pixelmap	pixelmap	28812   	0       	0
```

开发者可以从中提取出标签信息如下：

* buf\_name：srcImageSize-7008x4672-pixelMapSize-7008x4672-streamsize-3422437-mimetype-jpeg
* buf\_type：pixelmap
* leak\_type：pixelmap

将上述标签与命名规则匹配后，可确认进程com.example.dfx\_test申请了一块130965504字节的DMA内存，进而推断：该应用[使用ImageSource完成图片解码](../harmonyos-guides/image-decoding.md)功能将一张7008×4672的JPEG图片解码为等尺寸的PixelMap，由此产生该DMA内存分配。

### 内存栈日志分析方法

通过[内存栈日志获取方法](bpta-stability-dmaleak-fault-mode-overreview.md#section2689241446)获取到内存栈日志后，开发者可以将内存栈日志导入DevEco Studio中，分析其中可疑的内存调用栈，排查潜在的内存泄漏点。具体操作步骤如下：

1. 单击下图1处导入文件按钮导入内存栈日志。
2. 单击All Anonymous VM下的VM:ION泳道查看DMA内存申请的调用栈，如下图2处。
3. 单击3处Call Trees查看内存申请调用栈。
4. 单击4处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
5. 找到异常申请的内存及其调用栈，如下图5、6处框选的内容。这里建议将Bytes从大到小排序，按照申请大小顺序排查内存调用栈，分析可疑的内存泄漏点。
6. 结合调用栈对代码进行分析，找到泄漏根因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/E3JZRy85TqOiTA7Vc5qfaQ/zh-cn_image_0000002729491141.png "点击放大")

## 开发态问题分析方法

针对开发验证过程中遇到的DMA内存泄漏问题，开发者可借助DevEco Studio的Profiler调优功能或hidumper等工具，在本地复现问题并抓取维测日志进行分析。

### 故障分析工具说明

开发者如果在开发态遇到DMA内存泄漏的问题可以尝试使用以下开发态工具进行分析：

* [hidumper](../harmonyos-guides/hidumper.md)工具：开发者可以使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid --show-dmabuf”命令获取指定pid的内存使用情况，并打印DMA内存详细信息。这里获取到的DMA内存详细信息等效于开发者通过运维态订阅方式拿到的DMA内存泄漏故障日志，执行命令后的输出结果如下：

  ```screen
  -------------------------------[memory]-------------------------------

                               Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
                             Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
                            ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
                   ------------------------------------------------------------------------------------------------------------------------------------------------------
                 GL        1680540              0              0              0        1680540              0              0              0              0              0
              Graph        3534416              0              0              0        3534416              0              0              0              0              0
        ark ts heap           1625           6144              0           1304              0           5992           5992              0              0              0
  arkts-static heap             13            276              0              0              0              0              0              0              0              0
              guard              0              0              0              0              0              0              0              0              0              0
        native heap          34510          37160              0          32652              0          24412          24080          89600          85130           5389
               .hap           1620              0              0           1616              4              0              0              0              0              0
     AnonPage other          97850           5732              8          97640              0          10864          10832              0              0              0
              stack           1256              0              0           1256              0             28             28              0              0              0
                .db            128              0              0            128              0              0              0              0              0              0
                .so          56735          83004          27968          33336           2732           4252            138              0              0              0
                dev             21              0            356             16              0              0              0              0              0              0
               .ttf            379           1496              0              0              0              0              0              0              0              0
     FilePage other          15407           3192           6384          12100           1156              8              0              0              0              0
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
              Total        5465570         137004          34716         180048        5218848          45556          41070          89600          85130           5389

  native heap:
    jemalloc meta:           874            472              0            848              0            520            493              0              0              0
    jemalloc heap:         32372          31492              0          30772              0          23604          23376              0              0              0
         brk heap:          1248           5196              0           1016              0            272            195              0              0              0
        musl heap:            16              0              0             16              0             16             16              0              0              0

  Purgeable:
          PurgSum:0 kB
          PurgPin:0 kB

  DMA:
              Dma:3534416 kB
  Process                pid          fd         size_bytes        ino         exp_pid        exp_task_comm         buf_name        exp_name               buf_type           leak_type
  xample.dfx_test        23338        72         101122048         762         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        76         101122048         763         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        78         101122048         764         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        82         101122048         765         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        96         101122048         766         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        98         101122048         767         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        108        101122048         768         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
  xample.dfx_test        23338        290        13418496          821         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-282
  xample.dfx_test        23338        294        13418496          822         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-311
  xample.dfx_test        23338        305        13418496          823         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-302
  xample.dfx_test        23338        308        13418496          824         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-309
  xample.dfx_test        23338        312        13418496          825         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-320
  ......

  Ashmem:
  Total Ashmem:3372 kB
  ```
* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio的Profiler调优功能对应用进程的内存申请趋势以及内存申请调用栈进行分析，定位出具体泄漏点。更多功能可参考[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

**说明** 

hidumper命令行工具更多用于实时观察应用的内存占用和DMA内存使用详情，无法帮助开发者直接定位到内存泄漏点，更多用于脚本压测。而DevEco Studio的Profiler调优功能不仅能图形化展示应用的内存增长趋势，还可以抓取出录制过程中应用申请的内存和对应的内存调用栈。因此，推荐开发者在开发态分析问题时优先使用DevEco Studio的Profiler调优功能分析DMA内存泄漏问题。

### 故障分析方法

开发者在调试过程中，如果遇到应用闪退或者后台冷启问题，可以在DevEco Studio中找到日志组件如下图1处，再选择应用终止如下图2处，单击3选择应用进程名，筛选出调试应用的历史退出原因，如果原因为“ResourceLeak(IonLeak)”如下图4所示，说明应用在调试过程中发生了DMA内存泄漏故障。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/ZyRvWmyYRHeg-5ingSf8SA/zh-cn_image_0000002729611101.png "点击放大")

确认问题为DMA内存泄漏后，推荐开发者使用DevEco Studio的Profiler工具中的Allocation功能进行分析，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。具体分析步骤如下：

1. 启动录制前先在Allocation的配置页中执行如下图所示的准备工作：单击下图1处录制设置按钮，单击下图2处打开JS栈记录开关，单击下图3处打开异步回栈开关。由于NativeHeap的Malloc频率非常高，可以单击取消勾选4处的Malloc复选框，不抓取应用Malloc内存分配栈，减少对DMA内存分析的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/r7x-9Pg1SBONi9oe0X6zDw/zh-cn_image_0000002699891774.png "点击放大")
2. 启动抓取后，可做正常的用户操作，遍历可疑的泄漏场景。
3. 抓取完成后，结合[内存栈日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section94641340515)定位内存泄漏点。
