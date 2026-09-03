---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-arkts-localhandle-mode
title: LocalHandle类型内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkTS内存泄漏故障模式说明 > LocalHandle类型内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:20721ed98399f4f310cb5c3b4019e2f9243f83633e05e3ea1e6fa7b7ca397551
---

## 概述

本文旨在指导HarmonyOS应用开发者定位LocalHandle类型的ArkTS内存泄漏问题。若泄漏对象的根节点为LocalHandleRoot类型，即可确认为此类泄漏问题。

## 根因描述

LocalHandle类型泄漏对象在内存快照中的根节点归类为 LocalHandleRoot。由于Native侧napi\_value内的LocalHandle强持有该ArkTS对象，垃圾回收（GC）机制无法自动回收该内存。

LocalHandle的核心作用是管理临时对象的生命周期，确保在方法执行期间对象有效。主要应用场景包括：

1. **方法参数临时操作**：当ArkTS调用本地方法并传入对象参数时，Native代码通过LocalHandle临时持有该参数，确保GC在方法执行期间不回收该对象。
2. **同步返回值封装**：Native方法需要返回一个新的ArkTS对象（如封装计算结果）时，在方法内部创建的对象可通过LocalHandle安全传递回ArkTS环境。
3. **单次链式调用辅助**：在复杂的Native方法内部，若需创建中间对象（如临时数组、工具类实例）辅助计算，这些对象的引用通常作为LocalHandle管理，随方法结束自动清理。

**注意** 

LocalHandle需要napi\_open\_handle\_scope()/napi\_close\_handle\_scope()来管理对象的生命周期，其内存泄漏的根本原因就是未合理使用scope接口来规范LocalHandle对象作用域。

## LocalHandle问题分析思路

### 分析步骤

当应用触发ArkTS OOM故障导致崩溃，或其他ArkTS内存泄漏问题时，开发者可按以下步骤分析：

1. 确认泄漏对象：根据内存泄漏分析方法查看内存快照文件，定位内存占用大的泄漏对象，查看其引用链，确定距离（Distance）为1的根节点。
2. 判断故障模式：若根节点为LocalHandleRoot对象，即可确认为LocalHandle持有ArkTS对象导致的内存泄漏。
3. 确认泄漏场景：结合泄漏对象的整条引用链，确认具体泄漏的场景，并参考[Handle泄漏检测工具使用方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1943877608)进一步分析。
4. 追溯业务代码：根据工具检测结果，结合代码，确认是哪一种根因引起，并使用对应的解决方案。

### 根因

创建LocalHandle相关引用的对象的常用方法有以下几种：

