---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-arkts-memory-leaks-overview
title: ArkTS内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkTS内存泄漏故障模式说明 > ArkTS内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:a175cca868bba42f5e6265a434e240109d7b0060e756c840bcb3f89307a609dc
---

## 概述

本文系统介绍了ArkTS应用开发中的OOM（Out of Memory，内存溢出）问题场景及内存泄漏分析方法，涵盖核心概念、内存快照工具原理及使用技巧。本文提供ArkTS OOM问题的分析与定位实践系列文章，旨在系统梳理典型故障场景与问题分析方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [GlobalHandle类型内存泄漏故障模式说明](bpta-stability-memleak-arkts-globalhandle-mode.md)：ArkTS在Native侧通过napi\_create\_reference()等方式创建强引用来管理ArkTS对象，对应全局句柄GlobalHandle。开发者需合理使用GlobalHandle，避免因生命周期管理异常导致ArkTS对象内存泄漏。文章列举了五种被GlobalHandle根节点持有导致的内存泄漏场景，介绍分析步骤并提供对应案例。
* [LocalHandle类型内存泄漏故障模式说明](bpta-stability-memleak-arkts-localhandle-mode.md)：ArkTS在Native侧通过napi\_open\_handle\_scope()/napi\_close\_handle\_scope()来管理napi\_value的生命周期，对应局部句柄LocalHandle。开发者需合理使用napi\_open\_handle\_scope()和napi\_close\_handle\_scope()来管理napi\_value的生命周期，避免因生命周期管理异常导致ArkTS对象内存泄漏。文章列举了四种创建LocalHandle的常用方法，介绍分析步骤并提供对应案例。
* [VMRoot类型内存泄漏故障模式说明](bpta-stability-memleak-arkts-vmroot-mode.md)：ArkTS虚拟机会在ArkTS堆内存中创建SourceTextModule和GlobalEnv，这部分对象在通常情况下会作为ROOT集常驻在虚拟机中，在内存快照中呈现为VMRoot。文章列举了SourceTextModule持有的模块级对象泄漏和GlobalEnv持有的全局对象泄漏场景，介绍分析步骤并提供对应案例。
* [申请超大对象导致OOM故障模式说明](bpta-stability-memleak-arkts-huge-mode.md)：若开发者一次性申请超大内存对象，即使对象生命周期管理合理，仍可能因短时间内申请内存超过堆上限导致内存溢出。文章介绍开发者一次性申请超大内存导致ArkTS OOM故障的场景，介绍分析步骤并提供对应案例。

## ArkTS内存相关概念介绍

在鸿蒙应用进程中，ArkTS内存由一个SharedHeap和多个LocalHeap组成。每个ArkTS线程拥有独立的LocalHeap，用于存储线程私有对象；所有ArkTS线程共享一个SharedHeap，用于存放ArkTS共享数据。这种设计在保障线程隔离性的同时，进一步提供共享数据能力提升数据传输效率。

方舟虚拟机（ArkVM）采用标记-清除/压缩算法进行[GC垃圾回收](../harmonyos-guides/gc-introduction.md)，高效回收不再使用的内存。GC基于可达性分析算法，从根节点GC Root开始遍历，标记所有从GC Root可达的对象为“存活”状态。在清除阶段，GC扫描整个内存堆，将未标记为存活的对象视为垃圾对象，并释放其占用的内存空间。

在实际开发中，业务结束后存在无法正常释放的ArkTS对象，即内存泄漏。内存泄漏持续占用空间导致剩余内存递减，难以满足后续业务分配需求，最终可能触发ArkTS OOM（应用进程因堆内存不足导致无法正常运行的异常状态，常表现为运行时堆耗尽触发的闪退）。

理解上述概念是定位和解决内存问题的前提，开发者需掌握内存堆结构、GC工作基本原理以及内存泄漏与OOM的因果关系，从而在实际开发中有效预防和排查内存异常，保障应用的流畅与稳定。

## ArkTS根节点类型

ArkTS支持多种GC Root类型，通过分析Root类型可定位虚拟机无法回收对象的原因，进而辅助开发者进行内存分析与优化。主要GC Root类型如下：

