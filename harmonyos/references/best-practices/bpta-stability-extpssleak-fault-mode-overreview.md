---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-extpssleak-fault-mode-overreview
title: 泛PSS内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > 泛PSS内存泄漏故障模式说明 > 泛PSS内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:df3c3c49dd9117322bcce36f955016f1dac0206c88a85364802ac100bca85845
---

系统周期监控应用泛PSS内存，如果应用的泛PSS内存使用量超过阈值，系统会抓取维测日志并通过资源泄漏事件通知给应用。如果应用切换到后台后未及时释放内存，那么系统会管控此应用。本文提供了泛PSS内存泄漏问题分析与定位实践系列文章，旨在系统梳理泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [泛PSS内存泄漏故障模式说明](bpta-stability-app-extpssleak-fault-mode.md)：系统周期监控应用进程整体内存占用，如果应用进程未管理好持有的DMA、PSS、GPU等内存，就会导致应用进程整体内存膨胀，超过系统管控阈值。系统会在后台对应用进程进行管控，导致应用出现后台业务中断、冷启动等故障。此文围绕应用泛PSS内存泄漏问题，为开发者提供了开发态和运维态的分析思路，并以典型的PSS过大导致泛PSS内存泄漏的案例为例展示分析思路。

## 泛PSS内存泄漏基本概念与故障检测机制

### 泛PSS内存以及泄漏概念介绍

