---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-arkts-globalhandle-mode
title: GlobalHandle类型内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkTS内存泄漏故障模式说明 > GlobalHandle类型内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:fad8d31adc7fbc39423b3a63110dee757b5d74ab17202785dc322f70bcd6978c
---

## 概述

本文旨在指导HarmonyOS应用开发者定位GlobalHandle类型的ArkTS内存泄漏问题。若泄漏对象的根节点为GlobalHandleRoot类型，即可确认为此类泄漏问题。

## 根因描述

GlobalHandle类型的故障模式是指泄漏对象的根节点为GlobalHandleRoot类型的ArkTS对象。由于Native侧napi\_ref内的GlobalHandle强持有该ArkTS对象，垃圾回收（GC）机制无法自动回收该内存，导致GlobalHandle类型内存泄漏。

GlobalHandle的核心作用是延长ArkTS对象的生命周期，确保GC在主动释放前不回收该对象，主要应用场景包括：

1. **延长对象生命周期**：允许在不同的Native方法中复用同一个ArkTS对象，避免LocalHandle失效导致GC错误回收该对象。
2. **支持异步操作**：当本地后台线程需长时间持有并使用ArkTS对象（如回调函数）时，必须使用GlobalHandle确保对象在异步操作完成前始终有效。
3. **封装与上下文传递**：通过napi\_wrap()将ArkTS对象与本地资源（如文件句柄、网络连接）绑定，使Native代码能通过该引用反向操作对应的ArkTS对象。

## 典型泄漏场景

GlobalHandle内存泄漏通常发生在创建了GlobalHandle但未能适时释放的情况下，经典场景：

1. **未成对释放的接口调用**：在系统或自定义Native组件接口中，若Native侧创建了全局句柄持有传入的ArkTS对象（如回调接口），必须提供对应的释放接口。若只创建不释放，GC将无法回收该对象及其闭包内引用的所有对象。
2. **异步任务中的引用遗忘**：本地代码启动异步任务（如循环执行的后台线程）并持有ArkTS回调的GlobalHandle。若任务完成或取消时，忘记调用napi\_delete\_reference()释放引用，将导致泄漏。
3. **封装对象未被正确析构**：使用napi\_wrap()关联ArkTS对象与本地资源后，当GC回收ArkTS对象时，会触发析构回调。若在此回调中未使用napi\_remove\_wrap()释放对应的全局句柄，将造成泄漏。

## GlobalHandle问题分析思路

### 分析步骤

当应用触发ArkTS OOM故障导致崩溃，或其他内存泄漏问题时，开发者可按以下步骤分析：

1. 确认泄漏对象：根据内存泄漏分析方法查看内存快照文件，定位内存占用大的泄漏对象，查看其引用链，确定距离（Distance）为1的根节点。
2. 判断故障模式：若根节点为GlobalHandleRoot对象，即可确认为GlobalHandle持有导致的泄漏。
3. 确认泄漏场景：结合泄漏对象的整条引用链，确认具体泄漏场景，并参考[Handle泄漏检测工具使用方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1943877608)进一步分析。
4. 追溯业务代码：根据工具检测结果，结合代码确认全局句柄创建未释放的位置，并使用对应的释放接口修复。

### 常见场景

常见接口错误使用GlobalHandle的场景：

