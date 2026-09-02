---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes
title: JSVM OOM故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > JSVM OOM故障模式说明 > JSVM OOM故障模式概述
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:447259c305562308407125fd17d17753aab0e1f0428dac5013f6f8a1c4404e96
---

HarmonyOS JSVM-API（详细参考：[JSVM-API简介](../harmonyos-guides/jsvm-introduction.md)）基于标准JS引擎提供了一套稳定的API，支持创建和销毁引擎、执行JS代码、JS与C++的交互等关键功能，可在应用运行期间直接执行动态加载的JS代码。此外，可将对性能和底层系统调用有较高要求的核心功能用C/C++实现，并将C++方法注册到JS侧，从而在JS代码中直接调用，以提高应用执行效率。

本章提供了使用JSVM-API过程中引发JS引擎OOM（Out Of Memory）问题的分析与定位实践系列文章，旨在系统梳理典型故障场景与诊断方法，引导开发者在编码中建立良好的内存使用习惯。共有如下两篇：

* [JS对象被Native持有导致内存泄漏故障模式说明](bpta-jsvm-oom-js-object-held-by-native.md)：JSVM-API允许开发者通过创建引用、作用域等方式管理JS对象的生命周期，需合理使用这些接口，避免应用运行过程中产生过高的内存峰值。本文列举了五种JSVM-API错误使用的场景，分析JS对象被Native侧引用导致内存不及时释放的问题，并通过堆快照文件展示这些场景的堆内存特征。
* [JS对象长期被JS持有导致内存泄漏故障模式说明](bpta-jsvm-oom-js-object-held-by-js-object.md)：JS引擎通过GC机制保证JS代码执行结束后释放JS对象所占用的内存，若想在JS代码执行过程中及时释放内存，需依靠开发者对JS对象生命周期的管理。本文通过两种场景分析JS对象内存占用过高导致引擎OOM的问题，并通过堆快照文件展示这类情况的堆内存特征。

## JSVM-API JS引擎堆内存简介

JSVM-API引入开源项目V8 JavaScript engine（以下简称V8）作为底层JS引擎，其内存划分为多个核心区域，如下表所示：

| 区域 | 用途 |
| --- | --- |
| 代码空间 | 存储编译后的字节码与机器码 |
| 堆空间 | 动态分配对象（内存管理的核心区域） |
| 栈空间 | 存储函数调用与原始类型 |

**说明** 

堆空间存放JS源码中创建的对象，是内存泄漏问题的高发区域。

### V8堆内存管理（分代模型）

V8的堆内存管理基于**分代假说**：大多数对象的生命周期较短。基于这一假设，堆内存被划分为新生代和老生代两大区域。

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

V8会在满足特定条件时触发**垃圾回收**，回收已结束生命周期的JS对象，释放内存，以供后续分配；将未结束生命周期的JS对象转移到老生代，降低内存碎片。

V8提供调整GC的参数与配置，可结合业务对内存或性能进行激进优化。

## OOM

当老生代到达容量上限时会产生OOM问题。

这类内存问题通常使用堆导出技术导出堆内存快照，让开发者能够看到OOM时的堆内存使用情况，辅助定位OOM问题。

### 堆内存快照

JSVM-API提供了几种堆内存导出的方式和调试方法：

1. 参考[JSVM-API调试&定位](../harmonyos-guides/jsvm-debugger-cpuprofiler-heapsnapshot.md)方法，利用V8原生的堆导出能力，导出Heap Snapshot格式堆快照。

   **说明** 

   这种方式导出较大堆内存快照时的耗时较长，可能会被HarmonyOS认定为应用卡死导致导出失败。
2. 调用JSVM-API [OH\_JSVM\_TakeRawHeapSnapshot()](../harmonyos-references/capi-jsvm-h.md#oh_jsvm_takerawheapsnapshot)导出Raw Heap格式的堆快照。
3. 通过JSVM-API [OH\_JSVM\_SetHeapThresholdCallback()](../harmonyos-references/capi-jsvm-h.md#oh_jsvm_setheapthresholdcallback)与[OH\_JSVM\_TakeRawHeapSnapshot()](../harmonyos-references/capi-jsvm-h.md#oh_jsvm_takerawheapsnapshot)的配合，在堆内存达到设定的堆内存水线时导出堆内存快照。
4. 通过[hidumper](../harmonyos-guides/hidumper.md)命令导出某个进程的Heap Snapshot或Raw Heap格式的堆快照。
