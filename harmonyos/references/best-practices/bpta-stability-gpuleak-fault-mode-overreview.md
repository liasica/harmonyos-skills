---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-gpuleak-fault-mode-overreview
title: GPU内存泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > GPU内存泄漏故障模式说明 > GPU内存泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:d4415d30727c486761e25efbed47e2341e5ac67e17e494433da23019441337fe
---

系统会对应用GPU内存进行监控。当应用GPU内存使用超过阈值且整机处于低内存状态时，系统会抓取维测数据并对应用进行管控。本文旨在为开发者介绍系统的GPU内存泄漏检测机制，并提供开发态与运维态的问题分析思路。针对GPU内存泄漏的二级根因，下文以单应用自渲染场景为例提供了相关故障模式说明：

* [单应用自渲染GPU内存泄漏故障模式说明](bpta-stability-gpuleak-self-rendering-fault-mode.md)：应用通过自渲染的形式过量申请GPU内存超过阈值，系统会主动管控问题应用，造成应用前台闪退等体验影响。本文通过应用进行自渲染导致GPU内存泄漏的案例，为开发者提供了开发态和运维态的故障定位以及分析思路。

**说明** 

开发者可通过阅读[内存基础知识](bpta-memory-basic-knowledge.md)了解内存基础概念。

## GPU内存泄漏基本概念与故障检测机制

### GPU内存基础概念

* GPU内存：GPU可访问的存储空间，既包含专用板载显存，也涵盖统一内存管理的缓冲资源。它主要用于存放帧缓冲、纹理、着色器常量、顶点与索引数据，以及计算管线产生的中间结果。
* GPU内存泄漏：已分配的GPU内存（如缓冲、纹理等）因失去引用且未调用相应释放接口，导致资源持续被占用而无法回收复用。

### GPU内存泄漏常见原因

分配后无对应释放：

* 显式调用创建函数（如：CreateTexture()、vmaCreateBuffer()）申请GPU内存后，未在不需要时调用销毁函数。
* 只释放了外层包装对象，忘记释放内部关联的GPU资源。

错误路径或异常分支遗漏释放：

* GPU内存分配成功但在后续初始化失败时直接返回，跳过了清理代码。
* 应用在循环内部分配GPU资源，每次迭代都重新分配但不在迭代结束时释放。

### GPU内存大小获取方式

开发者可以通过[OH\_HiDebug\_GetGraphicsMemory()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_getgraphicsmemory)方法读取到当前应用进程的GPU内存占用，和预期GPU内存占用比较，判断应用自身是否发生了GPU内存泄漏故障。

### GPU内存泄漏检测原理

系统会周期性或在分配GPU内存时监控应用的GPU内存使用总量，如果应用进程GPU内存总量超过阈值，那么系统会判定该应用发生了GPU内存泄漏。

对于已确认泄漏的问题应用，系统将采取主动管控策略。该策略的触发需同时满足以下两个前置条件：

* 应用自身泄漏：应用GPU内存大于一定阈值，超出合理使用范围。
* 整机资源紧张：整机进入低内存状态。

只有在上述条件均成立时，系统才会对问题应用执行管控操作（终止进程），从而优先保障整机稳定性，避免因资源耗尽导致黑屏、卡死等严重故障。

**说明** 

1. 低端设备的内存总量较小，更容易进入低内存状态。

2. 整机压力影响因素较多，应用需要关注自身内存是否超阈值，是否超出合理使用范围，只要超出或接近阈值，就需要进行相关优化，提升应用保活成功率和良好的使用体验。

## 故障感知

开发者可以按需订阅相关故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，故障事件中包含应用申请的GPU内存大小等内存信息，同时会附带GPU内存基础维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，如果应用发生了GPU内存泄漏故障，那么事件的Reason会显示ResourceLeak(GpuLeak)、ResourceLeak(GpuRsLeak)或者GpuKiller。开发者可以通过监听此事件，快速判断本次发生的故障类型，也可以与其他应用终止事件汇总分析此类故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)感知应用GPU内存泄漏问题，当事件参数中的resource\_type为gpu\_memory时，表明应用进程发生了GPU内存泄漏，收到的资源泄漏事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"11235809489999226959","bundle_name":"com.example.dfx_test","bundle_version":"1.0.1","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1779983144774_34482.log"],"level":"warning","log_over_limit":false,"memory":{"gpu":6263288,"ion":0,"pss":0,"rss":68264,"sys_avail_mem":2196480,"sys_free_mem":1207616,"sys_total_mem":16035444,"vss":71521476},"pid":34482,"resource_type":"gpu_memory","time":1779983144721,"uid":20020198}}
```

### 订阅应用终止事件

应用触发GPU内存泄漏故障后，可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因，如果reason为ResourceLeak(GpuLeak)、ResourceLeak(GpuRsLeak)或者GpuKiller，说明本次应用终止原因为应用发生了GPU内存泄漏故障，开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明，收到的应用终止事件示例如下：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"616930575450354120","bundle_version":"1.0.1","foreground":true,"reason":"GpuKiller","time":1777877700534}}
```

