---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-rssleak-fault-mode-overreview
title: RSS内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > RSS内存泄漏故障模式说明 > RSS内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:c6a18a2016ddfb49b7e6c9dc5f2867991d64dd03f63e98554ea2fb4d1e909e4c
---

系统会监控应用RSS内存的使用情况，如果应用RSS内存使用超过阈值并且整机处于低内存状态时，系统会抓取维测数据并对应用进行管控。本文旨在为开发者介绍系统的RSS内存泄漏检测机制，并提供开发态与运维态的问题分析思路。

此外，本文还提供了RSS内存泄漏问题分析与定位实践系列文章，旨在系统梳理泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [NativeHeap堆过大导致内存泄漏故障模式说明](bpta-stability-nativeheap-fault-mode.md)：NativeHeap内存是应用RSS内存的重要组成部分，通过malloc()或new操作符等方式动态申请。若申请后未及时释放，导致NativeHeap内存持续堆积，易引发RSS内存泄漏。此文提供开发态与运维态的分析思路，并构造NativeHeap过大导致RSS内存泄漏的典型案例以展示分析方法。
* [匿名映射过大导致内存泄漏故障模式说明](bpta-stability-anon-fault-mode.md)：匿名映射内存是应用RSS内存的重要组成部分，通过mmap()等方式申请。若申请的匿名内存未及时释放，导致匿名映射持续堆积，易引发RSS内存泄漏。此文提供开发态与运维态的分析思路，并构造匿名映射过大导致RSS内存泄漏的典型案例以展示分析方法。
* [文件映射过大导致内存泄漏故障模式说明](bpta-stability-filepage-fault-mode.md)：文件映射通过将文件内容直接映射到进程虚拟地址空间，实现零拷贝访问，是RSS内存的重要来源。若映射文件过大或使用后未及时解除映射，易引发RSS内存泄漏。此文提供开发态与运维态的分析思路，并构造文件映射过大导致RSS内存泄漏的典型案例以展示分析方法。
* [栈内存过大导致内存泄漏故障模式说明](bpta-stability-stack-fault-mode.md)：栈内存用于存储局部变量、函数调用链及返回地址等运行时信息。若应用未正确管理线程退出机制或线程数量过多，栈空间累积将引发RSS内存泄漏。此文提供开发态与运维态的分析思路，并构造线程申请过多导致RSS内存泄漏的典型案例以展示分析方法。
* [组合使用过大导致内存泄漏故障模式说明](bpta-stability-association-fault-mode.md)：NativeHeap过大、匿名映射过大、文件映射过大等单类问题各自未必触发RSS泄漏管控，但叠加累积后极易突破系统阈值，同样会引发RSS内存泄漏。此文提供开发态与运维态的分析思路，并构造NativeHeap与匿名映射组合过大导致RSS内存泄漏的典型案例以展示分析方法。

**说明** 

开发者可通过阅读[内存基础知识](bpta-memory-basic-knowledge.md)了解内存基础概念。

## RSS内存泄漏基本概念与故障检测机制

### RSS内存以及泄漏概念介绍

* 常驻RSS内存：常驻内存（RSS）大小指操作系统分配给进程的物理内存中，当前实际驻留于RAM（物理内存）的那部分容量。
* Swap RSS内存：Swap RSS内存指进程被换出到磁盘交换区的内存页大小。当物理内存紧张时，操作系统会将进程中不活跃的内存页换出至磁盘，以释放RAM空间，这部分被换出的内存即为Swap RSS内存。
* 应用RSS内存总值（下文以RSS内存代替） = 应用进程常驻RSS值 + 应用进程Swap RSS值。
* RSS内存泄漏：指进程的应用RSS内存持续不合理增长。
* RSS内存泄漏故障：当应用RSS内存大于一定阈值时，系统会判定应用对内存使用超过合理范围，存在内存泄漏。系统会在整机处于低内存状态时主动终止发生了内存泄漏的应用进程，并上报RSS内存泄漏事件，称为RSS内存泄漏故障。

RSS内存泄漏常见原因有：

1. 代码缺陷导致动态分配的内存未释放。
2. 业务实现不合理导致内存占用过大。
3. 业务过于复杂导致内存占用过大。

### RSS内存大小获取方式

开发者可以通过以下几种方法读取到进程的常驻RSS和Swap RSS内存占用：

