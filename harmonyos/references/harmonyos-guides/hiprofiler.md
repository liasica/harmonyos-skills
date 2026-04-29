---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiprofiler
title: hiprofiler
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > hiprofiler
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:23+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:50c28ce64617ad1ee1ed33c7d3bb86a57b14b29adbddc85c856d5d1784acecd9
---

## Hiprofiler简介

HiProfiler调优组件旨在为开发者提供一系列调优能力，可以用来帮助分析内存、性能等问题。

整体架构包括PC端和设备端。主体部分是PC端的数据展示页面和设备端的性能调优服务。PC端和设备端服务采用C/S模型，PC端的调优数据在[DevEco Studio](ide-software-install.md)和[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases)网页中展示。设备端程序运行在系统环境中，包含多个部分，其中hiprofilerd进程负责与DevEco通信，作为调优服务。设备端还包括命令行工具hiprofiler\_cmd和数据采集进程hiprofiler\_plugins。调优服务控制数据采集进程获取调优数据，数据最终流向DevEco Studio，整个过程可抽象为生产者-消费者模型。目前已完成多个插件，包括nativehook、CPU、ftrace、GPU、hiperf、xpower和memory数据采集，实现了CPU、GPU、内存和能耗等多维度调优。

Hiprofiler工具对标业界调优工具，并提供更多能力，比如[跨语言回栈、能耗数据获取、长时间堆内存抓栈功能](hiprofiler.md#插件参数说明)等。

## 环境要求

* 根据hdc命令行工具指导，完成[环境准备](hdc.md#环境准备)。
* 确保设备已正常连接，并执行hdc shell。

## 架构简介

1. PC端通过DevEco或Smartperf调用hiprofiler\_cmd命令行工具；
2. hiprofiler\_cmd进程启动hiprofilerd调优服务和hiprofiler\_plugins插件进程；
3. hiprofiler\_plugins开启对应插件，将获取到的调优数据汇总至hiprofilerd进程；
4. hiprofilerd进程将调优数据以proto格式存储到文件，或者实时返回给PC端；
5. PC端解析数据，生成泳道，展示获取到的调优数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nnas7oUxT5-jKu3XU8jqxw/zh-cn_image_0000002589324875.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=86D9F19B88BCC9474BB603AA8780F13203F0975FEF262E9983EDF1B5400CA69E)

## 命令行说明

使用hiprofiler\_cmd命令行工具可以调用不同插件并输入不同参数，以满足不同的调优需求。示范命令如下：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. --nonblock \
8. <<CONFIG
9. request_id: 1
10. session_config {
11. buffers {
12. pages: 16384
13. }
14. }
15. plugin_configs {
16. plugin_name: "ftrace-plugin"
17. sample_interval: 1000
18. config_data {
19. hitrace_categories: "binder"
20. buffer_size_kb: 204800
21. flush_interval_ms: 1000
22. flush_threshold_kb: 4096
23. trace_period_ms: 200
24. }
25. }
26. CONFIG
```

| 命令 | 命令说明 |
| --- | --- |
| -c | 设置该选项后，需要将配置文件放入/data/local/tmp目录下，将路径作为参数输入。 |
| -o | 自定义文件保存路径（需要以/data/local/tmp开头）。若不设置路径，则调优数据自动保存至/data/local/tmp/hiprofiler\_data.htrace。重复调优会覆盖原来路径的文件。 |
| -k | 杀掉已存在的调优服务进程。 |
| -s | 拉起调优服务进程。 |
| -t | 设置调优持续时间，单位：s。 |
| --nonblock | 设置hiprofiler\_cmd通过非阻塞的方式运行。  执行命令后，hiprofiler\_cmd转入后台运行，继续执行其他命令。  如果不设置该参数，hiprofiler\_cmd会阻塞执行，直到该命令结束。  **说明**：从API version 23开始支持该参数。 |

输入完hiprofiler\_cmd参数后，需要输入插件配置信息，以<<CONFIG开头，CONFIG结尾。每个插件需要的配置不同，参考[插件参数说明](hiprofiler.md#插件参数说明)。

以下是session config字段介绍：

| 字段 | 字段说明 |
| --- | --- |
| buffers | 共享内存页的数量。 |
| split\_file | 是否拆分文件。true代表拆分文件；false代表不拆分文件。 |
| split\_file\_max\_size\_mb | 设置split\_file为true的情况下，定义每个拆分文件的最大大小。 |

plugin\_configs字段介绍：

| 字段 | 字段说明 |
| --- | --- |
| plugin\_name | 开启插件的名字。 |
| sample\_interval | 插件获取调优数据的间隔，单位：ms。 |
| config\_data | 插件具体参数。每个插件需要的参数不同，参考各插件proto定义。  （代码路径：developtools/profiler/protos）。 |

生成的trace文件通过hdc file recv命令导到本地，然后上传到smartperf网站或者DevEco Studio进行解析。

## 支持插件列表

| 插件名字 | 简介 | 规格说明 |
| --- | --- | --- |
| [native hook](hiprofiler.md#native-hook插件) | 获取堆内存分配的调用栈信息。 | 采集的进程仅支持[使用调试证书签名的应用](hiprofiler.md#使用调试证书签名的应用)。 |
| [ftrace plugin](hiprofiler.md#ftrace-plugin插件) | 获取内核打点的trace事件，以及hitrace打点的数据。 | - |
| [cpu plugin](hiprofiler.md#cpu-plugin插件) | 获取进程CPU使用率信息，包括进程级和线程级的使用率。 | - |
| [gpu plugin](hiprofiler.md#gpu-plugin插件) | 获取进程GPU使用率信息。 | - |
| [xpower plugin](hiprofiler.md#xpower-plugin插件) | 获取进程能耗使用情况的数据。 | - |
| [memory plugin](hiprofiler.md#memory-plugin插件) | 获取进程内存占用情况，主要是获取进程smaps节点的数据。 | - |
| [diskio plugin](hiprofiler.md#diskio-plugin插件) | 获取进程磁盘空间占用情况。 | - |
| [network profiler](hiprofiler.md#network-profiler插件) | 通过进程内打点，获取进程HTTP/HTTPS请求的详细信息。 | 采集的进程仅支持[使用调试证书签名的应用](hiprofiler.md#使用调试证书签名的应用)。 |
| [network plugin](hiprofiler.md#network-plugin插件) | 获取进程网络流量统计信息。 | - |
| [hisysevent plugin](hiprofiler.md#hisysevent-plugin插件) | 通过hisysevent命令，获取hisysevent的事件记录数据。 | - |
| [hidump plugin](hiprofiler.md#hidump-plugin插件) | 通过SP\_daemon命令获取相关数据。 | - |

## 使用调试证书签名的应用

注意

确认命令指定的应用是否为可调试应用，可执行hdc shell "bm dump -n bundlename | grep appProvisionType"查询，预期返回信息为"appProvisionType": "debug"。

以包名com.example.myapplication为例，可执行如下命令查询：

```
1. hdc shell "bm dump -n com.example.myapplication | grep appProvisionType"
```

如果包名对应的应用是可调试应用，预期返回信息如下：

```
1. "appProvisionType": "debug",
```

构建可调试应用需要使用调试证书进行签名，申请调试证书及签名可参考：[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)。

## 插件参数说明

### native hook插件

获取堆内存分配的调用栈信息（通过malloc、mmap、calloc或realloc等基础库函数分配堆内存的调用栈），包括跨语言堆内存分配信息（如在ArkTS语言中调用napi分配native堆内存），还能展示内存泄漏未释放堆内存调用栈信息。

注意

[应用加密](code-protect.md)后只能回native栈，不能回JS栈。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| fp\_unwind | bool | true表示使用fp回栈方式进行回栈；  false表示使用dwarf回栈方式进行回栈。 | fp回栈是利用了x29寄存器保存的fp指针，函数的fp指针始终指向父函数（调用方）的fp指针，调优服务根据这一特点进行回栈，根据ip计算相对PC，然后查找maps对应区间来进行符号化。  由于现在编译期越来越优化，出现寄存器重用或者编译禁用fp，会导致fp方式回不出相应的栈；混合栈情况下，fp不会记录多重混合，于是便需要dwarf回栈方式做更精确的回栈。  dwarf回栈是根据pc寄存器在map表中查找对应的map信息，由于dwarf是逐级解析调用栈，所以其性能会比fp有劣化。  注意：fp回栈暂不支持调优非aarch64架构的设备。 |
| statistics\_interval | int | 统计间隔，表示将一个统计周期内的栈进行汇总，单位：s。 | 为实现长时间轻量化采集，提供统计模式抓栈。如果更关注调优时的性能，只需要知道每个调用栈出现的次数和总大小，不需要知道每一次具体时间，可以使用统计模式。 |
| process\_name | string | 需要进行内存调优的进程名 | 和/proc/节点下的进程名一致。 |
| startup\_mode | bool | 是否抓取进程启动阶段内存。默认不抓取启动阶段内存。 | 记录进程孵化启动到调优结束这个期间内堆内存分配的信息。 |
| js\_stack\_report | int | 是否开启跨语言回栈。  0：不抓取js栈。  1：开启抓取js栈。 | 为方舟环境提供跨语言回栈功能。 |
| malloc\_free\_matching\_interval | int | 匹配间隔，单位：s，指在相应时间间隔内，将malloc和free进行匹配。匹配到的就不进行落盘。 | 在匹配间隔内，分配并释放了的调用栈不被记录，减少了抓栈服务进程的开销。此参数设置的值大于0时，需同步将statistics\_interval参数设置为0。 |
| offline\_symbolization | bool | 是否开启离线符号化。  true：使用离线符号化。  false：使用在线符号化。 | 使用离线符号化时，根据IP匹配符号的操作在网页端（smartperf）完成，优化了native daemon的性能，减少了调优时的进程卡顿。但离线符号化会将符号表写入trace文件，导致文件大小比在线符号化时更大。 |
| sample\_interval | int | 采样大小。 | 设置此参数时开启采样模式。采样模式下对于malloc size小于采样大小进行概率性统计。调用栈分配内存大小越大，出现次数越高，被统计的几率越大。 |
| restrace\_tag | string | 需要抓取资源的类型 | 参数可多次添加不同类型。当前支持类型见表[restrace\_tag参数介绍](hiprofiler.md#restrace_tag参数介绍)。 |

### restrace\_tag参数介绍

| 参数名称 | 资源类型 | 开始支持的版本 |
| --- | --- | --- |
| RES\_GPU\_VK | vulkan类型的GPU内存分配栈。 | 21 |
| RES\_GPU\_GLES\_BUFFER | OpenGLES的buffer类型GPU内存分配栈。 | 21 |
| RES\_GPU\_GLES\_IMAGE | OpenGLES的image类型GPU内存分配栈。 | 21 |
| RES\_GPU\_CL\_BUFFER | OpenCL类型的buffer类型GPU内存分配栈。 | 21 |
| RES\_GPU\_CL\_IMAGE | OpenCL类型的image类型GPU内存分配栈。 | 21 |
| RES\_FD\_OPEN | 调用open时的句柄函数调用栈。 | 23 |
| RES\_FD\_EPOLL | 调用epoll时的句柄函数调用栈。 | 23 |
| RES\_FD\_EVENTFD | 调用eventfd时的句柄函数调用栈。 | 23 |
| RES\_FD\_SOCKET | 调用socket/socketpair时的句柄函数调用栈。 | 23 |
| RES\_FD\_PIPE | 调用pipe时的句柄函数调用栈。 | 23 |
| RES\_FD\_DUP | 调用dup时的句柄函数调用栈。 | 23 |
| RES\_FD\_ALL | 以上所有fd相关函数调用时的句柄函数调用栈。 | 23 |
| RES\_THREAD\_PTHREAD | 线程创建时的调用栈。 | 23 |
| RES\_THREAD\_ALL | 以上线程相关操作时的调用栈。 | 23 |
| RES\_ARKTS\_HEAP\_MASK | arkts内存分配栈。 | 23 |
| RES\_JS\_HEAP\_MASK | 龙雀虚拟机JSVM内存跟踪 | 23 |
| RES\_KMP\_HEAP\_MASK | kmp内存分配栈。 | 23 |
| RES\_SO\_MASK | SO内存分配栈。 | 23 |
| RES\_ASHMEM\_MASK | ashmem内存分配栈。 | 23 |
| RES\_RN\_HEAP\_MASK | rn内存分配栈。 | 23 |
| RES\_DMABUF\_MASK | dmabuf内存分配栈。 | 23 |
| RES\_ARK\_GLOBAL\_HANDLE | ark全局句柄分配栈。 | 23 |
| RES\_VMA\_ARKWEB | ArkWeb PA分配器内存跟踪。 | 23 |
| RES\_ARK\_LOCAL\_HANDLE | ark本地句柄分配栈。 | 23 |

**结果分析**

开启fp回栈+跨语言回栈（其中绿色部分为js栈）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/YgfI5fdzREmu8lfhPZBNfA/zh-cn_image_0000002589244811.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=0F68961BF14EE5C333CBB3FB1BEE5B984AE8B6785D0E91003B91901BE9DCB119)

开启dwarf回栈和跨语言回栈（可以展示出native -> js ->native的栈）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0iYDmxVaSECjCXCObT3txQ/zh-cn_image_0000002558765006.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=F650C9B9880FD7C83177BFC396A1A7D9F333CA2A4631EC1F3A6F6143D38C3455)

开启统计模式，在此模式下，栈数据会周期性展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/7PCYiwB1T-SaqA6VwAGMdg/zh-cn_image_0000002558605350.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=65DA88085227F34E1D1440841A8F4C22DEF66D1AE14012622A489DC1CCDD5BD7)

开启非统计模式，在此模式下，栈数据不会周期性展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/J6hfxM7DQeuOECm3s1TJzg/zh-cn_image_0000002589324877.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=CFFE097E90C140A8ECD5FAF90B7D61C2B7C8D449C81BF423963C993BC147624E)

### ftrace plugin插件

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| ftrace\_events | string | 抓取的trace event。 | 记录内核打点的trace event。 |
| hitrace\_categories | string | 抓取的hitrace打点信息。 | 调用hitrace能力，获取数据以proto格式写入文件。 |
| hitrace\_apps | string | 抓取的hitrace信息的进程。 | 设置此参数时，只有对应进程的trace信息会被记录。添加此参数时， hitrace\_categories不支持添加binder，否则会导致trace数据解析异常。 |
| buffer\_size\_kb | int | buffer缓存大小，单位：kB。 | hiprofiler\_plugins进程读取内核事件所需要的缓存大小。推荐使用默认数值：204800。 |
| flush\_interval\_ms | int | 采集数据频率，单位：ms。 | 推荐使用默认数值：1000。 |
| flush\_threshold\_kb | int | 刷新数据大小。 | 超过threshold刷新一次数据至文件。用smartperf默认数值即可。 |
| parse\_ksyms | bool | 是否获取内核数据。 | true：获取内核数据；false：不获取内核数据。 |
| trace\_period\_ms | int | 读取内核数据的频率。 | 用smartperf默认数值即可。 |

**结果分析**

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 10 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "ftrace-plugin"
16. sample_interval: 1000
17. config_data {
18. ftrace_events: "binder/binder_transaction"
19. ftrace_events: "binder/binder_transaction_received"
20. buffer_size_kb: 204800
21. flush_interval_ms: 1000
22. flush_threshold_kb: 4096
23. parse_ksyms: true
24. clock: "boot"
25. trace_period_ms: 200
26. debug_on: false
27. }
28. }
29. CONFIG
```

此命令读取的内核binder\_transaction和binder\_transaction\_received数据，这两个字段同时使用，才能完整展示binder两端数据。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace命令将文件导出到当前目录，然后用smartperf将该文件打开并解析。结果示例如下图：

点击binder transaction右边的箭头，可以跳转到binder对端的进程或线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/2r1V4RazSnulaytm9hrtGg/zh-cn_image_0000002589244813.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=5713C7F626849F66A1C2353573600FA1E774D17E44149208A50515CED2F201A2)

