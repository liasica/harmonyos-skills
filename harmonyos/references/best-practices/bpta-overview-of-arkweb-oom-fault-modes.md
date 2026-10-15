---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-arkweb-oom-fault-modes
title: ArkWeb V8 OOM故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkWeb OOM故障模式说明 > ArkWeb V8 OOM故障模式概述
category: best-practices
scraped_at: 2026-10-16T07:06:52+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:21a41af502dd4fbb281f19684a696b02310c0f97094680648c20e22ea2983a5c
---

[ArkWeb（方舟Web）](../harmonyos-guides/arkweb.md)是HarmonyOS新一代Web组件内核，为开发者提供原生Web服务能力，旨在让Web内容成为鸿蒙应用的一部分，如同使用原生控件般自然、高效。ArkWeb是基于Chromium内核深度定制的鸿蒙原生Web容器，V8是其内部用于执行JavaScript代码的核心引擎之一。

本章提供ArkWeb V8引擎OOM（Out Of Memory）问题的分析与定位实践文章，旨在系统梳理典型故障场景与诊断方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [JS对象长期被JS持有导致内存泄漏故障模式说明](bpta-arkweb-oom-js-object-held-by-js-object.md)：ArkWeb V8引擎通过GC机制保证JS代码执行结束后释放JS对象所占内存，若想在JS代码执行过程中及时释放内存，则需依靠开发者对JS对象生命周期的管理。本文通过两种场景分析JS对象内存占用过高导致引擎OOM的问题，并通过堆快照文件展示这类情况的堆内存特征。

## ArkWeb V8引擎堆内存简介

V8 JavaScript engine（以下简称V8）作为底层JS引擎，其内存划分若干核心区域，如下表所示：

| 区域 | 用途 |
| --- | --- |
| 代码空间 | 存储编译后的字节码与机器码 |
| 堆空间 | 动态分配对象（内存管理的核心区域） |
| 栈空间 | 存储函数调用与原始类型 |

**说明** 

堆空间存放JS源码中创建的对象，是内存泄漏问题的高发区域。

### V8堆内存管理（分代模型）

V8的堆内存管理基于**分代假说**：大多数对象的生命周期较短。基于这一假说，堆内存被划分为新生代和老生代。

**新生代（New Space / Young Generation）**

* **作用**：存放新创建的对象。
* **容量**：默认约1–8MB。
* **特点**：预期对象生命周期短，垃圾回收频率高，速度快。
* **内部结构**：分为相等的两个半空间（From-Space和To-Space），任意时刻仅一半被使用，另一半用于暂存存活对象。

**老生代（Old Space / Old Generation）**

* **作用**：存放经过多次GC后存活的对象。
* **容量**：默认约1.4GB。
* **特点**：对象存活时间长，GC频率低但资源消耗较大。
* **子区域划分**：老生代进一步细分为多个空间，如Old Pointer Space存放包含指针的对象、Old Data Space存放仅包含原始数据的对象、Large Object Space存放体积超过1MB的大对象、Code Space存放JIT编译后的代码、Map Space存放对象布局结构信息。

### 垃圾回收算法

V8会在满足特定条件时触发GC（垃圾回收）。GC会回收生命周期已结束的JS对象，释放内存。释放的内存将用作下一次对象分配。GC还会将生命周期未结束的JS对象转移到老生代，降低内存碎片。

V8提供了调整GC的参数与配置，可结合业务对内存/性能进行激进优化。

## V8 OOM

当老生代达到容量上限时会触发OOM问题。

这类内存问题通常使用堆导出技术获取堆内存快照，帮助开发者查看OOM时的堆内存使用情况，以便定位OOM问题。

### 堆内存快照

快照格式说明：

**heapsnapshot格式：**业界标准的JS堆内存快照格式，可直接导入Chrome浏览器DevTools进行可视化分析。

**rawheap格式：**为解决heapsnapshot格式导出耗时较长的问题，鸿蒙推出了rawheap格式。可使用[js-rawheap-translator工具](../doccenter-capabilities/js-rawheap-translator.md)解析为heapsnapshot文件。

ArkWeb堆内存快照导出方法：

参考[查询虚拟机堆内存](../doccenter-capabilities/hidumper.md#查询虚拟机堆内存)，使用命令[hidumper](../doccenter-capabilities/hidumper.md) --arkweb-js pid [--raw]导出内存快照。其中--arkweb-js表示执行arkweb js堆dump，pid为应用进程ID，--raw为非必选参数，表示导出rawheap格式文件，如果使用了该选项，可使用[js-rawheap-translator工具](../doccenter-capabilities/js-rawheap-translator.md)将rawheap格式文件转换为heapsnapshot格式文件。不使用该选项，默认导出heapsnapshot格式文件。

堆内存快照分析方法：

得到heapsnapshot格式文件后，参考[devtools通用分析手段](../doccenter-capabilities/use-jsvm-about-analyze-memory-usage.md)，导入Chrome浏览器DevTools进行可视化分析。