**方法一****：**在shell命令行或应用代码中读取/proc/{pid}/status

```screen
cat /proc/<pid>/status | grep -E "^(VmRSS|VmSwap|Rss)"
```

开发者执行命令后可以得到应用常驻RSS内存值（VmRSS），应用Swap RSS内存值（VmSwap）：

```screen
VmRSS:      6572 kB
RssAnon:            2272 kB
RssFile:            4288 kB
RssShmem:             12 kB
VmSwap:     1484 kB
```

**方法二****：**通过PerformanceAnalysisKit中[hidebug.getRssInfo](../harmonyos-references/js-apis-hidebug.md#hidebuggetrssinfo24)()方法获取当前RSS和Swap内存占用。

### RSS内存泄漏检测原理

系统会在应用申请RSS内存时检测应用RSS内存占用，如果应用进程使用的RSS内存超过系统阈值，系统会判定应用发生了RSS内存泄漏。

对于已确认泄漏的问题应用，系统将采取主动管控策略。该策略的触发需同时满足以下两个前置条件：

* 应用自身泄漏：应用RSS内存大于一定阈值，超出合理使用范围。
* 整机资源紧张：整机进入低内存状态。

只有在上述条件均成立时，系统才会对问题应用执行管控操作（终止进程），从而优先保障整机稳定性，避免因资源耗尽导致黑屏、卡死等严重故障。

**说明** 

1. 低端设备的内存总量较小，更容易进入低内存状态。
2. 整机压力影响因素较多，应用需要关注自身内存是否超阈值，是否超出合理使用范围，只要超出阈值，就需要进行相关优化，提升应用保活成功率和良好的使用体验。

## 故障感知

开发者可以按需订阅相关故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，故障事件中包含应用申请的RSS内存以及NativeHeap、ArkTSHeap等子类型内存信息，同时会附带Smaps等维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，如果应用发生了RSS内存泄漏故障，那么事件的Reason会显示RssThresholdKiller。 开发者可以通过监听此事件，快速判断本次发生的故障类型，也可以与其他应用终止事件汇总分析此类故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可以通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)获取到本次系统管控的内存维测日志。应用触发RSS内存泄漏故障后，可以通过HiAppEvent收到如下hiappevent.event.RESOURCE\_OVERLIMIT事件回调，其中resource\_type的值为rss\_memory。开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-resourceleak-events.md#params字段说明)了解更详细的故障参数说明。

```screen
HiAppEvent onReceive: domain=OS
HiAppEvent eventName=RESOURCE_OVERLIMIT
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"bundle_name":"com.example.myapplication","bundle_version":"1.0.0","memory":{"pss":2100257,"rss":1352644,"sys_avail_mem":250272,"sys_free_mem":60004,"sys_total_mem":1992340,"vss":2462936},"pid":20731,"resource_type":"rss_memory","time":1502348798106,"uid":20010044,"external_log": ["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572401_6808.log"], "log_over_limit": false}}
```

### 订阅应用终止事件

