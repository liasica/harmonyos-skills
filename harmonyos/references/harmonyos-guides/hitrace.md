---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace
title: hitrace
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > hitrace
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:e7452f8e1e4d92712f5f84bd53143321c5324c36baa82a5a4f3fc92cea6627a5
---

hitrace命令行工具提供trace信息采集能力，支持采集系统提供的打点和开发者使用[HiTraceMeter接口](hitracemeter-intro.md)在应用中设置的打点。该工具支持多种方式采集文本格式或二进制格式的trace信息，帮助开发者观测程序运行情况和定位故障问题。

## 环境要求

* 根据hdc命令行工具指导，完成[hdc环境准备](hdc.md#环境准备)。
* 确保设备已正常连接，并执行hdc shell。

## 命令行说明

| 命令 | 含义说明 |
| --- | --- |
| -h/--help | 查看帮助。 |
| -l/--list\_categories | 查看tag列表。 |
| --trace\_begin | 开始捕获trace。 |
| --trace\_finish | 结束捕获trace。 |
| --trace\_finish\_nodump | 结束捕获trace，与--trace\_finish的区别是不输出trace信息。 |
| --trace\_dump | 导出trace信息。未指定-o/--output参数时，文本格式Trace默认输出至stdout。 |
| --record | 使能录制模式，允许长时间采集并落盘trace数据，必须和--trace\_begin或--trace\_finish一起使用。 |
| --overwrite | 设置内核缓冲区满之后的行为，未设置此选项时默认丢弃最老数据，设置此选项后丢弃最新数据。 |
| --file\_size | 设置文件大小（单位为KB），仅在采集二进制格式trace数据时有效。 |
| --total\_size | 设置总文件大小（单位为KB），仅在录制模式下采集二进制格式trace数据时有效。  **说明**：从API version 24开始，支持该命令。 |
| -b N/--buffer\_size N | 设置用于存储和读取trace的缓冲区大小（单位为KB）。最小值为512，最大值与设备当前可用内存有关。 |
| -t N/--time N | 设置hitrace采集时长，单位为s。 |
| -o/--output filename | 指定保存trace数据的文件名称，必须和命令--trace\_dump或--record或--dump\_bgsrv一起使用。仅支持输出到 /data/local/tmp 目录下。  **说明**：  对于API version 24及之后版本，导出trace格式为二进制时，支持此命令。  对于API version 23及之前版本，导出trace格式为二进制时，不支持此命令。 |
| -z | 压缩捕获的trace数据。 |
| --text | 导出trace数据为文本格式（默认为文本格式）。 |
| --raw | 导出trace数据为二进制格式（默认为文本格式）。 |
| --trace\_clock | 设置向trace添加时间戳的时钟类型，可以是boot（默认）、global、mono、uptime或perf。不同设备支持的时钟类型不同，建议使用默认的boot进行采集，其时间为从本次开机起的时间戳，单位为s。每种时间类型的说明如下：  - boot：系统启动后的时间戳，休眠或系统挂起时也会计时。  - global：全局同步的时钟，可能有性能开销。  - mono：系统启动后的时间戳，休眠或系统挂起时不会计时。  - uptime：系统启动后的时间戳，类似于mono。  - perf：高性能计数器，适合性能分析。 |
| --start\_bgsrv | 开启快照模式trace捕获。 |
| --dump\_bgsrv | 触发快照模式trace输出到文件。 |
| --stop\_bgsrv | 关闭快照模式trace捕获。 |
| --trace\_level | 设置trace输出级别阈值，输出级别可以是Debug、Info、Critical、Commercial或其对应缩写D、I、C、M。  **说明**：从API version 19开始，支持该命令。 |
| --get\_level | 查询trace输出级别阈值。  **说明**：从API version 20开始，支持该命令。 |

**说明** 

trace信息可以用两种不同的格式保存，分别为文本格式和二进制格式。文本格式的trace可以直接用文本编辑器查看，二进制格式的trace可以使用[Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host)工具进行可视化trace分析。工具下载链接：[developtools\_smartperf\_host官方发行版](https://gitcode.com/openharmony/developtools_smartperf_host/releases)。

## 常用命令

### 查看帮助信息

```shell
hitrace -h
```

**使用样例**：

```shell
$ hitrace -h
2025/05/28 15:19:52 hitrace enter, running_state is SHOW_HELP
usage: hitrace [options] [categories...]
options include:
  -b N                   Set the size of the buffer (KB) for storing and reading traces.
                         The default buffer size is 18432 KB.
  --buffer_size N        Like "-b N".
  -l                     List available hitrace categories.
  --list_categories      Like "-l".
  -t N                   Set the hitrace running duration in seconds (5s by default), which depends on
                         the time required for analysis.
  --time N               Like "-t N".
  --trace_clock clock    Sets the type of the clock for adding a timestamp to a trace, which can be
                         boot (default), global, mono, uptime, or perf.
  --trace_begin          Start capturing traces.
  --trace_dump           Dump traces to a specified path (stdout by default).
  --trace_finish         Stop capturing traces and dumps traces to a specified path (stdout by default).
  --trace_finish_nodump  Stop capturing traces and not dumps traces.
  --record               Enable or disable long-term trace collection tasks in conjunction with
                         "--trace_begin" and "--trace_finish".
  --overwrite            Set the action to take when the buffer is full. If this option is used,
                         the latest traces are discarded; if this option is not used (default setting),
                         the earliest traces are discarded.
  -o filename            Specifies the name of the target file (stdout by default).
  --output filename      Like "-o filename".
  -z                     Compresses a captured trace.
  --text                 Specify the output format of trace as text.
  --raw                  Specify the output format of trace as raw trace, the default format is text.
  --start_bgsrv          Enable trace_service in snapshot mode.
  --dump_bgsrv           Trigger the dump trace task of the trace_service.
  --stop_bgsrv           Disable trace_service in snapshot mode.
  --file_size            Sets the size of the raw trace (KB). The default file size is 102400 KB.
                         Only effective in raw trace mode
  --total_size           Sets the total size of all traces (KB). The default total size is 2048 × 1024 KB.
                         Only effective in raw trace mode
  --trace_level level    Set the system parameter "persist.hitrace.level.threshold", which can control
                         the level threshold of tracing. Valid values for "level" include
                         D or Debug, I or Info, C or Critical, M or Commercial.
  --get_level            Query the system parameter "persist.hitrace.level.threshold",
                         which can control the level threshold of tracing.
```

### 查看hitrace包含的tag

```shell
hitrace -l
```

各tag具体含义参考下面的tag名称与描述对照表。

| tag名称 | 描述 |
| --- | --- |
| ability | 用户态trace标签，能力管理器服务。 |
| accesscontrol | 用户态trace标签，访问控制模块。 |
| accessibility | 用户态trace标签，无障碍软件服务管理器。 |
| ace | 用户态trace标签，ArkUI跨平台引擎开发框架。 |
| animation | 用户态trace标签，动画模块。 |
| app | 用户态trace标签，应用模块。通过[HiTraceMeter](hitracemeter-intro.md)接口做的trace打点属于app tag。 |
| ark | 用户态trace标签，Ark模块。 |
| account | 用户态trace标签，账户管理器。 |
| binder | 内核态trace标签，binder通信内核信息。 |
| bluetooth | 用户态trace标签，蓝牙通信。 |
| cloud | 用户态trace标签，云子系统。 |
| commercial | 用户态trace标签，nolog版本标签。 |
| commonlibrary | 用户态trace标签，通用库。 |
| dcamera | 用户态trace标签，分布式相机。 |
| daudio | 用户态trace标签，分布式音频。 |
| devicemanager | 用户态trace标签，设备管理器。 |
| deviceauth | 用户态trace标签，设备认证。 |
| deviceprofile | 用户态trace标签，设备配置文件。 |
| dhfwk | 用户态trace标签，分布式硬件框架。 |
| dinput | 用户态trace标签，分布式输入。 |
| dlpcre | 用户态trace标签，数据防泄露凭证服务。 |
| disk | 内核态trace标签，磁盘I/O。 |
| distributeddatamgr | 用户态trace标签，分布式数据管理器。 |
| dscreen | 用户态trace标签，分布式屏幕。 |
| dsched | 用户态trace标签，分布式调度。 |
| dsoftbus | 用户态trace标签，分布式软总线。 |
| drm | 用户态trace标签，数字版权管理。 |
| erofs | 内核态trace标签，增强型只读文件系统。 |
| ffrt | 用户态trace标签，FFRT任务。 |
| filemanagement | 用户态trace标签，文件管理。 |
| freq | 内核态trace标签，CPU频率。 |
| gresource | 用户态trace标签，全局资源管理器。 |
| graphic | 用户态trace标签，图形模块。 |
| hdcd | 用户态trace标签，hdcd工具。 |
| hdf | 用户态trace标签，硬件驱动框架。 |
| huks | 用户态trace标签，通用密钥库。 |
| idle | 内核态trace标签，CPU空闲信息。 |
| interconn | 用户态trace标签，互联子系统。 |
| ipa | 内核态trace标签，热功耗分配器。 |
| irq | 内核态trace标签，IRQ事件。 |
| irqoff | 内核态trace标签，IRQ禁用代码段追踪。 |
| i2c | 内核态trace标签，I2C总线事件。 |
| load | 内核态trace标签，CPU负载。 |
| membus | 内核态trace标签，内存总线利用率。 |
| memory | 内核态trace标签，内存信息。 |
| memreclaim | 内核态trace标签，内核内存回收。 |
| misc | 用户态trace标签，misc模块。 |
| mdfs | 用户态trace标签，移动分布式文件系统。 |
| mmc | 内核态trace标签，嵌入式多媒体卡命令。 |
| multimodalinput | 用户态trace标签，多模态输入。 |
| musl | 用户态trace标签，musl模块。 |
| net | 用户态trace标签，网络模块。 |
| notification | 用户态trace标签，通知模块。 |
| nweb | 用户态trace标签，NWeb模块。 |
| ohos | 用户态trace标签，系统通用标签。 |
| pagecache | 内核态trace标签，页缓存。 |
| power | 用户态trace标签，电源管理器。 |
| preemptoff | 内核态trace标签，抢占禁用代码段追踪。 |
| push | 用户态trace标签，推送子系统。 |
| regulators | 内核态trace标签，电压电流调节器。 |
| rpc | 用户态trace标签，RPC与IPC通信。 |
| samgr | 用户态trace标签，服务能力管理组。 |
| sched | 内核态trace标签，CPU调度。 |
| schedlt | 内核态trace标签，轻量级CPU调度。  **说明**：从API version 23开始，支持该标签。 |
| security | 用户态trace标签，安全子系统。 |
| sensors | 用户态trace标签，传感器模块。 |
| sync | 内核态trace标签，DMA同步。 |
| useriam | 用户态trace标签，用户身份与访问管理。 |
| ufs | 内核态trace标签，通用闪存存储命令。 |
| usb | 用户态trace标签，USB子系统。 |
| virse | 用户态trace标签，虚拟化服务。 |
| workq | 内核态trace标签，内核worker队列。 |
| window | 用户态trace标签，窗口管理器。 |
| zbinder | 内核态trace标签，zbinder事件。 |
| zcamera | 用户态trace标签，相机模块。 |
| zimage | 用户态trace标签，图像模块。 |
| zmedia | 用户态trace标签，媒体模块。 |
| zaudio | 用户态trace标签，音频模块。 |

**使用样例**：

```shell
$ hitrace -l
2025/05/27 16:24:38 hitrace enter, running_state is SHOW_LIST_CATEGORY
            tagName:   description:
             ability - Ability Manager
       accesscontrol - Access Control Module
       accessibility - Accessibility Manager
             account - Account Manager
......
```

### 捕获指定时长文本格式trace

不指定-o参数时，默认将捕获到的trace内容显示在命令行窗口。下面参数是指定采集10秒的数据，缓冲区大小为204800KB，采集的tag为app。

```shell
hitrace -t 10 -b 204800 app
```

**使用样例**：

```shell
$ hitrace -t 10 -b 204800 app
2025/06/04 10:14:52 start capture, please wait 10s ...
# tracer: nop
#                                          _-----=> irqs-off
#                                         / _----=> need-resched
#                                        | / _---=> hardirq/softirq
#                                        || / _--=> preempt-depth
#                                        ||| /     delay
#           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
#              | |           |       |   ||||      |         |
 KstateRecvThrea-1132    (    952) [003] .... 589942.951387: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951554: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 15461 KILLED][SIG 9]|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951693: tracing_mark_write: E|952|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951737: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 589942.951909: tracing_mark_write: B|952|H:ProcessEvent, eventId: 6|I62
 state_change_ha-1139    (    952) [001] .... 589942.952510: tracing_mark_write: E|952|I62
2025/06/04 10:15:02 TraceFinish done.
```

指定-o参数时，可以将trace信息保存到指定目录，建议保存在/data/local/tmp路径下。

```shell
hitrace -t 10 -b 204800 app -o /data/local/tmp/test.ftrace
```

**使用样例**：

```shell
$ hitrace -t 10 -b 204800 app -o /data/local/tmp/test.ftrace
2025/06/04 10:19:47 start capture, please wait 10s ...
2025/06/04 10:19:57 capture done, start to read trace.
2025/06/04 10:19:57 trace read done, output: /data/local/tmp/test.ftrace
2025/06/04 10:19:57 TraceFinish done.
```

### 捕获指定时长二进制格式trace

命令带--raw参数时可捕获二进制格式trace，捕获二进制格式trace时不支持指定路径，固定保存在路径/data/log/hitrace下。采集结束后生成文件的绝对路径会显示在命令行窗口。

```shell
hitrace -t 10 -b 204800 app --raw
```

**使用样例**：

```shell
$ hitrace -t 10 -b 204800 app --raw
2025/06/04 10:21:16 hitrace enter, running_state is RECORDING_SHORT_RAW
2025/06/04 10:21:16 args: tags:app bufferSize:204800 overwrite:1
2025/06/04 10:21:16 start capture, please wait 10s ...
2025/06/04 10:21:27 capture done, output files:
    /data/log/hitrace/record_trace_20250604102116@590322-695861087.sys
```

### 快照模式捕获文本格式trace

快照模式下，trace信息保存在内核缓冲区。当数据量超出缓冲区大小时，默认丢弃最早的数据。

使用以下命令开启快照模式，指定缓冲区大小为204800KB，采集的tag为app和graphic。

```shell
hitrace --trace_begin -b 204800 app graphic
```

**使用样例**：

```shell
$ hitrace --trace_begin -b 204800 app graphic
2025/06/04 16:03:39 hitrace enter, running_state is RECORDING_LONG_BEGIN
2025/06/04 16:03:39 args: tags:app,graphic bufferSize:204800 overwrite:1
2025/06/04 16:03:39 OpenRecording done.
```

在开启快照模式后，可以使用下面的命令将当前缓冲区内的数据导出。默认将trace信息显示到命令行窗口。

```shell
hitrace --trace_dump
```

**使用样例**：

```shell
$ hitrace --trace_dump
2025/06/04 16:07:57 start to read trace.
# tracer: nop
#                                          _-----=> irqs-off
#                                         / _----=> need-resched
#                                        | / _---=> hardirq/softirq
#                                        || / _--=> preempt-depth
#                                        ||| /     delay
#           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
#              | |           |       |   ||||      |         |
 KstateRecvThrea-1132    (    952) [002] .... 610865.463378: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463503: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 14446 KILLED][SIG 9]|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463626: tracing_mark_write: E|952|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463654: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610865.463767: tracing_mark_write: B|952|H:ProcessEvent, eventId: 6|I62
 state_change_ha-1139    (    952) [001] .... 610865.463879: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.506055: tracing_mark_write: B|952|H:ProcessEvent, eventId: 0|I62
 state_change_ha-1139    (    952) [001] .... 610866.506297: tracing_mark_write: B|952|H:HandleStateTransition, 20020111_com.ohos.medialibrary.medialibrarydata_[6255]|I62
 state_change_ha-1139    (    952) [001] .... 610866.506782: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.506824: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.557458: tracing_mark_write: B|952|H:ProcessEvent, eventId: 0|I62
 state_change_ha-1139    (    952) [001] .... 610866.558060: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.558101: tracing_mark_write: E|952|I62
```

导出时也可以使用-o命令保存到指定文件，建议保存到/data/local/tmp路径下。

```shell
hitrace --trace_dump -o /data/local/tmp/test.ftrace
```

**使用样例**：

```shell
$ hitrace --trace_dump -o /data/local/tmp/test.ftrace
2025/06/04 16:09:10 start to read trace.
2025/06/04 16:09:10 trace read done, output: /data/local/tmp/test.ftrace
```

需要停止采集时，有如下三种命令：

1. 停止采集，并将当前缓冲区内的trace信息显示到命令行窗口。

   ```shell
   hitrace --trace_finish
   ```

   **使用样例**：

   ```shell
   $ hitrace --trace_finish
   2025/06/04 16:22:02 start to read trace.
   # tracer: nop
   #                                          _-----=> irqs-off
   #                                         / _----=> need-resched
   #                                        | / _---=> hardirq/softirq
   #                                        || / _--=> preempt-depth
   #                                        ||| /     delay
   #           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
   #              | |           |       |   ||||      |         |
   KstateRecvThrea-1132    (    952) [002] .... 610865.463378: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
   KstateRecvThrea-1132    (    952) [002] .... 610865.463503: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 14446 KILLED][SIG 9]|I62
   KstateRecvThrea-1132    (    952) [002] .... 610865.463626: tracing_mark_write: E|952|I62
   KstateRecvThrea-1132    (    952) [002] .... 610865.463654: tracing_mark_write: E|952|I62
   ```
2. 停止采集，并将当前缓冲区内的trace信息保存到指定文件。建议保存路径为/data/local/tmp。

   ```shell
   hitrace --trace_finish -o /data/local/tmp/test.ftrace
   ```

   **使用样例**：

   ```shell
   $ hitrace --trace_finish -o /data/local/tmp/test.ftrace
   2025/06/04 16:24:52 start to read trace.
   2025/06/04 16:24:52 trace read done, output: /data/local/tmp/test.ftrace
   2025/06/04 16:24:52 Trace Closed.
   ```
3. 停止采集，不输出trace信息。

   ```shell
   hitrace --trace_finish_nodump
   ```

   **使用样例**：

   ```shell
   $ hitrace --trace_finish_nodump
   2025/06/04 16:26:11 hitrace enter, running_state is RECORDING_LONG_FINISH_NODUMP
   2025/06/04 16:26:11 end capture trace.
   ```

### 快照模式捕获二进制格式trace

快照模式下捕获二进制格式trace时不支持指定tag，默认采集以下tag。

```shell
"net", "dsched", "graphic", "multimodalinput", "dinput", "ark", "ace", "window","zaudio", "daudio", "zmedia", "dcamera", "zcamera", "dhfwk", "app", "gresource", "ability", "power", "samgr", "ffrt", "nweb", "hdf", "virse", "workq", "ipa", "sched", "freq", "disk", "sync", "binder", "mmc", "membus", "load"
```

使用下面的命令开启捕获二进制trace。

```shell
hitrace --start_bgsrv
```

**使用样例**：

```shell
$ hitrace --start_bgsrv
2025/06/04 16:44:54 hitrace enter, running_state is SNAPSHOT_START
2025/06/04 16:44:54 OpenSnapshot done.
```

使用以下命令将当前缓冲区的trace信息导出到文件。二进制格式trace支持指定路径（目前仅支持设定路径为/data/local/tmp）导出或显示到命令行窗口。

```shell
hitrace --dump_bgsrv
```

**使用样例1**：

不指定路径的标准快照模式命令例如：

```shell
$ hitrace --dump_bgsrv
2025/06/04 16:50:34 hitrace enter, running_state is SNAPSHOT_DUMP
2025/06/04 16:50:35 DumpSnapshot done, output:
    /data/log/hitrace/trace_20250604164454@613340-339960.sys
```

**使用样例2**：

从API version 24开始，快照模式下支持指定路径，例如：

```shell
$ hitrace --dump_bgsrv -o /data/local/tmp/test.sys
2025/06/04 16:50:34 hitrace enter, running_state is SNAPSHOT_DUMP
2025/06/04 16:50:35 DumpSnapshot done, output:
     /data/local/tmp/test.sys
```

在结束捕获时，可以使用下面的命令停止采集。

```shell
hitrace --stop_bgsrv
```

**使用样例**：

```shell
$ hitrace --stop_bgsrv
2025/06/04 16:52:51 hitrace enter, running_state is SNAPSHOT_STOP
2025/06/04 16:52:52 CloseSnapshot done.
```

### 录制模式捕获trace

录制模式下，系统会持续保存运行时生成的二进制格式trace，文件大小超过设定的值时会生成新文件。支持指定保存路径（目前仅支持设定路径为/data/local/tmp）。

使用以下命令开启录制模式。缓冲区大小设定为204800KB，文件大小设为102400KB，采集的tag为app和graphic。

```shell
hitrace --trace_begin --record -b 204800 --file_size 102400 app graphic
```

**使用样例1**：

不指定路径的录制模式下例如：

```shell
$ hitrace --trace_begin --record -b 204800 --file_size 102400 app graphic
2025/06/04 17:03:37 hitrace enter, running_state is RECORDING_LONG_BEGIN_RECORD
2025/06/04 17:03:37 args: tags:app,graphic bufferSize:204800 overwrite:1 fileSize:102400
2025/06/04 17:03:37 trace capturing.
```

**使用样例2**：

从API version 24开始，录制模式下支持指定路径，例如：

```shell
$ hitrace --trace_begin --record sched app -o /data/local/tmp --total_size 1024000
2025/06/04 17:03:37 hitrace enter, running_state is RECORDING_LONG_BEGIN_RECORD
2025/06/04 17:03:37 args: tags:sched, app bufferSize:18432 overwrite:1 totalSize:1024000
2025/06/04 17:03:37 trace capturing.
```

采集结束时，使用以下命令停止采集，命令行窗口会显示生成的文件的绝对路径。

```shell
hitrace --trace_finish --record
```

**使用样例**：

```shell
$ hitrace --trace_finish --record
2025/06/04 17:06:14 hitrace enter, running_state is RECORDING_LONG_FINISH_RECORD
2025/06/04 17:06:15 capture done, output files:
    /data/log/hitrace/record_trace_20250604170337@614463-183970330.sys
    /data/log/hitrace/record_trace_20250604170423@614508-554071886.sys
    /data/log/hitrace/record_trace_20250604170552@614597-598551039.sys
```

### 捕获trace后进行压缩

```shell
hitrace -z -b 102400 -t 10 sched freq idle disk -o /data/local/tmp/test.ftrace
```

**使用样例**：

```shell
$ hitrace -z -b 102400 -t 10 sched freq idle disk -o /data/local/tmp/test.ftrace
2024/11/14 12:00:18 start capture, please wait 10s ...
2024/11/14 12:00:28 capture done, start to read trace.
2024/11/14 12:00:29 trace read done, output: /data/local/tmp/test.ftrace
2024/11/14 12:00:29 TraceFinish done.
```

### 设置和查询trace输出级别阈值

打点级别优先级从高到低分别为 M（Commercial）、C（Critical）、I（Info）、D（Debug），低于trace输出级别阈值的打点将不会生效。

开发者可使用带trace级别的打点接口（参考[@ohos.hiTraceMeter](../harmonyos-references/js-apis-hitracemeter.md)和[trace.h](../harmonyos-references/capi-trace-h.md)中的API version 19的trace打点接口），测试不同阈值下的trace输出是否符合预期。

```shell
// 设置trace输出级别阈值
hitrace --trace_level D/I/C/M
hitrace --trace_level Debug/Info/Critical/Commercial
// 查询trace输出级别阈值
hitrace --get_level
```

**使用样例**：

```shell
$ hitrace --trace_level Info
2025/08/16 10:34:23 hitrace enter, running_state is SET_TRACE_LEVEL
2025/08/16 10:34:23 success to set trace level.
$ hitrace --get_level
2025/08/16 10:34:29 hitrace enter, running_state is GET_TRACE_LEVEL
2025/08/16 10:34:29 the current trace level threshold is Info
```

## trace文件名说明

使用hitrace命令行工具采集二进制格式trace信息时，可以指定文件路径（目前仅支持设定路径为/data/local/tmp）。默认保存在/data/log/hitrace路径下，hitrace自动生成文件名并将绝对路径显示在命令行窗口。

快照模式下生成的trace文件名以trace开头，录制模式下生成的trace文件名以record开头，后面为本地时间和boot time（从开机时间开始的时间戳）。

以下面这个文件名为例：20250701215441说明这个文件生成的时间为2025年7月1日21时54分41秒，此时对应的boot time为6016.653165227。

```shell
$ hitrace --dump_bgsrv
2025/07/01 21:54:41 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/01 21:54:42 DumpSnapshot done, output:
    /data/log/hitrace/trace_20250701215441@6016-653165227.sys
```

## 常见问题

### 执行hitrace命令后显示错误码1

**现象描述**

执行hitrace命令后报错，错误码为1。

```shell
$ hitrace --dump_bgsrv
2025/07/04 17:20:38 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/04 17:20:38 error: DumpSnapshot failed, errorCode(1)
```

**可能原因&解决方法**

错误码1表示hiview进程状态异常，可以尝试重启手机后重新采集。

### 执行hitrace命令后报错“not support category on this device”

**现象描述**

执行hitrace命令后报错，命令行窗口显示“not support category on this device”。

```shell
$ hitrace -t 10 aaa
2025/07/04 17:24:21 error: aaa is not support category on this device.
2025/07/04 17:24:21 error: parsing args failed, exit.
```

**可能原因&解决方法**

命令中指定的tag不存在，建议使用“hitrace -l”命令查看支持的tag范围。

### 执行hitrace命令后显示错误码1004

**现象描述**

执行hitrace命令后报错，错误码为1004。

```shell
$ hitrace --dump_bgsrv
2025/07/04 17:25:58 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/04 17:25:58 error: DumpSnapshot failed, errorCode(1004)
```

**可能原因&解决方法**

1004表示写入文件错误，可能的原因包括：

1. 采集文本格式trace时，使用-o参数指定输出的文件路径不存在或无权限。建议将trace保存到/data/local/tmp路径下。
2. 磁盘空间已满时，不会生成新的trace文件，建议释放磁盘空间，确保空闲空间大于500MB，然后重新采集。

### 执行hitrace命令后报错“illegal path”

**现象描述**

执行hitrace命令后报错，命令行窗口显示“illegal path”。

```shell
$ hitrace --dump_bgsrv -o /data/local/test
2026/03/27 17:25:58 hitrace enter, running_state is SNAPSHOT_DUMP
2026/03/27 17:25:58 error: illegal path
```

**可能原因&解决方法**

illegal path表示指定的路径非法，可能的原因包括：

1. 采集二进制格式trace时，使用-o参数指定输出的文件路径不是/data/local/tmp或其子目录。改为/data/local/tmp或其子目录即可。
2. 录制模式下，使用-o参数指定输出的文件路径不是/data/local/tmp或其子目录。改为/data/local/tmp或其子目录即可。