### memory plugin插件

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| report\_sysmem\_vmem\_info | bool | 是否读取虚拟内存数据。 | 从/proc/vmstat节点读取内存数据。 |
| report\_process\_mem\_info | bool | 是否获取进程详细内存数据，如rss\_shmem，rss\_file，vm\_swap等。 | 从/proc/${pid}/stat节点读取内存数据。 |
| report\_smaps\_mem\_info | bool | 是否获取进程smaps内存信息。 | 从/proc/${pid}/smaps节点获取进程smaps内存数据。 |
| report\_gpu\_mem\_info | bool | 是否获取进程GPU使用情况。 | 读取/proc/gpu\_memory节点数据。 |
| parse\_smaps\_rollup | bool | 是否从smaps\_rollup节点读取smaps统计数据。 | 读取/proc/{pid}/smaps\_rollup节点的smaps统计数据，相比使用report\_smaps\_mem\_info参数调优服务性能会更好（如CPU，内存使用优化）。 |

内存信息包含如下：

* MemTotal：总内存大小。
* MemFree：空闲内存大小。
* Buffers：文件的缓冲大小。
* Cached：缓存的大小。
* Shmem：已被分配的共享内存大小。
* Slab：内核数据缓存大小。
* SUnreclaim：不可回收的Slab大小。
* SwapTotal：交换空间的总大小。
* SwapFree：未被使用交换空间的大小。
* Mapped：设备和文件等映射的大小。
* VmallocUsed：已被使用的虚拟内存大小。
* PageTables：管理内存分页的索引表大小。
* KernelStack：Kernel消耗的内存。
* Active： 在经常使用中的缓冲或高速缓冲存储器页面文件的大小。
* Inactive：在不经常使用中的缓冲或高速缓冲存储器页面文件的大小。
* Unevictable：不能被释放的内存页。
* VmallocTotal：vmalloc虚拟内存总大小。
* CmaTotal：总的连续可用内存。
* CmaFree：空闲的可用内存。
* Zram：Zram的使用大小。
* ZramTotal：Zram的总大小。