应用触发RSS内存泄漏故障后，可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因，如果reason为RssThresholdKiller，说明本次应用终止原因为应用发生了RSS内存泄漏故障，开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明。

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"616930575450354120","bundle_version":"1.0.1","foreground":true,"reason":"RssThresholdKiller","time":1777877700534}}
```

**说明** 

如果应用在同一个生命周期内触发多次故障上报，那么这几次故障事件会持有相同的app\_running\_unique\_id，开发者可以根据app\_running\_unique\_id对应用发生的多个故障进行关联。

## 日志规格与日志获取

系统会在检测到应用发生RSS内存泄漏后，通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将系统抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径，并对提取出的维测日志进行分析。

### 日志规格

对于RSS内存泄漏故障，开发者可以结合以下几种维测日志进行问题分析：

* 轻量化Smaps日志，用于分析RSS内存泄漏时进程的RSS内存的详细分布。日志内容可以参考[rss内核管控](../harmonyos-guides/resource-leak-guidelines.md#rss内核管控)。
* 轻量化NMD维测日志，用于分析RSS内存泄漏时进程NativeHeap内存的详细分布。维测详情可参考[内存维测](../harmonyos-guides/resource-leak-guidelines.md#内存维测)的LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO字段。日志内容如下：

  ```screen
  LOGGER_MEMCHECK_SAMPLE_NMD_INFO

              size       allocated         nmalloc         ndalloc

                 8           17384          511848          509675
                16          129376          338438          330352
                32         1138816         1026155          990567
                48         3161808         1322095         1256224
                64         1869376          908151          878942
  ......

  ************ endl ************

  LOGGER_MEMCHECK_SAMPLE_NMD_INFO

              size       allocated         nmalloc         ndalloc

                 8           17384          511848          509675
                16          129376          338438          330352
                32         1138816         1026155          990567
                48         3161808         1322095         1256224
                64         1869376          908151          878942
  ......

  ************ endl ************
  ```

  开发者重点关注size和allocated两列：

  + size：应用申请的内存经过对齐后的大小，size向下取整，查看所有size的块中哪个size申请的总内存较大， 一般情况下优先分析较大的内存对应的size。
  + allocated：size申请的NativeHeap内存大小。
* 内存栈日志，记录了抓栈期间进程申请的RSS内存的调用栈，日志内容可参考[内存栈](../harmonyos-guides/resource-leak-guidelines.md#内存栈)。

### 内存栈日志获取方法

RSS内存泄漏的运维态维测仅包含轻量化Smaps作为基础维测，如果需要进一步定位到代码行，可以参考以下方法获取NMD维测日志与内存栈日志进行下一步分析：

* 通过订阅[应用灰度采集](../harmonyos-guides/hiretrieval.md)，在运维态订阅内存调用栈日志。
* 应用自行通过[RSS内存大小获取方式](bpta-stability-rssleak-fault-mode-overreview.md#section2077483014414)监听RSS水线，在合理的时机调用[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)方法主动采集内存调用栈日志。
* 通过用户描述、资源泄漏事件中的页面切换信息或流水日志等信息推测故障复现路径，参考[开发态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section1663214591559)使用DevEco Studio的Profiler调优功能抓取相关内存调用栈日志。

**说明** 

1. 应用内存栈受到应用内存泄漏的速度影响较大，对于快速泄漏问题，推荐开发者参考[订阅资源泄漏事件（ArkTS）](../harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts.md)，在订阅资源泄漏事件的同时，使用setEventConfig()方法补充订阅应用页面切换信息，以此分析泄漏场景，并在开发态对泄漏问题进行复现和定位。
2. 内存调用栈采集时，对应用性能存在一定影响，影响大小和应用内存申请频率和业务场景强相关，并且需要能命中泄漏时机，命中率无法预测。

## 运维态问题分析方法

对于运维态通过[订阅资源泄漏事件](bpta-stability-rssleak-fault-mode-overreview.md#section151162273105)感知到的资源泄漏故障，开发者可以优先参考[基础日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section112542151112)对获取到的基础维测进行分析，初步定界至二级根因。如果已经通过[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取到了应用内存栈维测日志，那么可以尝试根据[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)定位至泄漏点。

### 基础日志分析方法

开发者可以分析轻量化Smaps日志，将所有内存按照内存类别（Category）聚类并按照总内存占用排序，选定Rss+Swap占用最高的内存类型作为本次内存泄漏问题的二级根因：

**表1** 内存类别与二级故障根因映射表

| 内存类别（通过Category列获取） | 二级故障根因 | 定位手段 |
| --- | --- | --- |
| native heap | NativeHeap堆过大 | 参考[NativeHeap堆过大导致内存泄漏故障模式说明](bpta-stability-nativeheap-fault-mode.md)。 |
| AnonPage other（包含[anon]或已命名的Name） | 其他匿名页映射大 | 参考[NativeHeap堆过大导致内存泄漏故障模式说明](bpta-stability-nativeheap-fault-mode.md)。 |
| ark ts heap | 匿名映射-动态ArkTS虚拟机堆内存较大，但还未OOM | 优先用Smaps定界到二级根因。 |
| FilePage other（name中包含ashmem） | 匿名映射-Ashmem过大，但还未触发Ashmem泄漏管控 |
| jsvm heap | 匿名映射-龙雀JSVM虚拟机堆内存较大，但还未OOM |
| kotlin heap | 匿名映射-KMP Kotlin堆内存较大，但还未OOM |
| dart heap | 匿名映射-Flutter虚拟机堆内存较大，但还未OOM |
| rn-hermes heap | 匿名映射-RN虚拟机堆内存较大，但还未OOM |
| arkweb-js heap | 匿名映射-ArkWeb V8虚拟机堆内存较大，但还未OOM |
| arkts-static heap | 匿名映射-静态ArkTS虚拟机堆内存较大，但还未OOM |
| stack | 栈内存过大 |
| .so | 文件映射-共享库过大 |
| .ttf | 文件映射-字体文件过大 |
| .hap | 文件映射-HAP包过大 |
| FilePage other | 文件映射-其他过大 |
| / | Native Heap、ArkTS虚拟机堆、文件映射等组合使用过大 |

具体分析方法如下：

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
  ......
  ```
