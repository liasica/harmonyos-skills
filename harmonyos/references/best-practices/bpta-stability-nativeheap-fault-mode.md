---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-nativeheap-fault-mode
title: NativeHeap堆过大导致内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > RSS内存泄漏故障模式说明 > NativeHeap堆过大导致内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:077f84346d415e443d27b456ed6971dc3794925a8c1e2ef4525ae07c58f9a83e
---

## 概述

应用的NativeHeap堆过大属于RSS内存泄漏的二级根因之一。本文旨在介绍NativeHeap堆过大的可能根因，结合案例提供开发态与运维态的问题分析思路。

## 根因描述

NativeHeap堆内存：在RSS的细分统计中，NativeHeap是由原生代码（C/C++）通过系统内存分配器动态申请的常驻物理内存。如：通过malloc()、calloc()、realloc()、free()或new、delete等方式申请常驻物理内存。

NativeHeap堆内存泄漏：应用由于申请的内存未释放、过量申请缓存等原因，导致NativeHeap堆过大，最后导致了RSS内存泄漏问题。

此类问题，通常情况下，会有如下几种可能原因：

1. 【基础对象泄漏】手动通过malloc()、new等动态分配的内存，未手动释放。
2. 【循环引用】多个智能指针间相互持有，构成环状循环引用，导致智能指针计数未清零而泄漏。
3. 【生命周期管理不当】通过系统接口申请系统资源后未释放。
4. 【跨语言导致泄漏】ArkTS对象持有Native对象导致Native内存泄漏。
5. 【过量缓存】业务为了性能提升，通过缓存机制保留内存，但是由于缓存机制保护不合理导致泄漏。比如阈值设计不合理，出现代码流程错误导致超预期的数量和大小使用。
6. 【业务过载】由于业务需要申请内存，但是相关资源对内存消耗极大，导致内存超限。

## 问题分析思路

### 运维态问题分析思路

开发者可以根据[基础日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section112542151112)对日志中的轻量化smaps维测信息进行分析，如果类型为“native heap”的内存最大，那么可以将当前遇到的RSS内存泄漏问题精确到NativeHeap内存泄漏问题。除了使用[运维态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section174994597510)中展示的通用方法外，NativeHeap堆过大问题还可以通过以下方法缩小内存调用栈分析范围：

* 分析轻量化NMD维测日志，排查可疑的内存泄漏区间如下：
  1. 单次申请32-48字节范围内的堆内存有127MB左右（133161808字节）。
  2. 单次申请48-64字节范围内的堆内存有336MB左右（351869376字节）。

  ```screen
  LOGGER_MEMCHECK_SAMPLE_NMD_INFO
              size       allocated         nmalloc         ndalloc

                 8           17384          511848          509675
                16          129376          338438          330352
                32         1138816         1026155          990567
                48       133161808         1322095         1256224
                64       351869376          908151          878942
  ......
  ```
* 根据[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)找到NativeHeap内存调用栈后，计算每份内存的Bytes/Count，筛选符合可疑size范围的内存调用栈，并通过调用栈进一步确认泄漏位置。每个内存调用栈申请的总内存Bytes与申请次数count，如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/kuk19PI7Riu5MP5BclDP9Q/zh-cn_image_0000002680624044.png "点击放大")

### 开发态问题分析思路

如果应用发生了RSS内存泄漏，可以参考[开发态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section1663214591559)，结合场景复现并使用DevEco Studio中Profiler工具的Allocation功能定位NativeHeap内存泄漏问题。

## 案例分析

### 案例一：malloc申请内存未释放

此案例通过模拟动态malloc申请NativeHeap内存未释放，构造NativeHeap内存泄漏，最终触发系统管控，导致了应用闪退。

**运维态分析思路**

* 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
* 在故障日志中找到关键字LOGGER\_MEMCHECK\_SAMPLIFY\_SMAPS\_INFO，并读取数据如下：

  ```screen
  LOGGER_MEMCHECK_SAMPLIFY_SMAPS_INFO
      Size         Rss        Swap                Category      Counts    Name
       512          44           8       arkts-static heap           2    [anon:ArkTs Static Object Space]
       256         180          44       arkts-static heap           1    [anon:ArkTs Static Non Movable Space]
   1582104         112           0          AnonPage other          42    [anon]
   1780224        1044         292             ark ts heap          34    [anon:ArkTS Heap]
       512          12           4             ark ts heap           2    [anon:ArkTS Heapread only space]
      3072        1424        1112             ark ts heap          12    [anon:ArkTS Heapnon movable space]
       256          40           8             ark ts heap           1    [anon:ArkTS Heapshared non movable space]
       256          44           4             ark ts heap           1    [anon:ArkTS Heapshared read only space]
     40960         320       40160             ark ts heap           1    [anon:ArkTS Heapshared huge object space]
      5888        5712          16             ark ts heap          23    [anon:ArkTS Heapappspawn space]
       512         272          32             ark ts heap           2    [anon:ArkTS Heapshared old space]
       768          36         340             ark ts heap           3    [anon:ArkTS Heapsemi space]
      2560        1592           0             ark ts heap          10    [anon:ArkTS Heapshared appspawn space]
  33554432         120           0          AnonPage other           5    [anon:partition_alloc]
       128          32           4          FilePage other           4    /system/bin/appspawn
        32           0          32             native heap           1    [anon:native_heap:meta]
      2124        1796           8                     .so           4    /system/lib/ld-musl-aarch64.so.1
      2992          48          16          AnonPage other           1    [anon:ld-musl-aarch64.so.1.bss]
         4           4           0          AnonPage other           1    [kshare]
        16          16           0          AnonPage other           2    [shmm]
      6288        3724        2520             native heap         108    [anon:native_heap:brk]
       280           4           0          FilePage other           1    /system/etc/zoneinfo/tzdata
     47136         904         872             native heap          24    [anon:native_heap:jemalloc meta]
   9186304     6041112      277404             native heap           9    [anon:native_heap:jemalloc]
       512          44           8       arkts-static heap           2    [anon:ArkTs Static Object Space]
       256         180          44       arkts-static heap           1    [anon:ArkTs Static Non Movable Space]
     47136         904         872             native heap          24    [anon:native_heap:jemalloc meta]
   9186304     6041112      277404             native heap           9    [anon:native_heap:jemalloc]
  ```
