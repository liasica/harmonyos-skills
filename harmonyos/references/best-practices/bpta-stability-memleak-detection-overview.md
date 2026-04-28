---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-detection-overview
title: 内存泄漏类问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 资源泄漏类问题检测 > 内存泄漏类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:50+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:60d447043eb743d2c55944b51122af271053c1e4756eb8c8875a6ef98b2c26ac
---

## 概述

严格意义上的内存泄漏是指程序在运行过程中，动态分配的内存未能被正确释放，没有任何指针指向这部分内存，导致这部分内存无法再被程序使用，且随着程序运行时间的增加，泄漏的内存会逐渐累积，最终可能导致程序内存耗尽甚至崩溃。广义上的内存泄漏也包含对内存的无限制缓存导致的应用内存超标，这种场景下，内存块的起始地址其实是保存在程序中，并没有丢失，只不过是因为内存块的生命周期过长且堆积过多。内存泄漏检测的目标是上述两种内存泄漏状况都能检查出来。

终端设备上的内存管理机制非常复杂，存在各种不同类型的内存分配器，每种内存分配器有各自管理内存的方式，不过基本上可以分成两大类：用户态内存和内核态内存。

以用户态内存为例，常见的有如下几类：

1. 虚拟机内存

   使用mmap系统调用映射出若干块内存，然后由ArkTS虚拟机自行管理，用于保存虚拟机对象。
2. native内存

   使用malloc或者new分配出来的内存，由jemalloc或者musl之类的分配器来进行管理，本质上也是使用brk或者mmap系统调用从内核映射出来的。
3. 其它专用内存

   比如ArkWeb使用的partition alloc分配器。

上述内存基本都是使用mmap映射出来后，由用户态的内存分配器来进行管理，当然应用也可以将mmap映射出来的内存进行自行管理，即不使用上述默认的这些分配器。

除此之外，还有一类是内核类内存，这类内存一般是由内核或者特定的驱动进行管理的，用于某些特殊专用目的，常见的有如下几类：

1. ashmem（Anonymous Shared Memory）

   即共享内存，常见于在用户态进程间共享和传递大批量数据。
2. dmabuf（ION）

   常用于设备间高效数据传输，比如GPU和显示控制器之间的数据传输。
3. GPU

   GPU驱动管理的内存，比如纹理，Buffer等数据。
4. vmalloc

   适用于大块内存分配，物理地址不连续，但是虚拟机地址连续。
5. slab

   适用于小块内存分配。

在上述内存分配器中，ashmem、dmabuf、GPU这三类内核内存实际上的需求和使用方是应用，一般都是应用控制其生命周期，所以如果出现泄漏，也应该算到应用头上。而其中ashmem、dmabuf这两类内存又是能在进程间共享的，需要多个应用同时释放内存块的引用关系（关闭句柄和unmap地址），内核的内存才能释放。vmalloc和slab一般是在驱动中使用，跟用户态进程关系不大，这类内存会有系统方案管控，不在这里详细阐述。

本章节主要描述的是用户态的虚拟机内存、native内存的泄漏检测方法。

## 实现原理

### 虚拟机内存

目前有如下3种能在开发态使用的检测虚拟机内存泄漏的方法：

1. 对比两次snapshot堆快照

   对于能比较稳定复现，有特定业务场景的泄漏问题，可以使用IDE工具对比两次snapshot快照的方式来定位问题，通过对比两次快照文件，可以获知新增了哪些虚拟机对象，这时候可以结合业务逻辑分析这些新增对象是否合理来判断是否真的泄漏。
