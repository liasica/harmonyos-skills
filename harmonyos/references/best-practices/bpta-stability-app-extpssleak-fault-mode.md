---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-extpssleak-fault-mode
title: 应用泛PSS内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > 泛PSS内存泄漏故障模式说明 > 应用泛PSS内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:2736e2acb2fb65c7fbf52706e3277d23bc2d1023cd5a4342a860e661c36ac5ee
---

## 概述

应用独自持有的PSS、GPU和DMA等内存作为进程泛PSS内存的主要组成部分，任何内存使用不当都会导致应用泛PSS内存的膨胀。本文旨在为开发者介绍应用发生泛PSS内存泄漏的主要根因，并基于案例介绍开发态与运维态的问题分析思路。

## 根因描述

泛PSS内存泄漏，是指因应用对PSS、GPU或DMA等内存管理不当，导致整体内存持续膨胀并最终超出系统阈值，从而触发系统主动管控的现象。其诱因可能是单一类型内存占用过大，也可能是多种类型内存共同超标所致。

## 问题分析思路

开发者遇到泛PSS内存泄漏故障时，可以参考[运维态问题分析方法](bpta-stability-extpssleak-fault-mode-overreview.md#section20798125344614)以及[开发态问题分析方法](bpta-stability-extpssleak-fault-mode-overreview.md#section14940175311467)，找到占用最高的内存类型，并按照各类型的内存泄漏问题分析方法进行分析。

## 案例分析

为直观展示泛PSS内存泄漏的根因定位方法，下文结合NativeHeap堆内存申请过大导致泛PSS内存泄漏的负向案例介绍了开发态与运维态下的问题分析过程。

### 案例：NativeHeap堆内存申请过大导致内存泄漏

此负向案例为应用NativeHeap堆内存申请过大，系统检测到应用发生泛PSS内存泄漏后在后台管控此应用，应用切回前台时，发现应用冷启动。

**运维态分析思路**

如果开发者在运维态遇到此问题，可以按照如下步骤进行分析：

1. 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，在应用发生故障后通过事件回调收到如下事件：

   ```screen
   HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"12202262270997654243","bundle_name":"com.example.dfx_test","bundle_version":"1.0.1","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1786362868260_20926.log"],"level":"kill","log_over_limit":false,"memory":{"gpu":0,"ion":0,"pss":4833588,"pss_detail":{".db":32,".hap":41828,".so":14406,".ttf":444,"anon_page_other":0,"ark ts heap":46429,"arkweb-js heap":0,"arkweb-pa heap":5,"dart heap":0,"dev":5,"file_page_other":0,"jsvm heap":0,"kotlin heap":0,"native heap":4726260,"other":0,"rn-hermes heap":0,"stack":424},"rss":0,"sys_avail_mem":10747904,"sys_free_mem":5234728,"sys_total_mem":16032868,"vss":0},"pid":20926,"resource_type":"pss_memory","time":1786362868241,"uid":20020207}}
   ```

   从事件中解析出以下关键信息：

   * "bundle\_name":"com.example.dfx\_test"，说明发生泄漏的进程为com.example.dfx\_test。
   * "resource\_type":"pss\_memory"，说明应用发生的泄漏类型是泛PSS内存泄漏问题。
   * "memory":{"gpu":0,"ion":0,"pss":4833588,"pss\_detail":{......}}，说明应用发生泛PSS内存泄漏时，应用没有使用GPU和DMA内存，而是使用了4833588KB的PSS内存，导致了应用进程的泛PSS内存泄漏问题。开发者可以进一步根据pss\_detail字段展示信息确认是哪个子类型内存出现异常。例如：将本次事件中的pss\_detail字段转为json格式后，可以明确PSS内存占用异常是因为native heap类型的内存使用了4726260KB：

     ```screen
     "pss_detail": {
         ".db": 32,
         ".hap": 41828,
         ".so": 14406,
         ".ttf": 444,
         "anon_page_other": 0,
         "ark ts heap": 46429,
         "arkts-static heap": 15,
         "arkweb-js heap": 0,
         "arkweb-pa heap": 5,
         "dart heap": 0,
         "dev": 5,
         "file_page_other": 0,
         "jsvm heap": 0,
         "kotlin heap": 0,
         "native heap": 4726260,
         "other": 0,
         "rn-hermes heap": 0,
         "stack": 424
     },
     ```
   * "external\_log":["/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_1786362868260\_20926.log"]，说明系统收到了一份关于泛PSS内存泄漏故障的基础维测日志。开发者可以参考[PSS基础日志分析方法](bpta-stability-extpssleak-fault-mode-overreview.md#section28196459359)对故障日志进行分析，初步定界至PSS中的哪个子类型内存出现异常。
2. 通过external\_log获取到基础维测日志后，在故障日志中找到关键字LOGGER\_MEMCHECK\_SMAPS\_INFO，读取数据如下：

   ```screen
                                       Shared      Shared      Private     Private                                                                 
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
   1572612     8           8           0           0           8           0           12          0           37          AnonPage other                   [anon]                                      
   268         0           0           0           0           0           0           20          0           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libadapter_ndk_stub.so
   208580      0           0           0           0           0           0           11148       529         5           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
   2488        0           0           0           0           0           0           168         7           4           .so                              /data/storage/el1/bundle/arkwebcore/libs/arm64/libffmpeg.so
   85380       41824       41824       0           0           41824       0           0           0           3           .hap                             /data/storage/el1/bundle/entry.hap          
   1244        392         392         0           0           392         0           44          44          4           .so                              /data/storage/el1/bundle/libs/arm64/libc++_shared.so
   1096        476         476         0           0           468         8           36          36          4           .so                              /data/storage/el1/bundle/libs/arm64/libentry.so
   40980       12          8           8           0           4           0           12          12          4           .so                              /data/storage/el1/bundle/libs/arm64/libhypersandemo.so
   20          4           4           0           0           4           0           0           0           5           .hap                             /data/storage/el2/base/files/hiappevent/databases/appevent.db-dwr
   32          32          32          0           0           32          0           0           0           1           .db                              /data/storage/el2/base/files/hiappevent/databases/appevent.db-shm
   2048        76          0           0           76          0           0           0           0           1           dev                              /dev/__parameters__/param_sec_dac           
   80          0           0           0           0           0           0           0           0           1           dev                              /dev/__parameters__/param_selinux           
   4           4           0           0           4           0           0           0           0           1           dev                              /dev/__parameters__/u:object_r:accessibility_param:s0
   4           4           0           0           4           0           0           0           0           1           dev                              /dev/__parameters__/u:object_r:ark_profile:s0
   4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libworkschedextension.z.so.bss]       
   4           0           0           0           0           0           0           4           4           1           AnonPage other                   [anon:libxml2.z.so.bss]                     
   72          0           0           0           0           0           0           12          0           1           AnonPage other                   [anon:libxmpsdk.so.bss]                     
   4           0           0           0           0           0           0           4           0           1           AnonPage other                   [anon:libzlib.z.so.bss]                     
   5752        136         133         4           0           132         0           5564        1117        104         native heap                      [anon:native_heap:brk]                      
   47136       952         920         36          0           916         0           896         344         24          native heap                      [anon:native_heap:jemalloc meta]            
   7354880     4657436     4655706     2188        0           4655248     0           94296       68008       11          native heap                      [anon:native_heap:jemalloc]                 
   32          0           0           0           0           0           0           32          32          1           native heap                      [anon:native_heap:meta]                     
   50331648    0           0           0           0           0           0           120         5           5           arkweb-pa heap                   [anon:partition_alloc]                      
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:21023]    
   ......
   ```

   将所有内存按照内存类别（Category）聚类并按照总内存占用排序，找到Pss+SwapPss占用最高的内存类型为native heap，且此类型占用了超过4655706KB的PSS内存和68008KB的SwapPss内存。
3. 通过[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取轻量化NMD维测以及内存调用栈后，参考[运维态问题分析思路](bpta-stability-nativeheap-fault-mode.md#section151162273105)进行下一步分析：
   1. 通过分析以下NMD维测日志，得出：应用申请了12次402653184字节的内存，共申请了4831838208字节，导致应用发生了泛PSS内存泄漏。

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
   2. 将内存栈日志导入DevEco Studio中Profiler工具，并按照[运维态问题分析思路](bpta-stability-nativeheap-fault-mode.md#section151162273105)找到异常申请的内存及其调用栈如下图所示。从筛选出的内存调用栈可以看出这份内存共申请了12次，总共申请了4.5GB内存，单次申请内存约402653184字节，恰好与分析NMD维测日志得到的结果一致，进一步证实此调用栈为泄漏的内存栈。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/EOP7QjIGTbu68uv_Io8vLg/zh-cn_image_0000002699731884.png "点击放大")
4. 分析内存调用栈指向的代码段，发现应用循环申请超大内存未释放，最终导致了泛PSS内存泄漏：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/T2YJ-mU-Q6aqmSFMTvs5UQ/zh-cn_image_0000002729491139.png "点击放大")

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现泛PSS内存泄漏的场景，那么可以通过尝试复现此场景并使用DevEco Studio中Profiler工具的Allocation功能抓取内存异常增长的点。具体分析步骤如下：

1. 启动抓取后，遍历可疑的泄漏场景复现泛PSS内存泄漏问题。
2. 录制完成后，单击All Heap中的Native Heap泳道，发现NativeHeap内存异常增长：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RCQ9nHwMTHOVwkZbB1Tqbg/zh-cn_image_0000002729611099.png)
3. 参考[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)点击Native Heap泳道，找到可疑的内存调用栈如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/DKbrQAycS8ujYc6oLZxLag/zh-cn_image_0000002699891772.png "点击放大")
4. 分析内存调用栈指向的代码段，发现应用正在循环申请超大内存未释放，最终导致了泛PSS内存泄漏：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/9yo2E_5_RR-V-qx3isWGlA/zh-cn_image_0000002699731886.png "点击放大")

**修复建议**

分配与释放的成对匹配：

* 每处malloc()、new必须有对应的free()、delete。
* 重置指针前先释放。

异常安全与提前返回路径：

* 用RAII处理异常分支。
* 减少函数内多个return路径的重复释放代码。
