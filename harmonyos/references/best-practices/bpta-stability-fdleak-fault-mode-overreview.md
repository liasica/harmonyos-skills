---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-fdleak-fault-mode-overreview
title: 句柄泄漏故障模式概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 句柄泄漏故障模式说明 > 句柄泄漏故障模式概述
category: best-practices
scraped_at: 2026-09-04T06:33:25+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:2128674f405e3bb280bb97ae53d64e4d9b90c2d0366a4716dfbe9768d41c3240
---

系统会监控进程句柄数量，当进程持有的句柄数量超过阈值，系统会抓取维测并对异常应用进行管控。本文旨在介绍句柄泄漏检测机制，并提供开发态与运维态的问题分析思路。此外，本文还提供句柄泄漏问题分析与定位实践系列文章，旨在系统梳理句柄泄漏常见根因与问题分析方法，引导开发者在编码中建立良好的句柄资源使用习惯。文章如下：

* [句柄泄漏故障模式说明](bpta-stability-app-fdleak-fault-mode.md)：此文围绕应用进程的文件句柄泄漏、socket句柄泄漏、pipe句柄泄漏、ASHMEM句柄泄漏、dmabuf句柄泄漏5种常见类型，结合案例为开发者展示了每种句柄泄漏类型的根因分布和问题分析思路。

## 句柄泄漏基本概念与故障检测机制

### 句柄以及句柄泄漏概念介绍

在操作系统中，文件描述符（File Descriptor，简称FD，又称句柄）是系统为每个进程分配的非负整数索引，用于访问文件、套接字、管道等I/O资源。每个进程拥有独立的文件描述符表，系统维护其与打开的文件之间的映射关系。系统按需分配句柄，通常从最小可用数字开始递增，且受整机资源限制，每个进程持有的句柄数量有明确上限。句柄泄漏指程序在打开文件、套接字或其他I/O资源后未能正确关闭对应描述符，导致系统无法回收资源的现象，其影响逐级放大，初期往往不易察觉。

句柄泄漏常见原因：

* 资源未释放：打开文件或套接字后，逻辑执行完毕但是未调用close()方法。
* 异常路径遗漏：在函数执行过程中发生错误或异常跳转时，导致位于正常逻辑之后的资源释放代码未执行。
* 循环内累积：在循环体内部反复打开资源却未及时关闭，导致短时间内耗尽句柄配额。
* 子进程继承问题：调用fork()创建子进程后，子进程未能及时关闭不需要的文件描述符，导致系统无法回收资源。

### 句柄数量获取方式

开发者可以参考以下方法读取应用进程当前持有的句柄数：

* 应用自行查询/proc/self/fd\_num，获取自身持有的句柄数量。

  ```screen
  # cat /proc/self/fd_num
  1008
  ```

### 句柄泄漏系统检测机制

在HarmonyOS上，系统会周期性检测应用进程的句柄使用量，当超过系统阈值时，系统会判定应用出现了较严重的句柄泄漏故障，并管控后台应用。

## 故障感知

如果需要感知应用是否发生过句柄泄漏故障，开发者可以订阅以下故障事件：

### 订阅资源泄漏事件

应用触发句柄泄漏故障后，开发者可以通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)获取本次系统管控的句柄维测日志，如果resource\_type的值为fd，说明本次应用终止原因为句柄泄漏故障。开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-resourceleak-events.md#params字段说明)了解更详细的故障参数说明。以下为发生了句柄泄漏故障后，应用收到的资源泄漏事件回调示例：

```screen
HiAppEvent onReceive: domain=OS
HiAppEvent eventName=RESOURCE_OVERLIMIT
HiAppEvent eventInfo={"domain":"OS","name":"RESOURCE_OVERLIMIT","eventType":1,"params":{"bundle_name":"com.example.myapplication","bundle_version":"1.0.1","fd":{"num":20068,"top_fd_num":20008,"top_fd_type":"pipe"},"pid":11796,"resource_type":"fd","time":1784534499111,"uid":20020215,"external_log": ["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1784534499125_11796.log"], "log_over_limit": false}}
```

### 订阅应用终止事件