* 泛PSS内存：应用实际占用的[PSS](../harmonyos-guides/performance-analysis-kit-terminology.md#pss)、DMA和GPU内存总和。
* DMA内存：在HarmonyOS上，DMA内存指DMA驱动分配的，支持在多进程、多硬件之间共享访问的RAM内存。详情可见：[DMA内存及泄漏概念介绍](bpta-stability-dmaleak-fault-mode-overreview.md#section41401348165316)。
* GPU内存：GPU专用板载显存或通过统一内存管理的图形/计算缓冲资源。详情可见：[GPU内存基础概念](bpta-stability-gpuleak-fault-mode-overreview.md#section84161216133017)。
* [PSS](../harmonyos-guides/performance-analysis-kit-terminology.md#pss)内存：进程实际占用的物理内存总量。计算方式为：将RSS和Swap内存中的共享部分按使用该内存的进程数量进行分摊后，再将其与进程私有内存相加。

### 泛PSS内存大小获取方式

开发者可分别获取应用的PSS、DMA、GPU内存占用大小，计算进程内存占用总和，与预期总内存占用对比，判断应用是否发生泛PSS内存泄漏故障。各类内存大小的获取方式如下：

* PSS：使用[hidebug.getPss()](../harmonyos-references/js-apis-hidebug.md#hidebuggetpss)方法读取进程当前使用的PSS内存大小。
* GPU：参考[GPU内存大小获取方式](bpta-stability-gpuleak-fault-mode-overreview.md#section133116064920)。
* DMA：参考[DMA内存大小获取方式](bpta-stability-dmaleak-fault-mode-overreview.md#section714741117548)。

### 泛PSS内存泄漏检测原理

系统会周期监控应用的泛PSS内存占用，如果应用泛PSS内存占用超过系统预设阈值，系统会判定应用发生了泛PSS内存泄漏故障。对发生了泛PSS内存泄漏的应用，系统会根据应用的前后台状态执行以下操作：

* 如果检测到应用泄漏时，应用处于后台，系统会直接管控此应用。
* 如果检测到应用泄漏时，应用恰好处于前台，系统会等待应用切换到后台。等待一段时间后，系统会对应用泛PSS内存占用进行二次校验。

## 故障感知

开发者可以按需订阅相关故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，故障事件中包含应用申请的泛PSS内存以及各子类型内存信息，同时会根据应用发生故障时的内存分布附带Smaps、DMA、GPU等基础维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，系统会对发生了泛PSS内存泄漏故障的应用进行管控，此时事件的终止原因为ResourceLeak(PSSSoftLeak)或者ResourceLeak(PSSLeak)。 开发者可以通过订阅此事件，快速判断本次发生的故障类型，也可以与其他应用终止事件汇总分析此类故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可以通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)感知应用泛PSS内存泄漏问题，当事件参数中的resource\_type为pss\_memory时，表明应用进程发生了泛PSS内存泄漏。收到的资源泄漏事件示例如下：

```screen
HiAppEvent onReceive: domain=OS
HiAppEvent eventName=RESOURCE_OVERLIMIT
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"3385906026137528975","bundle_name":"com.example.lk","bundle_version":"1.0.0","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1786179535693_21146.log","/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1786179535694_21146.log"],"level":"kill","log_over_limit":false,"memory":{"gpu":0,"ion":980344,"pss":2621223,"pss_detail":{".db":16,".hap":348,".so":14309,".ttf":219,"anon_page_other":1536012,"ark ts heap":5662,"arkweb-js heap":0,"arkweb-pa heap":5,"dart heap":0,"dev":22,"file_page_other":0,"jsvm heap":0,"kotlin heap":0,"native heap":25676,"other":0,"rn-hermes heap":0,"stack":404},"rss":0,"sys_avail_mem":10969088,"sys_free_mem":4494312,"sys_total_mem":16032868,"vss":0},"page_switch_log":"[\"/data/storage/el2/log/page_switch/snapshot/page_switch-com.example.lk-2-1-20260808165855680.log\",\"/data/storage/el2/log/page_switch/snapshot/page_switch-com.example.lk-1-2-20260808165855680.log\"]","pid":21146,"resource_type":"pss_memory","time":1786179535680,"uid":20020205}}
```

从收到的资源泄漏事件中，提取出以下有效信息：

* resource\_type字段的值为pss\_memory，说明本次发生的资源泄漏问题属于泛PSS内存泄漏问题。
* external\_log字段的值为["/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_1786179535693\_21146.log","/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_1786179535694\_21146.log"]，开发者可以通过此路径找到泛PSS内存泄漏故障日志。

  **说明** 

  系统通过HiAppEvent下发的资源泄漏日志，默认无法通过文件名区分日志类型，需搜索关键词确认包含的内存维测信息。建议开发者参考[configEventPolicy接口参数设置说明](../harmonyos-guides/hiappevent-watcher-resourceleak-events.md#configeventpolicy接口参数设置说明)，在resourceoverlimitpolicy中使能useRefinedLogFileName参数，开启资源泄漏日志精细化命名功能。开启后，开发者可直接通过文件名识别日志用途，推断维测信息。
* memory字段的值为{"gpu":0,"ion":980344,"pss":2621223,"pss\_detail":{......},"rss":0,"sys\_avail\_mem":10969088,"sys\_free\_mem":4494312,"sys\_total\_mem":16032868,"vss":0}，将其按照JSON格式整理后如下：

  ```screen
  "memory": {
      "gpu": 0,
      "ion": 980344,
      "pss": 2621223,
      "pss_detail": {
          ".db": 16,
          ".hap": 348,
          ".so": 14309,
          ".ttf": 219,
          "anon_page_other": 1536012,
          "ark ts heap": 5662,
          "arkweb-js heap": 0,
          "arkweb-pa heap": 5,
          "dart heap": 0,
          "dev": 22,
          "file_page_other": 0,
          "jsvm heap": 0,
          "kotlin heap": 0,
          "native heap": 25676,
          "other": 0,
          "rn-hermes heap": 0,
          "stack": 404
      },
      "rss": 0,
      "sys_avail_mem": 10969088,
      "sys_free_mem": 4494312,
      "sys_total_mem": 16032868,
      "vss": 0
  },
  ```

  开发者可以从"pss":2621223判断应用的PSS内存占用约2621223KB，是应用发生泛PSS内存泄漏的主要原因；从"ion": 980344判断应用的DMA内存占用约980344KB，是应用发生泛PSS内存泄漏的次要原因。

### 订阅应用终止事件

应用触发泛PSS内存泄漏故障后，可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因，如果终止原因为ResourceLeak(PSSSoftLeak)或者ResourceLeak(PSSLeak)，说明应用发生了泛PSS内存泄漏问题。开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明。

以ResourceLeak(PSSLeak)管控原因为例，应用会收到应用终止事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"616930575450354120","bundle_version":"1.0.1","foreground":false,"reason":"ResourceLeak(PSSLeak)","time":1777877700534}}
```

其中，reason字段的值为ResourceLeak(PSSLeak)，foreground字段的值为false，说明应用处于后台时泛PSS内存超过系统管控阈值，系统在后台管控了此应用。

**说明** 

1. ResourceLeak(PSSSoftLeak)和ResourceLeak(PSSLeak)都代表应用泛PSS内存占用过大，系统对此应用进行了后台管控，开发者不用关注两个原因之间的差别。

2. 如果应用在同一个生命周期内触发多次故障上报，那么这几次故障事件会持有相同的app\_running\_unique\_id，开发者可以根据app\_running\_unique\_id对应用发生的多个故障进行关联。

## 日志规格与日志获取

系统会在检测到应用发生泛PSS内存泄漏后，通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将系统抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径，并对提取出的维测日志进行分析。

### 日志规格

对于泛PSS内存泄漏故障，开发者可以结合以下几种维测日志进行问题分析：

* Smaps日志，用于分析内存泄漏时进程的PSS内存的详细分布。维测详情可参考[内存维测](../harmonyos-guides/resource-leak-guidelines.md#内存维测)的LOGGER\_MEMCHECK\_SMAPS\_INFO字段下的维测信息。
* 轻量化NMD维测日志，用于分析进程NativeHeap内存的详细分布。维测详情可参考[内存维测](../harmonyos-guides/resource-leak-guidelines.md#内存维测)的LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO字段下的维测信息。
* jemalloc快照详细信息，用于分析进程NativeHeap内存的详细分布。维测详情可参考[内存维测](../harmonyos-guides/resource-leak-guidelines.md#内存维测)的LOGGER\_MEMCHECK\_DETIAL\_INFO字段下的维测信息。
* GPU内存基础维测日志，记录了应用申请GPU内存的详细分布。详细信息可参考[ASHMEM/DMA/GPU/GPU\_RS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)中gpu/gpu\_rs内存泄漏维测信息。
* DMA内存基础维测日志，记录了应用申请DMA内存的详细分布。详细信息可参考[ASHMEM/DMA/GPU/GPU\_RS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)中DMA内存泄漏维测信息。
* 内存栈日志，记录了抓栈期间进程申请的内存的调用栈。系统会根据当前占用的PSS、GPU和DMA内存大小，决定抓取的内存类型和范围。

### 内存栈日志获取方法

泛PSS内存泄漏的运维态维测默认包含Smaps、jemalloc快照详细信息等基础维测日志。如果需要进一步定位到代码行，可参考以下方法获取内存栈日志进行下一步分析：

* 应用自行通过[泛PSS内存大小获取方式](bpta-stability-extpssleak-fault-mode-overreview.md#section97711425164714)监听泛PSS内存大小，确定占用最大的内存类型，在合理的时机调用[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)方法主动采集对应内存类型的内存调用栈日志。
* 通过用户描述、资源泄漏事件中的[页面切换日志](../harmonyos-guides/pageswitch-log.md)或流水日志等信息推测故障复现路径，通过DevEco Studio中Profiler工具的Allocation功能抓取相关内存调用栈日志。

## 运维态问题分析方法

对于运维态泛PSS内存泄漏故障，开发者可以参考[订阅资源泄漏事件](bpta-stability-extpssleak-fault-mode-overreview.md#section151162273105)从事件提供的memory信息中找到占用最高的内存类型。开发者可以优先结合获取的维测日志分析top内存占用问题，不同内存类型及其分析方法见下表：

| 内存类型 | 问题分析方法 |
| --- | --- |
| PSS | 优先参考[PSS基础日志分析方法](bpta-stability-extpssleak-fault-mode-overreview.md#section28196459359)初步定界至二级根因，如果已经通过[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取到了应用内存栈维测日志，那么可以根据[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)定位至泄漏点。 |
| DMA | 参考DMA内存泄漏[运维态问题分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section10889164472315)定位至内存泄漏点。 |
| GPU | 参考GPU内存泄漏[运维态问题分析方法](bpta-stability-gpuleak-fault-mode-overreview.md#section1045562816)定位至内存泄漏点。 |

### PSS基础日志分析方法

对于PSS内存泄漏，开发者可以优先分析Smaps日志，将问题定界至NativeHeap堆过大、匿名映射过大等二级根因。

将所有内存按照内存类别（Category）聚类并按照总内存占用排序，找到Pss+SwapPss占用最高的内存类型，并参考[基础日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section112542151112)映射出本次内存泄漏问题的二级根因。如：从以下维测信息中可以确定AnonPage other类型的内存使用了9947148KB的PSS内存和292948KB的SwapPss内存，占用最高。开发者可以明确此问题的二级根因为其他匿名页映射大，并参考[匿名映射过大导致内存泄漏故障模式说明](bpta-stability-anon-fault-mode.md)进行后续定位。

```screen
                                    Shared      Shared      Private     Private
Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
11812668    9947148     9947148     0           0           9947148     0           292960      292948      47          AnonPage other                   [anon]
268         0           0           0           0           0           0           20          0           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so
208580      0           0           0           0           0           0           11148       617         5           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
2488        0           0           0           0           0           0           168         9           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so
85360       16          16          0           0           16          0           0           0           3           .hap                             /data/storage/el1/bundle/entry.hap
1244        160         160         0           0           144         16          28          28          4           .so                              /data/storage/el1/bundle/libs/arm64/libc++_shared.so
1080        324         324         0           0           312         12          32          32          4           .so                              /data/storage/el1/bundle/libs/arm64/libentry.so
40980       12          8           8           0           4           0           12          12          4           .so                              /data/storage/el1/bundle/libs/arm64/libhypersandemo.so
20          0           0           0           0           0           0           0           0           5           .hap                             /data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr
32          32          32          0           0           32          0           0           0           1           .db                              /data/storage/el2/base/files/hiappevent/databases/appevent.db-shm
2048        76          0           0           76          0           0           0           0           1           dev                              /dev/__parameters__/param_sec_dac
80          0           0           0           0           0           0           0           0           1           dev                              /dev/__parameters__/param_selinux
4           4           0           0           4           0           0           0           0           1           dev                              /dev/__parameters__/u:object_r:accessibility_param:s0
......
```

## 开发态问题分析方法

对于在开发验证过程中遇到的泛PSS内存泄漏问题，或者运维态遇到的已知场景的泛PSS内存泄漏问题，开发者可以在本地使用DevEco Studio中Profiler工具的Allocation功能、hidumper等开发工具复现问题并抓取维测日志进行分析。

### 故障分析工具说明

* [hidumper](../harmonyos-guides/hidumper.md)：在内存泄漏故障问题定位分析过程中，开发者可以使用以下指令抓取维测日志辅助问题定位。
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid”命令获取指定进程的内存使用情况，pid为指定的进程号。
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem-smaps pid”命令获取指定进程的详细内存使用情况，pid为指定的进程号。开发者可以参考[PSS基础日志分析方法](bpta-stability-extpssleak-fault-mode-overreview.md#section28196459359)对PSS内存泄漏问题作初步分析。执行命令后的输出结果如下：

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
    2048        72          0           0           72          0           0           0           0           1           dev                              /dev/__parameters__/param_sec_dac
    80          0           0           0           0           0           0           0           0           1           dev                              /dev/__parameters__/param_selinux
    4           4           0           0           4           0           0           0           0           1           dev                              /dev/__parameters__/u:object_r:accessibility_param:s0
    4           4           0           0           4           0           0           0           0           1           dev                              /dev/__parameters__/u:object_r:ark_profile:s0
    4           4           4           0           0           4           0           0           0           1           AnonPage other                   [anon:libwifi_utils.z.so.bss]
    4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libwindowstageani_kit.z.so.bss]
    16          12          12          0           0           12          0           4           0           1           AnonPage other                   [anon:libwm.z.so.bss]
    4           4           4           0           0           4           0           0           0           1           AnonPage other                   [anon:libwmutil.z.so.bss]
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
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid --show-dmabuf”命令获取指定pid的内存使用情况，并打印DMA内存详细信息。开发者获取的DMA内存详细信息等效于通过[订阅资源泄漏事件](bpta-stability-extpssleak-fault-mode-overreview.md#section151162273105)获取的DMA内存泄漏故障日志，开发者可以参考[DMA内存基础日志分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section170311436201)对DMA内存占用问题作初步分析。执行命令后的输出结果如下：

    ```screen
    -------------------------------[memory]-------------------------------

                                 Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
                               Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
                              ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
                     ------------------------------------------------------------------------------------------------------------------------------------------------------
                   GL        1680540              0              0              0        1680540              0              0              0              0              0
                Graph        3534416              0              0              0        3534416              0              0              0              0              0
          ark ts heap           1625           6144              0           1304              0           5992           5992              0              0              0
                guard              0              0              0              0              0              0              0              0              0              0
          native heap          34510          37160              0          32652              0          24412          24080          89600          85130           5389
                 .hap           1620              0              0           1616              4              0              0              0              0              0
       AnonPage other          97850           5732              8          97640              0          10864          10832              0              0              0
                stack           1256              0              0           1256              0             28             28              0              0              0
                  .db            128              0              0            128              0              0              0              0              0              0
                  .so          56735          83004          27968          33336           2732           4252            138              0              0              0
                  dev             21              0            356             16              0              0              0              0              0              0
                 .ttf            379           1496              0              0              0              0              0              0              0              0
       FilePage other          15407           3192           6384          12100           1156              8              0              0              0              0
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Total        5465570         137004          34716         180048        5218848          45556          41070          89600          85130           5389

    native heap:
      jemalloc meta:           874            472              0            848              0            520            493              0              0              0
      jemalloc heap:         32372          31492              0          30772              0          23604          23376              0              0              0
           brk heap:          1248           5196              0           1016              0            272            195              0              0              0
          musl heap:            16              0              0             16              0             16             16              0              0              0

    Purgeable:
            PurgSum:0 kB
            PurgPin:0 kB

    DMA:
                Dma:3534416 kB
    Process                pid          fd         size_bytes        ino         exp_pid        exp_task_comm         buf_name        exp_name               buf_type           leak_type
    xample.dfx_test        23338        72         101122048         762         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        76         101122048         763         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        78         101122048         764         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        82         101122048         765         22851          allocator_host        NULL            mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        96         101122048         766         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        98         101122048         767         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        108        101122048         768         22851          allocator_host        23338           mm_heap_helpers        xcomponent         xcomponent-s-surfaceView
    xample.dfx_test        23338        290        13418496          821         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-282
    xample.dfx_test        23338        294        13418496          822         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-311
    xample.dfx_test        23338        305        13418496          823         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-302
    xample.dfx_test        23338        308        13418496          824         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-309
    xample.dfx_test        23338        312        13418496          825         1428           allocator_host        23338           mm_heap_helpers        web                web-surface-320
    ......

    Ashmem:
    Total Ashmem:3372 kB
    ```
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid --show-gpumem”命令获取指定pid的内存使用情况，并打印GPU内存详细信息。详细信息可参考[ASHMEM/DMA/GPU/GPU\_RS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)中gpu内存泄漏字段说明。开发者可以参考[GPU内存基础维测分析方法](bpta-stability-gpuleak-fault-mode-overreview.md#section1971511522381)对GPU内存占用问题作初步分析。执行命令后的输出结果如下：

    ```screen
    # hidumper --mem 55126 --show-gpumem

    -------------------------------[memory]-------------------------------

                                 Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
                               Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
                              ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
                     ------------------------------------------------------------------------------------------------------------------------------------------------------
                   GL        1030592              0              0              0        1030592              0              0              0              0              0
                Graph              0              0              0              0              0              0              0              0              0              0
          ark ts heap           2474           1112              0           2380              0           7320           6459              0              0              0
    arkts-static heap              0              0              0              0              0            340             11              0              0              0
                guard              0              0              0              0              0              0              0              0              0              0
          native heap          16836           1992              0          16440              0          50128          17561          65396          63523           2022
                 .hap            356              0              0            356              0              0              0              0              0              0
       AnonPage other           1728            236              0           1680              0           6776            784              0              0              0
                stack            324              0              0            324              0             80             80              0              0              0
                  .db             12              0              0             12              0              0              0              0              0              0
                  .so          11072          59652           3348            960            480          33172           1559              0              0              0
                  dev              7              0            328              4              0              0              0              0              0              0
                 .ttf            294           1336              0              0              0              0              0              0              0              0
       arkweb-pa heap              0              0              0              0              0            120              4              0              0              0
       FilePage other           1379           4068            284            256             24           3564            130              0              0              0
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Total        1091662          68396           3960          22412        1031096         101500          26588          65396          63523           2022

    native heap:
      jemalloc meta:           706             48              0            700              0            876            281              0              0              0
      jemalloc heap:         15365           1936              0          14976              0          44248          16770              0              0              0
           brk heap:           749              8              0            748              0           4988            494              0              0              0
          musl heap:            16              0              0             16              0             16             16              0              0              0

    Purgeable:
            PurgSum:0 kB
            PurgPin:0 kB

    DMA:
                Dma:0 kB

    Ashmem:
    Total Ashmem:16 kB

    GPU:
    ctx_227      55126      55126 used summary:1053216768 grow:0 driver:3776512 kmd:1695744 jit:0 map:210 0 0 bg:0
    com.example.dfx_test
    Total U(device): 1048610050
    Total A(device): 1049436160
    Total P(device): 0
    Total U(host): 399432
    Total A(host): 614400
    Total P(host): 0
    C: cq memory(not in total memory) : 4096

    C: host default memory (Total memory: 208904)
      5:                    5 / 80
      6:                    5 / 240
      7:                  146 / 9472
      8:                   19 / 2912
      9:                  222 / 84288
     10:                  203 / 104840
     11:                    5 / 7072

    C: host internal memory (Total memory: 190528)
      7:                  458 / 43968
      8:                  204 / 26112
      9:                  224 / 71808
     10:                    5 / 4360
     11:                    4 / 6208
     16:                    1 / 38072

    C: gles default device (Total memory: 14721)
      1:                    1 / 1
      6:                    1 / 32
      7:                    4 / 256
      8:                    1 / 160
     10:                    1 / 512
     11:                    1 / 1024
     12:                    1 / 2048
     14:                    1 / 10688
    ```
* [hiprofiler](../harmonyos-guides/hiprofiler.md)：开发者可以根据应用进程内存占用分布，使用对应的命令抓取内存栈，来分析此问题的泄漏点。
* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio中Profiler工具的Allocation功能对应用进程的内存申请趋势、内存占用分布以及内存申请调用栈进行分析，定位出具体泄漏点。更多功能可参考[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

**说明** 

hidumper命令行工具更多用于实时观察应用的内存占用和进程内存使用分布，无法帮助开发者直接定位到内存泄漏点。hiprofiler命令行工具则仅能抓取预设时长的内存栈日志，无图形化界面，多用于压测场景使用脚本周期抓取维测日志。而DevEco Studio的Profiler调优功能不仅能图形化展示应用的内存增长趋势，还可以抓取出录制过程中应用申请的内存和对应的内存调用栈直接分析。因此，推荐开发者在开发态分析问题时优先使用DevEco Profiler调优工具分析泛PSS内存泄漏问题。

### 故障分析方法

开发者在调试过程中，如果遇到应用后台业务中断或者应用冷启动问题，可以通过[订阅应用终止事件](bpta-stability-extpssleak-fault-mode-overreview.md#section19969124021018)或者[订阅资源泄漏事件](bpta-stability-extpssleak-fault-mode-overreview.md#section151162273105)感知当前是否发生了泛PSS内存泄漏故障，并根据资源泄漏事件中的memory字段确定此次泛PSS内存泄漏故障的top根因。开发者可以根据确定的top内存类型参考各自的分析方法抓取维测日志并分析，不同内存类型及其分析方法见下表：

| top内存类型 | 问题分析方法 |
| --- | --- |
| PSS | PSS实际为去重后的RSS内存，因此分析方法可参考RSS内存泄漏[故障分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section2982114911114)。 |
| DMA | 参考DMA内存泄漏[故障分析方法](bpta-stability-dmaleak-fault-mode-overreview.md#section198045621516)。 |
| GPU | 参考GPU内存泄漏[故障分析方法](bpta-stability-gpuleak-fault-mode-overreview.md#section113804961519)。 |