* 分析smaps维测，并按照Category列进行聚类，对每种类型的Rss列、Swap列求和，得到每种内存类型的申请总量，经过排序发现native heap类型的内存总量最大：

  ```screen
     Size         Rss        Swap                Category      Counts     Name
     47136         904         872             native heap          24    [anon:native_heap:jemalloc meta]
   9186304     6041112      277404             native heap           9    [anon:native_heap:jemalloc]
  ```
* 参考[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取轻量化NMD维测以及内存调用栈后，可以参考[运维态问题分析思路](bpta-stability-nativeheap-fault-mode.md#section151162273105)进行下一步分析，通过分析以下NMD维测日志，可以得出：402653184字节的内存共申请了4831838208字节，导致应用发生了RSS内存泄漏。

  ```screen
  ******************************
  LOGGER_MEMCHECK_SAMPLE_NMD_INFO
              size       allocated         nmalloc         ndalloc
                 8          380464          335069          287511
                16          595840          234006          196766
                32         4292576          288151          154008
                48         7271040          310762          159282
                64         7685056          567100          447021
                80         4250640          106810           53677
                96         1257792           32049           18947
               112         1301552           14495            2874
               128         2095232           27505           11136
               160          770080            9013            4200
     ......
            393216          393216               3               2
            458752          458752               1               0
            524288         1048576               3               1
            655360          655360               6               5
            917504          917504               2               1
           1048576         2097152               3               1
           1835008         1835008               2               1
           8388608         8388608               2               1
         402653184      4831838208              12               0
  ************ endl ************
  ```
* 获取到内存栈日志后，开发者可以使用DevEco Studio中Profiler工具，导入内存栈日志进一步分析泄漏点：
  + 打开DevEco Studio中的Profiler组件，单击下图①处导入获取的内存栈日志。
  + 单击选择All Heap下的Native Heap泳道，如下图②处。
  + 单击③处Call Trees查看内存申请调用栈。
  + 单击④处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
  + 找到内存申请异常的内存及其调用栈，如下图⑤处框选的内容。从框选的内容中可以看出这份内存栈共申请了6次，总共申请了2.25GB内存，单次申请内存约402653184字节，恰好与分析NMD维测日志得到的结果一致，进一步证实此调用栈为泄漏的内存栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/mVAHRNaXThat9RAaM851RA/zh-cn_image_0000002710303807.png "点击放大")
* 分析内存调用栈指向的代码段，可以得出应用正在循环申请一次超大内存，且未释放，最终导致了RSS内存泄漏：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/FLHsyor-TZmEhaz6e_RkXQ/zh-cn_image_0000002680464162.png "点击放大")

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现RSS内存泄漏的场景，那么可以通过尝试复现此场景并使用DevEco Studio中Profiler工具的Allocation功能抓取内存异常增长的点，可以参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。

* 录制完成后，单击All Heap中的Native Heap泳道，发现NativeHeap内存异常增长：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/fVAb4BNrQNyRfIfrOS60xw/zh-cn_image_0000002710143971.png "点击放大")
* 单击①处Call Trees按钮，单击②处筛选Created & Existing，可以找到异常申请的内存块和它的内存申请调用栈，内存申请调用栈如下图③处框中所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/vufK6CImQ2e5b0E3NbfXMA/zh-cn_image_0000002680624056.png "点击放大")
* 分析内存调用栈指向的代码段，可以得出应用正在循环申请一次超大内存，且未释放，最终导致了RSS内存泄漏：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/X-dg3Z9dQh2ajXputiGkjw/zh-cn_image_0000002710303817.png "点击放大")

**修复建议**

分配与释放的成对匹配

* 每处malloc()、new必须有对应的free()、delete。
* 重置指针前先释放。

异常安全与提前返回路径

* 用RAII处理异常分支。
* 减少函数内多个return路径的重复释放代码。