1. VMRoot类型：虚拟机创建的模块级根节点，主要包括SourceTextModule和GlobalEnv两类。此类根节点本身由虚拟机管理，无需开发者主动释放，但其所引用的对象需要通过断开引用链来释放。
2. LocalHandleRoot/GlobalHandleRoot类型：Handle本质上是Native代码对ArkTS对象的强引用，可防止GC提前回收该ArkTS对象。仅在开发者代码涉及Native交互时才会出现。Handle分为局部引用（LocalHandle）和全局引用（GlobalHandle）：
   * LocalHandle（napi\_value）：在Native代码执行上下文中创建的、作用域较短的引用，通过napi\_handle\_scope管理其作用域。
   * GlobalHandle（napi\_ref）：开发者自行管理生命周期的强引用，生命周期持久。出现内存泄漏时，需重点检查应用是否通过对应接口及时释放napi\_ref。

   **说明** 

   作用域及生命周期管理方法参考[使用Node-API接口进行生命周期相关开发](../harmonyos-guides/use-napi-life-cycle.md)。
3. FrameRoot类型：栈帧根节点，表示对象在栈上创建，或由栈上相关对象持有。当调用某函数且未退出其作用域时，局部变量和函数入参对象均被视为FrameRoot类型根节点。此类节点通常无需开发者特别关注，因为栈展开时对象被标记为不可达，会由 GC 回收，内存即可释放。

关于ArkTS虚拟机内存堆模型及GC回收流程的详细介绍，请参阅[分析ArkTS/JS内存](bpta-arkts-js-memory-analysis.md)。

## ArkTS内存堆OOM概念介绍

基于ArkTS虚拟机内存堆模型，各堆及Space均设有独立内存上限。鸿蒙应用运行期间，若剩余ArkTS内存不足导致申请ArkTS对象失败，应用进程会触发GC回收。在GC回收后，若剩余内存不足仍旧无法申请本次ArkTS对象，即触发堆内存溢出（OOM）导致进程闪退。因此，开发者需关注各内存堆及内部Space的内存上限。

### 虚拟机内存堆大小上限

| 内存堆 | 内存上限 |
| --- | --- |
| LocalHeap | 主线程448MB，子线程（worker/taskpool）768MB |
| SharedHeap | 778MB |
| TotalHeap | 1.5GB |

### 内存堆内部Space大小上限

**LocalHeap**：触发OOM时，默认对触发OOM的线程对应的LocalHeap进行采样。LocalHeap的Space内存上限如下表所示：

| 内存堆 | 内存空间 | 内存上限 |
| --- | --- | --- |
| 主线程LocalHeap | OldSpace+HugeSpace | 350MB左右 |
| NonMovableSpace | 64MB左右 |
| 子线程LocalHeap | OldSpace+HugeSpace | 687MB左右 |
| NonMovableSpace | 64MB左右 |

**SharedHeap**：触发OOM时，默认对触发OOM的线程对应的共享堆对象进行采样，进程级堆快照需要开发者按需设置。SharedHeap的Space内存上限如下表所示：

| 内存堆 | 内存空间 | 内存上限 |
| --- | --- | --- |
| SharedHeap | SharedOldSpace | 350MB左右 |
| SharedHugeSpace | 350MB左右 |
| SharedNonMovableSpace | 64MB左右 |

**说明** 

当SharedOldSpace达到上限且SharedHugeSpace剩余空间大于100MB时，SharedOldSpace可向SharedHugeSpace借用内存，极限情况下上限可达600MB。