注意

Active和Inactive的区别在于内存空间中是否包含最近被使用过的数据。当物理内存不足，需要释放正在使用的内存空间时，会优先释放Inactive的内存空间。

**结果分析**

通过hiprofiler\_cmd 命令获取memory数据。

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "memory-plugin"
16. sample_interval: 5000
17. config_data {
18. report_process_tree: true
19. report_sysmem_mem_info: true
20. sys_meminfo_counters: PMEM_MEM_TOTAL
21. sys_meminfo_counters: PMEM_MEM_FREE
22. sys_meminfo_counters: PMEM_BUFFERS
23. sys_meminfo_counters: PMEM_CACHED
24. sys_meminfo_counters: PMEM_SHMEM
25. sys_meminfo_counters: PMEM_SLAB
26. sys_meminfo_counters: PMEM_SWAP_TOTAL
27. sys_meminfo_counters: PMEM_SWAP_FREE
28. sys_meminfo_counters: PMEM_MAPPED
29. sys_meminfo_counters: PMEM_VMALLOC_USED
30. sys_meminfo_counters: PMEM_PAGE_TABLES
31. sys_meminfo_counters: PMEM_KERNEL_STACK
32. sys_meminfo_counters: PMEM_ACTIVE
33. sys_meminfo_counters: PMEM_INACTIVE
34. sys_meminfo_counters: PMEM_UNEVICTABLE
35. sys_meminfo_counters: PMEM_VMALLOC_TOTAL
36. sys_meminfo_counters: PMEM_SLAB_UNRECLAIMABLE
37. sys_meminfo_counters: PMEM_CMA_TOTAL
38. sys_meminfo_counters: PMEM_CMA_FREE
39. sys_meminfo_counters: PMEM_KERNEL_RECLAIMABLE
40. sys_meminfo_counters: PMEM_ACTIVE_PURG
41. sys_meminfo_counters: PMEM_INACTIVE_PURG
42. sys_meminfo_counters: PMEM_PINED_PURG
43. report_sysmem_vmem_info: true
44. report_process_mem_info: true
45. report_app_mem_info: false
46. report_app_mem_by_memory_service: false
47. report_purgeable_ashmem_info: true
48. report_dma_mem_info: true
49. report_gpu_mem_info: true
50. }
51. }
52. CONFIG
```

此命令读取系统的内存的基本统计信息。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace命令将文件导出到当前目录，然后通过smartperf打开并解析。结果示例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/gGvublt6RemyR3zfHcbN6g/zh-cn_image_0000002558765008.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=4EB4C2B7BA5146EE3C4ED27CBCA257A5FB94F3B2669A1CF02AB2FEE63FC7237B)

通过DevEco Studio 的工具获得内存的数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Wh_-p6V-S6-M9VzkPatCBQ/zh-cn_image_0000002558605352.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=5CE307A4D6F54AFDFF8DDFDB38B38CA29EAF2F5B0B876B61D854E36825397026)

通过DevEco->profiler->Allocation工具，选择Memory泳道，可以使用profiler的memory plugin功能。上图展示了框选时间段的进程smaps内存信息。

### xpower plugin插件

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| bundle\_name | string | 需要进行能耗调优的进程名。 | 和/proc/节点下的进程名一致。 |
| message\_type | XpowerMessageType | 需要获取能耗数据的类型。 | 数据类型包括：REAL\_BATTERY、APP\_STATISTIC、APP\_DETAIL、COMPONENT\_TOP、ABNORMAL\_EVENTS和THERMAL\_REPORT。 |

**结果分析**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/0s0KzA51RmGUjqffytF6HQ/zh-cn_image_0000002589324879.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=70F55747487B8869C28A83CB3E4A748908BCA04FC92C7DF1C5CCC2B11C16F71C)

通过DevEco->profiler->real time monitor工具，可以获取相关进程能耗数据。

### GPU plugin插件

获取GPU使用率相关信息的数据。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| pid | int | 需要进行调优的进程ID，与/proc/节点下的进程ID一致。 | - |
| report\_gpu\_info | bool | 是否展示指定进程的GPU使用率信息。 | true: 展示指定进程的GPU数据，需要设置pid。false: 不展示指定进程的GPU数据。 |

### CPU plugin插件

获取CPU使用率的相关信息。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| pid | int | 需要进行调优的进程ID。 | 和/proc/节点下的进程ID一致。 |
| report\_process\_info | bool | 是否展示指定进程的CPU使用率信息。 | true：展示指定进程的数据，需要设置pid参数；  false：不展示指定进程的数据，仅展示系统级CPU使用率数据。 |
| skip\_thread\_cpu\_info | bool | 是否跳过线程CPU使用率数据。 | true：不展示每个线程CPU使用率的信息，开启此参数时可以降低调优服务的开销；  false：展示每个线程CPU使用率的信息。 |

CPU 基本信息包含如下：

* Start Time：采集时间的时间戳。
* Duration：前一次采集到本次采集的时间差。
* TotalLoad%：总的CPU使用率。
* UserLoad%：CPU在用户态空间运行的使用率。
* SystemLoad%：CPU在内核空间运行的使用率。
* Process：进程号。

**结果分析**

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "cpu-plugin"
16. sample_interval: 1000
17. config_data {
18. report_process_info: true
19. }
20. }
21. CONFIG
```

