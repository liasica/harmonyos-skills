---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ashmemleak-fault-mode-overreview
title: ASHMEM内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ASHMEM内存泄漏故障模式说明 > ASHMEM内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:6a697ddc6d88602573f82a09933672ad16f19333ec9a3397bb66a0c3bed5490c
---

## 概述

系统会监控应用ASHMEM（Anonymous Shared Memory）内存占用。当应用ASHMEM内存使用超过系统管控阈值且整机处于低内存状态时，系统会抓取维测数据并管控此应用。本文旨在为开发者介绍系统的ASHMEM内存泄漏检测机制，并提供开发态与运维态的问题分析思路。此外，本文还提供了ASHMEM内存泄漏问题分析与定位实践系列文章，旨在系统梳理泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的内存使用习惯。文章如下：

* [ASHMEM内存泄漏故障模式说明](bpta-stability-app-ashmemleak-fault-mode.md)：应用在使用ASHMEM进行IPC数据传输、图像共享或媒体缓冲等场景中，因未正确释放ASHMEM机制创建的共享内存区域导致内存持续占用超过系统管控阈值，系统会主动管控问题应用，造成应用前台闪退等故障。此文通过典型的ASHMEM内存泄漏案例，为开发者提供开发态和运维态的问题分析思路。

**说明** 

开发者可通过阅读[内存基础知识](bpta-memory-basic-knowledge.md)了解内存基础概念。

## ASHMEM内存泄漏基本概念与故障检测机制

### ASHMEM内存及泄漏概念介绍

* ASHMEM：匿名共享内存，是一种共享内存IPC机制，允许进程创建和共享内存区域。
* ASHMEM内存泄漏：已分配的ASHMEM内存区域因失去引用且未调用相应释放接口，内存区域持续占用而无法回收复用。
* ASHMEM内存泄漏故障：当应用ASHMEM内存大于一定阈值时，系统会判定应用对内存使用超过合理范围，存在内存泄漏。系统会在整机处于低内存状态时主动终止发生了ASHMEM内存泄漏的应用进程，并上报ASHMEM内存泄漏事件，称为ASHMEM内存泄漏故障。

ASHMEM在HarmonyOS中的主要使用场景包括：

* IPC数据传输：多个进程之间通过ASHMEM共享大块数据，用于跨进程通信的数据传递。
* 图像/位图共享：应用将图像数据通过ASHMEM在不同组件或进程间共享，避免数据拷贝带来的性能开销。
* 媒体缓冲共享：音视频播放、编解码过程中，通过ASHMEM在播放器与编解码器之间传递缓冲数据。
* 图形缓冲共享：图形渲染管线中，通过ASHMEM在不同图形模块间共享缓冲资源。

### ASHMEM内存泄漏检测原理

系统通过周期性轮询及关键操作（如ASHMEM内存分配）触发两种方式，实时监控整机ASHMEM内存的总使用量。

当整机ASHMEM内存占用超过预设的系统检测阈值时，系统将启动内存泄漏排查流程，分析持有ASHMEM内存的应用进程。若系统检测出某一应用的ASHMEM内存占用超出系统管控阈值，则判定该应用发生内存泄漏。

对于已确认泄漏的问题应用，系统将采取主动管控策略。该策略的触发需同时满足以下两个前置条件：

1. 应用自身泄漏：目标应用的ASHMEM内存占用已超过其合理使用上限（即系统管控阈值）。
2. 整机资源紧张：整机进入低内存状态。

只有在上述条件均成立时，系统才会管控问题应用进程，从而优先保障整机稳定性，避免因资源耗尽导致重启、冻屏等严重故障。

**说明** 

1. 低端设备的内存总量较小，更容易进入低内存状态。

2. 整机压力影响因素较多，应用需要关注自身内存是否超出合理使用范围，只要超过或接近系统管控阈值，就需要进行相关优化，提升应用保活成功率和良好的使用体验。

## 故障感知

