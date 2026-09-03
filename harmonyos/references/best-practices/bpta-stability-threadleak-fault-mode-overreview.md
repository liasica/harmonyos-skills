---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-threadleak-fault-mode-overreview
title: 线程泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 线程泄漏故障模式说明 > 线程泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:fa49d64bcbfcb94f6c8a1c53401e9577b975812210970820b656a8f517815de6
---

系统监控应用申请的线程数量，当应用线程数量超过系统阈值时，会抓取维测信息，并对应用进行管控。本文旨在为开发者介绍系统的线程泄漏检测机制，并提供开发态与运维态的问题分析思路。此外，本文还提供线程泄漏问题分析与定位实践系列文章，旨在系统梳理线程泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的线程使用习惯。文章如下：

* [线程泄漏故障模式说明](bpta-stability-app-threadleak-fault-mode.md)：线程是应用并发执行的核心资源，可通过pthread\_create()、std::thread()等方式创建。若管理不当（如线程未正常退出、线程任务阻塞），会导致线程持续堆积，最终触发系统管控，用户感知应用闪退。同时，此文为开发者提供了开发态和运维态两种场景的分析思路，构造典型线程泄漏案例并展示分析过程。

## 线程泄漏基本概念与故障检测机制

### 线程以及线程泄漏概念介绍

进程：操作系统分配资源（内存、文件句柄、网络端口等）的最小单位。每个独立运行的程序即为一个进程，例如微信、浏览器、游戏各自对应一个进程。

线程：进程内部的执行路径，是CPU调度执行的最小单位。一个进程至少包含一个主线程；同一进程内的所有线程共享该进程的堆内存、文件句柄等资源；而每个线程则独有栈、程序计数器和局部变量。

线程泄漏是一种故障现象：程序创建的线程在完成任务后无法正常退出、系统无法回收，持续占用系统线程资源，且不断新建而不释放。当线程数量超过预设阈值时，系统判定存在线程泄漏。系统检测到应用发生线程泄漏后，会主动管控该应用进程，并上报资源泄漏事件。

线程泄漏常见原因：

1. 线程未正确结束：线程函数异常未返回，未调用pthread\_exit()。
2. 线程引用未释放：线程对象/资源未delete，导致无法回收。
3. 线程创建失控：并发场景下无限制创建线程。
4. 同步机制死锁：线程互相等待，无法结束。

### 线程数量获取方式

开发者可以通过以下方法读取到进程的线程数量：

在shell命令行或应用代码中读取/proc/self/status：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cat /proc/self/status | grep Threads ``` |

开发者执行命令后得到应用进程中线程的数量：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Threads:        39 ``` |

### 线程泄漏检测原理

系统通过定时轮询机制扫描所有进程的线程数占用，当应用申请的线程数超过系统阈值后，会判定应用发生了线程泄漏。对发生线程泄漏的应用，系统会根据应用的前后台状态执行以下操作：

* 如果检测到应用泄漏时，应用处于后台，系统会直接管控此应用。
* 如果检测到应用泄漏时，应用恰好处于前台，系统会等待应用切到后台。等待一段时间后，系统会对应用线程占用数量进行二次校验。
* 如果检测到应用泄漏且同时系统冻屏时，系统会直接触发管控，不区分应用的前后台状态。

## 故障感知

开发者按需订阅相关故障事件：

* 订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，资源泄漏事件中包含应用申请的线程数量，同时也包含维测日志。开发者可以结合故障事件提供的信息与维测日志进一步分析后续改进方向。
* 订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)，若应用因线程泄漏发生终止，事件的reason字段会上报ResourceLeak(ThreadLeak)或者ThreadKiller。 开发者可以通过监听此事件，快速识别本次应用终止的故障类型，也可以汇总其他应用终止事件，分析线程泄漏故障在所有故障中的占比。

### 订阅资源泄漏事件

开发者可以通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)获取到本次系统管控的线程维测信息。应用触发线程泄漏故障后，通过HiAppEvent收到如下hiappevent.event.RESOURCE\_OVERLIMIT事件回调，其中resource\_type的值为thread，其余更详细的故障参数可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-resourceleak-events.md#params字段说明)进一步了解。

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` HiAppEvent eventInfo.domain=OS HiAppEvent eventInfo.name=RESOURCE_OVERLIMIT HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"app_running_unique_id":"13544159712879771749","bundle_name":"com.example.dfx_test","bundle_version":"1.0.1","external_log":["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1784269276384_15802.log"],"level":"warning","log_over_limit":false,"pid":15802,"resource_type":"thread","thread":{"num":1241},"time":1784269276371,"uid":20020212}} ``` |

### 订阅应用终止事件

开发者可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来监控系统管控原因。应用触发系统管控后，若事件中reason为ResourceLeak(ThreadLeak)或ThreadKiller，表明本次故障由线程泄漏引发。不同的reason代表不同的管控形式，具体如下表所示：