此命令读取cpu的基本统计信息。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace命令将文件导出到当前目录，然后通过smartperf打开并解析。结果示例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/I_fBbkHLTfKBAAnylqAYKg/zh-cn_image_0000002589244815.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=884F403956915F04E852F2E77919228C8CC3ACB1AFA60F26C8797691F4F7ED22)

### diskio plugin插件

获取整机磁盘I/O使用率的相关信息。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| report\_io\_stats | IoReportType | 磁盘I/O统计类型。 | 该类型为枚举类型，目前支持：IO\_REPORT。 |

当设置成IO\_REPORT时，会获得如下磁盘IO信息：

* Data Read：从磁盘读取到内存的总字节数。
* Data Read/sec：每秒从磁盘读取到内存的字节数。
* Data Write：从内存写入磁盘的总字节数。
* Data Write/sec：每秒从内存写入磁盘的字节数。
* Reads In：读入的字节数。
* Reads In/sec：每秒读取的字节数。
* Write Out：写入的字节数。
* Write Out/sec：每秒写入的字节数。

**结果分析**

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "diskio-plugin"
16. sample_interval: 1000
17. config_data {
18. report_io_stats: IO_REPORT
19. }
20. }
21. CONFIG
```

此命令读取disk io的基本统计信息。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace将文件导出到当前目录，然后通过smartperf打开并解析。结果示例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/QmvYV5NXQiOODeq_ryBL7w/zh-cn_image_0000002558765010.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=39BD2D57F597661B210203CA7BFDB9CC235EF71322E284CBE16564F909321DFE)

### hidump plugin插件

获取应用进程的fps帧率的数据。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| report\_fps | bool | 是否报告帧率数据。 | true：报告应用进程的帧率数据；  false：不报告帧率数据。 |
| sections | uint32 | 每1秒上报多少次帧率数据。 | 默认值为10，即每隔100毫秒上报一次帧率数据。 |

**结果分析**

该插件暂时不支持smartperf工具方式的trace数据解析，只支持DevEco Studio模式下的trace数据解析。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/CYSLXSi-QIuvf8GYIRyAcg/zh-cn_image_0000002558605354.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=859F5A38FC9B0E9346250A82145E786499FA17A1DECE5A6BFBE186CDA1ED5719)

### hisysevent plugin插件

获取系统事件记录的数据。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 详细介绍 |
| --- | --- | --- | --- |
| msg | string | 自定义的字符串。 | 该字符串作为保留字段，并未实际使用。使用时可传入空字符串 |
| subscribe\_domain | string | 订阅的domain。 | 该字段用来订阅具体的domain下的所有事件。如果为空串，则订阅所有domain下的所有事件。 |
| subscribe\_event | string | 订阅的event。 | 该字段用来订阅具体的event。如果为空串，则订阅所有event。 |

**结果分析**

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "hisysevent-plugin"
16. config_data {
17. msg: "hisysevent-plugin"
18. subscribe_domain: ""
19. subscribe_event: ""
20. }
21. }
22. CONFIG
```

