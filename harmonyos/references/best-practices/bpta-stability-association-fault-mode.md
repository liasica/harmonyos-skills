---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-association-fault-mode
title: 组合使用过大导致内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > RSS内存泄漏故障模式说明 > 组合使用过大导致内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-11-24T12:47:57+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:d790ffac8c61b77c56744bc0f786e0206bb1334f6acaf79e8c8583f433d68981
---

## 概述

NativeHeap过大、匿名映射过大、文件映射过大等单类问题各自未必触发RSS泄漏管控。这些单类问题叠加累积后极易突破系统阈值，同样会引发RSS内存泄漏。本文聚焦于此类组合内存过大场景，为开发者提供分析方法与优化建议。

## 问题分析思路

### 运维态问题分析思路

开发者可以参考[基础日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section112542151112)分析轻量化Smaps维测日志，将所有内存按照内存类别（Category）聚类并按照总内存占用排序，选取TOP3占用的内存类型作为本次问题分析的重点。结合[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取到的内存栈日志后，还可以按照[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)对调用栈进行分析并找到优化点。

**说明** 

如果怀疑的内存类型为NativeHeap堆内存，还可以参考[运维态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section174994597510)中提供的思路进行分析。

### 开发态问题分析思路

如果应用发生了RSS内存泄漏，参考[开发态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section1663214591559)找到占比TOP3的内存类型。然后根据[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)分析录制后的内存调用栈，确定可疑内存泄漏点。

## 案例分析

为直观展示组合过大导致内存泄漏的问题定位方法，下文结合NativeHeap与匿名映射组合过大导致内存泄漏的负向案例介绍了开发态与运维态下的问题分析过程。

### 案例：NativeHeap与匿名映射组合过大导致内存泄漏

此负向案例为应用NativeHeap内存过大与匿名映射组合过大，系统检测到应用发生RSS内存泄漏后在前台管控此应用，最终造成应用闪退故障。

**运维态分析思路**

* 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，在沙箱中接收到故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
* 在故障日志中找到关键字LOGGER\_MEMCHECK\_SAMPLIFY\_SMAPS\_INFO，并读取数据如下：

  ```screen
  LOGGER_MEMCHECK_SAMPLIFY_SMAPS_INFO
      Size         Rss        Swap                Category      Counts    Name
       512           0          52       arkts-static heap           2    [anon:ArkTs Static Object Space]
       512           0         288       arkts-static heap           2    [anon:ArkTs Static Non Movable Space]
   4150716     2253640       18176          AnonPage other          61    [anon]
   1778944         120         804             ark ts heap          19    [anon:ArkTS Heap]
      3328         232        2380             ark ts heap           4    [anon:ArkTS Heapnon movable space]
       512           8           8             ark ts heap           2    [anon:ArkTS Heapread only space]
       256           4          44             ark ts heap           1    [anon:ArkTS Heapshared non movable space]
       256          28          20             ark ts heap           1    [anon:ArkTS Heapshared read only space]
     40960           0       40480             ark ts heap           1    [anon:ArkTS Heapshared huge object space]
      6144         292        5740             ark ts heap           1    [anon:ArkTS Heapappspawn space]
      1792         236        1196             ark ts heap           6    [anon:ArkTS Heapsemi space]
      2560         188        1540             ark ts heap           8    [anon:ArkTS Heapshared appspawn space]
       256         104         120             ark ts heap           1    [anon:ArkTS Heapshared old space]
  33554432           0         120          arkweb-pa heap           5    [anon:partition_alloc]
       148         144           4          FilePage other           4    /system/bin/appspawn
        36          20          16             native heap           1    [anon:native_heap:meta]
      2180        1852          20                     .so           4    /system/lib/ld-musl-aarch64.so.1
      2992          60          20          AnonPage other           1    [anon:ld-musl-aarch64.so.1.bss]
        28           8          12                     .so           4    /system/lib64/chipset-sdk-sp/libclang_rt.ubsan_minimal.so
         4           0           4          AnonPage other           1    [anon:ArkTS Code:/etc/abc/framework/arkCommon.abc]
     34844         980        1020             native heap          21    [anon:native_heap:jemalloc meta]
   7391744     3783808      989812             native heap          16    [anon:native_heap:jemalloc]
       284         256           8                     .so           4    /system/lib64/chipset-sdk-sp/libunwinder.z.so
         8           8           0          AnonPage other           1    [anon:libunwinder.z.so.bss]
        84          80           0                     .so           4    /system/lib64/chipset-sdk-sp/libhitrace_meter.so
         4           4           0          AnonPage other           1    [anon:libhitrace_meter.so.bss]
  ......
  ```
* 分析Smaps维测日志，并按照Category列进行聚类，对每种类型的Rss列、Swap列求和，得到每种内存类型的申请总量，经过排序发现占比最大的为NativeHeap堆内存（占用约4.5GB）和匿名映射内存（占用约2.1GB）：

  ```screen
     Size         Rss        Swap                Category      Counts    Name
   4150716     2253640       18176          AnonPage other          61    [anon]
  ......
     34844         980        1020             native heap          21    [anon:native_heap:jemalloc meta]
   7391744     3783808      989812             native heap          16    [anon:native_heap:jemalloc]
  ......
  ```
* 优先分析占用最高的NativeHeap堆内存，参考[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取轻量化NMD维测日志以及内存调用栈后，按照[运维态问题分析思路](bpta-stability-nativeheap-fault-mode.md#section151162273105)进行下一步分析：
  + 分析以下NMD维测日志得出：402653184字节的内存共申请了4831838208字节，导致应用NativeHeap堆内存过大。

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
  + 参考[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)选中Native Heap泳道并找到内存申请异常的内存及其调用栈如下图所示。从图中可以看出这份内存栈共申请了12次402653184字节大小的内存块，总共申请了4.5GB内存，恰好与分析NMD维测日志得到的结果一致，进一步证实此调用栈为泄漏的内存栈。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/2QiqCn8ATK6m42MiiQR35A/zh-cn_image_0000002729611093.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=A74E8FE1D04A42D93299CD232B593BF86B79DEB47C19076432A017F97B7B6B5C "点击放大")
  + 分析内存调用栈指向的代码段，发现应用正在循环申请超大内存但是未释放，最终导致NativeHeap内存占用过大。内存调用栈指向的代码段如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/_t6ISQM0Souoc7r9Y_EN2g/zh-cn_image_0000002699891766.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=F80AC962C743B0CF8181851476CCED09A00FEA8E60EDBC2994F5A5E324B444C1)
* 再分析占用第二大的匿名页内存，并找到匿名映射过大的原因，具体步骤如下：
  + 参考[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)选中VM:others泳道并按Bytes列从大到小排序，找到内存申请异常的内存及其调用栈如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/-JI6LvWVSHKdAUwPwZHA0w/zh-cn_image_0000002699731880.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=975F96E8857D8BD54F5810FDE22916CE9E8800944E699F332531821CD07783CC "点击放大")
  + 分析内存调用栈指向的代码段，发现应用通过Native层MmapMemoryLeak()函数申请一次超大匿名页内存且未释放。累计申请过多导致匿名页内存过大。内存调用栈指向的代码段如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/0Rr1BBu6Rq2-tl3xqQjreA/zh-cn_image_0000002729491135.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F84C72BAF5033B4857103FAC2EF3618D226B4359B3223D4AB58872E61B2E3FB "点击放大")

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现RSS内存泄漏的测试场景。尝试复现此场景并使用DevEco Studio中Profiler工具的Allocation功能抓取内存异常增长点。具体分析步骤如下：

