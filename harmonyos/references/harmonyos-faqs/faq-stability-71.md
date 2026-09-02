---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-71
title: 应用闪退-Native内存(PSS_MEMORY)泄漏问题排查
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用闪退-Native内存(PSS_MEMORY)泄漏问题排查
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3b8062f508de75d22f473b140fa13251c70bcf7ffce4a86129d0e0d29c24aadc
---

## 问题现象

应用在使用过程中出现闪退，hilog日志中PROCESS\_KILL的Reason为Pss Kill，memory\_leak中生成memleak-native-[process\_name]-[pid]的内存泄漏日志文件。

## 背景知识

* 内存泄漏是指程序在申请分配内存后，由于疏忽或错误未能释放已经不再使用的内存空间，导致这部分内存无法被后续的程序使用。随着时间推移，未释放的内存会逐渐累积，最终可能导致系统性能下降甚至崩溃。
* native内存泄漏是一种资源泄漏类型，其检测机制为以应用进程平均动态峰值内存作为基线，当动态内存峰值超过基线值2倍时，判定泄漏，同时触发管控。
* 参考文档[日志获取](../harmonyos-guides/resource-leak-guidelines.md#日志获取)，native内存泄漏会生成三个故障日志文件以供分析：
  + memleak-native-[process\_name]-[pid]-sample.txt：内存采样日志文件，用于观察内存增长趋势，确认泄漏情况。
  + memleak-native-[process\_name]-[pid]-smaps.txt：内存维测日志文件，记录了一些内存相关的统计信息，用于不同泄漏问题的维测。
  + memleak-native-[process\_name]-[pid]-[timestamp].txt：内存栈文件，检测到泄漏后抓取15min内的进程内存trace，用于分析内存分配时的调用栈。
* [Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/README_zh.md)：是一款深入挖掘数据、细粒度展示数据的性能功耗调优工具，可采集CPU调度、频点、进程线程时间片、堆内存、帧率等数据，采集的数据通过泳道图清晰地呈现给开发者，同时通过GUI以可视化的方式进行分析。工具当前为开发者提供了五个分析模板，分别是帧率分析、CPU/线程调度分析、应用启动分析、TaskPool分析、动效分析。

native泄漏问题速查表：

| 序号 | 泄漏类型 | 判断方法 | 解决方案 |
| --- | --- | --- | --- |
| 1 | 堆内存泄漏 | native\_heap:jemalloc的PSS+SwapPSS > Summary的PSS\*0.5 | 找到最大的内存块，解析调用栈，分析业务代码确认泄漏点 |
| 2 | ashmem泄漏 | dev/ashmem的PSS > Summary的PSS\*0.5 | 找到最大Virtual\_size的调用栈，分析业务代码确认泄漏点。 |

## 问题定位

应用进程触发native泄漏的管控后，系统会抓取泄漏相关的信息，在memory\_leak生成三个故障日志文件以供分析。

1. **分析内存采样文件memleak-native-[process\_name]-[pid]-sample.txt。**

   日志规格如下：

   ```txt
   *************************************************************
   *                    ***** READ ME *****                    *
   *************************************************************
   *    RSS: Resident Set Size                                 * <- 物理内存中的内存总量(包含共享内存)
   *    PSS: Proportional Set Size                             * <- 物理内存中的内存总量(均摊共享内存)
   *    PSS = RSS + Offset                                     * <- Offset：按比例均摊的共享内存
   *    TotalPSS = PSS + SwapPSS                               * <- SwapPSS：在Swap空间的进程内存
   *    TotalMem = TotalPSS + AvcMem + MediaMem + GPU + ION    *
   *                   ***** Two Modes *****                   *
   *    Estimate Mode: RSS & SwapPSS is real                   *
   *    Real Mode(Realtime with *): everything is real         *
   *                   ***** OTHER MEM *****                   *
   *    GPU: GPU mem of process                                * <- 进程使用的GPU内存
   *    ION: ION mem of process                                * <- 进程使用的ION内存
   *    MediaMem: apply mem through media_service              * <- 进程通过Media Kit创建的内存
   *    AvcMem: apply mem through avcodec_service              * <- 进程通过AVCodec Kit创建的内存
   *    ~ means negligible memory(safe to ignore in analysis)  * <- ~ 表示内存占用可以忽略不计（在分析中可以安全地忽略）
   *************************************************************
   *                   ***** Attention *****                   *
   *    Formulas about TotalMem and sub-items may change,      *
   *    please reference current annotation formula            *
   *************************************************************

   pid:	12448
   processName:	com.hx.example
   SoftThreshold:	1992294(KB)    <- 进程基线，五次超过该基线则上报泄漏
   HardThreshold:  3040870(KB)    <- 进程硬门限，两次超过则上报泄漏

   Index   RSS(KB)     Offset(KB)  PSS(KB)     SwapPSS(KB)     TotalPSS(KB)    MediaMem(KB)    AvcMem(KB)      ION(KB)         GPU(KB)         TotalMem(KB)    Level   RunningTime(s)  Realtime
   4       2503640     0           2503640     50380           2554020         ~               ~               151908          1760            2707688         W       235016          2026/01/03 22:47:42
   5       2529104     0           2529104     50352           2579456         ~               ~               151908          1760            2733124         W       235136          2026/01/03 22:49:42
   6       2582704     0           2582704     55284           2637988         ~               ~               151908          1760            2791656         W       235256          2026/01/03 22:51:42
   7       2650688     0           2650688     55304           2705992         ~               ~               151908          1760            2859660         W       235376          2026/01/03 22:53:42
   8       2812108     0           2812108     53196           2865304         ~               ~               153396          1760            3020460         W       235496          2026/01/03 22:55:42
   9       2813904     -162851     2651053     4767            2655820         ~               ~               153396          1760            2810976         W       235496          *2026/01/03 22:55:42
   10      2912612     -162851     2749761     53036           2802797         ~               ~               153396          1760            2957953         W       235616          2026/01/03 22:57:42
   11      3132364     -162851     2969513     53684           3023197         ~               ~               153396          1760            3178353         E       235856          2026/01/03 23:01:42
   12      3410748     -162851     3247897     56040           3303937         ~               ~               153396          1760            3459093         E       236096          2026/01/03 23:05:42
   ```

   TotalMem逐渐增长多次触发了门限，排查各列同步增长情况，分析出哪种类型的内存造成了增长。本例中观察到是PSS内存。
2. **分析内存维测文件memleak-native-[process\_name]-[pid]-smaps.txt。**

   日志规格如下：

   ```txt
   Generated by HiviewDFX @OpenHarmony
   LOGGER_MEMCHECK_GERNAL_INFO
   	pidNumber: 12448
   	processName: com.hx.example
   	PidStartTime: 33055318
   	RealPssMemory: 2810976

   ******************************
   LOGGER_MEMCHECK_MEMINFO   <- 整机内存统计信息
   MemTotal:       11737892 kB
   MemAvailable:    1590272 kB
   SwapTotal:       8388608 kB
   IonTotalUsed:     748340 kB
   GpuTotalUsed:     263744 kB
   AshmemUsed:       376970 kB
   // ...
   ************ endl ************

   *****************************
   LOGGER_MEMCHECK_SMAPS_INFO  <- 进程Smaps汇总信息，Smaps是Linux的proc文件系统提供的查看系统下运行进程内存使用情况的文件
   get info realtime:	2026/01/03 22:55:42  <- 信息获取时间

   -------------------------------[memory]-------------------------------

                                       Shared      Shared      Private     Private                                                                 
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
   1298176     83240       83240       0           0           83240       0           12          12          447         ark ts heap                      [anon:ArkTS Heap]                         
   1827840     1354712     1351534     3804        0           1350908     0           24088       2883        39          native heap                      [anon:native_heap:jemalloc]               
   13128       11960       11170       0           1472        0           10488       0           0           129         FilePage other                   anon_inode:dev/ashmem/Create PixelMap     
   3792        3792        3742        0           100         0           3692        0           0           79          FilePage other                   anon_inode:dev/ashmem/EXTRawData          
   // ...
   46758840    2820652     2661268     180936      12028       2571940     55748       53192       4479        12558                                        Summary
   *****************************
   LOGGER_MEMCHECK_PROC_INFO  <- ashmem/ion/gpu对应泄漏内存节点信息打印(泄漏类型不同，落盘的内存信息不同)
   ASHMEM_PROCESS_INFO
   realtime:	2026/01/03 22:56:01
   Process ashmem overview info:  <- 所有进程ashmem概览信息
   ---------------------------------------------------------------------------------
   Process_name Virtual_size Physical_size
   Total ashmem  of [com.hx.example] virtual size is  37333276, physical size is 34271232 
   // ...
   Process ashmem detail info: <- 进程ashmem详细信息
   ---------------------------------------------------------------------------------
   Process_name	Process_ID	Fd	Cnode_idx	Applicant_Pid	Ashmem_name	Virtual_size	Physical_size	magic
   com.hx.example	12448	612	328359	12448	dev/ashmem/srcImageSize-100x100-pixelMapSize-100x100-streamsize-4150-mimetype-jpeg	40000	40960	3791671
   com.hx.example	12448	616	328359	12448	dev/ashmem/Create PixelMap	93000	94208	3820895
   com.hx.example	12448	1618	328359	1418	dev/ashmem/gralloc_shared_attr	4096	4096	3820167
   // ...
   ---------------------------------------------------------------------------------

   ************ endl ************
   // 两次jemalloc的申请情况（两次记录间隔5min），系统会根据两次NMD信息抓取内存栈。
   // NMD：堆内存布局的快照
   // Size：用户申请的内存经过对齐后的大小，jemalloc对齐size的分割是按照一个特定算法算的，8字节是最小单位，从第二个size开始，最小step是16，一个size到它的两倍size之间有4个分档。用户态传入的申请大小会向下对齐到离它最近的size中。
   // Allocated：size申请的总内存。
   ******************************
   LOGGER_MEMCHECK_SAMPLE_NMD_INFO <- 第一次jemalloc的申请情况
   size       allocated         nmalloc         ndalloc
      8        59381096         8322296          899659
   // ...
   128       798179712         6492379          256600
   ************ endl ************

   ******************************
   LOGGER_MEMCHECK_SAMPLE_NMD_INFO <- 第二次jemalloc的申请情况
   size       allocated         nmalloc         ndalloc
      8        79077136        10978034         1093392
   // ...
   128      1060568960         8563116          277421
   ************ endl ************
   ```

   查看进程Smaps汇总信息LOGGER\_MEMCHECK\_SMAPS\_INFO，根据PSS列与SwapPSS列之和与总PSS的比值，找出占用过大的内存类型，根据不同方法定位。

   * 场景一：堆内存泄漏。
     + 判定方法：native\_heap:jemalloc的PSS+SwapPSS > Summary的PSS\*0.5。
     + 定位方法：
       1. 分析两次jemalloc的申请情况LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO，观察allocated列和size列，找到申请总内存最大的size，可能存在泄漏点。

          ```txt
          LOGGER_MEMCHECK_SAMPLE_NMD_INFO
          size       allocated         nmalloc         ndalloc
            8        79077136        10978034         1093392
          // ...
          128      1060568960         8563116          277421   <- 128size的内存块已申请内存allocated最多
          ```
       2. 使用HiSmartPref分析内存栈文件memleak-native-[process\_name]-[pid]-[timestamp].txt，拖拽导入，框选All Heap，选择Created & Existing，找到最大size的调用栈，分析业务代码确认泄漏点。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/oU71ag5bSByIAJBqLXq8dw/zh-cn_image_0000002628554906.png "点击放大")
   * 场景二：ashmem泄漏。
     + 判定方法：dev/ashmem的PSS > Summary的PSS\*0.5。
     + 定位方法：
       1. 分析ashmem内存信息LOGGER\_MEMCHECK\_ASHMEM\_INFO，筛选Process\_name为泄漏应用的数据，排查Virtual\_size列哪个内存块大小出现的次数最多，可能存在泄漏点。

          ```txt
          Process ashmem detail info: <- 进程ashmem详细信息
          ---------------------------------------------------------------------------------
          Process_name  Process_ID  Fd  Cnode_idx  Applicant_Pid     Ashmem_name           Virtual_size	Physical_size	magic
          com.hx.example	12448	  616	328359	 12448	      dev/ashmem/Create PixelMap   12582912	12582912	3820895   <- Virtual_size为12582912bytes出现次数最多
          ```
       2. 使用HiSmartPref分析内存栈文件memleak-native-[process\_name]-[pid]-[timestamp].txt，拖拽导入，框选All Anonymous VM，选择Created & Existing，找到最大Virtual\_size的调用栈，分析业务代码确认泄漏点。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/IZDK2UfvQwKdX5QL33lZaA/zh-cn_image_0000002628395006.png "点击放大")