对于GPU内存泄漏故障，不同的退出原因代表了不同的管控形式或泄漏原因：

| Reason | 管控原因 |
| --- | --- |
| GpuKiller | 应用自渲染申请GPU内存超过系统前台管控阈值，系统会在整机进入低内存时管控问题应用。通常表现为应用前台闪退。 |
| ResourceLeak(GpuLeak) | 应用自渲染申请GPU内存超过系统周期检测阈值触发的系统管控，通常表现为应用后台冷起。 |
| ResourceLeak(GpuRsLeak) | 应用统一渲染造成系统render\_service进程占用GPU过大触发的系统管控，通常表现为应用前台闪退。 |

**说明** 

如果应用在同一个生命周期内触发多次故障上报，那么这几次故障事件会持有相同的app\_running\_unique\_id，开发者可以根据app\_running\_unique\_id对应用发生的多个故障进行关联。

## 日志规格与日志获取

系统会在检测到应用发生GPU内存泄漏后，通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径，并对提取出的维测日志进行分析。

### 日志规格

对于GPU内存泄漏故障，开发者可以结合以下几种维测日志进行问题分析：

* GPU内存基础维测日志，记录了应用申请GPU内存的详细分布，详细信息可参考[ashmem/ion/gpu/gpu\_rs内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemiongpugpu_rs内存泄漏日志规格)中gpu/gpu\_rs内存泄漏维测信息。
* GPU内存栈，记录了抓栈期间进程申请的GPU内存的调用栈，详细信息可参考[内存栈](../harmonyos-guides/resource-leak-guidelines.md#内存栈-1)。

### 内存栈日志获取方法

GPU内存泄漏的运维态维测日志仅包含GPU内存基础维测日志，如果需要进一步定位至代码行，可以参考以下方法获取内存栈日志进行下一步分析：

* 通过订阅[应用灰度采集](../harmonyos-guides/hiretrieval.md)，在运维态订阅GPU内存调用栈日志。
* 应用自行通过[获取显存信息](../harmonyos-guides/hidebug-guidelines.md#获取显存信息)接口监控GPU内存使用量，在合理的时机调用[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)方法主动采集内存调用栈日志。
* 通过用户描述、资源泄漏事件中的页面切换信息或流水日志等信息推测故障复现路径，参考[开发态问题分析方法](bpta-stability-gpuleak-fault-mode-overreview.md#section6388155112816)使用DevEco Studio的Profiler调优功能抓取相关内存调用栈日志。

## 运维态问题分析方法

### GPU内存基础维测分析方法

开发者可以通过分析GPU占用分布来判定当前的二级根因：

* 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到故障日志：GPU内存基础维测日志。
* 在GPU内存基础维测日志中通过LOGGER\_MEMCHECK\_PROC\_INFO关键字找到GPU内存维测信息：

  ```screen
  LOGGER_MEMCHECK_PROC_INFO
  ctx_141      14981      14981 used summary:2064384000 grow:0 driver:700416 kmd:671744 jit:0 map:12 0 0
  com.example.dfx_test
  Total U(device): 216329800
  Total A(device): 271974400
  Total P(device): 0
  Total U(host): 13404608
  Total A(host): 14221312
  Total P(host): 0
  C: vulkan default device : 4976200
  C: vulkan image : 209715200
  C: vulkan hebc header : 1638400
  C: cq memory(not in total memory) : 819200
  C: vulkan default device (Total memory: 4976200)
    1:                  200 / 200
    6:                  400 / 16000
    7:                  600 / 38400
    8:                  200 / 32000
    9:                  200 / 89600
   11:                  200 / 204800
   13:                  200 / 1318400
   15:                  200 / 3276800

  C: vulkan image (Total memory: 2097152000)
   21:                  200 / 2097152000

  C: vulkan hebc header (Total memory: 1638400)
   14:                  200 / 1638400

  C: cq memory(not in total memory) (Total memory: 819200)
   13:                  200 / 819200

  C: vulkan external memory(not in total memory) (Total memory: 0)
   (empty)

  C: host default memory (Total memory: 1473600)
    5:                  400 / 6400
    6:                  600 / 25600
    7:                  400 / 32000
    8:                 1200 / 185600
    9:                 1200 / 384000
   10:                  200 / 102400
   11:                  600 / 737600

  C: host internal memory (Total memory: 11574208)
    5:                  400 / 6400
    7:                10498 / 1007808
    8:                  200 / 38400
    9:                 2600 / 832000
   10:                  600 / 523200
   11:                 1000 / 1552000
   16:                  200 / 7614400

  ......
  ```
* 分析每个通道（“C:”或者“Channel:”）的GPU内存占用（“Total memory”），通过排序找到占用最大的GPU内存类型，并按照如下规则定位至二级根因：

  | 关键字 | 二级根因 |
  | --- | --- |
  | C: vulkan | vulkan内存申请/释放没有配对。 |
  | C: gles、Channel: Texture、Channel: Buffer | OpenGLES内存申请/释放没有配对。 |
  | C: cl | OpenCL内存申请/释放没有配对。 |
* 例如通过以下信息可以确认当前GPU内存泄漏故障的二级根因为vulkan内存申请/释放没有配对：

  ```screen
  C: vulkan image (Total memory: 2097152000)
   21:                  200 / 2097152000
  ......
  ```

  "21: 200 / 2097152000"表示2^20~2^21字节大小的GPU内存，申请了200次，总占用2097152000字节。开发者可以根据场景以及纹理（vulkan主要用于纹理渲染等用途）申请大小排查泄漏点。

### 内存栈日志分析方法

通过[内存栈日志获取方法](bpta-stability-gpuleak-fault-mode-overreview.md#section2689241446)获取到内存栈日志后，开发者可以将内存栈日志导入DevEco Studio中，分析其中可疑的内存调用栈，排查可疑内存泄漏点：

* 单击下图①处导入文件按钮导入内存栈日志。
* 基于前置分析的二级根因单击选择不同的泳道，如下图②处：应用发生的是Vulkan内存泄漏，因此选择Vulkan泳道。开发者也可以根据哪个泳道的GPU内存存在明显增长趋势，来确定当前的GPU内存泄漏问题属于哪个二级根因。
* 单击③处Call Trees查看内存申请调用栈。
* 单击④处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
* 找到内存申请异常的内存及其调用栈，如下图⑤、⑥处框选的内容。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ekpOVYPrQQGvqFNa9AAS0Q/zh-cn_image_0000002710303851.png)
* 结合调用栈对代码进行分析，找到泄漏根因。

## 开发态问题分析方法

对于在开发验证过程中遇到的GPU内存泄漏问题，或者运维态遇到的已知场景的GPU内存泄漏问题，开发者可以在本地使用DevEco Studio的Profiler调优功能、hidumper等开发工具对问题进行复现并抓取维测进行分析。

### 故障分析工具说明

开发者如果在开发态遇到GPU内存泄漏的问题可以尝试使用以下开发态工具进行分析：

* [hidumper](../harmonyos-guides/hidumper.md)：在内存泄漏故障问题定位分析过程中，开发者可以使用以下指令抓取维测辅助问题定位。
  + 使用[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)中的“hidumper --mem pid”命令获取指定进程的内存使用情况，pid为指定的进程号。其中，第“GL”行第“Pss Total”列为当前进程使用的GPU内存使用总量。执行命令后的输出结果如下：
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
* [hiprofiler](../harmonyos-guides/hiprofiler.md)：开发者定界当前问题为GPU内存泄漏问题时，可以通过[抓取指定进程GPU图形内存调用栈](../harmonyos-guides/hiprofiler.md#抓取指定进程gpu图形内存调用栈)进行分析。
* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio的Profiler工具中的Allocation功能对应用进程的内存申请趋势以及内存申请调用栈进行分析，定位出具体泄漏点。使用指导可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。

### 故障分析方法

* 开发者在调试过程中，如果遇到应用闪退或者冷起问题，可以在DevEco Studio中找到日志组件如下图①处，再选择应用终止如下图②处，单击③选择应用进程名，筛选出调试应用的历史退出原因，如果原因为“GpuKiller”或者“ResourceLeak:Gpu Leak”如下图④所示，说明应用在调试过程中发生了GPU内存泄漏故障。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/pG22BX24TEa60cWL9E2q5g/zh-cn_image_0000002680464202.png "点击放大")

* 确认问题为GPU内存泄漏后，开发者可以使用DevEco Studio的Profiler工具中的Allocation功能进行分析，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。
* 启动录制前可以先在Allocation的配置页中执行如下准备工作：
  + 单击①处过滤泳道按钮，单击②处增加勾选Graphic Memory泳道。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/st4HiXirT9qMsAzoSz_WAQ/zh-cn_image_0000002710144015.png "点击放大")
  + 单击①处录制设置按钮，单击②处打开JS栈记录开关，单击③处打开异步回栈开关。由于NativeHeap的Malloc频率非常高，因此可以单击取消勾选④处Malloc复选框，不抓取应用Malloc内存分配栈，减少对GPU内存分析的影响。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/cp_AQ8uqQD6MOE58TPWHgA/zh-cn_image_0000002680624100.png "点击放大")
* 启动抓取后，可做正常的用户操作，遍历可疑的泄漏场景。
* 抓取完成后，结合[内存栈日志分析方法](bpta-stability-gpuleak-fault-mode-overreview.md#section94641340515)定位内存泄漏点。