* 完成录制后，单击下图1处Memory的options按钮展开观察内存类型，并在下图2处选择除了GL、Graph外的所有内存复选框。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/jSi-1_UnSAmkJ8XKVvkcCg/zh-cn_image_0000002729611095.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E42911AC508C0B9CD5C437AE7AB8A97740F9874856E897FAF5ED5F8452439C4)
* 展开Memory泳道，观察每个时刻各子类型内存占比与增长趋势如下图：Native Heap和AnonPage Other两个泳道存在明显增长趋势，应该优先排查这两处内存是否存在泄漏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Lbl7zE2kTOaaxRXlwfHQbw/zh-cn_image_0000002699891768.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=688BA51530EF8091F5CB49A423AB8978FF6DDC63C3373581CBE550BADEF02522)

* 选中Native Heap泳道并找到内存申请异常的内存及其调用栈如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ZJ19NaLCQY-xZOvC3lljsA/zh-cn_image_0000002699731882.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=21F39018CD8ABD8A717B0C3F80CAEE60F75AED2511F811699871F90AEA1B76FE "点击放大")
* 分析内存调用栈指向的代码段，发现应用正在循环申请超大内存但是未释放，最终导致NativeHeap内存占用过大。内存调用栈指向的代码段如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/JQsu2ynFTliB_fEKbPVh5A/zh-cn_image_0000002729491137.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BF4F088400BE1A89B41AA860F58DA09F234C7325678C8C8264D8247E3E08000)
* 选中VM:others泳道并按Sizes列从大到小排序，找到内存申请异常的内存及其调用栈如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/oJ2Bv5hpQ-CusWs8wiyFqA/zh-cn_image_0000002729611097.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=24E81749E158C696B3EF7B8DFCE1E4BF234522CC24E9E199CA7F886FD00E8300 "点击放大")
* 分析内存调用栈指向的代码段，发现应用通过Native层MmapMemoryLeak()函数申请一次超大匿名页内存且未释放。累计申请过多导致匿名页内存过大。内存调用栈指向的代码段如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/24CCuOTxQXOg5mT6ZUoppg/zh-cn_image_0000002699891770.png?HW-CC-KV=V1&HW-CC-Date=20261124T044756Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F36DBB2A86A770854C99CFB448B292F019D4E86109842C13F692E0C2980C32B "点击放大")

**修复建议**

对于NativeHeap堆内存过大：分配与释放必须严格成对匹配，确保每次malloc()或new操作都有对应的free()或delete操作，重置指针前先释放旧内存。同时应借助RAII机制管理异常分支中的资源释放，并减少函数内多处return路径带来的重复释放代码，从源头规避遗漏风险。

对于匿名映射过大：需全面梳理代码执行流，涵盖异常跳转、循环迭代与异步信号上下文，严格保证mmap()与munmap()成对出现，避免内存泄漏。

**说明** 

组合过大导致RSS内存泄漏问题，优先分析内存占用最大的子内存类型，可以参考[RSS内存泄漏故障模式概述](bpta-stability-rssleak-fault-mode-overreview.md)定界至具体二级根因，再根据不同的二级根因跳转至对应的故障模式说明查找问题分析方法。