| reason | 管控形式 |
| --- | --- |
| ThreadKiller | 应用申请线程数量过多导致系统冻屏时，系统会触发管控，不区分应用的前后台状态。 |
| ResourceLeak(ThreadLeak) | 应用线程申请数量过多超过后台管控阈值时，系统会在应用切后台时对其进行清理，通常表现为重新打开应用时冷启动。 |

以ResourceLeak(ThreadLeak)管控原因为例，会收到应用终止事件，示例如下：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2, "params":{"app_running_unique_id":"4861316576349011847","bundle_version":"1.0.1","foreground":false,"reason":"ResourceLeak(ThreadLeak)","time":1783932252439}} ``` |

其中，reason字段为ResourceLeak(ThreadLeak)，foreground字段为false，代表系统检测到该应用线程占用超过管控阈值，切后台之后管控此应用。开发者也可以通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明。

## 日志规格与日志获取

系统会在检测到应用发生线程泄漏后，通过[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)将抓取的维测日志发送至应用沙箱，开发者可以从资源泄漏事件的external\_log字段中提取出日志路径，并对提取出的维测日志进行分析。

### 日志规格

对于线程泄漏故障，开发者可以结合以下两种维测日志进行问题分析：

* 线程泄漏基础日志，详细信息可参考[线程泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#线程泄漏日志规格)。
* 线程泄漏内核管控日志，详细信息可参考[thread内核管控](../harmonyos-guides/resource-leak-guidelines.md#thread内核管控)。

### 线程泄漏调用栈日志获取方法

线程泄漏的运维态维测日志仅包含线程基础日志，如果需要进一步定位到代码行，可以参考以下方法获取线程调用栈日志进行下一步分析：

* 应用自行通过[线程数量获取方式](bpta-stability-threadleak-fault-mode-overreview.md#section2077483014414)监控线程数量，在合理的时机调用[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)方法主动采集线程泄漏调用栈日志。
* 通过用户描述或流水日志等手段推测故障复现路径后，使用DevEco Studio中Profiler工具的Allocation功能抓取相关线程调用栈日志，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。

## 运维态问题分析方法

### 线程泄漏基础日志分析方法

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者在沙箱中接收到维测日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 线程泄漏维测日志的“summary”字段记录了发生泄漏时进程内的线程总数，开发者可依据该进程实际使用的线程数量，评估线程泄漏严重程度。

   |  |  |
   | --- | --- |
   | ``` 1 ``` | ``` summary: XXXX ``` |
3. 线程泄漏维测日志的详细信息会按照线程名聚类统计，输出Top10的线程占用量、线程的启动时间、近20次页面切换等信息，支撑开发者识别定位。
   * 页面切换信息如下所示：通过APP\_PAGE\_HISTORY\_INFO信息获取应用近20次页面切换信息，初步分析可能导致线程泄漏的业务场景。

     |  |  |
     | --- | --- |
     | ``` 1 2 3 4 5 6 7 8 9 ``` | ``` ***************************** APP_PAGE_HISTORY_INFO   15:04:19.740 :enters foreground   15:04:18.546 :leaves foreground   15:04:15.931 /ets/pages/threadleak   15:04:12.556 :enters foreground   15:04:00.083 :leaves foreground   15:03:57.669 :enters foreground ***************************** ``` |
   * Top10泄漏线程信息如下所示：通过Top 10 Thread Name信息，可初步定位线程泄漏时Top占用的线程和对应的线程数量。

     |  |  |
     | --- | --- |
     | ``` 1 2 3 4 5 6 7 ``` | ``` Top 10 Thread Name: 913	process1 3	gpu-work-client 2	OS_Actor_402 1	IPC_11_13795 1	IPC_12_13796 1	IPC_13_13797 ``` |
   * 线程启动信息如下所示：通过线程启动信息获取线程创建时间，结合hilog流水日志进一步分析执行的业务。

     |  |  |
     | --- | --- |
     | ``` 1 2 3 4 5 ``` | ``` ====================================================== tid	thread_name	start_time(jiffies) 221	process1	4688297 240	IPC_3_4318	3081382 …… ``` |
4. 日志留存了采样时间点的线程栈快照如下所示：通过快照数据即可判定线程此时的运行状态，日志中的\_\_pthread\_cond\_timedwait表示线程正在等待唤醒。开发者可结合业务流程，按照线程创建调用链路追溯，定位线程泄漏的具体位置。

   |  |  |
   | --- | --- |
   | ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ``` | ``` ====================================================== Result: 0 ( no error ) Timestamp:2024-06-27 03:45:20.000 Pid:41897 Uid:1013 Process name:process1 Tid:1527, Name:xxx #00 pc 00000000001b6464 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(98dc7600a0fc62125e291b93ca336154) #01 pc 00000000001b8468 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(98dc7600a0fc62125e291b93ca336154) #02 pc 00000000000c108c /system/lib64/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+20)(9cbc937082b3d7412696099dd58f4f78242f9512) #03 pc 000000000024654c /system/lib64/platformsdk/xxx.so(mindspore::Worker::WaitUntilActive()+204)(534ce78b66262dc14658c35fa018662f) #04 pc 000000000023da14 /system/lib64/platformsdk/xxx.so(mindspore::ActorWorker::RunWithSpin()+256)(534ce78b66262dc14658c35fa018662f) #05 pc 000000000023edb0 /system/lib64/platformsdk/xxx.so(void* std::__h::__thread_proxy[abi:v15004]<std::__h::tuple<std::__h::unique_ptr<std::__h::__thread_struct, std::__h::default_delete<std::__h::__thread_struct>>, void (mindspore::ActorWorker::*)(), mindspore::ActorWorker*>>(void*)+60)(534ce78b66262dc14658c35fa018662f) #06 pc 00000000001baac0 /system/lib/ld-musl-aarch64.so.1(start+236)(98dc7600a0fc62125e291b93ca336154) …… ``` |