开发者可以按需订阅相关故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，故障事件中包含应用申请的ASHMEM内存大小等内存信息，同时会附带ASHMEM内存基础维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，如果应用发生了ASHMEM内存泄漏问题，那么事件的终止原因为ResourceLeak(AshmemLeak)或者AshmemKiller。开发者可以通过监听此事件，快速判断本次发生的故障类型，也可以与其他应用终止事件汇总分析此类故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可以通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)感知应用ASHMEM内存泄漏问题，当事件泄漏类型为ashmem\_memory时，表明应用进程发生了ASHMEM内存泄漏，收到的资源泄漏事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"11235809489999226959","bundle_name":"com.example.dfx_test","bundle_version":"1.0.1","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1779983144774_34482.log"],"level":"warning","log_over_limit":false,"memory":{"ashmem":20971520,"gpu":0,"ion":0,"pss":0,"rss":68264,"sys_avail_mem":2196480,"sys_free_mem":1207616,"sys_total_mem":16035444,"vss":71521476},"pid":34482,"resource_type":"ashmem_memory","time":1779983144721,"uid":20020198}}
```

其中，resource\_type字段的值为ashmem\_memory，说明本次发生的资源泄漏问题属于ASHMEM内存泄漏问题。external\_log字段的值为/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_1779983144774\_34482.log，开发者可以通过此路径找到ASHMEM内存泄漏故障日志。

### 订阅应用终止事件

开发者可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因。如果终止原因为ResourceLeak(AshmemLeak)或者AshmemKiller，说明应用发生了ASHMEM内存泄漏问题。根据不同的管控原因，开发者可以判断本次内存泄漏的严重程度，管控原因的描述与影响如下表所示：

| Reason | 管控原因 |
| --- | --- |
| AshmemKiller | 应用ASHMEM内存超过系统前台管控阈值，系统会在整机进入低内存时管控问题应用，通常表现为应用前台闪退。 |
| ResourceLeak(AshmemLeak) | 应用ASHMEM内存超过系统周期检测阈值触发的系统管控，通常表现为应用后台冷启动。 |

以AshmemKiller管控原因为例，应用会收到应用终止事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"616930575450354120","bundle_version":"1.0.1","foreground":true,"reason":"AshmemKiller","time":1777877700534}}
```

其中，reason字段为AshmemKiller，foreground字段为true，说明此次应用终止是因为系统检测到应用ASHMEM内存占用超过系统前台管控阈值，触发了系统前台管控。开发者也可以通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明。

**说明** 

如果应用在同一个生命周期内触发多次故障上报，那么这几次故障事件会持有相同的app\_running\_unique\_id，开发者可以根据app\_running\_unique\_id对应用发生的多个故障进行关联。

## 日志规格与日志获取

系统会在检测到应用发生ASHMEM内存泄漏后，通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径，分析提取出的维测日志。

### 日志规格

对于ASHMEM内存泄漏问题，开发者可以结合以下几种维测日志进行问题分析：

* ASHMEM内存基础维测日志，记录了应用申请ASHMEM内存的详细分布，包括每个ASHMEM区域的名称、大小、引用计数和映射状态等信息，详细信息可参考[ASHMEM/DMA/GPU/GPU\_RS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)中ASHMEM内存泄漏维测信息。
* 内存栈日志，记录了抓栈期间进程申请的ASHMEM内存的调用栈，详细信息可参考[内存栈](../harmonyos-guides/resource-leak-guidelines.md#内存栈-1)。

### 内存栈日志获取方法

ASHMEM内存泄漏的运维态维测日志仅包含ASHMEM内存基础维测日志。如果需要进一步定位至代码行，开发者可以通过用户描述或流水日志等手段推测故障复现路径，并参考[开发态问题分析方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section796854014215)使用DevEco Studio的Profiler调优功能抓取相关内存调用栈日志。

## 运维态问题分析方法

对于运维态通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)感知到的资源泄漏故障，开发者可以优先参考[ASHMEM内存基础维测日志分析方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section170311436201)对获取到的基础维测日志进行分析，初步定界至相关业务。如果已经通过[内存栈日志获取方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section2689241446)获取到了应用内存栈维测日志，那么可以尝试根据[内存栈日志分析方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section94641340515)定位至泄漏点。

### ASHMEM内存基础维测日志分析方法