此命令示例抓取所有hisystem event订阅事件信息。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace将文件导出到当前目录，然后通过smartperf打开并解析。结果示例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/qexs4nvKR_60_zSNN7JLhw/zh-cn_image_0000002589324881.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=B23CDFDA899B3970C1314ED6CF33B4858709F618722B44F59321ACE5C295FEC4)

### network plugin插件

获取网络上行下载相关的数据。统计网络管理模块提供的网络流量、连接状态等。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 必选 | 详细介绍 |
| --- | --- | --- | --- | --- |
| pid | int32 | 进程ID。 | 否 | 获取指定进程的网络数据。可以传入多个参数。参数缺省时，则抓取整机的网络数据。 |
| startup\_process\_name | string | 启动的进程名。 | 否 | 如果需要抓取指定进程启动的网络数据，则需要指定此参数。 |
| restart\_process\_name | string | 重启的进程名。 | 否 | 如果需要抓取指定进程重启的网络数据，则需要指定此参数。 |

注意

startup\_process\_name和restart\_process\_name不能同时为空。

网络信息数据包含如下：

* StartTime：采集时间的时间戳。
* Duration：前一次采集到本次采集的时间差。
* Data Received：接收的网络数据总字节数。
* Data Received/sec：每秒接收的网络数据字节数。
* Data Send：发送的网络数据总字节数。
* Data Send/sec：每秒发送的网络数据字节数。
* Packets In：接收的网络总数据包数。
* Packets In/sec：每秒接收的网络数据包数。
* Packets Out：发送的网络总数据包数。
* Packets Out/sec：每秒发送的网络数据包数。