* 分析轻量化Smaps维测，并按照Category列进行聚类，对每种类型的“Rss”列、“Swap”列求和，得到每种内存类型的申请总量，进行统一排序找出内存总量占用最大的内存类型。

  例如，经过排序发现native heap类型的内存总量最大：

  ```screen
       Size         Rss        Swap                Category      Counts    Name
      47136         904         872             native heap          24    [anon:native_heap:jemalloc meta]
    9186304     6041112      277404             native heap           9    [anon:native_heap:jemalloc]
  ......
  ```

  那么可以断定，此时发生的RSS内存泄漏的二级故障为NativeHeap堆过大。

### 内存栈日志分析方法

开发者可以将内存栈日志导入DevEco Studio中，分析其中可疑的内存调用栈，排查可疑内存泄漏点：

* 单击下图①处导入文件按钮导入内存栈日志。
* 基于前置分析的二级根因单击选择不同的泳道，如下图②处：
  + 如果二级故障为NativeHeap堆过大，那么选中All Heap泳道。
  + 如果二级故障为其他，那么选中ALL Anonymous VM泳道。
* 单击③处Call Trees查看内存申请调用栈。
* 单击④处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
* 找到内存申请异常的内存及其调用栈，如下图⑤、⑥处框选的内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/VTB7KrmXSyG4L5qbeM-bMg/zh-cn_image_0000002680624004.png "点击放大")
* 结合调用栈对代码进行分析，找到泄漏根因。

## 开发态问题分析方法

对于在开发验证过程中遇到的RSS内存泄漏问题，或者运维态遇到的已知场景的RSS内存泄漏问题，开发者可以在本地使用DevEco Studio中Profiler工具的Allocation功能、hidumper等开发工具对问题进行复现并抓取维测进行分析。

### 故障分析工具说明