3. **结合业务代码分析泄漏点。**
   * 排查方向：
     + 堆内存泄漏：
       - 基础对象泄漏：malloc/new等动态分配的内存，未释放。
       - 循环引用：多个智能指针间相互持有，构成环状循环引用，导致智能指针计数未清零而泄漏。
       - 生命周期管理不当：通过系统接口申请系统资源后未释放。
       - 跨语言导致泄漏：ArkTS对象持有native对象导致native内存泄漏。
       - 过量缓存：业务为了性能提升，通过缓存机制保留内存，但是由于缓存机制保护不合理导致泄漏。比如阈值设计不合理，出现代码流程错误导致超预期的数量和大小使用。
       - 业务过载：业务请求方案需要申请内存发送请求，但是业务消费方由于代码流程错误，或负载等原因消费不及时，导致业务过载，内存超预期使用。
     + ashmeme内存泄漏：
       - 如使用了Node-API在native层创建并使用decode()解码获取PixelMap，需排查申请未释放、把PixelMap缓存到应用生命周期的容器类中、引用计数多加等可能。
       - 如使用了JS层的PixelMap，需排查JS对象泄漏或者缓存太多导致PixelMap大量占用，可使用DevEco Studio中的profiler工具抓取两次snapshot，分析对象的增量。
       - pixmap使用的ashmem内存，应用可自定义绑定pixmap名字，当出现ashmem泄漏，快速根据ashmem块的名字锁定哪张图片存在问题，反推至对应的问题组件。JS层API：[setMemoryNameSync](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)，NATIVE层API：[OH\_PixelmapNative\_SetMemoryName()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)。

## 分析结论

* 堆内存泄漏：应用存在native内存泄漏，申请的堆内存不断增加，触发了系统管控导致闪退。
* ashmeme内存泄漏：应用存在ashmem泄漏，使用了PixelMap对象未释放。

## 修改建议

程序需要正确管理分配的资源，使用完毕后需立刻释放。常见泄漏问题修复方法可见[资源泄漏类问题优化建议](../best-practices/bpta-stability-leak-opt.md)和[资源泄漏类问题案例](../best-practices/bpta-scenario-stability-leak.md)。