### 线程泄漏调用栈日志分析方法

开发者通过[线程泄漏调用栈日志获取方法](bpta-stability-threadleak-fault-mode-overreview.md#section2975173711173)获得线程泄漏调用栈日志，将调用栈日志导入DevEco Studio的Profiler工具中，分析其中可疑的线程调用栈，排查可疑线程泄漏点，操作步骤如下：

1. 单击下图1处，导入线程泄漏调用栈日志。
2. 单击下图2处选择Threads泳道。
3. 单击下图3处Call Trees查看线程申请调用栈。
4. 单击下图4处选择Created & Existing，筛选申请并且未释放的线程及其调用栈。
5. 将抓取的线程栈按照Count列排序，筛选出申请次数异常的线程及其调用栈，如下图5、6处框选内容。
6. 结合调用栈对代码进行分析，找到泄漏原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/dtVGQtO2Sx-iw-4ku9zzVg/zh-cn_image_0000002729597777.png "点击放大")

## 开发态问题分析方法

针对开发验证阶段发现的线程泄漏问题，以及运维阶段复现的已知线程泄漏场景，开发者可在本地使用DevEco Studio中的Profiler调优工具、hidumper等开发工具对问题进行复现并抓取维测信息进行分析。

### 故障分析工具说明

* [hidumper](../harmonyos-guides/hidumper.md)：在分析线程泄漏问题的过程中，开发者可以使用[查询fd及线程信息](../harmonyos-guides/hidumper.md#查询fd及线程信息)中的 “hidumper -p <pid> --thread -v”命令获取指定进程的线程使用情况，辅助问题定位。

  |  |  |
  | --- | --- |
  | ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` # hidumper -p 48469 --thread -v Thread num: 32 Top 10 Thread Names: 11      V8 DefaultWorke 5       OS_GC_Thread 2       example.dfx_test 1       OS_FFRT_2_3 1       OS_FFRT_3_1 1       OS_FFRT_Delay 1       OS_EVENT_POLL 1       OS_IPC_0_48663 1       OS_AppEvent_Ls 1       OS_IPC_2_48666 tid     thread_name     start_time 48469   example.dfx_test 2363475 48663   OS_IPC_0_48663  2363555 48664   OS_IPC_1_48664  2363555 48665   OS_DfxWatchdog  2363555 48666   OS_IPC_2_48666  2363557 …… ``` |
* DevEco Profiler调优工具：开发者可使用DevEco Studio的Profiler调优功能，分析应用进程的线程申请趋势与线程申请的调用栈，定位线程泄漏点。更多功能可参考[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

**说明** 

开发阶段：推荐使用DevEco Studio的Profiler调优功能，不仅支持图形化展示应用的线程增长趋势，也支持抓取录制过程中应用申请的线程数量和线程调用栈。

测试阶段：测试阶段重点需要的是脚本形式批量部署和长时间采集，推荐使用hidumper命令行定时监控应用的线程占用情况。

### 故障分析方法

开发者在调试时，若遇到由线程泄漏故障引起的应用闪退或者冷启动，可以使用DevEco Studio中Profiler工具的Allocation功能进行问题定位，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。

1. 启动录制时先在Allocation的配置页中执行准备工作，如下图所示：
   * 单击图1处选择监控应用进程，单击图2处选择Allocation功能，单击图3处创建Session。
   * 单击图4处过滤泳道按钮，单击图5处选择System Resources泳道。
   * 单击图6处开始执行录制。
   * 应用执行可能发生线程泄漏的业务，等待业务执行完成，停止录制，获得录制结果。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/fzS08YhFSg-93CXYo3eJAA/zh-cn_image_0000002699878452.png "点击放大")
2. 获得录制结果如下图所示：单击下图1处展开Threads泳道，再单击下图2处的Call Trees，即可在图3中查看线程数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/CVxvA77NQt2PgsV4Z9RmjA/zh-cn_image_0000002699718588.png "点击放大")
3. 最后，发现线程数量异常，通过结合[线程泄漏调用栈日志分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section19835127163117)定位线程泄漏点。