* 对象创建：napi\_create\_xxx()系列接口，包括[napi\_create\_object()](../harmonyos-guides/use-napi-about-object.md#napi_create_object)、 [napi\_create\_int32()](../harmonyos-guides/use-napi-basic-data-types.md#napi_create_int32)、 [napi\_create\_string\_utf8()](../harmonyos-guides/use-napi-about-string.md#napi_create_string_utf8)等接口，用于在Native侧创建对应的ArkTS数据类型。
* 属性访问：napi\_get\_property()系列接口，包括[napi\_get\_named\_property()](../harmonyos-guides/use-napi-about-property.md#napi_get_named_property)、 [napi\_set\_named\_property()](../harmonyos-guides/use-napi-about-property.md#napi_set_named_property)、 [napi\_get\_property()](../harmonyos-guides/use-napi-about-property.md#napi_get_property)等接口，用于在Native侧读取或修改ArkTS对象的属性。
* 方法调用：[napi\_call\_function()](../harmonyos-guides/use-napi-about-function.md#napi_call_function)接口，用于从Native侧调用ArkTS侧的函数，实现“Native回调ArkTS”或“Native调用ArkTS方法”。
* 异步任务：[napi\_create\_async\_work()](../harmonyos-references/napi.md#napi_create_async_work)接口，用于将耗时操作移至子线程，避免阻塞ArkTS主线程。

上述方法创建的LocalHandle相关引用的对象，需正确使用napi\_open\_handle\_scope()/napi\_close\_handle\_scope()来管理对象的生命周期。特别是开发者使用libuv进行异步任务操作时，若在回调函数中创建ArkTS对象且未纳入Scope管理范围，将导致ArkTS对象生命周期泄漏至全局。

常见典型错误案例可参考[napi\_open\_handle\_scope与napi\_close\_handle\_scope进行生命周期相关开发典型错误场景](../harmonyos-guides/napi-faq-about-stability.md#napi_open_handle_scope与napi_close_handle_scope进行生命周期相关开发典型错误场景)。

### 关键字

LocalHandleRoot：Native代码为了管理临时对象创建了句柄LocalHandle。在生成Heap Snapshot时，该类句柄持有的根节点归入LocalHandleRoot，开发者可据此确认泄漏对象问题类型。

## 开发态故障案例分析

### LocalHandle持有ArkTS对象泄漏案例

**问题现象**

开发者单击应用“LocalHandle memory leak”按钮两次，第二次单击按钮时剩余内存不足申请内存失败，触发应用进程OOM闪退，系统生成jscrash日志和rawheap二进制快照文件。

**代码示例**

代码中前端按钮调用Native接口no\_open\_close\_handle\_scope()，该接口在UV异步任务后触发AfterWorkCallback()回调函数。在AfterWorkCallback()函数中存在300次循环，每次循环创建一个内存大小为1MB的string对象。LocalHandle持有创建的对象，但不添加napi\_open\_handle\_scope()/napi\_close\_handle\_scope()来管理生命周期，该字符串对象为LocalHandleRoot。示例如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/z5fo8IKjQAG3HG5LVPWcpQ/zh-cn_image_0000002729464443.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Uvqpd0zDRsSny2YZtv1GMw/zh-cn_image_0000002699865072.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/zGGUVqqWS-u7tlnKZy-0Sg/zh-cn_image_0000002729584403.png "点击放大")

**问题分析思路**

1. 参考[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)，在应用崩溃后获取崩溃日志，查看崩溃日志中的Reason字段为OutOfMemory，明确应用进程崩溃原因是OOM故障。

2. 参考[运维态内存快照获取方法](bpta-overview-of-arkts-memory-leaks-overview.md#section16548548153614)，获取OOM生成的rawheap快照文件，将内存快照导入到DevEco Studio查看。

3. 参考[运维态内存泄漏分析方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1289738624)，发现内存快照中有大量Distance为1的string对象，在内存快照中占用了最多的内存。查看string对象的根节点类型为LocalHandleRoot，说明是LocalHandle持有ArkTS对象导致泄漏。内存快照如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/I4M3QA3KQwmUew4Ww1IslA/zh-cn_image_0000002699705184.png "点击放大")

4. 使用[Handle泄漏检测工具使用方法](bpta-overview-of-arkts-memory-leaks-overview.md#section1943877608)进行进一步分析，找到对应创建LocalHandle引用的调用栈。检测工具获取的调用栈如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/VkThOCmUTDqsMKs6ozO-ig/zh-cn_image_0000002729464445.png)

5. 分析调用栈可知泄漏对象创建路径，结合业务代码分析是否存在内存泄漏场景。查看该调用栈，发现开发者没有调用napi\_open\_handle\_scope()和napi\_close\_handle\_scope()合理管控napi\_value的生命周期导致内存泄漏。

**问题结论与总结**

回调函数AfterWorkCallback中创建了string对象并通过napi\_value持有了该string对象。该任务在libuv调度，且未使用napi\_open\_handle\_scope()和napi\_close\_handle\_scope()来合理规范napi\_value的作用域，导致该napi\_value泄漏到全局。napi\_value持有的大量string对象也因此无法释放，造成内存泄漏。

**修复建议**

开发者在使用napi\_value时应使用napi\_open\_handle\_scope()和napi\_close\_handle\_scope()来管理对象生命周期。本次泄漏示例中，开发者可在Native接口no\_open\_close\_handle\_scope()中使用napi\_open\_handle\_scope()和napi\_close\_handle\_scope()来解决本次泄漏问题。

**说明** 

使用LocalHandle的关键在于严格遵守其自动化生命周期和作用域规则。LocalHandle无需也绝不能手动释放，但必须确保只在创建LocalHandle的作用域内访问该句柄。一旦业务逻辑需要跨越异步边界或多次方法调用，就应升级为使用GlobalHandle，即[napi\_ref](../harmonyos-guides/use-napi-life-cycle.md#napi_ref)。