* [hidumper](../harmonyos-guides/hidumper.md)：在内存泄漏故障问题定位分析过程中，开发者可以使用以下指令抓取维测辅助问题定位：
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid”命令获取指定进程的内存使用情况，pid为指定的进程号。

    ```screen
    # hidumper --mem 9598

    -------------------------------[memory]-------------------------------

                                 Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
                               Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
                              ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
                     ------------------------------------------------------------------------------------------------------------------------------------------------------
                   GL              0              0              0              0              0              0              0              0              0              0
                Graph              0              0              0              0              0              0              0              0              0              0
          ark ts heap          46325           6888              0          45804              0             88              2              0              0              0
    arkts-static heap              4              0              0              4              0            416             15              0              0              0
                guard              0              0              0              0              0              0              0              0              0              0
          native heap        2382093           3528              0        2381572              0          31500           1365          68892          67285           3247
                 .hap          41744              0              0          41744              0              0              0              0              0              0
       AnonPage other           1544            356              0           1500              0           6140            172              0              0              0
                stack            420              0              0            420              0              0              0              0              0              0
                  .db             32              0              0             32              0              0              0              0              0              0
                  .so           9701          56360           3720           1020           1096          31772            905              0              0              0
                  dev             17              0            384             16              0              0              0              0              0              0
                 .ttf            436           1564              0             12              0              0              0              0              0              0
       arkweb-pa heap              0              0              0              0              0            120              4              0              0              0
       FilePage other            314           2332              8              0             12           4284            169              0              0              0
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Total        2485262          71028           4112        2472124           1108          74320           2632          68892          67285           3247

    native heap:
      jemalloc meta:          1199             72              0           1196              0            528             30              0              0              0
      jemalloc heap:       2379910           3432              0        2379392              0          25916           1101              0              0              0
           brk heap:           952             24              0            952              0           5056            234              0              0              0
          musl heap:            32              0              0             32              0              0              0              0              0              0

    Purgeable:
            PurgSum:0 kB
            PurgPin:0 kB

    DMA:
                Dma:0 kB

    Ashmem:
    Total Ashmem:16 kB
    ```
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem-smaps pid”命令获取指定进程的详细内存使用情况，pid为指定的进程号。

    ```screen
    # hidumper --mem-smaps 9598

    -------------------------------[memory]-------------------------------

                                        Shared      Shared      Private     Private
    Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
    1572536     4           4           0           0           4           0           12          0           27          AnonPage other                   [anon]
    264         0           0           0           0           0           0           20          0           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so
    200324      0           0           0           0           0           0           11136       443         5           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
    2476        0           0           0           0           0           0           168         6           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so
    85312       41740       41740       0           0           41740       0           0           0           3           .hap                             /data/storage/el1/bundle/entry.hap
    1244        436         436         0           0           392         44          0           0           4           .so                              /data/storage/el1/bundle/libs/arm64/libc++_shared.so
    1080        536         536         0           0           492         44          0           0           4           .so                              /data/storage/el1/bundle/libs/arm64/libentry.so
    40980       24          20          8           0           4           12          0           0           4           .so                              /data/storage/el1/bundle/libs/arm64/libhypersandemo.so
    20          4           4           0           0           4           0           0           0           5           .hap                             /data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr
    32          32          32          0           0           32          0           0           0           1           .db                              /data/storage/el2/base/files/hiappevent/databases/appevent.db-shm
    4           4           0           4           0           0           0           0           0           1           AnonPage other                   [anon:libvsync.z.so.bss]
    4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libwallpaperextensionability.z.so.bss]
    8           8           0           8           0           0           0           0           0           1           AnonPage other                   [anon:libwant.z.so.bss]
    4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libwebview_common.z.so.bss]
    4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libzlib.z.so.bss]
    6072        976         952         24          0           952         0           5056        234         100         native heap                      [anon:native_heap:brk]
    24600       1268        1199        72          0           1196        0           528         30          18          native heap                      [anon:native_heap:jemalloc meta]
    3422720     2382392     2379481     3428        0           2378964     0           25916       1101        12          native heap                      [anon:native_heap:jemalloc]
    32          32          32          0           0           32          0           0           0           1           native heap                      [anon:native_heap:meta]
    50331648    0           0           0           0           0           0           120         4           5           arkweb-pa heap                   [anon:partition_alloc]
    28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:10790]
    28          12          12          0           0           12          0           0           0           1           stack                            [anon:signal_stack:15311]
    28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:9818]
    28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:9819]
    28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:9820]
    ......
    ```
* [hiprofiler](../harmonyos-guides/hiprofiler.md)：对于RSS内存泄漏问题，开发者定界当前泄漏问题为native heap、AnonPage other、FilePage other、Ashmem等类型内存发生泄漏时，可以使用[堆内存分配调用栈数据采样记录](../harmonyos-guides/hiprofiler.md#堆内存分配调用栈数据采样记录)中展示的命令对进程的堆内存分配操作抓栈，来分析此问题的泄漏点。
* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio中Profiler工具的Allocation功能对应用进程的内存申请趋势以及内存申请调用栈进行分析，定位出具体泄漏点。更多功能可参考[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

### 故障分析方法

* 开发者在调试过程中，如果遇到应用闪退问题，可以在DevEco Studio中找到日志组件如下图①处，再选择应用终止如下图②处，单击③选择应用进程名，筛选出调试应用的历史退出原因，如果原因为“RssThresholdKiller”如下图④所示，说明应用在调试过程中发生了RSS内存泄漏故障。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/yoCAP5ClQ1aKHY_xcZC8Uw/zh-cn_image_0000002710303775.png "点击放大")
* 确认问题为RSS内存泄漏后，开发者可以使用DevEco Studio中Profiler工具的Allocation功能进行分析，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。如果发现应用内存占用超出开发者预期，那么可以初步断定存在内存泄漏问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/LmDFa60KQL6IFgRX6AUPFQ/zh-cn_image_0000002680464136.png "点击放大")
* 展开Memory泳道，如果发现Native Heap、AnonPage Other、Dev、Guard、.so、.ttf、Stack等泳道增长明显，那么可以初步定界为RSS内存泄漏问题，并且能精确到是哪种二级根因。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/UWKc57MlSdKJEk5k1IFV9g/zh-cn_image_0000002710143951.png "点击放大")
* 最后根据二级根因，结合[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)定位内存泄漏点。