虚拟机Heap内部结构请参考[LocalHeap结构](../harmonyos-guides/gc-introduction.md#localheap结构)和[SharedHeap结构](../harmonyos-guides/gc-introduction.md#sharedheap结构)。

**说明** 

Snapshot内存快照中，存放在SharedHeap中的对象类型包括：string、method、JSSharedObject、SharedArray、SharedMap、SharedSet、SharedArrayBuffer，以及代码中使用sendable创建的业务对象。若对象的proto原型为上述基本类型之一，则该对象存放在SharedHeap中。

## Snapshot内存快照检测原理

Snapshot是方舟虚拟机在运行时完整导出虚拟机内存堆中ArkTS对象并生成的结构化数据文件。当前系统支持线程级与进程级两种内存快照。

### 内存快照形式

**线程级内存快照：**包含触发OOM线程的所有ArkTS对象，涵盖该线程LocalHeap对象及SharedHeap中与该线程存在引用关系的对象。

**说明** 

由于SharedHeap溢出时，触发OOM的线程未必是泄漏最严重的线程，且线程级快照中的SharedHeap对象信息可能不完整，此类场景需抓取进程级快照。

**进程级内存快照：**包含整个进程的所有ArkTS对象。导出进程级快照的方法参考[内存快照获取方法](bpta-overview-of-arkts-memory-leaks-overview.md#section9836115155612)。

### 内存快照格式说明

**heapsnapshot格式：**业界标准的JS堆内存快照格式，可直接导入DevEco Studio进行可视化分析。

**rawheap格式：**为解决heapsnapshot格式导出耗时较长的问题，鸿蒙推出了rawheap格式。应用发生ArkTS内存OOM时会自动生成rawheap二进制文件，可使用[rawheap-translator工具](../harmonyos-guides/rawheap-translator.md)解析为heapsnapshot文件，DevEco Studio也支持直接导入rawheap文件。

### 开发态内存快照获取方法

**1.应用OOM时获取**

应用发生ArkTS内存OOM时，系统自动生成rawheap快照文件。开发态可通过hdc命令从设备获取，运维态参考[OOM故障事件订阅方式说明](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)。

**2.通过DevEco Studio获取**

开发者可参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)，在DevEco Studio中通过Profiler-Snapshot功能生成内存快照文件。

**3.通过hidumper命令行工具获取**

开发者可以参考[查询虚拟机堆内存](../harmonyos-guides/hidumper.md#查询虚拟机堆内存)，使用命令hidumper --mem-jsheap pid [-T tid] [--raw]导出内存快照。其中--mem-jsheap表示执行ArkTS堆dump，pid为应用进程ID，-T tid指定进程内线程，--raw表示导出rawheap文件。

**4.进程级快照获取**

使用命令hidumper --mem-jsheap pid --raw --single获取指定进程的进程级rawheap快照文件。

### 运维态内存快照获取方法

**1.通过hidebug接口获取**

开发者可调用[hidebug.dumpJsHeapData()](../harmonyos-references/js-apis-hidebug.md#hidebugdumpjsheapdata9)接口导出heapsnapshot文件，或调用[hidebug.dumpJsRawHeapData()](../harmonyos-references/js-apis-hidebug.md#hidebugdumpjsrawheapdata24)接口导出rawheap文件。

**2.通过****jsLeakWatcher接口获取**

开发者可调用[ohos.hiviewdfx.jsLeakWatcher()](../harmonyos-references/js-apis-jsleakwatcher.md)接口导出heapsnapshot或rawheap快照文件。

**3.通过故障事件订阅获取**

开发者可通过[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)获取崩溃日志或rawheap文件。

**4.进程级快照获取**

开发者可调用[hidebug.setProcDumpInSharedOOM()](../harmonyos-references/js-apis-hidebug.md#hidebugsetprocdumpinsharedoom24)接口开启进程级快照开关，开启后应用在共享堆OOM场景下自动生成进程级rawheap快照文件。

## 开发态内存泄漏分析

### 开发态录制工具

当需要内存优化或排查疑似内存泄漏时，可使用DevEco Studio、hidumper命令行工具[查询虚拟机堆内存](../harmonyos-guides/hidumper.md#查询虚拟机堆内存)等开发态工具导出内存快照进行分析。

### 开发态内存泄漏分析方法

1. **排查泄漏对象：**

在DevEco Studio中打开内存快照文件，按Retained size降序排列内存对象，优先关注占用较大的业务对象。可通过聚类功能确认主要泄漏对象。此外，可对同一应用进程在相同场景下抓取两次快照进行对比，精确定位内存变化。

2. **确认泄漏对象故障模式**：

定位泄漏对象的引用根节点（distance为1），查看其Root类型以确定故障模式。

**内存快照如何查看GC Root类型**：

在Snapshot内存快照中，虚拟节点handle包含四种RootType的虚拟节点信息，对应四种[ArkTS根节点类型](bpta-overview-of-arkts-memory-leaks-overview.md#section14558183832315)。RootType虚拟节点仅代表Root节点类型，Root节点被何种RootType虚拟节点持有，即代表该Root类型。四种RootType虚拟节点中，LocalHandleRoot类型和GlobalHandleRoot类型在API24及之后版本的内存快照中可以查看，VMRoot和FrameRoot在API26及之后版本的内存快照中可以查看。四种RootType虚拟节点如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/994QPaCDQ96HQv8cu0zniQ/zh-cn_image_0000002729464439.png)

3. **进一步确认泄漏根因或堆栈：**

若泄漏对象的根节点类型为VMRoot，需要查看引用链中对象是否重复创建，结合业务通过断开引用链来释放泄漏对象，可参考[ArkTS内存泄漏案例及常见问题](https://developer.huawei.com/consumer/cn/forum/topic/0208195932431565320?fid=0109140870620153026)。

若泄漏对象的根节点类型为LocalHandleRoot/GlobalHandleRoot，可使用HandleRoot泄漏检测工具确认持有泄漏对象的混合堆栈。

### Handle泄漏检测工具使用方法

1. 在DevEco Studio -> Profiler中的Allocation模板中可以使用Handle泄漏检测工具，录制泄漏场景可以获取到快照泄漏对象对应的调用栈信息，精准定位泄漏对象在代码中的调用关系。泄漏检测工具配置步骤如下：

1. 打开DevEco Studio中的Profiler组件，选中下图1处创建Allocation模板。
2. 在过滤泳道中选择添加如下图2处所示ArkTS Snapshot泳道。
3. 单击3处设置录制配置项。
4. 在设置中关闭统计模式，打开录制异步栈，选择如下图4所示LocalHandle/GlobalHandle。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/KywSKeJeSn2nLc4vwOcFww/zh-cn_image_0000002699865068.png "点击放大")

2. 开始录制Allocation会话，操作应用的泄漏场景。

3. 操作应用后结束录制，Allocation录制结束后会同步抓取内存快照。Handle泄漏检测工具分析步骤如下：

1. 单击下图1处查看ArkTS Snapshot泳道。
2. 依据[开发态内存泄漏分析方法](bpta-overview-of-arkts-memory-leaks-overview.md#section12155162055917)分析内存快照的结果，单击泄漏对象的根节点如下图2处。
3. 单击下图3处Native List查看ArkTS对象内存申请调用栈。双击Native List中的调用栈可以跳转至4处对应的完整调用栈。
4. 下图4处显示的Category代表调用栈类别，GlobalHandle会标注Native(G)，LocalHandle会标注Native(L)。
5. 选中下图5处ArkTS Object List，可以看到该调用栈申请的ArkTS对象，单击对应的跳转按钮可以跳转回2处内存快照中对应的ArkTS对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nQ5rUyeBTO6iUe440x29rQ/zh-cn_image_0000002729584399.png "点击放大")

## 运维态内存泄漏分析

### OOM故障事件订阅方式

1. [订阅崩溃事件](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md)：应用可订阅hiAppEvent.event.APP\_CRASH事件回调。该回调无法直接判断是否为OOM，需解析external\_log获取jscrash崩溃日志以确认进程崩溃原因。
2. [订阅资源泄漏事件](../harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts.md)：应用可订阅hiAppEvent.event.RESOURCE\_OVERLIMIT事件回调。当resource\_type字段为js\_heap时，表示发生OOM。通过external\_log可获取OOM快照（rawheap文件）。

### OOM故障日志规格说明

**jscrash崩溃日志**

应用OOM时会产生崩溃日志，重点关注[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)中的几个关键字段。日志中Error name显示故障类型，OOM时显示OutOfMemoryError；Error message显示错误信息，里面会有导致崩溃的申请内存的大小，崩溃的堆类型等信息；Stacktrace表示导致崩溃的故障堆栈信息。崩溃日志示例如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/clKV1iIuTj-mTKYgmSUxGQ/zh-cn_image_0000002699705180.png)

**rawheap文件**

OOM触发后，可在/data/log/reliability/resource\_leak/memory\_leak目录下获取二进制rawheap文件，解析方式如下：

1. **工具转换**：使用[rawheap-translator工具](../harmonyos-guides/rawheap-translator.md)将rawheap解析为heapsnapshot格式。
2. **直接导入**：在DevEco Studio的Profiler模块中，通过[离线导入内存快照文件](../harmonyos-guides/ide-snapshot-basic-operations.md#section6760173514388)功能直接打开rawheap文件。

### 运维态内存泄漏分析方法

1. **排查泄漏对象**：

在DevEco Studio中打开内存快照文件，按Retained size降序排列内存对象，优先关注占用较大的业务对象；可以通过聚类来确认占比较大的泄漏对象。

2. **确认泄漏对象故障模式**：

定位泄漏对象的引用根节点（distance为1），查看其Root类型以确定故障模式。进一步通过泄漏对象的名字、属性名和文件名找到相关业务逻辑和场景。

3. **进一步确认泄漏根因或堆栈**：

通过泄漏对象的名字，属性名和文件名等信息，参考对应故障模式文档，找到相关业务逻辑和场景。若能确认内存泄漏的业务逻辑和场景后，可以尝试场景复现，通过开发态流程分析。

具体分析思路，可参考[ArkTS/JS内存分析思路](bpta-arkts-js-memory-analysis.md#section3880144118139)。
