---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-leak-guidelines
title: Resource Leak（资源泄漏）检测
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > Resource Leak（资源泄漏）检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d57d3d7c9f2742bda4e014ac994a5574d3e0beff8a80c58ccf98bae5dc42b7fe
---

## 简介

资源泄漏是指句柄、线程或内存等资源，在应用运行过程中没有被正确释放，导致资源被长期占用且无法被其他应用使用，如果某一类资源耗尽，系统可能出现卡死或重启等异常情况。为了应对资源泄漏问题，系统会提供资源泄漏检测、判决、维测日志抓取、日志上报的能力，为开发者提供详细的维测日志以辅助故障定位。本文将主要介绍[资源泄漏检测能力](resource-leak-guidelines.md#实现原理)以及[资源泄漏日志的规格](resource-leak-guidelines.md#日志获取)。

## 基本概念

资源泄漏主要分为三类：内存泄漏、句柄泄漏和线程泄漏。对于每种泄漏，系统会通过周期采样的方式对进程的资源使用情况进行检测，如果资源使用超过阈值，会抓取对应维测并上报泄漏事件。通过Hiappevent资源泄漏事件进行订阅，订阅方法详见[资源泄漏事件](hiappevent-watcher-resourceleak-events.md)。

## 实现原理

资源泄漏具体检测方式如下：

| 泄漏类型 | 检测机制 |
| --- | --- |
| 句柄泄漏（FD\_LEAK） | 每隔60s遍历一次进程，获取进程fd句柄总数，超过**阈值（5000个）** 时抓取详细句柄信息，同步上报泄漏。 |
| 线程泄漏（THREAD\_LEAK） | 每隔60s遍历一次进程，获取进程的总线程数，超过**阈值（700个）** 时抓取详细线程名信息，同步上报泄漏。 |
| 内存泄漏（MEMORY\_LEAK） - JS泄漏（JS\_LEAK） | 虚拟机内部进行插桩，当**堆内存的使用率超过85%**或者**触发OOM时**会抓取heapdump，同步上报该故障。 |
| 内存泄漏（MEMORY\_LEAK） - native内存泄漏（PSS\_MEMORY） | 以应用进程平均动态峰值内存作为基线，以200s作为基准，当**动态内存峰值超过基线值2倍时，判定泄漏，同时触发管控。** |
| 内存泄漏（MEMORY\_LEAK） - ashmem/ion/gpu等内存泄漏（KERNEL\_MEMORY） | 基于ashmem/ion/gpu的基线值，超过基线值时会判定泄漏，同步抓取维测信息。 |

说明

1. 表格中所述阈值/基线均为系统默认，如果生态在开发过程中需要自行设定基线，可以使用[hidebug.setAppResourceLimit接口](../harmonyos-references/js-apis-hidebug.md#hidebugsetappresourcelimit12)进行设置，该接口建议在开发阶段调用，不要在正式发布阶段使用。
2. 虚拟机内存使用率计算公式 = heapUsed / totalHeap。

   heapUsed：当前虚拟机使用的堆大小，单位：KB。可通过[hidebug.getAppVMMemoryInfo()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappvmmemoryinfo12)接口获取。

   totalHeap：当前虚拟机的堆总大小，单位：KB。可通过[hidebug.getAppVMMemoryInfo()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappvmmemoryinfo12)接口获取。
3. 当应用上报JS\_ERROR/CPP\_CRASH故障，Error message包含“OutOfMemory”时，可参考[内存泄漏分析方法](../best-practices/bpta-stability-leak-way.md#section728319329442)辅助定位。
4. 管控是指当系统判定应用发生泄漏后，主动终止泄漏应用的行为。

## 约束和限制

1. 句柄泄漏调用栈、native内存泄漏调用栈、js泄漏内存快照等维测因为开销较大，所以在[nolog版本](performance-analysis-kit-terminology.md#nolog版本)默认不开启。
2. 如果开发者希望获取到nolog版本的js泄漏内存快照，可参考[资源泄漏事件订阅（ArkTS）](hiappevent-watcher-resourceleak-events-arkts.md)增加对nolog版本js内存快照的订阅。

## 日志获取

资源泄漏日志由LeakDetector模块进行管理，可通过以下方式获取：

* 方式一：通过[DevEco Testing进行探索测试](exploratory-testing.md)并获取日志。

  DevEco Testing工具会收集设备/data/log/reliability/resource\_leak/路径下的资源泄漏故障日志，根据进程名、故障和时间分类显示。

  | 泄漏类型 | 日志文件名称 |
  | --- | --- |
  | 句柄泄漏（FD\_LEAK） | [pid]\_fd\_leak.txt |
  | 线程泄漏（THREAD\_LEAK） | [pid]\_thread\_leak.txt |
  | 内存泄漏（MEMORY\_LEAK） - js泄漏（JS\_LEAK） | memleak-js-[process\_name]-[pid]-[tid]-[timestamp].rawheap |
  | 内存泄漏（MEMORY\_LEAK） - native内存泄漏（PSS\_MEMORY） | memleak-native-[process\_name]-[pid]-sample.txt  memleak-native-[process\_name]-[pid]-smaps.txt  memleak-native-[process\_name]-[pid]-[timestamp].txt |
  | 内存泄漏（MEMORY\_LEAK） - ashmem/ion/gpu等内存泄漏（KERNEL\_MEMORY） | memleak-kernel-[module]-0-sample.txt  memleak-kernel-[module]-0-[timestamp].txt |

  注意

  1. native内存泄漏的调用栈（memleak-native-[process\_name]-[pid]-[timestamp].txt）无法直接在DevEco Studio打开，需要修改后缀名为.nas，然后使用DevEco Studio-Profiler-打开并分析，详情见[内存分析及优化](ide-insight-session-allocations-memory.md)。
  2. js泄漏的维测日志 memleak-js-[process\_name]-[pid]-[tid]-[timestamp].rawheap 为二进制内存快照文件，需要通过[translator工具](rawheap-translator.md)转换为.heapsnapshot文件，通过DevEco Studio或浏览器打开展示，详情见[Snapshot离线导入](ide-snapshot-basic-operations.md#section6760173514388)。
* 方式二：通过DevEco Studio主动采集日志。

  DevEco Studio的profiler模块提供[Allocation](ide-insight-session-allocations-memory.md)（获取native调用栈profiler）和 **[Snapshot](ide-arkts-memory-leak-analysis.md)** （获取JS层heapdump）两种采集方式：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/xxEnx5K6SD-R9mOimmne9w/zh-cn_image_0000002558605334.png?HW-CC-KV=V1&HW-CC-Date=20260429T053352Z&HW-CC-Expire=86400&HW-CC-Sign=79C8A91477D1DA1A5E693D3D5C0B514B9D96643AF093218193AF1A5BEA2B20BD)
* 方式三：通过HiAppEvent接口订阅。

  HiAppEvent对外提供故障订阅接口，可以订阅各类故障打点，详见[HiAppEvent介绍](hiappevent-intro.md)，其中资源泄漏的订阅方式详见[资源泄漏事件介绍](hiappevent-watcher-resourceleak-events.md)。资源泄漏故障日志存于/data/storage/el2/log/resourcelimit/路径，日志名统一为RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log，可根据日志内容区分文件类型。

## 句柄泄漏日志规格

故障日志文件名：[pid]\_fd\_leak.txt（**方式一**）或RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log（**方式三**）。

### 日志头部信息

| 字段 | 说明 |
| --- | --- |
| time | 故障发生时间。 |
| pid | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
| process | 应用进程包名。 |
| leaked fd nums | 判定泄漏时获取的句柄数量（快照）。 |

```
1. time: 2024/06/27 11:55:28
2. pid: 1380
3. process: process1
4. leaked fd nums: 5111
```

### 句柄类型详细信息

* **Leaked fd Top 10：** 按照句柄名聚类，获取泄漏句柄中最多的类型。第一列为泄漏数量，第二列为泄漏类型，如下即ashmem类型的句柄存在4796个。

  ```
  1. FdCount FileDescriptor
  2. *****************************
  3. Leaked fd Top 10:
  4. 4796    ashmem
  5. 259 socket
  6. 119 dmabuf
  7. 48 eventfd
  8. 42 sync_file
  9. 17 eventpoll
  10. 3 /sys/kernel/debug/tracing/trace_marker
  11. 3 /dev/null
  12. 2 /dev/hvgr0
  ```
* **Dir Type Top 10：** 针对文件句柄类型，会单独根据文件路径聚类。如下，根据“**Leaked fd Top 10**”无法看出具体泄漏的类型，但是通过“**Dir Type Top 10**”能确定是“/data/storage/el2/database/rdb”路径下的文件句柄泄漏，且能大概感知是db泄漏。

  ```
  1. Dir Type Top 10:
  2. 6175 /data/storage/el2/database/rdb
  3. 5 /dev/urandom
  4. 3 /sys/kernel/debug/tracing/trace_marker
  5. 3 /dev/null
  6. 1 anon_inode:[signalfd]
  7. 1 /dev/binder
  8. 1 /proc/
  9. 1 /system/app/PhoneClone/PhoneClone.hap
  ```

  说明

  若top句柄为unknown，说明维测没有权限获取泄漏进程的句柄。

### 特殊类型句柄维测信息

如果**Leaked fd Top 10**的TOP句柄信息属于ashmem/socket/pipe/sync\_file/dmabuf这五类特殊类型，且该类型的句柄个数超过1000个，日志中会增加整机详细的维测信息，具体如下：

* **ashmem类型句柄**

  ashmem（共享内存），当TOP 1的句柄类型为ashmem时，抓取整机ashmem内存的详细信息如下。

  | 字段 | 说明 |
  | --- | --- |
  | Process\_name | 持有该ashmem内存块的应用进程包名。 |
  | Process\_ID | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
  | Fd | 该进程持有的句柄。 |
  | Applicant\_Pid | 申请该ashmem内存块的进程pid，可根据此字段识别该内存块的申请来源。 |
  | Ashmem\_name | 共享内存的名字，开发者可通过提供的API进行设置，用来判断存储的资源类型，指向不同的领域。 |
  | Size | 单个ashmem块的大小，单位：B。 |

  说明

  开发者可通过提供的API接口设置ashmem内存：

  JS层API：[setMemoryNameSync](../harmonyos-references/arkts-apis-image-pixelmap.md#setmemorynamesync13)。

  NATIVE层API：[OH\_PixelmapNative\_SetMemoryName](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_setmemoryname)。

  ```
  1. *****************************
  2. LOGGER_MEMCHECK_ASHMEM_INFO
  3. Process ashmem detail info:
  4. ---------------------------------------------------------------------------------
  5. Process_name Process_ID Fd Cnode_idx Applicant_Pid Ashmem_name Size
  6. process1 781 18 328233 781 dev/ashmem/PolicyVolumeMap 384
  7. ...........
  8. ...........
  ```
* **socket类型句柄**

  socket（网络通信），当TOP 1的句柄类型为socket时，抓取整机socket内存的详细信息如下。

  | 字段 | 说明 |
  | --- | --- |
  | ProcessName | 持有该socket内存块的应用进程包名。 |
  | ProcessID | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
  | Fd | 该进程持有的句柄。 |
  | inode | 文件系统对象信息。 |
  | PeerTid | 对端tid（对于有连接的socket为对应值，无连接为0）。 |

  ```
  1. Process socket info:
  2. ----------------------------------------------------
  3. ProcessName ProcessID Fd inode PeerTid
  4. process1   6874   3   0    0
  5. ........
  6. .........
  ```
* **pipe类型句柄**

  pipe（进程间通信），当TOP 1的句柄类型为pipe时，以fd维度抓取整机pipe内存的详细信息如下。

  | 字段 | 说明 |
  | --- | --- |
  | ProcessName | 持有该pipe内存块的应用进程包名。 |
  | ProcessID | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
  | Fd | 该进程持有的句柄。 |
  | PipeName | 管道名。 |
  | inode | 文件系统对象信息。 |
  | MaxUsage | 最大使用量。 |
  | NumAccounted | 累计大小量。 |
  | RingSize | RingBuf大小，单位：KB。 |

  ```
  1. Process pipe info:
  2. ------------------------------------
  3. ProcessName ProcessID Fd PipeName inode MaxUsage NumAccounted RingSize
  4. process1 629 7 / 11 16 16 16
  5. process1 629 8 / 11 16 16 16
  6. ........
  ```
* **sync\_file类型句柄**

  sync\_file（显存），当TOP 1的句柄类型为sync\_file时，以fd维度抓取整机sync\_file的详细信息如下。

  | 字段 | 说明 |
  | --- | --- |
  | ProcessName | 持有该sync\_file内存块的应用进程包名。 |
  | ProcessID | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
  | Fd | 该进程持有的句柄。 |
  | FenceName | sync\_file名字。 |
  | inode | 文件系统对象信息。 |
  | FenceNum | fence个数。 |
  | TimelineName | fence的Timeline名字。 |
  | DriverName | 驱动名字。 |
  | Status | fence的状态。 |
  | Timestamp | fence的时间戳。 |

  ```
  1. Process fence info:
  2. ----------------------------------------------------
  3. ProcessName ProcessID Fd FenceName inode FenceNum TimelineName DriverName Status Timestamp
  4. process1 1309 25 NULL 4186 1 0:online_composer_gfx_primary ukmd_release_fence_2941430 1 91607485502500
  5. process1 1309 26 NULL 4186 1 0:online_composer_gfx_primary ukmd_release_fence_2941430 1 91607485502500
  6. ........
  ```
* **dmabuf类型句柄**

  dmabuf（也称ion内存），当TOP 1的句柄类型为dmabuf时，以fd维度抓取了整机dmabuf的详细信息如下 **。**

  | 字段 | 说明 |
  | --- | --- |
  | Process name | 持有该ion内存块的应用进程包名。 |
  | Process ID | 发生故障进程的pid，可以用于在流水日志中搜索相关进程信息。 |
  | Fd | 该进程持有的句柄。 |
  | size | buffer内存大小，单位：B。 |
  | magic | buffer唯一标识（**magic相同表示指向同一块buffer）** 。 |
  | buf->pid | 申请者的pid。 |
  | buf->task\_comm | 申请buffer的进程名。 |

  ```
  1. Process dma_heap info:
  2. ----------------------------------------------------
  3. Process name       Process ID               fd             size            magic         buf->pid   buf->task_comm
  4. process1              971               23          3145728               36              971       process2
  5. process1              971               24          1048576               38              971       process2
  6. ........
  ```

### 句柄栈信息

当判定句柄泄漏后，会hook该进程的pipe/open等系统调用10分钟，抓取调用栈，并基于相同调用栈聚类。如下每一行都是一个调用栈，调用顺序为从右到左，其中num后面的数字表示调用栈总个数，bt后面为具体调用栈。具体栈信息可通过[addr2line](https://llvm.org/docs/CommandGuide/llvm-symbolizer.html)解析到对应的函数。

```
1. *****************************
2. LOGGER_MEMCHECK_FD_STACK_INFO
3. pid: 12326
4. get stack time: 2024/06/17 19:16:48
5. ==============================FdTrack Stack==============================
6. Generated by HiviewDFX @HarmonyOS
7. ==============================Sorted by num==============================
8. num 8272 bt [/system/lib64/libfdleak_tracker.so+0x1fb58] [/system/lib/ld-musl-aarch64.so.1+0x1d3154] [/system/lib/ld-musl-aarch64.so.1+0x148940] [/system/lib64/platformsdk/libuv.so+0x1ab30] [/system/lib64/platformsdk/libuv.so+0x1cbd0] [/system/lib64/module/file/libfs.z.so+0x17109c] [/system/lib64/module/file/libfs.z.so+0x170af4] [/system/lib64/module/file/libfs.z.so+0x1701c8] [/system/lib64/platformsdk/libace_napi.z.so+0x34828]
9. num 3968 bt [/system/lib64/libfdleak_tracker.so+0x1fb58] [/system/lib/ld-musl-aarch64.so.1+0x1d3154] [/system/lib64/platformsdk/libipc_core.z.so+0x4ac64] [/system/lib64/platformsdk/libbackup_kit_inner.z.so+0x532d4] [/system/lib64/platformsdk/libbackup_kit_inner.z.so+0x4f8fc] [/system/lib64/platformsdk/libipc_core.z.so+0x38420] [/system/lib64/platformsdk/libipc_core.z.so+0x4e99c] [/system/lib64/platformsdk/libipc_core.z.so+0x4eb34] [/system/lib64/platformsdk/libipc_core.z.so+0x4edc8]
10. num 3968 bt [/system/lib64/libfdleak_tracker.so+0x1fb58] [/system/lib/ld-musl-aarch64.so.1+0x1d3154] [/system/lib64/platformsdk/libipc_core.z.so+0x4ac64] [/system/lib64/platformsdk/libbackup_kit_inner.z.so+0x532b0] [/system/lib64/platformsdk/libbackup_kit_inner.z.so+0x4f8fc] [/system/lib64/platformsdk/libipc_core.z.so+0x38420] [/system/lib64/platformsdk/libipc_core.z.so+0x4e99c] [/system/lib64/platformsdk/libipc_core.z.so+0x4eb34] [/system/lib64/platformsdk/libipc_core.z.so+0x4edc8]
```

注意

1. 这里统计的是10分钟内全量申请句柄的调用栈，并没有将已经close的去掉。
2. 栈信息只有在log版本直接存在；nolog版本若未开“开发者模式”，则不抓取栈信息，如果发现不存在栈信息，需要在“开发者选项”中打开“系统资源泄漏日志”，并重启设备，来使能资源泄漏的抓栈功能。

### 句柄泄漏聚类规则

应用程序在同一或不同版本上、不同时间产生的泄漏问题可能为同一原因，开发者可以从故障日志中提取故障特征，根据故障特征将多份故障日志进行聚类，以提高泄漏问题的分析效率。

1. 通过[句柄泄漏日志](resource-leak-guidelines.md#句柄泄漏日志规格)中的top10的文件句柄数以及top10的文件路径句柄数判定是哪种类型的句柄泄漏，将占比最多的句柄类型作为本次故障的故障特征。
2. ashmem、ion等特殊类型句柄，可参考[ASHMEM\_LEAK](resource-leak-guidelines.md#ashmemiongpugpu_rs聚类规则)、[ION\_LEAK](resource-leak-guidelines.md#ashmemiongpugpu_rs聚类规则)规则进行聚类。

## 线程泄漏日志规格

故障日志文件名：[pid]\_thread\_leak.txt（**方式一**）或RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log（**方式三**）。

### 日志头部信息

| 字段 | 说明 |
| --- | --- |
| time | 检测到线程泄漏的时间。 |
| pid | 发生故障进程的pid，用于在流水日志中查询相关进程信息。 |
| vss | 单个进程全部可访问的地址空间，其大小可能包括还尚未在内存中驻留的部分，单位：KB。 |
| rss | 单个进程实际占用的内存大小，包括该进程所使用共享库全部内存大小，单位：KB。 |
| process | 发生故障的应用包名。 |
| summary | 判定泄漏时进程线程总数。 |

```
1. time: 2024/06/27 03:45:19
2. pid: 41897
3. vss: 12783644
4. rss: 2229352
5. process: process1
6. summary: 879
```

### 线程类泄漏详细信息

* **Top 10 Thread Name：** 按照线程名聚类，获取泄漏最多的线程，第一列为泄漏数量，第二列为线程名称（若创建线程时未指定线程名，则表现为线程名和进程名相同）。

  ```
  1. Top 10 Thread Name:
  2. 913 process1
  3. 3 gpu-work-client
  4. 2 OS_Actor_402
  5. 1 IPC_11_13795
  6. 1 IPC_12_13796
  7. 1 IPC_13_13797
  ```
* **线程启动信息**：可根据线程启动时间推测。

  | 字段 | 说明 |
  | --- | --- |
  | tid | 检测到泄漏时未释放线程的线程号 |
  | thread\_name | 未释放的线程名 |
  | start\_time(jiffies) | 线程创建时间 |

  ```
  1. ======================================================
  2. tid thread_name start_time(jiffies)
  3. 221 process1 4688297
  4. 240 IPC_3_4318 3081382
  5. ...
  6. ...
  ```
* **线程快照**：抓取判定泄漏时线程的调用栈，可由此看下线程做的任务，推测线程未退出的原因（如：\_\_pthread\_cond\_timedwait表示线程正在等待唤醒）。

  ```
  1. ======================================================
  2. Result: 0 ( no error )
  3. Timestamp:2024-06-27 03:45:20.000
  4. Pid:41897
  5. Uid:1013
  6. Process name:process1
  7. Tid:1527, Name:xxx
  8. #00 pc 00000000001b6464 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(98dc7600a0fc62125e291b93ca336154)
  9. #01 pc 00000000001b8468 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(98dc7600a0fc62125e291b93ca336154)
  10. #02 pc 00000000000c108c /system/lib64/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+20)(9cbc937082b3d7412696099dd58f4f78242f9512)
  11. #03 pc 000000000024654c /system/lib64/platformsdk/xxx.so(mindspore::Worker::WaitUntilActive()+204)(534ce78b66262dc14658c35fa018662f)
  12. #04 pc 000000000023da14 /system/lib64/platformsdk/xxx.so(mindspore::ActorWorker::RunWithSpin()+256)(534ce78b66262dc14658c35fa018662f)
  13. #05 pc 000000000023edb0 /system/lib64/platformsdk/xxx.so(void* std::__h::__thread_proxy[abi:v15004]<std::__h::tuple<std::__h::unique_ptr<std::__h::__thread_struct, std::__h::default_delete<std::__h::__thread_struct>>, void (mindspore::ActorWorker::*)(), mindspore::ActorWorker*>>(void*)+60)(534ce78b66262dc14658c35fa018662f)
  14. #06 pc 00000000001baac0 /system/lib/ld-musl-aarch64.so.1(start+236)(98dc7600a0fc62125e291b93ca336154)
  15. ........
  ```

### 线程泄漏聚类规则

应用程序在同一或不同版本上、不同时间产生的泄漏问题可能为同一原因，开发者可以从故障日志中提取故障特征，根据故障特征将多份故障日志进行聚类，以提高泄漏问题的分析效率。

1. 分析[线程泄漏日志](resource-leak-guidelines.md#线程泄漏日志规格)中展示的top10线程，将占比最多的线程名作为本次故障的故障特征。

   注意

   系统已对同名线程进行了聚类，但是部分特殊场景下，线程名间可能会存在差异，如“IPC\_11\_13795”、“IPC\_12\_13796”，如果开发者希望进一步增强聚类效果，可以将全量线程中的相似进程名作为同一个故障特征，如“IPC\_xx\_xxx”，以提高聚类准确性。
2. 从线程泄漏日志中提取出线程对应的线程快照，并根据调用栈进行聚类。

## JS内存泄漏日志规格

**故障日志文件名：** memleak-js-[process\_name]-[pid]-[tid]-[timestamp].rawheap（**方式一**）或RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log（**方式三**）。

* 该文件记录了对象堆内存的详细信息。
* 日志文件需要将后缀名修改为.rawheap文件，再通过[translator工具](rawheap-translator.md)转换为.heapsnapshot文件，通过DevEco Studio或浏览器打开展示，详情见[Snapshot离线导入](ide-snapshot-basic-operations.md#section6760173514388)。
* API14后，需要将日志文件后缀名修改为.rawheap后，将其导入DevEco Studio并展示，详情见[Raw Heap离线导入](ide-snapshot-basic-operations.md#section6760173514388)。

### JS泄漏聚类规则

应用程序在同一或不同版本上、不同时间产生的泄漏问题可能为同一原因，开发者可以从故障日志中提取故障特征，根据故障特征将多份故障日志进行聚类，以提高泄漏问题的分析效率。

**聚类步骤描述**

1. 确认聚类范围，只聚类top20目录和retained size占5%以上的目录。
2. 通过聚类规则上报的故障进行聚类。为了保证聚类结果的有效性，不同目录下存放的对象不同，聚类规则也不同。
3. 统计各类对象的数量及内存大小，按照对象的数量或内存大小进行排序，找到内存占比最高的对象，作为本次上报故障的故障特征。

**聚类规则**

聚类规则主要分为三种：名称聚类，引用链聚类和属性聚类。不同类型的对象需要使用不同的聚类方法。

1. 名称聚类（通过对象名称进行聚类）

   Function(closure)目录下的对象，按照对象名称聚类，当名称相同时，视为一类。
2. 引用链聚类（通过对象的最短引用链聚类）

   Method，js\_set，Map，string和JSNativePointer等目录下的对象，优先通过引用链聚类。该类对象目录下名称一致，通过引用链可以区分对象创建场景。对比目录下各对象到GC ROOT的最短引用链（如果有多条最短引用链则选择retained size最大的那条引用链），最短引用链相同，则视为一类。
3. 对象名称+引用链聚类

   各类业务对象（业务侧创建的类对象和函数对象）带有路径对象名称和行号信息。相同的类或函数对象调用点不同，则引用链不同，需要根据不同的调用点进行区分。

   此外，framework，jsarray(array)也通过对象名称+引用链聚类。
4. 属性+引用链聚类

   jsobject（js\_shared\_object）目录下对象名称相同，但代表的对象并不一致，需要通过引用链对jsobject对象进行分类，即对不同调用点的jsobject进行区分。

   jsobject对象中存在大量distance为1的对象，这些对象无法通过引用链区分，但可以通过属性进行区分，即直接持有的对象是否一致，如果jsobject对象直接持有的对象名称都相同，且持有关系也相同，则归为一类。
5. 特殊聚类

   5.1 SourceTextModule

   SourceTextModule对象是系统侧创建的，用于持有export对象。每个ts文件会对应生成一个SourceTextModule对象，持有该ts文件中export的对象，因此天然就已经是聚类后的结果，不需要再次聚类。

   5.2 Promise/PromiseRecord/PromiseCapability/PromiseReaction

   异步相关的对象，请根据PromiseReaction下的handle信息+引用链进行聚类。PromiseReaction下的handle信息代表了该异步任务的上一个任务，可以通过上一个任务进行区分。

   5.3 proxy

   proxy往往与框架对象强相关，可以通过proxy下的target信息（handle）+引用链进行聚类。proxy下的target信息代表了proxy持有的被代理对象，proxy本身无意义，需要根据被proxy代理的对象进行区分。
6. 除上述类型外的其他基本类型：

   其他基本类型对象默认按照最短引用链聚类。

## native内存泄漏日志规格

**故障日志文件名：** 泄漏日志获取中方式一和方式三文件名不同，方式三为RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log，根据内容区分，方式一如下所示：

### 内存采样

日志文件：memleak-native-[process\_name]-[pid]-sample.txt，里面展示了进程号，进程名，基线值，内存采样的情况，可以直观的观察到内存的变化情况。

| 字段 | 说明 |
| --- | --- |
| SoftThreshold | 系统设定的该进程基线（也可由应用自身通过setAppResourceLimit接口设置），应用内存连续五次超过进程基线即上报内存泄漏事件，单位：KB。 |
| HardThreshold | 系统设定的进程硬门限，应用内存连续两次超过硬门限即上报内存泄漏事件，单位：KB。 |
| PSS | 按比例计算的驻留内存大小，共享库的内存按进程数均摊（**带\*的时间精准计算一次进程的PSS使用量**），单位：KB。 |
| Offset | 将共享库内存均摊后的偏差：RSS + Offset = PSS **（用于矫正后续不带\*号的PSS估算值）** ，单位：KB。 |
| RSS | 进程实际驻留在物理内存中的内存总量（包含共享库占用的全部内存），单位：KB。 |
| SwapPSS | 进程实际交换出去（即写入swap空间）的内存总量，单位：KB。 |
| TotalPSS | 进程PSS使用量的总和，单位：KB。 |
| AvcMem | 进程通过Avcodec\_service创建编解码实例创建的内存，由Avcodec\_service上报给hiview进行统计，单位：KB。 |
| MediaMem | 进程通过Media\_service接口创建的内存，由Media\_service上报给hiview进行统计，单位：KB。 |
| GPU | 进程使用GPU内存，单位：KB。 |
| ION | 进程使用ION内存，单位：KB。 |
| TotalMem | 进程使用的TotalPSS+ION+GPU+AvcMem+MediaMem内存的总和，单位：KB。 |
| Level | 当前进程的泄漏等级简写。 |
| RunningTime | 进程当前生命周期，单位：s。 |
| Realtime | 当前采样的真实时间。 |

```
1. /*************************************************************
2. /*                  ***** READ ME *****                      *
3. /*************************************************************
4. /*                 RSS: Resident Set Size                    *
5. /*                 PSS: Proportional Set Size                *
6. /*                 RSS + Offset = PSS                        *
7. /*                 TotalPSS = PSS + SwapPSS                  *
8. /*   TotalMem = TotalPSS + Av_Mem + Media_Mem + ION + GPU    *
9. /*                 ***** Two Modes *****                     *
10. /*      Estimate Mode: RSS & SwapPSS is real                 *
11. /*      Real Mode(Realtime with *): everything is real       *
12. /*      Media_rss:apply mem through media_service            *
13. /*      Avc_rss:apply mem through avcodec_service            *
14. /*    ~ means negligible memory(safe to ignore in analysis)  *
15. /*************************************************************
16. /*                   ***** Attention *****                   *
17. /*    Formulas about TotalMem and sub-items may change,      *
18. /*    please reference current annotation formula            *
19. /*************************************************************

21. pid: XXXX
22. processName: XXXXXX
23. SoftThreshold: 3500(KB)
24. HardThreshold: 1024000(KB)

26. Index   RSS(KB)     Offset(KB)  PSS(KB)     SwapPSS(KB)     TotalPSS(KB)     MediaMem(KB)   AvcMem(KB)    GPU(KB)       ION(KB)       TotalMem(KB)     Level   RunningTime(s)     Realtime
27. 1       14668       0           14668       5500            20168            ~              ~             ~             ~             20168            W       112             2025/04/23 12:28:02
28. 2       12732       0           12732       5476            18208            ~              ~             ~             ~             18208            W       352             2025/04/23 12:32:01
29. 3       13560       0           13560       5456            19016            ~              ~             ~             ~             19016            W       592             2025/04/23 12:36:02
30. 4       13576       0           13576       5440            19016            ~              ~             ~             ~             19016            W       832             2025/04/23 12:40:02
31. 5       13576       0           13576       5440            19016            ~              ~             ~             ~             19016            W       1072            2025/04/23 12:44:02
32. 6       13584       -8320       5264        5440            10704            ~              ~             ~             ~             10704            W       1072            *2025/04/23 12:44:02
33. 7       12984       -8320       4664        5084            9748             ~              ~             ~             ~             9748             W       1312            2025/04/23 12:48:02
```

### 内存维测

日志文件：memleak-native-[process\_name]-[pid]-smaps.txt

| 字段 | 说明 |
| --- | --- |
| RealPssMemory | 记录了realtime时刻采集的PSS值，单位：KB。 |
| LOGGER\_MEMCHECK\_MEMINFO | 下方记录了整机meminfo内存信息，如MemTotal、MemFree等。 |
| LOGGER\_MEMCHECK\_SMAPS\_INFO | 下方记录了该进程的smaps汇总信息。 |
| LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO | 下方记录了该进程的两次jemalloc的申请情况（两次记录间隔5min），系统会根据两次NMD信息抓取内存栈。 |
| LOGGER\_MEMCHECK\_DETIAL\_INFO | 下方记录了该进程的jemalloc快照详细信息。 |

```
1. Generated by HiviewDFX @HarmonyOS
2. LOGGER_MEMCHECK_GERNAL_INFO
3. pidNumber: 2017
4. processName: process1
5. PidStartTime: 1602
6. RealPssMemory: 83505

8. *****************************
9. LOGGER_MEMCHECK_MEMINFO
10. MemTotal:                             11332540 kB
11. MemFree:                               1686056 kB
12. ......

14. LOGGER_MEMCHECK_SMAPS_INFO
15. -------------------------------[memory]-------------------------------
16. Shared      Shared      Private     Private
17. Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
18. 2048        0           0           0           0           0           0           0           0           1                             /dev/__parameters__/param_sec_dac
19. ...
20. 45778196    744068      827123      213560      55288       403304      71916       308888      308888      6500                          Summary
21. ......

23. LOGGER_MEMCHECK_SAMPLE_NMD_INFO

25. size       allocated         nmalloc         ndalloc

27. 8           17384          511848          509675
28. 16          129376          338438          330352
29. 32         1138816         1026155          990567
30. 48         3161808         1322095         1256224
31. 64         1869376          908151          878942
32. ......

34. ************ endl ************

36. LOGGER_MEMCHECK_SAMPLE_NMD_INFO

38. size       allocated         nmalloc         ndalloc

40. 8           17384          511848          509675
41. 16          129376          338438          330352
42. 32         1138816         1026155          990567
43. 48         3161808         1322095         1256224
44. 64         1869376          908151          878942
45. ......

47. ************ endl ************

49. *****************************
50. LOGGER_MEMCHECK_PROC_INFO
51. ASHMEM_PROCESS_INFO
52. ---------------------------------------------------------------------------------
53. ---------------------------------------------------------------------------------
54. Process_name Process_ID Fd Cnode_idx Applicant_Pid Ashmem_name Virtual_size Physical_size magic
55. XXXXX           816             22      328234  816     dev/ashmem/PolicyVolumeMap      541             4096            7
56. ************ endl ************

58. ******************************
59. LOGGER_MEMCHECK_DETIAL_INFO
60. allocated         nmalloc   (#/sec)         ndalloc   (#/sec)       nrequests   (#/sec)           nfill   (#/sec)          nflush   (#/sec)
61. small:                      183785560        12591759       619        10371251       510         1289491        63         1313204        64          956094        47
62. large:                       31059968            3359         0            2946         0            3359         0            3359         0               0         0
63. total:                      214845528        12595118       619        10374197       510         1292850        63         1316563        64          956094        47

65. ......

67. bins:           size ind    allocated      nmalloc (#/sec)      ndalloc (#/sec)    nrequests   (#/sec)  nshards      curregs     curslabs  nonfull_slabs regs pgs   util       nfills (#/sec)     nflushes (#/sec)       nslabs     nreslabs (#/sec)      n_lock_ops (#/sec)       n_waiting (#/sec)      n_spin_acq (#/sec)  n_owner_switch (#/sec)   total_wait_ns   (#/sec)     max_wait_ns  max_n_thds
68. 8   0       198920       163820       8       138955       6       119703         5        1        24865           56             19  512   1  0.867         6526       0         4008       0           96        26995       1           10990       0               0       0               0       0            1226       0               0         0               0           0
69. 16   1      1802688      1143707      56      1031039      50       221165        10        1       112668          563            309  256   1  0.781       105471       5        82548       4         1942        80503       3          191126       9               0       0              14       0            4316       0               0         0               0           0
70. 32   2      9954560      1867465      91      1556385      76       267993        13        1       311080         2614            503  128   1  0.929       177825       8       136745       6         7713       176923       8          325128      15               2       0              52       0            8139       0               0         0               0           1
71. 48   3     35382816      3763756     185      3026614     148       300952        14        1       737142         2953            220  256   3  0.975       371881      18       283650      13        12022        60637       2          667997      32               2       0              17       0            2725       0               0         0               0           1
72. ......
```

说明

“LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO”与“LOGGER\_MEMCHECK\_DETIAL\_INFO”均为进程jemalloc快照，区别在于：

1. LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO：单次维测连续采样2次，间隔为5分钟，内容包含size、allocated、nmalloc、ndalloc等四列内存申请相关信息；
2. LOGGER\_MEMCHECK\_DETIAL\_INFO：单次维测仅采样1次，内容包含进程jemalloc的完整信息。

### 内存栈

**栈信息日志文件：** memleak-native-[process\_name]-[pid]-[timestamp].txt

* 检测到泄漏后抓取**15min内的进程内存trace**，可将日志如下图通过Open File加载到DevEco Studio进行解析。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/23iDJ7Z4T1SxoZ_5o0mM3A/zh-cn_image_0000002589324861.png?HW-CC-KV=V1&HW-CC-Date=20260429T053352Z&HW-CC-Expire=86400&HW-CC-Sign=67D1D897FF93B4007F54D1B6B21F44B3E0972DFB70765D792C9E7A915445DE98)

  注意

  系统自动抓的调用栈（memleak-native-[process\_name]-[pid]-[timestamp].txt）**无法直接在DevEco Studio打开，需要修改后缀名为.nas**。
* **All Heap：** 选择后展示抓取15分钟内的内存情况，记录了hook malloc等系统调用的堆栈。Native日志是以so+偏移的形式展示调用栈（每一行表示一次内存分配行为调用栈），需要结合符号表进一步分析。

  点击Call Trees可以查看抓取进程的调用栈，筛选“Created & Existing”，根据没有释放的内存占比排序，展开可查看详细进程调用信息，优先排查内存占用较高的堆栈。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/tc2l-E6bRQa-CyvoDYVcnA/zh-cn_image_0000002589244797.png?HW-CC-KV=V1&HW-CC-Date=20260429T053352Z&HW-CC-Expire=86400&HW-CC-Sign=33686D7A100230AB93FF413FC207F11D1E8CC22FAB9A84CFDA78C1134D1CE09E)

  说明

  1. 部分栈单看Existing可能感觉泄漏不大或者和检测到的内存峰值相差很多，但是栈里只是抓取的是15分钟内的堆栈信息和内存申请，很多进程泄漏是以几十甚至几百小时为单位的，长时间的泄漏达到上报时的泄漏大小。
* **All Anonymous VM：** 选择后记录了当前hook mmap系统调用的堆栈信息。

  同样选择“Created & Existing”，表示在hook抓取内存申请未释放的。长度越长代表在剩余内存中占用越多，优先排查。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/KKw6wTv3SDeA79zKXQ0fUQ/zh-cn_image_0000002558764992.png?HW-CC-KV=V1&HW-CC-Date=20260429T053352Z&HW-CC-Expire=86400&HW-CC-Sign=CFC4DEAE8141DC7788BE37DFA683995A9487829E06A10E3C6A55B03E7EBF022D)

### native泄漏聚类规则

应用程序在同一或不同版本上、不同时间产生的泄漏问题可能为同一原因，开发者可以从故障日志中提取故障特征，根据故障特征将多份故障日志进行聚类，以提高泄漏问题的分析效率。

对于PSS\_MEMORY故障，系统会发送两份故障日志给开发者进行分析，故障日志一（[内存维测](resource-leak-guidelines.md#内存维测)）用于存储进程的部分轻量化信息，如：smaps、ashmem、NMD等；故障日志二（[内存栈](resource-leak-guidelines.md#内存栈)）中用于存储系统检测到进程pss泄漏后抓取的栈信息。

1. 对故障日志一中的进程“LOGGER\_MEMCHECK\_SMAPS\_INFO”信息进行分析，根据以下表格所列方法计算各类型内存占比，筛选占比最高的内存泄漏类型。

   | 内存泄漏类型 | 计算方法 |
   | --- | --- |
   | 虚拟机对象泄漏 | 搜索关键字“ArkTS”，计算“Pss”列和“SwapPss”列之和占总内存比例。 |
   | 堆内存泄漏 | 搜索关键字“jemalloc”，计算“Pss”列和“SwapPss”列之和占总内存比例。 |
   | ashmem内存泄漏 | 搜索关键字“/dev/ashmem”，计算“Pss”列和“SwapPss”列之和占总内存比例。 |
   | anon类型内存较大 | 搜索关键字“[anon]”，计算“Pss”列和“SwapPss”列之和占总内存比例。 |

   说明

   1. 每一行“Pss”列以及“SwapPss”列之和为对应内存块的申请大小。
   2. “Name”列为内存块的内存标签。
2. 筛选出占比最高的内存泄漏类型后，可以根据以下规则进一步提取故障特征：

   * 虚拟机对象：筛选内存申请最大的内存标签作为故障特征，如：从以下日志中提取的故障标签为“[anon:ArkTS Heapsemi space]”。

     ```
     1. LOGGER_MEMCHECK_SMAPS_INFO
     2. -------------------------------[memory]-------------------------------
     3. Shared      Shared      Private     Private
     4. Size        Rss         Pss        Clean       Dirty         Clean       Dirty       Swap        SwapPss     Counts                 Name
     5. 1662976     68744       68744       0           0           68744       0           0           0           525                     [anon:ArkTS Heap]

     7. 5632        5600        2261        3452        0           2148        0           0           0           22                      [anon:ArkTS Heapappspawn space]

     9. 98304       74012       74012       0           0           74012       0           0           0           307                     [anon:ArkTS Heapsemi space]

     11. ...
     ```
   * 堆内存：筛选内存申请最大的内存标签作为故障特征，如：从以下日志中提取的故障标签为“[anon:native\_heap:jemalloc]”。

     ```
     1. LOGGER_MEMCHECK_SMAPS_INFO
     2. -------------------------------[memory]-------------------------------
     3. Shared      Shared      Private     Private
     4. Size        Rss         Pss        Clean       Dirty         Clean       Dirty       Swap        SwapPss     Counts                 Name
     5. 327168      171464      146921      25416       0           146048      0           0           0           17                      [anon:native_heap:jemalloc]
     6. 24600       3924        3586        348         0           3576        0           0           0           18                      [anon:native_heap:jemalloc meta]
     ```

     如果存在内存调用栈，可以根据NMD维测找到占用最高的内存区间，并结合抓取的调用栈维测聚类到具体代码段或者so作为怀疑点，具体分析方法可参考[Native泄漏分析方法](../best-practices/bpta-stability-leak-way.md#section1658571616574)。
   * ashmem内存：参考[ashmem聚类规则](resource-leak-guidelines.md#ashmemiongpugpu_rs聚类规则)。
   * anon内存：筛选内存申请最大的内存标签作为故障特征，如：从以下日志中提取的故障标签为“[anon]”。

     ```
     1. LOGGER_MEMCHECK_SMAPS_INFO
     2. -------------------------------[memory]-------------------------------
     3. Shared      Shared      Private     Private
     4. Size        Rss         Pss        Clean       Dirty         Clean       Dirty       Swap        SwapPss     Counts                 Name
     5. 38760       528         524         4           0           524         0           0           0           56                      [anon]
     ```

     如果存在内存调用栈，可通过分析调用栈中占比较高的聚类到具体代码段或者so作为怀疑点，具体分析方法可参考[Native泄漏分析方法](../best-practices/bpta-stability-leak-way.md#section1658571616574)。

   注意

   对于nolog版本，默认不开启抓栈，因此推荐开发者根据smaps信息对PSS内存占用的类型进行初步聚类。

## ashmem/ion/gpu/gpu\_rs内存泄漏日志规格

### 内存采样

* 日志文件：memleak-kernel-[module]-0-sample.txt（**方式一**）或 RESOURCE\_OVERLIMIT\_[TIMESTAMP]\_[PID].log（**方式三**）。

  | 字段 | 说明 |
  | --- | --- |
  | memoryName | 内核内存类型，如果发现进程存在泄漏（超过系统设定基线），会显示为该泄漏进程的进程名；如果memoryName打印类型为：ashmem/gpu/ion，则说明无进程泄漏。 |
  | softThreshold | 系统设定的软门限（超过8个采样周期，即30+分钟超过软门限后判定泄漏），单位：KB。 |
  | hardThreshold | 系统设定的硬门限（单次超过硬门限后判定泄漏），单位：KB。 |
  | topMemory | 检测到的内核内存峰值，单位：KB。 |

  ```
  1. memoryName:gpu
  2. softThreshold:2300(MB)
  3. hardThreshold:3450(MB)
  4. topMemory:4876824(KB)
  5. time(s) kernelMemory(KB)realtime
  6. 247681  4876824         2024/06/24 08:27:52
  ```

### 内存维测

日志文件：memleak-kernel-[module]-0-[timestamp].txt **（方式一）**

| 字段 | 说明 |
| --- | --- |
| LOGGER\_MEMCHECK\_MEMINFO | 整机内存信息概览。 |
| LOGGER\_MEMCHECK\_PROC\_INFO | ashmem/ion/gpu对应泄漏内存节点信息打印（泄漏类型不同，落盘内容不同）。 |
| LOGGER\_PROCESS\_DMABUF\_INFO | ion内存泄漏时获取的特殊节点内容，包含更多的内存块使用信息。 |
| LOGGER\_MEMCHECK\_RENDER\_SERVICE\_MEM | Render\_service进程的内存使用情况。 |

检测到ashmem/gpu/ion内存泄漏时，会抓取整机ashmem/gpu/ion内存信息，ashmem/ion与句柄泄漏ashmem/dmabuf日志规格相同，参考ashmem/dmabuf类型句柄。

日志抬头：

```
1. Generated by HiviewDFX @HarmonyOS
2. LOGGER_MEMCHECK_GERNAL_INFO
3. memoryName:ion
4. softThreshold:2800(MB)
5. hardThreshold:4200(MB)
6. appHardThreshold:4096(MB)
7. topMemory:0(KB)

9. *****************************
10. LOGGER_MEMCHECK_MEMINFO
11. MemTotal:       11738500 kB
12. MemFree:          116204 kB
13. MemAvailable:      95232 kB
14. Buffers:               0 kB
```

日志文件内“LOGGER\_MEMCHECK\_PROC\_INFO”会根据内存泄漏类型不同，落盘对应的内存信息，具体如下：

* ashmem内存泄漏：

  ```
  1. LOGGER_MEMCHECK_PROC_INFO
  2. realtime:       2025/05/30 19:52:42
  3. Process ashmem overview info:
  4. ---------------------------------------------------------------------------------
  5. Process_name Virtual_size Physical_size
  6. Total ashmem  of [XXXXXX] virtual size is  541, physical size is 4096
  7. Total ashmem  of [XXXXXX] virtual size is  299008, physical size is 299008
  8. Total ashmem  of [XXXXXX] virtual size is  37574896, physical size is 37470208
  9. ......
  10. Process ashmem detail info:
  11. ---------------------------------------------------------------------------------
  12. Process_name    Process_ID      Fd      Cnode_idx       Applicant_Pid   Ashmem_name     Virtual_size    Physical_size   magic
  13. XXXXX    816     22      328234  816     dev/ashmem/PolicyVolumeMap      541     4096    7
  14. ......
  15. ---------------------------------------------------------------------------------
  16. *****************************
  17. LOGGER_MEMCHECK_RENDER_SERVICE_MEM
  18. get info realtime:      2025/05/30 19:52:42

  20. -------------------------------[ability]-------------------------------

  22. ----------------------------------RenderService----------------------------------
  23. ......
  ```
* ion内存泄漏：

  ```
  1. *****************************
  2. LOGGER_MEMCHECK_PROC_INFO
  3. MM_DMABUF_INFO
  4. realtime: 2025/07/26 14:19:58
  5. Process pid fd size_bytes ino exp_pid exp_task_comm buf_name exp_name buf_type
  6. process1        1563 71 13926400 25690 11187 allocator_host 11563 mm_heap_helpers xcomponent
  7. process1        1563 75 1024000000 21095 11187 allocator_host 11563 mm_heap_helpers NULL
  8. process1        1563 77 1024000000 11557 11187 allocator_host 11563 mm_heap_helpers NULL
  9. process1        1563 79 1024000000 26747 11187 allocator_host 11563 mm_heap_helpers NULL
  10. ************ endl ************

  12. *****************************
  13. LOGGER_MEMCHECK_RENDER_SERVICE_MEM
  14. get info realtime:      2025/05/30 21:17:39

  16. -------------------------------[ability]-------------------------------

  19. ----------------------------------RenderService----------------------------------
  20. ......
  ```

  从HarmonyOS6.0.0开始，ion内存维测信息增加buf\_name、leak\_type等列，变更为以下形式：

  ```
  1. *****************************
  2. LOGGER_MEMCHECK_PROC_INFO
  3. MM_DMABUF_INFO
  4. Process       pid     fd  size_bytes  ino          exp_pid    exp_task_comm   buf_name    exp_name          buf_type    leak_type
  5. process1      65141   268 274432      430936       42829      allocator_host  65141       mm_heap_helpers   NULL        NULL
  6. ......
  7. ************ endl ************
  ```

  字段说明：

  | 字段 | 说明 |
  | --- | --- |
  | Process | 持有ION内存块的应用进程包名（16个字符截断）。 |
  | pid | 发生故障进程pid。 |
  | fd | 进程持有的句柄。 |
  | size\_bytes | 进程持有的ION内存buffer大小，单位：B。 |
  | ino | 文件inode号（索引节点号）。 |
  | exp\_pid | 从内核申请ION内存的进程pid。 |
  | exp\_task\_comm | 从内核申请ION内存的进程名。 |
  | buf\_name | ION内存的buffer名字。 |
  | exp\_name | ION内存的buffer扩展名。 |
  | buf\_type | ION内存的buffer类型。 |
  | leak\_type | ION内存泄漏维测的buffer类型。 |
* gpu/gpu\_rs内存泄漏：

  ```
  1. LOGGER_MEMCHECK_PROC_INFO
  2. GPU_PROCESS_INFO
  3. render_service
  4. ctx_1       1689       1455 used summary:3362426880 grow:0 driver:10432512 kmd:3260416 jit:131072
  5. process1
  6. Channel: xx default device (Total memory: 730594)
  7. 1:                    2 / 2
  8. 6:                    4 / 160
  9. 7:                    6 / 384
  10. 8:                  163 / 20928
  11. 9:                 1573 / 604160
  12. 10:                   48 / 24576
  13. 11:                    2 / 2048
  14. 13:                    2 / 12800
  15. 15:                    4 / 65536
  16. ......

  18. *****************************
  19. LOGGER_MEMCHECK_RENDER_SERVICE_MEM
  20. get info realtime:      2025/05/30 21:16:01

  22. -------------------------------[ability]-------------------------------

  25. ----------------------------------RenderService----------------------------------
  ```

  字段说明：

  + “ctx\_1 1689 1455 used summary:3362426880 grow:0 driver:10432512 kmd:3260416 jit:131072

    process1”表示上下文ctx\_1是由进程“process1”创建的，这个进程的进程号为“1455”，线程号为“1689”，总使用量为：“3362426880”字节。
  + “Channel: xx default device (Total memory: 730594)”表示进程申请的“xx default device”类型的gpu内存大小为730594字节。
  + “15: 4 / 65536” 表示 2^14~2^15大小的内存块申请了4次，总共申请了65536字节的内存。

说明

1. gpu\_rs内存泄漏与gpu泄漏的区别在于：gpu是应用自渲染发生的泄漏，gpu\_rs是通过进程render\_service进行统一渲染发生的泄漏。
2. 在资源泄漏资料中，ion、dmaheap、dmabuf 可理解为同一种内存类型，不作强区分。
3. 当前日志规格不代表维测的最终形态，后续会根据版本问题以及用户原声增加维测信息，变更形式包括但不限于行、列、段落等。

### 内存栈

从HarmonyOS 6.0.0开始，支持抓取gpu内存申请的调用栈以分析进程gpu泄漏问题。检测到泄漏后会收集15分钟内的gpu内存申请trace，开发者可本地搭建[Smartper](https://gitcode.com/openharmony-sig/smartperf)f环境并导入Profiler日志进行解析。

日志文件名称：memleak-kernel-[module]-[pid]-[timestamp].txt

### ashmem/ion/gpu/gpu\_rs聚类规则

应用程序在同一或不同版本上、不同时间产生的泄漏问题可能为同一原因，开发者可以从故障日志中提取故障特征，根据故障特征将多份故障日志进行聚类，以提高泄漏问题的分析效率。

**ashmem聚类规则**

1. 提取故障日志中的ashmem维测信息进行聚类，如下：

   ```
   1. Process_name    Process_ID      Fd      Cnode_idx       Applicant_Pid   Ashmem_name                     Virtual_size    Physical_size  magic
   2. XXXXX           816             22      328234          816             dev/ashmem/PolicyVolumeMap      541             4096            7
   3. XXXXX           816             22      328234          816             dev/ashmem/PolicyVolumeMap      541             4096            7
   4. XXXXX           816             22      328234          816             dev/ashmem/inputBuffer          541             1024            7
   5. XXXXX           816             22      328234          816             dev/ashmem/outputBuffer         541             512             7
   6. ......
   ```
2. 分析ashmem维测中的“Ashmem\_name”字段，来确认是否为同一类型的buffer泄漏，并将“Physical\_size”列之和占比最高的buffer作为本次故障的故障特征。

**ion聚类规则**

1. 提取故障日志中的ion维测信息来进行聚类，如下：

   ```
   1. *****************************
   2. LOGGER_MEMCHECK_PROC_INFO
   3. MM_DMABUF_INFO
   4. Process     pid      fd         size_bytes    ino        exp_pid      exp_task_comm    buf_name                                                                         exp_name           buf_type    leak_type
   5. process1    65141    246        278528        432510     42829        allocator_host    65141                                                                           mm_heap_helpers    NULL        NULL
   6. process1    65141    247        266240        434225     42829        allocator_host    65141                                                                           mm_heap_helpers    NULL        NULL
   7. process1    65141    248        274432        430933     42829        allocator_host    65141                                                                           mm_heap_helpers    NULL        NULL
   8. process1    65141    264        14036992      432500     42829        allocator_host    https://xxxx/xxxxx.png                                                          mm_heap_helpers    pixelmap    pixelmap
   9. process1    65141    266        14036992      426988     42829        allocator_host    https://xxxx/xxxxx.png                                                          mm_heap_helpers    pixelmap    pixelmap
   10. process1    65141    268        14036992      430936     42829        allocator_host    https://xxxx/xxxxx.png                                                          mm_heap_helpers    pixelmap    pixelmap
   11. process1    65141    258        4493312       432499     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   12. process1    65141    260        4493312       426987     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   13. process1    65141    262        4493312       431689     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   14. process1    65141    254        4493312       430935     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   15. process1    65141    256        4493312       431688     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   16. process1    65141    250        4493312       432498     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   17. process1    65141    252        4493312       430934     42829        allocator_host    srcImageSize-2160x2880-pixelMapSize-2160x2880-streamsize-761322-mimetype-webp   mm_heap_helpers    NULL        NULL
   18. ************ endl ************
   ```
2. 根据“leak\_type”和“buf\_name”对buffer进行分类，提取出“size\_bytes”之和占比最高buffer的“buf\_name”作为本次故障的故障特征。分析细节可参考[ION泄漏分析方法](../best-practices/bpta-stability-leak-way.md#section5493141412410)。

   说明

   如果“leak\_type”为NULL，可能存在多种类型的buffer，可以直接通过“buf\_name”进行区分。

**gpu/gpu\_rs聚类规则**

1. 解析故障日志中提供的gpu维测信息，统计包含“Total memory:”字段的行并解析出对应类型gpu内存的占用，筛选占用最高的gpu内存类型作为故障特征。如以下维测中，“host default memory”类型的gpu内存占用为“1789351”字节，可以作为故障特征进行聚类：

   ```
   1. C: cq memory(not in total memory) (Total memory: 4096)
   2. 13:                    1 / 4096

   4. C: vulkan external memory(not in total memory) (Total memory: 0)
   5. (empty)

   7. C: host default memory (Total memory: 1789351)
   8. 5:                  269 / 4304
   9. 6:                  370 / 15792
   10. 7:                  401 / 33088
   11. 8:                   96 / 14240
   12. 9:                  449 / 141696
   13. 10:                  265 / 173143
   14. 11:                  172 / 236391
   15. 12:                   68 / 187012
   16. 13:                   35 / 197576
   17. 14:                   17 / 251573
   18. 15:                    6 / 108304
   19. 16:                    1 / 51736
   20. 17:                    1 / 84184
   21. 19:                    1 / 290312
   ```
2. 聚类到gpu内存类型后，筛选出其中占用最大的内存段并进行聚类。

注意

不同的芯片平台中，gpu表现形式会存在差异：

C: host default memory (Total memory: 1789351)。

Channel: Texture (Total memory: 1789351)。
