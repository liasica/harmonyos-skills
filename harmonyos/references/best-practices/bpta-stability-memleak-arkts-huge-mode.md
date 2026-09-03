---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-arkts-huge-mode
title: 申请超大对象导致OOM故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkTS内存泄漏故障模式说明 > 申请超大对象导致OOM故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:4abc8e6c8086d59f49a2006fb2fa5ded6ba4a12c7da7440b4f0619167cd585cf
---

## 概述

本文旨在指导HarmonyOS应用开发者定位因单次申请超大对象导致的ArkTS OOM（Out of Memory，内存溢出）故障。开发者可通过查看崩溃日志中的Error message进行判断。若显示单次申请对象内存超大，则表明本次OOM由单次申请ArkTS内存过大引发。

## 根因描述

应用代码一次性申请超大内存，致使ArkTS内存超出虚拟机剩余可用堆内存，从而触发ArkTS OOM故障。

**说明** 

OOM故障根因是否为单次申请对象内存过大，无固定判定阈值，取决于应用剩余内存：剩余内存充足时可申请大内存对象，不足时则易触发ArkTS OOM故障。

## 超大对象分配OOM问题分析思路

### 分析步骤

1. 开发者需获取OOM时产生的jscrash日志。运维态可通过[订阅崩溃事件](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md)获取，开发态可在DevEco Studio -> log -> FaultLog中获取。
2. 查看jscrash日志中的Error message，若申请内存较大，则可能为一次性申请超大内存导致OOM。
3. 查看崩溃日志中Stacktrace的ArkTS崩溃堆栈，定位到具体申请内存的代码位置。崩溃日志示例如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/322BBqrJTu6lOtEySnmHRw/zh-cn_image_0000002729584407.png)
4. 开发者对申请内存的代码进行优化，避免一次性申请超大内存。

### 关键字

Error message：崩溃日志中Error message部分显示错误信息。若Error message中包含OutOfMemory及AllocateHugeObject字段，且申请内存size超大，可据此确认本次OOM原因为申请超大对象。

## 故障案例分析

### 一次性申请超大对象OOM案例

**问题现象**

开发者单击应用“Allocate huge\_obj”按钮，应用申请超大内存，触发应用进程闪退，系统生成jscrash日志和rawheap二进制快照文件。

**代码示例**

在Index.ets文件中，前端按钮调用HugeObj()函数，在函数中一次性申请500MB内存触发应用进程OOM故障。问题代码如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/0rr3tbnoT3Wd7TYSYgf9Ww/zh-cn_image_0000002699705188.png "点击放大")

**问题分析思路**

1. 应用崩溃后，通过[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)获取崩溃日志，崩溃日志如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/zWppo4OZSvqDTNCtIW3blA/zh-cn_image_0000002729464451.png)

2. 查看崩溃日志中的Reason字段为OutOfMemory，明确应用进程崩溃原因是OOM故障。

3. 查看Error message信息里申请的内存大小，发现应用一次性申请了500MB左右的超大内存，导致堆内存达到上限。

4. 分析Stacktrace崩溃栈信息定位到具体申请内存的ArkTS代码，发现是Index.ets文件第11行申请的内存触发了OOM。

**问题结论与总结**

本次应用崩溃是由于一次性申请了500MB超大内存，应用ArkTS内存超过虚拟机堆内存上限，触发了ArkTS OOM（Out of Memory，内存溢出）故障。通过分析Stacktrace崩溃栈可以定位到申请内存的代码位于Index.ets文件第11行。

**修复建议**

优化内存申请逻辑，避免一次性申请超大内存。开发者可以尝试先申请一部分，在使用完并释放后继续申请。ArkTS内存堆上限较低，如果开发者需要在应用中长期记录大量信息，可以将信息记录在[Ashmem](../harmonyos-references/js-apis-rpc.md#ashmem8)等其他类型内存中。