在出现ASHMEM内存泄漏的场景下，开发者可借助[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)获取ASHMEM基础维测日志，并以LOGGER\_MEMCHECK\_PROC\_INFO为关键字检索，得到如下维测日志：

```text
*****************************
LOGGER_MEMCHECK_PROC_INFO
ASHMEM_PROCESS_INFO
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
Process_name	Process_ID	Fd	Cnode_idx	Applicant_Pid	Ashmem_name	                Virtual_size	Physical_size	magic
com.example.lk	23632	        62	328330	        1635	        dev/ashmem/com.example.lk	307200	        16384	        320323
com.example.lk	23632	        64	328330	        23632	        dev/ashmem/XXXXXXXXXX	        2097090436	1951203328	320364
com.example.lk	23632	        65	328330	        23632	        dev/ashmem/XXXXXXXXXX	        2097090436	2097090560	320365
com.example.lk	23632	        66	328330	        23632	        dev/ashmem/XXXXXXXXXX	        2097090436	2097086464	320354
com.example.lk	23632	        67	328330	        23632	        dev/ashmem/Create PixelMap	2097090436	33812480	320369
---------------------------------------------------------------------------------
************ endl ************
```

**说明** 

ASHMEM内存维测日志中，一行代表申请的一个ASHMEM内存的句柄，magic是ASHMEM的唯一标识符。如果遇到两行ASHMEM的magic一致，说明两个ASHMEM句柄指向了同一块ASHMEM内存，在计算总内存占用的时候要做去重处理。

开发者可以先排查Physical\_size较大或者存在大量重复Physical\_size的ASHMEM内存，筛选出可疑的内存块。开发者可以根据ASHMEM内存块的Ashmem\_name初步排查可疑的业务。

对于与PixelMap相关的ASHMEM内存，推荐开发者使用[setMemoryNameSync()](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)和[OH\_PixelmapNative\_SetMemoryName()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)方法自定义ASHMEM内存标签。发生ASHMEM内存泄漏问题时，开发者可以根据ASHMEM块的名字快速锁定哪张图片存在问题，反推至对应的问题组件与业务场景。

### 内存栈日志分析方法

通过[内存栈日志获取方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section2689241446)获取到内存栈日志后，开发者可以将内存栈日志导入DevEco Studio中，分析其中可疑的内存调用栈，排查潜在的内存泄漏点。具体操作步骤如下：

1. 单击下图1处导入文件按钮导入内存栈日志。
2. 单击All Anonymous VM下的VM:ASHMem泳道查看ASHMEM内存申请的调用栈，如下图2处。
3. 单击下图3处Call Trees查看内存申请调用栈。
4. 单击下图4处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
5. 找到异常申请的内存及其调用栈，如下图5、6处框选的内容。这里建议将Bytes从大到小排序，按照申请大小顺序排查内存调用栈，分析可疑的内存泄漏点。
6. 结合调用栈对代码进行分析，找到泄漏根因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/2w2t7gQ5R4WtVDS3inXWEA/zh-cn_image_0000002699731892.png)

## 开发态问题分析方法

针对开发验证过程中遇到的ASHMEM内存泄漏问题，开发者可借助hidumper或DevEco Studio的Profiler调优功能等工具，在本地复现问题并抓取维测日志进行分析。

### 故障分析工具说明

开发者如果在开发态遇到ASHMEM内存泄漏的问题可以尝试使用以下开发态工具进行分析：