**结果分析**

示例命令：

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "network-plugin"
16. sample_interval: 1000
17. config_data {
18. }
19. }
20. CONFIG
```

此命令示例抓取整机网络数据信息。执行命令后，通过hdc file recv /data/local/tmp/hiprofiler\_data.htrace将文件导出到当前模板，然后通过smartperf打开并解析。结果示例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/4o44Y3vaQ1GqPMoqq7Md7Q/zh-cn_image_0000002589244817.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=DD73265805792012A3E79C8262D84D1A013F1A1FAE6323299144DFAAC68ECE6E)

### network profiler插件

获取进程的网络请求信息，会把每次HTTP请求当作一个数据点记录下来。

**参数介绍**

| 参数名字 | 类型 | 参数含义 | 必选 | 详细介绍 |
| --- | --- | --- | --- | --- |
| pid | int32 | 进程ID。 | 否 | 获取指定进程的网络数据。可以传入多个参数。参数缺省时，则抓取整机的网络数据。 |
| startup\_process\_name | string | 启动的进程名。 | 否 | 如果需要抓取指定进程启动的网络数据，则需要指定此参数。 |
| restart\_process\_name | string | 重启的进程名。 | 否 | 如果需要抓取指定进程重启的网络数据，则需要指定此参数。 |
| clock\_id | int | 时间时钟类型 | 是 | 1：BOOTTIME，系统启动后单调递增时间（含NTP调整）。  2：REALTIME，可调整的系统实时时间。  3：REALTIME\_COARSE，低精度实时时间。  4：MONOTONIC，无NTP调整的单调递增时间。  5：MONOTONIC\_COARSE，低精度单调递增时间。  6：MONOTONIC\_RAW，硬件原始单调递增时间。 |
| smb\_pages | int | 共享内存页数 | 是 | hiprofiler\_plugins进程和被调优进程建立的共享内存大小，建议值为16384个页大小，即：16384\*4096=67108864字节（64M）。 |
| flush\_interval | int | 磁盘写入间隔 | 否 | 每flush\_interval次网络请求触发一次磁盘写入，优化IO效率。  默认值为1。 |
| block | bool | 阻塞模式开关 | 否 | true：共享内存满时阻塞采集，可能影响性能。  false：共享内存满时丢弃超出部分的数据。  默认值为false。 |

**结果分析**

smartperf工具暂时不支持该插件的trace数据解析，若需分析network数据，请使用DevEco Studio的Profiler工具下的NetWork功能。可参考：

[网络诊断：NetWork分析](ide-profiler-network.md)

## 常用命令

### 堆内存分配调用栈数据采样记录

对com.example.insight\_test\_stage进程的堆内存分配操作进行抓栈，并开启fp回栈、离线符号化和统计模式。

```
1. $ hiprofiler_cmd \
2. -c - \
3. -t 30 \
4. -s \
5. -k \
6. <<CONFIG
7. request_id: 1
8. session_config {
9. buffers {
10. pages: 16384
11. }
12. }
13. plugin_configs {
14. plugin_name: "nativehook"
15. sample_interval: 5000
16. config_data {
17. save_file: false
18. smb_pages: 16384
19. max_stack_depth: 20
20. process_name: "com.example.insight_test_stage"
21. string_compressed: true
22. fp_unwind: true
23. blocked: true
24. callframe_compress: true
25. record_accurately: true
26. offline_symbolization: true
27. startup_mode: false
28. statistics_interval: 10
29. sample_interval: 256
30. js_stack_report: 1
31. max_js_stack_depth: 10
32. }
33. }
34. CONFIG
```

采集的数据会被保存至/data/local/tmp/hiprofiler\_data.htrace文件中，该文件包含了内存泄漏分析所需的函数调用信息、线程和动态库维度内存分配情况，以及调用栈次数和分配大小聚类信息。开启离线符号化，fp回栈，统计模式均可以提升调优服务处理数据速率。

抓取指定进程CPU使用率。

对进程号为1234的进程采集CPU数据，采集时长为30s，采样周期为1000ms，调优数据传输的共享内存大小是16384个内存页，采集的数据会被保存至/data/local/tmp/hiprofiler\_data.htrace文件中。

```
1. $ hiprofiler_cmd \
2. -c - \
3. -o /data/local/tmp/hiprofiler_data.htrace \
4. -t 30 \
5. -s \
6. -k \
7. <<CONFIG
8. request_id: 1
9. session_config {
10. buffers {
11. pages: 16384
12. }
13. }
14. plugin_configs {
15. plugin_name: "cpu-plugin"
16. sample_interval: 1000
17. config_data {
18. pid: 1234
19. report_process_info: true
20. }
21. }
22. CONFIG
```

抓取指定进程的GPU图形内存调用栈（需要使用最新smartperf release版本解析文件，下载链接：[smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases))。

```
1. $ hiprofiler_cmd \
2. -c - \
3. -t 30 \
4. -s \
5. -k \
6. <<CONFIG
7. request_id: 1
8. session_config {
9. buffers {
10. pages: 16384
11. }
12. }
13. plugin_configs {
14. plugin_name: "nativehook"
15. sample_interval: 5000
16. config_data {
17. save_file: false
18. smb_pages: 16384
19. max_stack_depth: 20
20. pid: 11237
21. string_compressed: true
22. fp_unwind: true
23. blocked: true
24. callframe_compress: true
25. record_accurately: true
26. offline_symbolization: true
27. startup_mode: false
28. statistics_interval: 10
29. malloc_disable: true
30. memtrace_enable: true
31. restrace_tag: "RES_GPU_VK"
32. restrace_tag: "RES_GPU_GLES_BUFFER"
33. restrace_tag: "RES_GPU_GLES_IMAGE"
34. restrace_tag: "RES_GPU_CL_BUFFER"
35. js_stack_report: 1
36. max_js_stack_depth: 10
37. }
38. }
39. CONFIG
```

命令中使用了malloc\_disable参数用于过滤nativeheap抓栈的数据；添加的restrace\_tag参数中没有"RES\_GPU\_CL\_IMAGE", 则不抓取OpenCL image类型的GPU内存分配栈。

从API version 23开始支持抓取指定进程创建[napi\_ref](use-napi-life-cycle.md#napi_ref)的调用栈，不会抓取创建弱引用的调用栈。

```
1. $ hiprofiler_cmd \
2. -c - \
3. -t 30 \
4. -s \
5. -k \
6. <<CONFIG
7. request_id: 1
8. session_config {
9. buffers {
10. pages: 16384
11. }
12. }
13. plugin_configs {
14. plugin_name: "nativehook"
15. sample_interval: 5000
16. config_data {
17. save_file: false
18. smb_pages: 16384
19. max_stack_depth: 20
20. pid: 11237
21. string_compressed: true
22. fp_unwind: true
23. blocked: true
24. callframe_compress: true
25. record_accurately: true
26. offline_symbolization: true
27. startup_mode: false
28. statistics_interval: 10
29. malloc_disable: true
30. memtrace_enable: true
31. restrace_tag: "RES_ARK_GLOBAL_HANDLE"
32. }
33. }
34. CONFIG
```

从API version 23开始支持LocalHandle对象内存录制功能。例如，可通过如下方式对com.example.insight\_test\_stage进程进行内存录制。

```
1. $ hiprofiler_cmd \
2. -c - \
3. -t 20 \
4. -s \
5. -k \
6. <<CONFIG
7. request_id: 1
8. session_config {
9. buffers {
10. pages: 16384
11. }
12. }
13. plugin_configs {
14. plugin_name: "nativehook"
15. sample_interval: 5000
16. config_data {
17. save_file: false
18. smb_pages: 16384
19. max_stack_depth: 20
20. process_name: "com.example.insight_test_stage"
21. string_compressed: true
22. fp_unwind: true
23. blocked: true
24. callframe_compress: true
25. record_accurately: true
26. offline_symbolization: true
27. startup_mode: true
28. statistics_interval: 10
29. malloc_disable: true
30. memtrace_enable: true
31. restrace_tag: "RES_ARK_LOCAL_HANDLE"
32. }
33. }
34. CONFIG
```

LocalHandle对象内存录制功能要求被测应用在启动时替换加载维测库，才能正常采集LocalHandle内存信息。

应用替换加载维测库方法：

1.应用处于退出状态：下发LocalHandle对象内存录制命令，设置startup\_mode参数为true，然后启动应用，应用启动后即可进行数据采集。

2.应用处于运行状态：下发LocalHandle对象内存录制命令，设置startup\_mode参数为true，然后重启应用，应用重启后即可进行数据采集。

说明

1.应用加载维测库后，只要应用不退出，维测库持续生效。此后，可以通过非启动模式录制localhandle内存。

2.使用此种方式后，此次应用打开的时长会变长，此次运行的性能上也会有损失。但不影响下次的使用。

3.此种方式抓取到的localhandle内存一定是泄漏的。

4.命令行方式获取的trace文件，可以通过DevEco Profiler[离线导入](ide-snapshot-basic-operations.md#section6760173514388)文件功能进行解析。导入的单个文件大小不超过1.5G。

## 常见问题

### 调优出现异常

**现象描述**

使用hiprofiler\_cmd命令时，显示Service not started。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ycvm7h36Q7mR6u7VSeQweg/zh-cn_image_0000002558765012.png?HW-CC-KV=V1&HW-CC-Date=20260429T053421Z&HW-CC-Expire=86400&HW-CC-Sign=6A9886CC9FB020B1426DF953F67CBFE96085CB0496176BB92B38D11F57759805)

**可能原因&解决方法**

调优服务未能开启，说明正在使用DevEco Studio调优或者上次调优异常退出，需要执行hiprofiler\_cmd -k之后再重新执行调优命令。

### 抓取到的trace文件为空

**现象描述**

抓取到的trace文件是空的

**可能原因&解决方法**

需要检查生成文件的路径是否在/data/local/tmp/目录下。如果目标路径是/data/local/tmp下的一个文件夹，则尝试对文件夹执行chmod 777操作。如果是user版本使用nativehook或者network profiler插件抓取的应用不是[使用调试证书签名的应用](hiprofiler.md#使用调试证书签名的应用)，也抓不到数据。

### 调优数据疑似不准确

**现象描述**

hiprofiler抓取到的native heap和hidumper查看的native heap有差异。

**可能原因&解决方法**

hidumper抓取的是进程维度内存使用情况，hiprofiler抓取到的是进程用户态通过基础库函数（malloc，mmap，realloc等，operator new也是调用的malloc）分配堆内存的数据。两者之间会有差异，差异存在于线程的内存缓存，堆内存延迟释放，加载器使用内存等。

### 调优时目标进程卡顿

**现象描述**

使用hiprofiler\_cmd命令抓取应用进程的内存trace，采用FP回栈或者dwarf回栈时，出现应用进程卡顿。

**可能原因&解决方法**

可以通过hiprofiler\_cmd命令中config参数配置来进行调整。

hiprofiler\_cmd命令中config参数的调整方法如下：

* 适当减小max\_stack\_depth和max\_js\_stack\_depth参数的值，减少回栈深度，减少调用栈信息的采集。
* 适当增大smb\_pages参数的值，增大调优数据传输的共享内存大小。默认值为16384个页大小，即：16384\*4096=67108864字节（64M）。可以调整到128M。
* 适当增加sample\_interval参数的值，增大采样线程栈的大小。默认值为256，可以调整到512。

### 调优时使用FP回栈异常

**现象描述**

使用hiprofiler\_cmd命令抓取应用进程的内存trace，对应的共享库（SO）无法进行基于FP的栈回溯。

**可能原因&解决方法**

检查对应的共享库编译时是否开启了-fomit-frame-pointer编译选项，需保证该选项保持关闭状态。