1. [napi\_create\_reference()](../harmonyos-references/napi.md#napi_create_reference)创建了对ArkTS对象的强引用，但未调用[napi\_delete\_reference()](../harmonyos-references/napi.md#napi_delete_reference)删除相关引用。
2. [napi\_wrap()](../harmonyos-guides/use-napi-about-class.md#napi_wrap)绑定了对ArkTS对象的强引用（最后一个参数非空），但未调用[napi\_remove\_wrap()](../harmonyos-guides/use-napi-about-class.md#napi_remove_wrap)解绑。
3. [napi\_acquire\_threadsafe\_function()](../harmonyos-guides/napi-data-types-interfaces.md#napi_threadsafe_function)增加了线程安全函数对象的引用计数，但未调用[napi\_release\_threadsafe\_function()](../harmonyos-references/napi.md#napi_release_threadsafe_function)清零，导致线程安全函数内的GlobalHandle泄漏。
4. [napi\_create\_promise()](../harmonyos-guides/use-napi-about-promise.md#napi_create_promise)创建的全局句柄持有了ArkTS对象，但未调用[napi\_resolve\_deferred()](../harmonyos-references/napi.md#napi_resolve_deferred)或[napi\_reject\_deferred()](../harmonyos-references/napi.md#napi_reject_deferred)进行响应闭环。
5. [setInterval()](../harmonyos-references/js-apis-timer.md#setinterval)创建的定时器持有了ArkTS对象，但未调用[clearInterval()](../harmonyos-references/js-apis-timer.md#clearinterval)删除定时器，且底层全局句柄持有该定时器。

### 关键字

GlobalHandleRoot：C++代码为了长期保留ArkTS对象引用创建了持久化句柄GlobalHandle。在Heap Snapshot快照中，该类句柄持有的根节点归入GlobalHandleRoot，开发者可据此确认泄漏对象问题类型。

## 开发态故障案例分析思路

### GlobalHandle持有ArkTS对象泄漏案例

**问题现象**

开发者单击应用“GlobalHandle memory leak”按钮四次，第四次单击按钮时剩余内存不足申请内存失败，触发应用进程OOM闪退，系统生成jscrash日志和rawheap二进制快照文件。

**代码示例**

代码中GlobalHandle()函数申请100MB的数组对象，箭头函数使用该数组对象，并传入自定义Native接口create\_but\_no\_delreference()。箭头函数传入Native接口后，napi\_create\_reference()创建的GlobalHandle持有传入的函数对象未释放，该函数对象即为GlobalHandleRoot。示例如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/vFLFbyIjQ-uMIAZmYR3xzw/zh-cn_image_0000002729464441.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/WC76LJkKTVGo1t20W8i0Jg/zh-cn_image_0000002699865070.png)

**问题分析思路**

1. 参考[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)，在应用崩溃后获取崩溃日志，查看崩溃日志中的Reason字段为OutOfMemory，明确应用进程崩溃原因是OOM故障。

2. 参考[运维态内存快照获取方法](bpta-overview-of-arkts-memory-leaks-overview.md#section16548548153614)，获取OOM生成的rawheap快照文件，将内存快照导入到DevEco Studio查看。

3. 参考[运维态内存泄漏分析方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1289738624)，发现内存快照中有三个内存占用100MB的array对象，在内存快照中占用了最多的内存。查看array对象的根节点为匿名函数，根节点类型为GlobalHandleRoot，说明是GlobalHandle持有导致泄漏。内存快照如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/g-DCDU52SG2XTxlmNW_ZiA/zh-cn_image_0000002729584401.png "点击放大")

4. 使用[Handle泄漏检测工具使用方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1943877608)进行进一步分析，找到对应创建GlobalHandle引用的调用栈。检测工具获取的调用栈如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/3R-yutBuT1uBAFxjWht3-A/zh-cn_image_0000002699705182.png "点击放大")

5. 分析调用栈可知泄漏对象创建路径，结合业务代码分析是否存在内存泄漏场景。查看该调用栈，发现开发者没有调用napi\_delete\_reference()合理管控napi\_ref的生命周期导致内存泄漏。

**问题结论与总结**

napi\_create\_reference()创建的引用关联，没有调用napi\_delete\_reference()删除相关引用，导致箭头函数及3个100MB的array对象无法释放，造成内存泄漏。

**修复建议**

开发者使用napi\_create\_reference()创建对ArkTS对象的引用后，应及时使用napi\_delete\_reference()删除相关引用，避免内存泄漏。本次泄漏示例中，开发者可在Native接口create\_but\_no\_delreference()结束前使用napi\_delete\_reference()释放strongRef来解决本次泄漏问题。

**说明** 

使用GlobalHandle的关键在于成对管理和明确的生命周期。每一次napi\_create\_reference()都必须对应一个明确的napi\_delete\_reference()调用点，通常放置在相关的销毁、取消或结束逻辑中。