* [hidumper](../harmonyos-guides/hidumper.md)：开发者可以使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的"hidumper --mem pid --show-ashmem"命令获取指定进程的内存使用情况，并打印ASHMEM内存详细信息。这里获取到的ASHMEM内存详细信息等效于开发者通过运维态订阅方式拿到的ASHMEM内存泄漏故障日志，执行命令后的输出结果如下：

  ```screen
  # hidumper --mem 46206 --show-ashmem

  -------------------------------[memory]-------------------------------

                               Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
                             Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
                            ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
                   ------------------------------------------------------------------------------------------------------------------------------------------------------
                 GL           2048              0              0              0           2048              0              0              0              0              0
              Graph              0              0              0              0              0              0              0              0              0              0
        ark ts heap           8633           1496              0           8512              0            548             36              0              0              0
  arkts-static heap              0              0              0              0              0            340             10              0              0              0
              guard              0              0              0              0              0              0              0              0              0              0
        native heap          22437           7372              0          21432              0          28708           1012          52784          50958           1966
               .hap            280              0              0            280              0              0              0              0              0              0
     AnonPage other           1871            360              0           1796              0           6144            143              0              0              0
              stack            360              0              0            360              0              0              0              0              0              0
                .db             32              0              0             32              0              0              0              0              0              0
                .so          10652          53840           3956           2560           1308          31812            776              0              0              0
                dev             15              0            364             12              0              0              0              0              0              0
               .ttf            165            924              0              0              0              0              0              0              0              0
     arkweb-pa heap              0              0              0              0              0            120              4              0              0              0
     FilePage other        4095893           2240            272             68        4095484           3576            118              0              0              0
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
              Total        4144485          66232           4592          35052        4098840          71248           2099          52784          50958           1966

  native heap:
    jemalloc meta:           960             84              0            944              0            724             32              0              0              0
    jemalloc heap:         19937           2848              0          19420              0          27696            979              0              0              0
         brk heap:          1508           4440              0           1036              0            288              1              0              0              0
        musl heap:            32              0              0             32              0              0              0              0              0              0

  Purgeable:
          PurgSum:0 kB
          PurgPin:0 kB

  DMA:
              Dma:0 kB

  Ashmem:
  Total Ashmem:4095584 kB
  Process_name    Process_ID      Fd      Cnode_idx       Applicant_Pid   Ashmem_name     Virtual_size    Physical_size  magic
  com.example.lk  46206   50      328444  1859    dev/ashmem/com.example.lk       307200  16384   834850
  com.example.lk  46206   64      328444  46206   dev/ashmem/XXXXXXXXXX   1048464400      1048465408      837698
  com.example.lk  46206   65      328444  46206   dev/ashmem/XXXXXXXXXX   1048464400      1048465408      837708
  com.example.lk  46206   66      328444  46206   dev/ashmem/XXXXXXXXXX   1048464400      1048465408      837709
  com.example.lk  46206   67      328444  46206   dev/ashmem/XXXXXXXXXX   1048464400      1048465408      837710
  ```

  开发者可以通过"Ashmem:"段落中"Total Ashmem"的值观察应用ASHMEM内存使用趋势，若该值持续增长且不回落，则说明应用存在ASHMEM内存泄漏的风险。

* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio的Profiler调优功能对应用进程的内存申请趋势以及内存申请调用栈进行分析，定位出具体泄漏点。更多功能可参考[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

**说明** 

hidumper命令行工具更多用于实时观察应用的内存占用和ASHMEM内存使用情况，无法帮助开发者直接定位到内存泄漏点，更多用于脚本压测。而DevEco Studio的Profiler调优功能不仅能图形化展示应用的内存增长趋势，还可以抓取出录制过程中应用申请的内存和对应的内存调用栈。因此，推荐开发者在开发态分析问题时优先使用DevEco Studio的Profiler调优功能分析ASHMEM内存泄漏问题。

### 故障分析方法

开发者在调试过程中，如果遇到应用闪退或者冷启动问题，可以通过[订阅资源泄漏事件](bpta-stability-ashmemleak-fault-mode-overreview.md#section84828182411)或者[订阅应用终止事件](bpta-stability-ashmemleak-fault-mode-overreview.md#section19969124021018)感知当前是否发生了ASHMEM内存泄漏故障。确认问题为ASHMEM内存泄漏后，推荐开发者按照以下步骤使用DevEco Profiler调优工具定位泄漏问题：

1. 启动Allocation分析：使用DevEco Studio的Profiler工具中的Allocation功能录制应用内存数据，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。
2. 复现泄漏场景：启动抓取后，遍历可疑的泄漏场景。
3. 分析内存栈日志：抓取完成后，结合[内存栈日志分析方法](bpta-stability-ashmemleak-fault-mode-overreview.md#section94641340515)定位内存泄漏点。