2. 堆使用率超标检测

   一般来说每个虚拟机实例都会有使用上限，根据当前实际虚拟机内存占用大小和上限进行比较，超过上限的一定百分比就比较容易发生卡顿甚至OOM，这时候可以导出一个快照文件进行分析，有两种方式：

   一是应用可以自行调用hidebug的API计算出堆使用率的占比，超过阈值则调用hidebug的dumpJsRawHeapData方法导出快照。

   说明

   调用[hidebug.getAppMemoryLimit()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappmemorylimit12)可以获取到MemoryLimit对象，MemoryLimit对象的vmHeapLimit是当前虚拟机线程的虚拟机内存使用上限。

   调用[hidebug.getAppVMMemoryInfo()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappvmmemoryinfo12)可以获取到VMMemoryInfo对象，VMMemoryInfo对象的totalHeap是当前虚拟机线程的虚拟机内存使用量。

   上述两个值相除就能得出当前虚拟机线程的堆使用率占比。

   二是利用系统的自动导出快照的能力，但是目前此能力仅仅局限在开发者选项打开场景下能使用，堆使用率触发的百分比可以通过hidebug.setAppResourceLimit("js\_heap", 90) 设置，建议是85%以上，否则容易误报。
3. JsLeakWatcher检测

   针对某些特定对象，如果生命周期结束后，理论上就能被GC，如果发现即使GC后该对象仍然存在这种情况，就可以判定为泄漏。这种泄漏检测方法比较精准，直接就能告知泄漏对象是谁，而无需像前面两种方法那样，需要从快照文件中自行分析泄漏对象是谁。

   接口请参考：[@ohos.hiviewdfx.jsLeakWatcher (js泄露检测)](../harmonyos-references/js-apis-jsleakwatcher.md)，目前建议仅在开发态使用。

### Native内存

目前在开发过程中用于检测native内存泄漏的主要方法是使用DevEco Studio的Profiler插件，特别是其Allocation模板功能。该工具能够通过hook malloc、free、mmap等函数来分析内存占用等问题。对于能够稳定复现的问题，可以直接使用该工具连接终端设备，复现问题后抓取日志进行分析。

业界也有类似[libmemunreachable方案](https://android.googlesource.com/platform/system/memory/libmemunreachable/+/main/README.md)，其检测原理主要基于可达性算法和标记 - 清除垃圾回收器思想，从定义的GC Root节点沿着内存中的引用关系进行遍历，如果能查找到，则认为根可达，即正在被使用；反之，如果堆中的某个内存块无法从 GC Root节点遍历到，那么该内存块就是不可达的，可能存在内存泄漏。这个方案往往要配合[malloc\_debug](https://android.googlesource.com/platform/bionic/+/master/libc/malloc_debug/README.md)一起使用。

目前系统未采用此类方案，因为根据实际经验发现，此方法误报率比较高。

### 内核内存

对于ashmem、ION、GPU等内核内存，会根据整机总内存大小和内存种类分别设置一个整机的使用门限，定时查询使用量是否超过该门限，当发现超过门限，系统会进一步查询是哪些进程占用了此类内核内存，然后按照大小排序，对排在首位的应用进程进行泄漏事件上报和管控。

系统也会对单个进程的不同内核类内存使用设置上限，当内存使用总量超过此门限时，会对应用触发管控。

说明

目前内核类内存泄漏维测信息只能通过DevEco Testing工具压测获得，系统检测到异常后会自动生成，仅限开发态才能获取到，暂无线上获取方式

## 约束与限制

1. 系统的虚拟机堆使用率超标检测能力，目前只有开发者选项打开且勾选了系统资源泄漏日志开关的场景下可用，不建议应用在线上部署虚拟机堆使用率超标的检测机制，因为目前导出的虚拟机快照文件比较大，且耗时较久，需要3-5s左右。
2. JsLeakWatcher建议只在开发态使用，如果要线上使用，请使用小批量灰度发布来控制规模。

* **[JS内存泄漏问题检测方法](bpta-stability-js-memleak-detection.md)**
* **[Native内存泄漏问题检测方法](bpta-stability-native-memleak-detection.md)**
* **[JsLeakWatcher开发实践](bpta-js-leak-watcher.md)**
* **[内存泄漏定制能力开放使用指导](bpta-malloc-dispatch-table.md)**