应用触发句柄泄漏故障后，开发者可以通过订阅[应用终止事件](../harmonyos-guides/app-killed-events.md)来查看系统管控的原因，如果reason为ResourceLeak(FDLeak)，说明本次应用终止的原因为句柄泄漏故障。开发者可通过[params字段说明](../harmonyos-guides/hiappevent-watcher-app-killed-events.md#params字段说明)了解更详细的故障参数说明。以下为发生了句柄泄漏故障后，应用收到的应用终止事件回调示例：

```screen
HiAppEvent eventInfo={"domain":"OS","name":"APP_KILLED","eventType":2,"params":{"app_running_unique_id":"2273502076130646286","bundle_version":"1.0.1","foreground":false,"reason":"ResourceLeak(FDLeak)","time":1784534489402}}
```

## 日志规格与日志获取

系统会在检测到应用发生句柄泄漏后，通过资源泄漏事件将系统抓取的故障日志发送给应用沙箱，开发者可以从故障事件的external\_log字段中提取出日志路径/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log，并对提取出的维测日志进行分析。

### 日志规格

对于句柄泄漏故障，开发者可以结合以下几种维测日志进行问题分析：

* 句柄基础维测日志：记录了应用申请句柄的详细分布。日志具体内容参考：[句柄泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏日志规格)。
* 句柄栈日志：记录了句柄申请调用栈信息。注意：句柄栈日志无法直接打开，开发者可以参考[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)将此日志导入DevEco Studio的Profiler工具分析。

### 句柄栈日志获取方法

句柄泄漏的运维态维测日志仅包含句柄基础维测日志，如果需要进一步定位到代码行，可以参考以下方法获取句柄栈日志进行下一步分析：

* 通过订阅[应用灰度采集](../harmonyos-guides/hiretrieval.md)，在运维态订阅句柄调用栈日志。
* 应用通过[句柄数量获取方式](bpta-stability-fdleak-fault-mode-overreview.md#section15612122912911)自行监听句柄水线，在合理的时机调用[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)方法主动采集句柄调用栈日志。
* 结合用户描述或流水日志等推测故障的复现路径，通过DevEco Studio中Profiler工具的Allocation功能抓取相关句柄调用栈日志。

## 运维态分析方法

运维态通过[订阅资源泄漏事件](bpta-stability-fdleak-fault-mode-overreview.md#section151162273105)感知到句柄泄漏故障后，开发者可以优先参考[句柄基础日志分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section9627141273)对获取到的基础维测日志进行分析，初步定界获取句柄泄漏的二级根因。如果通过[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)获取到了应用句柄栈维测日志，那么可以进一步根据[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)定位至泄漏点。

### 句柄基础日志分析方法

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 在故障日志中找到关键字Summary，并读取基础维测日志如下：

   ```screen
   *****************************
   Summary:
   Leaked fd:socket

   Leaked fd Top 10:
   20007	socket
   10	eventpoll
   8	eventfd
   8	pipe
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-dwr
   5	/data/storage/el2/base/files/hiappevent/databases/ap*ev*nt.db-wal
   3	/dev/null
   3	/sys/kernel/debug/tracing/trace_marker
   2	/dev/kmsg
   Top Dir 10:
   2	/proc/
   01	/proc/12196/sched_rtg_ctrl
   01	/proc/12196/task/12266/sched_qos_ctrl
   ```
3. 在基础维测日志中，系统已经将进程持有的所有句柄按照句柄类别聚类，并按照句柄个数将每一类句柄进行排序。Leaked fd Top 10中展示了数量前十的句柄。对于文件类型句柄，系统还会单独根据文件路径聚类，Top Dir 10中展示了数量前十的路径句柄。开发者可以从Leaked fd Top 10和Top Dir 10中筛选出数量最多的句柄，作为本次句柄泄漏的主要根因。开发者可以按照定位出的top句柄类型，索引出对应的二级故障，如下表所示：

   | 句柄类型 | 二级故障根因 | 定位手段 |
   | --- | --- | --- |
   | 文件 | 文件句柄泄漏 | 参考：[文件句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1460613474513) |
   | socket | socket句柄泄漏 | 参考：[socket句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1232317539454) |
   | pipe | pipe句柄泄漏 | 参考：[pipe句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section94463205454) |
   | ASHMEM | ASHMEM句柄泄漏 | 参考：[ASHMEM句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section1338618214454) |
   | dmabuf | dmabuf句柄泄漏 | 参考：[dmabuf句柄泄漏](bpta-stability-app-fdleak-fault-mode.md#section15702142194514) |
4. 句柄泄漏的运维态维测日志仅包含基础维测，如果需要进一步定位到代码行，可以参考[句柄栈日志获取方法](bpta-stability-fdleak-fault-mode-overreview.md#section4734165151217)获取句柄栈，然后参考[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)进行下一步分析。

### 句柄栈分析方法

开发者可以将句柄栈日志导入DevEco Studio的Profiler工具中，分析其中可疑的句柄调用栈，排查泄漏点：

1. 单击下图1处Open File按钮导入句柄栈日志。
2. 句柄泄漏选择File Descriptors泳道，如下图2处。
3. 单击下图3处Call Trees查看句柄申请调用栈。
4. 单击下图4处选择Created & Existing，筛选出已申请并且未释放的句柄及其调用栈。
5. 按照Count排序，优先排查数量最多的句柄，如下图5处。
6. 单击想要排查的句柄，展开其调用栈，如下图6处。
7. 结合调用栈对代码进行分析，找到泄漏根因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/bZqclYzKR5WM6zla3y0eVg/zh-cn_image_0000002729611109.png)

## 开发态分析方法

对于在开发验证过程中遇到的句柄泄漏问题，或者运维态遇到的已知场景的句柄泄漏问题，开发者可以在本地基于问题场景复现并使用hidumper、hiprofiler或DevEco Studio中Profiler工具的Allocation功能抓取维测日志进行分析。

### 故障分析工具说明

* [hidumper](../harmonyos-guides/hidumper.md)：使用[查询fd及线程信息](../harmonyos-guides/hidumper.md#查询fd及线程信息)中的“hidumper -p pid --fd”命令，查询进程详细fd信息。

  ```screen
  # hidumper -p 22519 --fd
  fd num: 386
  Summary:
  Leaked fd:ashmem

  Leaked fd Top 10:
  35      ashmem
  23      socket
  22      eventfd
  20      eventpoll
  16      pipe
  6       /data/storage/el2/database/entry/rdb/browser.db
  6       /data/storage/el2/database/entry/rdb/newsfeed.db
  5       /data/storage/el2/base/cache/web/rdb/nweb_stats.db-dwr
  5       /data/storage/el2/base/cache/web/rdb/web_snapshot.db
  5       /data/storage/el2/base/cache/web/rdb/web_snapshot.db-dwr
  Top Dir 10:
  31      /proc/
  01      /proc/22519/sched_rtg_ctrl
  01      /proc/22519/task/22759/sched_qos_ctrl
  01      /proc/22519/task/22799/sched_qos_ctrl
  01      /proc/22519/task/22828/sched_qos_ctrl
  01      /proc/22519/task/22829/sched_qos_ctrl
  01      /proc/22519/task/22862/sched_qos_ctrl
  01      /proc/22519/task/23033/sched_qos_ctrl
  01      /proc/22519/task/23232/sched_qos_ctrl
  01      /proc/22519/task/23234/sched_qos_ctrl
  01      /proc/22519/task/23235/sched_qos_ctrl
  5       /data/storage/el2/database/entry/kvdb/
  ```
* [hiprofiler](../harmonyos-guides/hiprofiler.md)：开发者定界当前泄漏问题为句柄泄漏时，可以使用句柄抓取命令抓取句柄申请调用栈，进而分析此问题的泄漏点。
* DevEco Profiler调优工具：开发者可以通过使用DevEco Studio中Profiler工具的Allocation功能抓取句柄申请调用栈，分析定位具体泄漏点。使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。

**说明** 

开发阶段：推荐使用DevEco Studio的Profiler调优功能，不仅支持图形化展示应用的句柄增长趋势，也支持抓取录制过程中应用申请的句柄调用栈。

测试阶段：测试阶段重点需要脚本形式批量部署和长时间采集，推荐使用hidumper命令行定时监控应用的句柄占用情况，当超过某阈值后使用hiprofiler命令抓取一段时间的句柄申请堆栈定位问题。

### 故障分析方法

开发者在调试过程中，如果遇到应用后台业务中断或者应用冷启问题，可以通过[订阅资源泄漏事件](bpta-stability-fdleak-fault-mode-overreview.md#section151162273105)或者[订阅应用终止事件](bpta-stability-fdleak-fault-mode-overreview.md#section19969124021018)感知当前发生了句柄泄漏故障。对于开发态存在的问题，如果开发者大致能够推断出当前出现句柄泄漏的场景，推荐开发者使用DevEco Studio中Profiler工具的Allocation功能抓取句柄的异常增长点。

1. 确认问题为句柄泄漏后，开发者可以使用DevEco Studio中Profiler工具的Allocation功能抓取句柄数量和申请调用栈，使用方法可参考[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)。
2. 启动录制后，不断尝试复现发生过句柄泄漏的场景。
3. 录制完成后，可参考[句柄栈分析方法](bpta-stability-fdleak-fault-mode-overreview.md#section1937413433216)对句柄泄漏点进行定位。
