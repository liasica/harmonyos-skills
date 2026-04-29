---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper
title: hidumper
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > hidumper > hidumper
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d55e42231b4abaca4450030d86c439084aa54442cca816593bbd83f3c57c376
---

HiDumper是用于统一系统信息导出的命令行工具，支持分析CPU、内存、存储等系统资源使用情况，查询系统服务运行情况，定位资源使用异常、通信等相关问题。

针对HiDumper所支撑的使用场景，本章节将介绍其查询内存信息、查询CPU使用情况、查询系统能力、查询进程信息、查询存储信息、查询系统信息等基础功能，以及系统故障日志获取，进程间通信记录导出，导出信息支持压缩转储等能力。

HiDumper命令行工具使用常见问题汇总在[常见问题](hidumper.md#常见问题)章节。

## 环境要求

* 根据hdc命令行工具指导，完成[环境准备](hdc.md#环境准备)。
* 请确保设备已正常连接，并执行hdc shell。

## 命令行说明

| 选项 | 说明 |
| --- | --- |
| -h | 帮助命令。 |
| [-lc](hidumper.md#查询系统信息) | 列出系统信息簇。 |
| [-ls](hidumper.md#查询系统服务列表) | 列出正在运行的系统能力。 |
| [-c](hidumper.md#查询系统信息) | 获取系统全量信息簇详细信息，包含设备信息、内核信息和环境变量等。 |
| [-c [base system]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询系统信息) | 获取指定信息簇详细信息，可选"base"或者"system"。 |
| [-s](hidumper.md#获取系统服务详细信息) | 获取所有系统能力详细信息。 |
| [-s [SA0 SA1]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#获取系统服务详细信息) | 获取一个或多个系统能力的详细信息。多个系统能力名称之间使用空格分隔。可通过 -ls 查询系统能力名称。 |
| [-s [SA] -a ["option"]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#获取指定系统服务提供的能力) | 执行单个系统能力的特定选项。  SA：系统能力名称。  option：该系统能力支持的选项。可通过 -s [SA] -a ["-h"] 获取单个系统能力支持的所有选项。 |
| [-e](hidumper.md#获取系统故障日志) | 获取记录的故障日志。输出日志的规格可参考：[CppCrash](cppcrash-guidelines.md#日志规格)、[JSCrash](jscrash-guidelines.md#日志规格)、[AppFreeze](appfreeze-guidelines.md#日志规格)。 |
| [-e --list [process\_name] [-n num] [--since timestamp] [--until timestamp]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#获取异常退出记录列表) | 获取异常退出记录列表。  **说明**：从API version 22开始，支持该参数。 |
| [-e --print [process\_name] [-n num] [--since timestamp] [--until timestamp]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#获取异常退出故障日志) | 获取异常退出故障日志。输出日志的规格可参考：[CppCrash](cppcrash-guidelines.md#日志规格)、[JSCrash](jscrash-guidelines.md#日志规格)、[AppFreeze](appfreeze-guidelines.md#日志规格)。  **说明**：从API version 22开始，支持该参数。 |
| [-e --print record\_id](hidumper.md#获取异常退出故障日志) | 获取指定异常退出记录id的故障日志。输出日志的规格可参考：[CppCrash](cppcrash-guidelines.md#日志规格)、[JSCrash](jscrash-guidelines.md#日志规格)、[AppFreeze](appfreeze-guidelines.md#日志规格)。  **说明**：从API version 22开始，支持该参数。 |
| [--net [pid]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询网络信息) | 获取网络信息，包含网络流量、网络接口统计、IP信息等。如果指定了进程的pid，则只输出该进程的网络流量使用信息。 |
| [--storage [pid]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询存储信息) | 获取存储信息，包含磁盘统计、磁盘使用量、文件句柄等信息。如果指定了进程的pid，则只显示该进程的io信息。 |
| [-p [pid]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询进程信息) | 获取进程信息，包括进程和线程的列表和信息。 |
| [--cpuusage [pid]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询进程cpu使用率) | 获取CPU使用率，取值范围(0, CPU核数]，按进程和类别分类；如果指定pid，则获取指定pid的CPU使用率。 |
| [--cpufreq](hidumper.md#查询cpu频率) | 获取CPU每个核的真实频率，单位：kHz。 |
| [--mem [--prune]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询整机内存) | 获取总内存使用情况。如果指定--prune，只导出精简的内存使用情况。  **说明**：从API version 20开始，支持--prune参数。 |
| [--mem pid [--show-ashmem] [--show-dmabuf]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询进程内存) | 获取指定pid的进程内存使用情况。  指定--show-ashmem，则补充打印该进程的ashmem使用详细信息。  指定--show-dmabuf，则补充打印DMA内存使用详情信息。  **说明**：  从API version 20开始，支持--show-ashmem、应用进程的--show-dmabuf参数。  从API version 23开始，支持系统服务进程的--show-dmabuf参数。 |
| [--zip](hidumper.md#导出信息压缩存储) | 保存命令输出到 /data/log/hidumper 下的压缩文件，压缩格式为 ZIP。 |
| [--ipc [pid]/-a --start-stat/stat/--stop-stat](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#获取进程间通信信息) | 统计一段时间进程IPC信息。如果使用-a，则统计所有进程IPC数据。使用--start-stat开始统计，使用--stat获取统计数据，使用--stop-stat结束统计。 |
| [--mem-smaps pid [-v]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询进程内存) | 获取pid内存统计信息，数据来源于/proc/pid/smaps，使用-v指定更多详细信息。（仅支持导出[debug版本应用](performance-analysis-kit-terminology.md#debug版本应用)）  **说明**：从API version 20开始，支持该参数。 |
| [--mem-jsheap pid [-T tid] [--gc] [--leakobj] [--raw]](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询虚拟机堆内存) | 必选参数pid。触发ArkTS应用JS线程的gc和堆内存快照导出。指定线程tid时，仅触发该线程的gc和堆内存快照导出；指定--gc时，仅触发gc，不导出快照；指定--leakobj时，应用开启泄露检测可获取泄露对象列表。  文件命名格式为：hidumper-jsheap-进程号-JS线程号-时间戳，文件内容为JSON结构的JS堆快照。  指定--raw时，堆快照以rawheap格式导出。  **说明**：从API version 19开始，支持--raw参数。 |

## 查询内存信息

HiDumper内存信息查询模块主要用于查看系统整机内存使用情况和单个进程内存使用情况。开发者需要了解相关的[内存基础知识](../best-practices/bpta-memory-basic-knowledge.md)。

### 查询整机内存

可使用hidumper --mem命令获取整机内存使用情况。

打印效果为：

```
1. $ hidumper --mem
2. -------------------------------[memory]-------------------------------
3. Total Memory Usage by PID:
4. PID       Total Pss(xxx in SwapPss)   Total Vss   Total Rss   Total Uss          GL       Graph         Dma     PurgSum     PurgPin    Name
5. 1          4309(2216 in SwapPss) kB  2158196 kB     4180 kB     1760 kB        0 kB        0 kB        0 kB        0 kB        0 kB    init
6. 2            45613(0 in SwapPss) kB 17452952 kB    48352 kB    44088 kB        0 kB        0 kB        0 kB        0 kB        0 kB    sysmgr-main
7. ...
8. Total Memory Usage by Size:
9. PID        Total Pss(xxx in SwapPss)    Total Vss    Total Rss    Total Uss           GL        Graph          Dma      PurgSum      PurgPin     Name
10. 3031         421826(0 in SwapPss) kB   5199308 kB    610812 kB    395712 kB         0 kB     17000 kB     17000 kB         0 kB         0 kB     xxx
11. 1473         409349(0 in SwapPss) kB   7014040 kB    449460 kB    389528 kB    160336 kB     57092 kB     57092 kB         0 kB         0 kB     xxx
12. ...
13. Total Pss by OOM adjustment:
14. System: 1426777 kB
15. xxx(pid=1473):  409349 kB
16. xxx(pid=992):     80734 kB (23720 kB in SwapPss)
17. ...
18. Total Pss by Category:
19. File-backed Page(1414160 kB):
20. 1053457 kB : .so
21. 322813 kB : other
22. 25616 kB : .hap
23. 8064 kB : .ttf
24. 3696 kB : .db
25. 514 kB : dev
26. Anonymous Page(2280332 kB):
27. 1348463 kB : native heap
28. 518107 kB : ark ts heap
29. 361195 kB : other
30. 49287 kB : stack
31. 3280 kB : dev
32. 0 kB : guard
33. GPU(160340 kB):
34. 160340 kB : GL
35. Graph(350708 kB):
36. 350708 kB : Graph
37. DMA(350708 kB):
38. 350708 kB : Dma

40. Total RAM:15803612 kB
41. Free RAM:10287099 kB (3999535 cached + 6287564 free)
42. Used RAM:3961668 kB (3163324 total pss + 798344 kernel)
43. Lost RAM:2086013 kB

45. Total RAM by Category:
46. hidumper - Hardware Usage:1860480 kB
47. CMA Usage:0 kB
48. -   Kernel Usage:656937 kB
49. Processes Usage:3694492 kB

51. Total Purgeable:
52. Total PurgSum:0 kB
53. Total PurgPin:0 kB
```

VSS (Virtual Set Size)表示当前进程虚拟内存的大小，包括所有映射到该进程地址空间的内存区域。

RSS (Resident Set Size)表示当前进程实际驻留在物理内存中的内存大小。

PSS (Proportional Set Size)是一种更精确的内存使用度量方法，它将共享库所占的内存按比例分配给每个使用该库的进程。

PurgSum（Purgeable Summary）表示当前进程可回收内存的总量。

PurgPin（Purgeable Pinned）表示可回收但暂时无法立即回收的内存。

GL代表GPU内存，包含应用使用的GPU内存和统一渲染在服务进程内产生的GPU内存。

Graph代表图形内存，即DMA内存。

可使用hidumper --mem --prune命令获取整机内存精简的使用情况。

打印效果为：

```
1. $ hidumper --mem --prune
2. -------------------------------[memory]-------------------------------
3. Total Memory Usage by PID:
4. PID        Total Pss(xxx in SwapPss)           GL     AdjLabel     Name
5. 1           4061(1668 in SwapPss) kB         0 kB        -1000     xxx
6. 2            101723(0 in SwapPss) kB         0 kB        -1000     xxx
7. ...
```

AdjLabel代表该进程内存的回收优先级，取值范围为[-1000, 1000]，该值越大则表示该进程越不重要，内存会被优先回收。

### 查询进程内存

可使用hidumper --mem pid命令获取指定进程的内存使用情况，pid为指定的进程号。

使用样例：

```
1. $ hidumper --mem 27336

3. -------------------------------[memory]-------------------------------

5. Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
6. Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
7. ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
8. ------------------------------------------------------------------------------------------------------------------------------------------------------
9. GL              0              0              0              0              0              0              0              0              0              0
10. Graph              0              0              0              0              0              0              0              0              0              0
11. ark ts heap          12676           5516              0          12468              0           3068           3068              0              0              0
12. guard              0              0              0              0              0              0              0              0              0              0
13. native heap          15427          27132              0          14424              0          18776          18776          55796          53564           2809
14. .hap              4              0              0              4              0              0              0              0              0              0
15. AnonPage other           1109           4932              0            968              0           4280           4280              0              0              0
16. stack           1404              0              0           1404              0             28             28              0              0              0
17. .db             32              0              0             32              0              0              0              0              0              0
18. .so          12877          58928          18868           5628           2028           1036           1036              0              0              0
19. dev             52              0            284             52              0              0              0              0              0              0
20. .ttf            296           1264              0              0              0              0              0              0              0              0
21. FilePage other          21933           1432           4300          21524            148              0              0              0              0              0
22. --------------------------------------------------------------------------------------------------------------------------------------------------------------------
23. Total          92998          99204          23452          56504           2176          27188          27188          55796          53564           2809

25. native heap:
26. jemalloc meta:          1010            276              0           1000              0            156            156              0              0              0
27. jemalloc heap:         13126          22412              0          12260              0          17876          17876              0              0              0
28. brk heap:          1259           4444              0           1132              0            744            744              0              0              0
29. musl heap:            32              0              0             32              0              0              0              0              0              0

31. Purgeable:
32. PurgSum:0 kB
33. PurgPin:0 kB

35. DMA:
36. Dma:0 kB

38. Ashmem:
39. Total Ashmem:144 kB
```

可使用hidumper --mem pid --show-ashmem获取指定pid的内存使用情况，同时打印ashmem使用详细信息。

使用样例：

```
1. $ hidumper --mem 27336 --show-ashmem
2. -------------------------------[memory]-------------------------------

4. Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
5. Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
6. ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
7. ------------------------------------------------------------------------------------------------------------------------------------------------------
8. GL              0              0              0              0              0              0              0              0              0              0
9. Graph              0              0              0              0              0              0              0              0              0              0
10. ark ts heap          12657           5516              0          12468              0           3068           3068              0              0              0
11. guard              0              0              0              0              0              0              0              0              0              0
12. native heap          15191          27132              0          14252              0          18780          18780          55792          53527           2629
13. .hap              4              0              0              4              0              0              0              0              0              0
14. AnonPage other           1094           4932              0            964              0           4280           4280              0              0              0
15. stack           1388              0              0           1388              0             28             28              0              0              0
16. .db             32              0              0             32              0              0              0              0              0              0
17. .so          12557          59184          18868           5372           2028           1036           1036              0              0              0
18. dev             52              0            284             52              0              0              0              0              0              0
19. .ttf            296           1264              0              0              0              0              0              0              0              0
20. FilePage other          21916           1432           4300          21524            148              0              0              0              0              0
21. --------------------------------------------------------------------------------------------------------------------------------------------------------------------
22. Total          92379          99460          23452          56056           2176          27192          27192          55792          53527           2629

24. native heap:
25. jemalloc meta:          1008            276              0           1000              0            156            156              0              0              0
26. jemalloc heap:         12892          22412              0          12088              0          17880          17880              0              0              0
27. brk heap:          1259           4444              0           1132              0            744            744              0              0              0
28. musl heap:            32              0              0             32              0              0              0              0              0              0

30. Purgeable:
31. PurgSum:0 kB
32. PurgPin:0 kB

34. DMA:
35. Dma:0 kB

37. Ashmem:
38. Total Ashmem:144 kB
39. Process_name    Process_ID      Fd      Cnode_idx       Applicant_Pid   Ashmem_name     Virtual_size    Physical_size   magic    -> 详细ashmem信息
40. wei.xxx.xxx  27336   72      328415  27336   dev/ashmem/Paf.Permission.appImg        147456  147456  14105
```

使用hidumper --mem pid --show-dmabuf命令可获取指定PID的内存使用情况，并打印DMA内存详细信息。

使用样例：

```
1. $ hidumper --mem 27336 --show-dmabuf
2. -------------------------------[memory]-------------------------------

4. Pss         Shared         Shared        Private        Private           Swap        SwapPss           Heap           Heap           Heap
5. Total          Clean          Dirty          Clean          Dirty          Total          Total           Size          Alloc           Free
6. ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )         ( kB )
7. ------------------------------------------------------------------------------------------------------------------------------------------------------
8. GL              0              0              0              0              0              0              0              0              0              0
9. Graph              0              0              0              0              0              0              0              0              0              0
10. ark ts heap          12657           5516              0          12468              0           3068           3068              0              0              0
11. guard              0              0              0              0              0              0              0              0              0              0
12. native heap          15191          27132              0          14252              0          18780          18780          55792          53527           2629
13. .hap              4              0              0              4              0              0              0              0              0              0
14. AnonPage other           1094           4932              0            964              0           4280           4280              0              0              0
15. stack           1388              0              0           1388              0             28             28              0              0              0
16. .db             32              0              0             32              0              0              0              0              0              0
17. .so          12557          59184          18868           5372           2028           1036           1036              0              0              0
18. dev             52              0            284             52              0              0              0              0              0              0
19. .ttf            296           1264              0              0              0              0              0              0              0              0
20. FilePage other          21916           1432           4300          21524            148              0              0              0              0              0
21. --------------------------------------------------------------------------------------------------------------------------------------------------------------------
22. Total          92379          99460          23452          56056           2176          27192          27192          55792          53527           2629

24. native heap:
25. jemalloc meta:          1008            276              0           1000              0            156            156              0              0              0
26. jemalloc heap:         12892          22412              0          12088              0          17880          17880              0              0              0
27. brk heap:          1259           4444              0           1132              0            744            744              0              0              0
28. musl heap:            32              0              0             32              0              0              0              0              0              0

30. Purgeable:
31. PurgSum:0 kB
32. PurgPin:0 kB

34. DMA:
35. Dma:0 kB
36. Process               pid         fd        size_bytes        ino       exp_pid       exp_task_comm     buf_name      exp_name      buf_type      leak_type
37. m.xxx.xxx             7612        87        40960             2750      1424          allocatxxxx       RSxxxxxx      xxxxx          xx            xxxx

39. Ashmem:
40. Total Ashmem:144 kB
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

可使用hidumper --mem-smaps pid命令获取指定进程的详细内存使用情况，该命令会累加相同内存段的内存值。

使用样例：

```
1. $ hidumper --mem-smaps 3456  # 3456 为目标可调试应用进程号

3. -------------------------------[memory]-------------------------------

5. Shared      Shared      Private     Private
6. Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
7. 16          0           0           0           0           0           0           4           4           3           FilePage other                   [anon]
8. 8           8           8           0           0           8           0           0           0           1           FilePage other                   /bin/init
9. 2048        52          0           0           52          0           0           0           0           1           dev                              /dev/__parameters__/param_sec_dac
10. 80          28          1           0           28          0           0           0           0           1           dev                              /dev/__parameters__/param_selinux
11. ...
```

统计信息说明：

| 字段 | 说明 |
| --- | --- |
| Counts | 相同内存段出现的次数。 |
| Category | 内存所属类别。 |

可使用hidumper --mem-smaps pid -v命令获取指定进程的详细内存使用情况，该命令会直接打印进程的所有内存信息，不会对相同内存信息做二次处理。

使用样例：

```
1. $ hidumper --mem-smaps 3456 -v   # 3456 为目标可调试应用进程号

3. -------------------------------[memory]-------------------------------
4. Shared      Shared      Private     Private
5. Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Category                   Name
6. 4           4           2           0           4           0           0           0           0           FilePage other             [anon]
7. 4           4           2           0           4           0           0           0           0           FilePage other             /bin/init
8. ...
```

**注意事项**

hidumper --mem-smaps [pid] [-v]命令调试的进程应为“使用调试证书签名的应用”，同[debug版本应用](performance-analysis-kit-terminology.md#debug版本应用)。

要确认命令指定的应用是否为可调试应用，可以执行以下命令进行查询：hdc shell "bm dump -n [应用包名] | grep appProvisionType"，预期返回信息为"appProvisionType": "debug"。

以包名com.example.myapplication为例，可执行如下命令查询：

```
1. hdc shell "bm dump -n com.example.myapplication | grep appProvisionType"
```

如包名对应的应用是可调试应用，预期返回信息：

```
1. "appProvisionType": "debug",
```

构建可调试应用需要使用调试证书进行签名，申请调试证书及签名可参考：[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)。

### 查询虚拟机堆内存

使用hidumper --mem-jsheap pid [-T tid] [--gc] [--leakobj] [--raw]命令可以查看ArkTS应用虚拟机堆内存。生成的堆内存文件存放于/data/log/reliability/resource\_leak/memory\_leak目录。

注意

hidumper --mem-jsheap pid [-T tid] [--gc] [--leakobj] [--raw]命令调试的进程应为“使用调试证书签名的应用”，同[debug版本应用](performance-analysis-kit-terminology.md#debug版本应用)。

确认命令指定的应用是否为可调试应用：参考上述hidumper --mem-smaps [pid] [-v]命令中的注意事项。

* 可使用hidumper --mem-jsheap pid命令获取指定进程所有JS线程的虚拟机堆内存，文件命名为：hidumper-jsheap-进程号-JS线程号-时间戳，如果有多个JS线程会生成多个文件。

  使用样例：

```
1. $ hidumper --mem-jsheap 64949  -> 64949 为目标应用进程号
2. $ ls | grep jsheap   -> 进入堆内存文件存放目录后执行
3. hidumper-jsheap-64949-64949-1751075546050
4. hidumper-jsheap-64949-64989-1751075546050
```

* 可使用hidumper --mem-jsheap pid -T tid命令获取指定进程指定JS线程的虚拟机堆内存，文件命名为：hidumper-jsheap-进程号-JS线程号-时间戳。

  使用样例：

```
1. $ hidumper --mem-jsheap 64949 -T 64949  -> 64949 为目标应用进程号
2. $ ls | grep jsheap  -> 进入堆内存文件存放目录后执行
3. hidumper-jsheap-64949-64949-1751075567710
```

* 可使用hidumper --mem-jsheap pid [-T tid] --raw获取指定进程或指定JS线程的虚拟机堆内存，生成的堆内存文件为rawheap格式，文件命名为hidumper-jsheap-进程号-JS线程号-时间戳.rawheap。rawheap的解析转换可参考使用：[rawheap-translator工具](rawheap-translator.md)。

  使用样例：

```
1. $ hidumper --mem-jsheap 64949 --raw  -> 64949 为目标应用进程号
2. $ ls | grep jsheap  -> 进入堆内存文件存放目录后执行
3. hidumper-jsheap-64949-64949-1751075546050.rawheap
4. hidumper-jsheap-64949-64989-1751075546050.rawheap
5. $ hidumper --mem-jsheap 64949 -T 64949 --raw  -> 64949 为目标应用进程号
6. $ ls | grep jsheap
7. hidumper-jsheap-64949-64949-1751075546055.rawheap
```

* 可使用hidumper --mem-jsheap pid --gc命令触发指定应用进程GC。该命令不会生成任何文件，执行成功不会有命令回显。

  使用样例：

  ```
  1. $ hidumper --mem-jsheap 64949 --gc  -> 64949 为目标应用进程号
  ```
* 可使用hidumper --mem-jsheap pid --leakobj获取指定进程的虚拟机堆内存和泄漏对象信息，文件命名为：hidumper-leaklist-进程号-时间戳。

  获取指定进程的虚拟机堆内存和泄露对象信息的前提是应用已通过[@ohos.hiviewdfx.jsLeakWatcher](../harmonyos-references/js-apis-jsleakwatcher.md)接口开启了泄漏检测功能。

  具体使用步骤为：

  1. 应用调用[jsLeakWatcher.enable](../harmonyos-references/js-apis-jsleakwatcher.md#jsleakwatcherenable)接口。
  2. 应用调用[jsLeakWatcher.watch](../harmonyos-references/js-apis-jsleakwatcher.md#jsleakwatcherwatch)接口。
  3. 执行hidumper --mem-jsheap [pid] --leakobj命令，导出虚拟机堆内存和泄漏对象信息。

  使用样例：

```
1. $ hidumper --mem-jsheap 64949 --leakobj
2. $ ls | grep leaklist
3. hidumper-leaklist-64949-1730873210483
```

上述生成的文件，可以通过hdc[文件传输](hdc.md#文件传输)命令从设备中获取。

## 查询CPU使用情况

使用hidumper工具查看CPU相关信息，可以了解到当前系统的CPU负载情况。

### 查询整机CPU使用率

可使用hidumper --cpuusage获取整机CPU使用率。

打印效果为：

```
1. $ hidumper --cpuusage

3. -------------------------------[cpuusage]-------------------------------

5. Load average: 12.1 / 12.2 / 12.1; the cpu load average in 1 min, 5 min and 15 min
6. CPU usage from 2024-11-06 11:59:33 to 2024-11-06 11:59:38
7. Total: 6.38%; User Space: 2.57%; Kernel Space: 3.81%; iowait: 0.02%; irq: 0.14%; idle: 93.46%
8. Details of Processes:
9. PID   Total Usage      User Space    Kernel Space    Page Fault Minor    Page Fault Major    Name
10. 105      109.01%           0.00%        109.01%             164                   0            tppmgr.elf
11. 2          0.89%           0.00%          0.89%               0                   0            sysmgr-main
12. ...
```

### 查询进程CPU使用率

可使用hidumper --cpuusage pid获取指定进程的CPU使用率。

打印效果为：

```
1. $ hidumper --cpuusage 1

3. -------------------------------[cpuusage]-------------------------------

5. Load average: 12.1 / 12.2 / 12.1; the cpu load average in 1 min, 5 min and 15 min
6. CPU usage from 2024-11-06 11:59:33 to 2024-11-06 11:59:35
7. Total: 3.80%; User Space: 1.45%; Kernel Space: 2.35%; iowait: 0.00%; irq: 0.14%; idle: 96.06%
8. Details of Processes:
9. PID   Total Usage      User Space    Kernel Space    Page Fault Minor    Page Fault Major    Name
10. 1          0.00%           0.00%          0.00%           38368                1394            init
```

### 查询CPU频率

可使用hidumper --cpufreq获取CPU频率信息。

打印效果为：

```
1. $ hidumper --cpufreq

3. -------------------------------[cpufreq]-------------------------------

6. cmd is: cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq

8. 1018000

10. cmd is: cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq

12. 1530000
13. ...
```

## 查询系统服务

### 查询系统服务列表

* 可使用hidumper -ls命令获取正在运行的系统服务列表。

打印效果为：

```
1. $ hidumper -ls
2. System ability list:
3. SystemAbilityManager             RenderService                    AbilityManagerService
4. DataObserverMgr                  AccountMgr                       AIEngine
5. BundleMgr                        FormMgr                          ApplicationManagerService
6. AccessibilityManagerService      UserIdmService                   UserAuthService
7. AuthExecutorMgrService           PinAuthService                   FaceAuthService
8. FingerprintAuthService           WifiDevice                       WifiHotspot
9. WifiP2p                          WifiScan                         1125
10. 1126                             BluetoothHost                    NetConnManager
11. NetPolicyManager                 NetStatsManager                  NetTetheringManager
12. ...
```

### 获取系统服务详细信息

* 可使用hidumper -s获取所有系统服务的详细信息。

打印效果为：

```
1. $ hidumper -s

3. -------------------------------[ability]-------------------------------

6. ----------------------------------SystemAbilityManager----------------------------------
7. The arguments are illegal and you can enter '-h' for help.

9. -------------------------------[ability]-------------------------------

12. ----------------------------------RenderService----------------------------------
13. ------Graphic2D--RenderService ------
14. Usage:
15. h                             |help text for the tool
16. ...
```

* 可使用hidumper -s [SA0] [SA1]获取指定的一个或多个系统服务的详细信息。其中系统能力名[SA0] [SA1]可通过上述hidumper -ls命令查询得到。

打印效果为：

```
1. $ hidumper -s WindowManagerService

3. -------------------------------[ability]-------------------------------

6. ----------------------------------WindowManagerService----------------------------------
7. Usage:
8. -h                             |help text for the tool
9. -a                             |dump all window information in the system
10. -w {window id} [ArkUI Option]  |dump specified window information
11. ------------------------------------[ArkUI Option]------------------------------------
12. ...
13. $ hidumper -s WindowManagerService RenderService

15. -------------------------------[ability]-------------------------------

18. ----------------------------------WindowManagerService----------------------------------
19. Usage:
20. -h                             |help text for the tool
21. -a                             |dump all window information in the system
22. -w {window id} [ArkUI Option]  |dump specified window information
23. ------------------------------------[ArkUI Option]------------------------------------

26. -------------------------------[ability]-------------------------------

29. ----------------------------------RenderService----------------------------------
30. ------Graphic2D--RenderService ------
31. Usage:
32. h                             |help text for the tool
33. screen                         |dump all screen information in the system
34. surface                        |dump all surface information
35. composer fps                   |dump the fps info of composer
36. ...
```

### 获取指定系统服务提供的能力

可使用hidumper -s [SA] -a ["option"]可以获取指定系统服务提供的能力。

以RenderService系统渲染服务为例，获取其使用帮助，打印效果如下：

```
1. $ hidumper -s RenderService -a "h"

3. -------------------------------[ability]-------------------------------

5. ----------------------------------RenderService----------------------------------
6. ------ Graphic2D--RenderService ------
7. Usage:
8. gles                          |inquire gpu info
9. h                             |help text for the tool
10. allInfo                       |dump all info
11. fpsCount                      |dump the refresh rate counts info
12. surfacenode                   |surfacenode [id]
13. trimMem                       |dump trim Mem info
14. surface                       |dump all surface information
15. MultiRSTrees                  |dump multi RS Trees info
16. fpsClear                      |[surface name]/composer fpsClear, clear the fps info
17. dumpMem                       |dump Cache
18. allSurfacesMem                |dump surface mem info
19. RSTree                        |dump RS Tree info
20. rsLogFlag                     |set rs log flag
21. nodeNotOnTree                 |dump nodeNotOnTree info
22. client                        |dump client ui node trees
23. clearFpsCount                 |clear the refresh rate counts info
24. hitchs                        |[windowname] hitchs, dump the hitchs info of window
25. vktextureLimit                |dump vk texture limit info
26. EventParamList                |dump EventParamList info
27. dumpNode                      |dump render node info
28. dumpExistPidMem               |dumpExistPidMem [pid], dump exist pid mem info
29. fps                           |[windowname] fps, dump the fps info of window
30. flushJankStatsRs              |flush rs jank stats hisysevent
31. screen                        |dump all screen information in the system
```

系统服务提供的具体功能，如获取GPU相关信息，可以使用以下命令，打印结果如下：

```
1. $ hidumper -s RenderService -a "gles"

3. -------------------------------[ability]-------------------------------

6. ----------------------------------RenderService----------------------------------

8. -- DumpGpuInfo:
9. GL_VENDOR: HUAWEI
10. GL_RENDERER: Maleoon 910
11. GL_VERSION: OpenGL ES 3.2 B283
12. GL_SHADING_LANGUAGE_VERSION: OpenGL ES GLSL ES 3.20
```

## 查询进程信息

可使用hidumper -p [pid]命令获取指定进程的相关信息，包括进程的挂载信息，进程的线程信息，线程的运行时间，进程等待通道信息。

注意

hidumper -p [pid]命令调试的进程应为“使用调试证书签名的应用”。

确认命令指定的应用是否为可调试应用：参考hidumper --mem-smaps [pid] [-v]命令中的介绍。

打印效果为：

```
1. $ hidumper -p 64949

3. -------------------------------[processes]-------------------------------

6. cmd is: ps -efT -p 64949

8. UID            PID   TID  PPID TCNT STIME TTY          TIME CMD
9. 20020169     64949 64949   629   17 11:40:14 ?     00:00:00 com.example.jsleakwatcher
10. 20020169     64949   733   629   17 11:40:28 ?     00:00:00 com.example.jsleakwatcher
11. ...
12. $ hidumper -p

14. -------------------------------[processes]-------------------------------

17. cmd is: ps -efT

19. UID            PID   TID  PPID TCNT STIME TTY          TIME CMD
20. root             1     1     0    1 10:46:59 ?     00:00:08 init --second-stage 2389791
21. root             2     2     0  127 10:46:59 ?     00:00:24 [sysmgr-main]
22. root             2     4     0  127 10:46:59 ?     00:00:00 [call_ebr]
23. ...
```

## 查询网络信息

可使用hidumper --net命令获取网络流量信息，网络接口统计信息、网口统计信息、IP信息、iptable信息和binder信息。该功能是通过netstat、ifconfig、iptables等系统命令获取网络信息。

打印效果为：

```
1. $ hidumper --net

3. -------------------------------[net traffic]-------------------------------

5. Received Bytes:0
6. Sent Bytes:51885

8. -------------------------------[net]-------------------------------

10. cmd is: netstat -nW  -> 通过netstat -nW命令查询网络连接、路由表、接口统计等网络相关信息。
11. ...
```

可使用hidumper --net [pid]命令获取指定进程的网络流量信息。

打印效果为：

```
1. $ hidumper --net 1

3. -------------------------------[net traffic]-------------------------------

5. Received Bytes:0
6. Sent Bytes:51885
```

## 查询存储信息

* 可使用hidumper --storage命令获取磁盘统计信息、磁盘使用量信息、文件句柄信息、IO流量统计信息和挂载信息。

打印效果为：

```
1. $ hidumper --storage

3. -------------------------------[storage]-------------------------------

6. cmd is: storaged -u -p
7. ...
```

* 可使用hidumper --storage [pid]命令获取指定进程的IO信息。

打印效果为：

```
1. $ hidumper --storage 1

3. -------------------------------[storage io]-------------------------------

6. /proc/1/io

8. rchar: 28848175
9. wchar: 4364169
10. syscr: 16886
11. syscw: 15866
12. read_bytes: 30617600
13. write_bytes: 10907648
14. cancelled_write_bytes: 734003
```

IO信息的相关字段解释如下：

* rchar：代表自进程启动以来所读取的总字符数，包括通过缓存或直接读取的字符。单位为Byte。
* wchar：代表自进程启动以来所写入的总字符数，包括通过缓存或直接写入的字符。单位为Byte。
* syscr：代表自进程启动以来所执行的 read 系统调用的次数。
* syscw：代表自进程启动以来所执行的 write 系统调用的次数。
* read\_bytes：代表自进程启动以来所读取的字节数，包括从文件系统、网络等设备读取的字节数。单位为Byte。
* write\_bytes：代表自进程启动以来所写入的字节数，包括写入到文件系统、网络等设备的字节数。单位为Byte。
* cancelled\_write\_bytes：代表自进程启动以来，因写入操作被取消而未写入的字节数。通常情况下，只有在向磁盘写入数据时发生错误或写入操作被中断时，该字段的值才会非零。单位为Byte。

## 查询系统信息

* 可使用hidumper -lc命令获取系统信息簇列表。

打印效果为：

```
1. $ hidumper -lc
2. System cluster list:
3. base                             system
```

* 可使用hidumper -c [系统信息簇名称]命令获取指定信息簇信息。

例如可使用hidumper -c base命令获取设备信息、内核版本、启动参数和启动时间。打印效果为：

```
1. -------------------------------[base]-------------------------------

3. BuildId: ALN-AL00 5.0.1.XXX(XXX)   -> 设备信息
4. ReleaseType: Beta1
5. OsVersion: phone/HUAWEI/HUAWEI/ALN/HarmonyOS-5.0.1.XXX(Beta1)/ALN-AL10/ALN-AL10/XX/5.0.1.XXX/default
6. DeviceType: phone
7. ...

9. /proc/version

11. Hongmeng version: HongMeng Kernel X.XX.XX  -> 内核版本

13. /proc/cmdline   -> 启动参数

15. ohos.boot.post_data_blks=0x0 ohos.boot.ptn_last_blk=0x772AFFF ...

17. cmd is: uptime -p

19. up 0 weeks, 0 days, 5 hours, 27 minutes   -> 启动时间
```

例如可使用hidumper -c system命令获取环境变量、内核模块信息、当前已加载的内核模块、slab信息、zone信息、vmstat、vmalloc信息、cpu频率信息和内存信息。打印效果为：

```
1. $ hidumper -c system

3. -------------------------------[system]-------------------------------

6. cmd is: printenv   -> 环境变量

8. _=/system/bin/printenv
9. LANG=en_US.UTF-8
10. HOME=/root
11. PULSE_STATE_PATH=/data/data/.pulse_dir/state
12. OLDPWD=/
13. PWD=/
14. TMP=/data/local/mtp_tmp/
15. PULSE_RUNTIME_PATH=/data/data/.pulse_dir/runtime
16. ...

18. /proc/modules   -> 内核模块信息

20. modem_driver 1490944 24 - Live 0x0000000000000000
21. hmtpp_freq_dal_kirin 20480 0 [permanent], Live 0x0000000000000000 (O)
22. kconsole 20480 0 [permanent], Live 0x0000000000000000 (O)
23. hmtpp_dal 40960 2 hmtpp_freq_dal_kirin, Live 0x0000000000000000 (O)
24. ...

26. cmd is: lsmod  -> 当前已加载的内核模块

28. Module                  Size  Used by
29. modem_driver         1490944  24
30. hmtpp_freq_dal_kirin    20480  0 [permanent]
31. kconsole               20480  0 [permanent]
32. hmtpp_dal              40960  2 hmtpp_freq_dal_kirin
33. ...

35. /proc/slabinfo   -> slab 信息

37. slabinfo - version: 2.0
38. #name       <active_objs> <num_objs> <objsize> <objperslab> <pagesperslab> : tunables <limit> <batchcount> <sharedfactor> : slabdata <active_slabs> <num_slabs> <num_pool> <sharedavail> <reclaimable>
39. slab-[16]                  48459  54432     16    252      1 : tunables 0 0 0 : slabdata    215    216      4 0 0
40. slab-[24]                  78315  83328     24    168      1 : tunables 0 0 0 : slabdata    496    496      4 0 0
41. slab-[32]                   5834   9954     32    126      1 : tunables 0 0 0 : slabdata     79     79      4 0 0
42. ...

44. /proc/zoneinfo   -> zone 信息

46. Node 0, zone      DMA
47. per-node stats
48. nr_inactive_anon 419922
49. nr_active_anon 11737
50. nr_inactive_file 381289
51. nr_active_file 456643
52. ...

54. /proc/vmstat   -> vmstat 信息

56. workingset_refault_anon    63071
57. workingset_refault_file        0
58. workingset_activate_anon     1742
59. workingset_activate_file        0
60. ...

62. /proc/vmallocinfo   -> vmalloc 信息

64. 0x0000000000000000-0x0000000000000000    4096 of_iomap+0xe4/0xec pages=1 phys=0xfb21b000 ioremap
65. 0x0000000000000000-0x0000000000000000    4096 of_iomap+0xe4/0xec pages=1 phys=0xffb85000 ioremap
66. 0x0000000000000000-0x0000000000000000    4152 gen_pool_add_owner+0x48/0xc0 pages=2 vmalloc
67. 0x0000000000000000-0x0000000000000000    4096 of_iomap+0xe4/0xec pages=1 phys=0xee262000 ioremap
68. ...

70. cmd is: cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq   -> CPU 频率信息

72. 1430000

74. cmd is: cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq

76. 1530000

78. cmd is: cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq

80. 1430000
81. ...

83. -------------------------------[memory]-------------------------------     -> 内存信息
84. Total Memory Usage by PID:
85. PID        Total Pss(xxx in SwapPss)    Total Vss    Total Rss    Total Uss           GL        Graph          Dma      PurgSum      PurgPin     Name
86. 1           4001(1672 in SwapPss) kB     59028 kB      5744 kB      1972 kB         0 kB         0 kB         0 kB         0 kB         0 kB     init
87. 2             50451(0 in SwapPss) kB 18014398163279052 kB     52088 kB     49448 kB         0 kB         0 kB         0 kB         0 kB         0 kB     sysmgr-main
88. 79             2741(0 in SwapPss) kB   2145468 kB      6052 kB      1292 kB         0 kB         0 kB         0 kB         0 kB         0 kB     crypto.elf
89. 80             8796(0 in SwapPss) kB   2156116 kB     12584 kB      6940 kB         0 kB         0 kB         0 kB         0 kB         0 kB     devmgr.elf
90. 85            96861(0 in SwapPss) kB  37180468 kB    100932 kB     94808 kB         0 kB         0 kB         0 kB         0 kB         0 kB     devhost.elf
91. 501            2256(0 in SwapPss) kB   2142484 kB      3892 kB      1620 kB         0 kB         0 kB         0 kB         0 kB         0 kB     hguard.elf
92. 586         1656(1412 in SwapPss) kB     32852 kB       744 kB       236 kB         0 kB         0 kB         0 kB         0 kB         0 kB     ueventd
93. ...
```

* 可使用hidumper -c命令获取全量信息簇信息。这包含上述base和system信息簇合集。

## 获取系统故障日志

可使用hidumper -e命令获取系统故障日志，打印对应故障日志的文件名及详细内容。

```
1. $ hidumper -e

3. -------------------------------[faultlog]-------------------------------

6. /data/log/faultlog/faultlogger/syswarning-com.ohos.sceneboard-20020022-20241106104006  -> 故障日志文件名

8. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
9. ...
```

## 获取异常退出记录列表

可使用hidumper -e --list命令获取异常退出记录列表。

```
1. $ hidumper -e --list
2. time                  foreground               reason              record_id              process_name
3. 2025-09-26 15:45:06   False                    ThreadBlock6S       05233453489239878113   xxx.xxx.sceneboard
4. 2025-09-26 15:45:03   False                    LowMemoryKill       23123453489239875544   xxx.xxx.sceneboard
5. 2025-09-26 14:43:06   False                    LowMemoryKill       45453453489233242345   xxx.xxx.sceneboard
6. 2025-09-26 12:42:05   True                     LowMemoryKill       45455345348923987811   xxx.xxx.sceneboard
7. 2025-09-26 10:45:45   False                    LowMemoryKill       78767783489239873255   xxx.xxx.sceneboard
8. 2025-09-26 10:40:06   False                    LowMemoryKill       78767783489239454666   xxx.xxx.systemui
9. ...
```

可使用hidumper -e --list process\_name命令可获取指定进程的异常退出记录列表。

```
1. $ hidumper -e --list sceneboard
2. time                  foreground               reason              record_id              process_name
3. 2025-09-26 15:45:06   False                    ThreadBlock6S       05233453489239878113   xxx.xxx.sceneboard
4. 2025-09-26 15:45:03   False                    LowMemoryKill       23123453489239875544   xxx.xxx.sceneboard
5. 2025-09-26 14:43:06   False                    LowMemoryKill       45453453489233242345   xxx.xxx.sceneboard
6. 2025-09-26 12:42:05   True                     LowMemoryKill       45455345348923987811   xxx.xxx.sceneboard
7. 2025-09-26 10:45:45   False                    LowMemoryKill       78767783489239873255   xxx.xxx.sceneboard
8. ...
```

可使用hidumper -e --list -n num命令获取异常退出记录列表，其中num参数用于指定要展示的记录条数。

```
1. $ hidumper -e --list -n 2
2. time                  foreground               reason              record_id              process_name
3. 2025-09-26 15:45:06   False                    ThreadBlock6S       05233453489239878113   xxx.xxx.sceneboard
4. 2025-09-26 15:45:03   False                    LowMemoryKill       23123453489239875544   xxx.xxx.sceneboard
```

可使用hidumper -e --list process\_name -n num --since timestamp --until timestamp命令获取指定进程指定时间内最新num条异常退出记录列表，其中num参数控制展示条数，timestamp参数控制时间范围。

说明

时间区间控制为前闭后开，且当起始时间和结束时间完全一致时，无法查到数据。

```
1. $ hidumper -e --list sceneboard -n 4 --since '2025-09-26 12:42:05' --until '2025-09-26 15:45:07'
2. time                  foreground               reason              record_id              process_name
3. 2025-09-26 15:45:06   False                    ThreadBlock6S       05233453489239878113   xxx.xxx.sceneboard
4. 2025-09-26 15:45:03   False                    LowMemoryKill       23123453489239875544   xxx.xxx.sceneboard
5. 2025-09-26 14:43:06   False                    LowMemoryKill       45453453489233242345   xxx.xxx.sceneboard
6. 2025-09-26 12:42:05   True                     LowMemoryKill       45455345348923987811   xxx.xxx.sceneboard
7. $ hidumper -e --list --since '2025-09-26 12:42:05' --until '2025-09-26 12:42:05'
8. no records found.
```

字段说明：

| 字段 | 说明 |
| --- | --- |
| time | 异常退出发生的时间。 |
| foreground | 异常退出发生时，进程是否在前台。True表示处于前台；False表示处于后台。 |
| reason | 异常退出原因，原因范围详见[reason字段说明](hidumper.md#reason字段说明)。 |
| record\_id | 异常退出记录ID。 |
| process\_name | 发生异常退出的进程名。 |

### reason字段说明

以下异常退出原因，可参考[应用终止分析思路和分析步骤](appkilled-guidelines.md#分析思路和分析步骤)进行问题排查处理。

| 类型 | 说明 |
| --- | --- |
| IllegalAudioRendererBySuspend | 应用未申请合理的后台任务，但是后台有大量音频播放。 |
| LowMemoryKill | 整机低内存。 |
| OomKiller | 整机内存耗尽，无法继续分配。 |
| PowerSaveClean | 整机切换到省电模式或应急模式。 |
| ResourceLeak(AshmemLeak) | 应用Ashmem内存占用超标。 |
| ResourceLeak(GpuLeak) | 应用GPU内存占用超标。 |
| ResourceLeak(GpuRsLeak) | 应用在Render Service进程内的GPU内存占用超标。 |
| ResourceLeak(IonLeak) | 应用的Ion内存占用超标。 |
| RssThresholdKiller | 应用的RSS（Resident Size Set）占用超标。 |
| SwapFull | 整机Swap空间耗尽。 |
| ThreadBlock6S | 应用主进程阻塞，该类型支持根据record\_id查看故障日志详情。 |
| AppInputBlock | 输入事件无响应，该类型支持根据record\_id查看故障日志详情。 |
| LifecycleTimeout | 生命周期超时，该类型支持根据record\_id查看故障日志详情。 |
| JsError | JS崩溃，该类型支持根据record\_id查看故障日志详情。 |
| CppCrash | Native崩溃，该类型支持根据record\_id查看故障日志详情。 |

## 获取异常退出故障日志

可使用 hidumper -e --print 命令获取系统故障日志，打印文件名和详细内容。

说明

异常退出记录最长保持30天，同一进程同类型的故障日志最多保留10条。查询的日志已被删除时，会给予提示。

```
1. $ hidumper -e --print

3. -------------------------------[faultlog]-------------------------------

5. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926154006  -> 故障日志文件名

7. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
8. ...   -> 故障日志详细内容，大量的文本内容，此处省略

10. -------------------------------[faultlog]-------------------------------

12. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926124106  -> 故障日志文件名

14. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
15. ...   -> 故障日志详细内容，大量的文本内容，此处省略

17. -------------------------------[faultlog]-------------------------------

19. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926114206  -> 故障日志文件名

21. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
22. ...   -> 故障日志详细内容，大量的文本内容，此处省略

24. -------------------------------[faultlog]-------------------------------

26. /data/log/faultlog/faultlogger/xxxx-com.xxx.systemui-20020022-20250926104506  -> 故障日志文件名

28. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
29. ...   -> 故障日志详细内容，大量的文本内容，此处省略

31. -------------------------------[faultlog]-------------------------------

33. /data/log/faultlog/faultlogger/xxxx-com.xxx.hidumper-20020022-20250926104206  -> 故障日志文件名

35. The faultlog has been deleted by the system due to expiration.  -> 日志过期被删除提示
```

可使用hidumper -e --print process\_name命令打印指定进程的系统故障日志文件名及详细内容。

```
1. $ hidumper -e --print systemui

3. -------------------------------[faultlog]-------------------------------

5. /data/log/faultlog/faultlogger/xxxx-com.xxx.systemui-20020022-20250926104506  -> 故障日志文件名

7. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
8. ...
```

可使用hidumper -e --print -n num命令打印系统故障日志的文件名及详细内容，并限制打印文件数量。

```
1. $ hidumper -e --print -n 2

3. -------------------------------[faultlog]-------------------------------

5. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926154006  -> 故障日志文件名

7. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
8. ...   -> 故障日志详细内容，大量的文本内容，此处省略

10. -------------------------------[faultlog]-------------------------------

12. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926124106  -> 故障日志文件名

14. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
15. ...   -> 故障日志详细内容，大量的文本内容，此处省略
```

可使用hidumper -e --print process\_name -n num --since timestamp --until timestamp命令获取系统故障日志，打印文件名和详细内容，同时限制指定进程的文件数量和时间范围。

```
1. $ hidumper -e --print sceneboard -n 2 --since '2025-09-26 12:40:05' --until '2025-09-26 15:45:07'

3. -------------------------------[faultlog]-------------------------------

5. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926154006  -> 故障日志文件名

7. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
8. ...   -> 故障日志详细内容，大量的文本内容，此处省略

10. -------------------------------[faultlog]-------------------------------

12. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926124106  -> 故障日志文件名

14. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
15. ...   -> 故障日志详细内容，大量的文本内容，此处省略
```

可使用hidumper -e --print record\_id命令获取指定异常退出记录id的系统故障日志，包括文件名及详细内容。若无匹配记录，则提示查询失败原因。

```
1. $ hidumper -e --print 05233453489239878113

3. -------------------------------[faultlog]-------------------------------

5. /data/log/faultlog/faultlogger/xxxx-com.xxx.sceneboard-20020022-20250926104006  -> 故障日志文件名

7. Generated by HiviewDFX@HarmonyOS  -> 故障日志详细内容
8. ...   -> 故障日志详细内容，大量的文本内容，此处省略

10. $ hidumper -e --print 23123453489239875544
11. this type of record does not have faultlog.  -> 查询失败原因
```

## 获取进程间通信信息

可使用hidumper --ipc -a --start-stat/stop-stat/stat命令获取整机采集时间区间内IPC信息。

打印效果为：

```
1. $ hidumper --ipc -a --start-stat
2. StartIpcStatistics pid:1473 success
3. StartIpcStatistics pid:775 success
4. StartIpcStatistics pid:1472 success
5. ...
6. $ hidumper --ipc -a --stat
7. GlobalStatisticsInfo
8. CurrentPid:1473
9. TotalCount:3
10. TotalTimeCost:3783
11. --------------------------------ProcessStatisticsInfo-------------------------------
12. CallingPid:625
13. CallingPidTotalCount:3
14. ...
15. $ hidumper --ipc -a --stop-stat
16. StopIpcStatistics pid:1473 success
17. StopIpcStatistics pid:775 success
18. StopIpcStatistics pid:1472 success
19. ...
```

可使用hidumper --ipc [pid] --start-stat/stop-stat/stat命令获取指定进程采集时间区间内的IPC信息。

打印效果为：

```
1. $ hidumper --ipc 1473 --start-stat
2. StartIpcStatistics pid:1473 success
3. $ hidumper --ipc 1473 --stat
4. GlobalStatisticsInfo
5. CurrentPid:1473
6. TotalCount:2
7. TotalTimeCost:2214
8. --------------------------------ProcessStatisticsInfo-------------------------------
9. CallingPid:625
10. CallingPidTotalCount:2
11. CallingPidTotalTimeCost:2214
12. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~InterfaceStatisticsInfo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
13. DescriptorCode:OHOS.ILocalAbilityManager_6
14. DescriptorCodeCount:2
15. DescriptorCodeTimeCost:
16. Total:2214 | Max:1444 | Min:770 | Avg:1107
17. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
18. ------------------------------------------------------------------------------------

20. $ hidumper --ipc 1473 --stop-stat
21. StopIpcStatistics pid:1473 success
```

## 导出信息压缩存储

hidumper提供有--zip命令支持将任意类型导出信息输出到 /data/log/hidumper 下的压缩文件，可以与其他命令组合使用，压缩格式为ZIP，文件命名为当前时间戳，如下打印效果所示。

```
1. $ hidumper --zip
2. 100%,[-],The result is:/data/log/hidumper/20250622-120444-166.zip
```

例如，对于 hidumper -e 命令获取系统故障日志，其输出的文本内容较多，可以考虑使用压缩存储，打印效果如下：

```
1. $ hidumper -e

3. -------------------------------[faultlog]-------------------------------

6. /data/log/faultlog/faultlogger/syswarning-com.ohos.sceneboard-20020022-20241106104006  -> 故障日志文件名

8. Generated by HiviewDFX@HarmonyOS
9. ...  -> 故障日志详细内容，大量的文本内容，此处省略
10. $ hidumper -e --zip
11. 100%,[-],The result is:/data/log/hidumper/20250623-092235-087.zip
```

## 常用ArkUI基础信息显示能力

ArkUI基于hidumper增强开发了获取组件树等信息的能力。

### 获取应用窗口信息

打印全量窗口信息，可以在全量信息中找出对应窗口的WinId，将该WinId作为参数传递给其他命令以获取相关信息。

```
1. hdc shell hidumper -s WindowManagerService -a '-a'
```

**使用样例：**

```
1. -------------------------------[ability]-------------------------------

4. ----------------------------------WindowManagerService---------------------------------
5. -------------------------------------ScreenGroup 1-------------------------------------
6. WindowName             DisplayId Pid     WinId Type Mode Flag ZOrd Orientation [ x    y    w    h    ]
7. ScreenLockWindow       0         1274    2     2110 1    0    4    0           [ 0    0    720  1280 ]
8. SystemUi_NavigationBar 0         1274    5     2112 102  1    3    0           [ 0    1208 720  72   ]
9. SystemUi_StatusBar     0         1274    4     2108 102  1    2    0           [ 0    0    720  72   ]
10. settings0              0         10733   11    1    1    1    1    0           [ 0    72   720  1136 ]
11. EntryView              0         1546    8     2001 1    0    0    8           [ 0    0    720  1280 ]
12. ---------------------------------------------------------------------------------------
13. SystemUi_VolumePanel   0         1274    3     2111 1    1    -1   0           [ 0    0    0    0    ]
14. SystemUi_DropdownPan   0         1274    6     2109 1    1    -1   0           [ 0    0    0    0    ]
15. SystemUi_BannerNotic   0         1274    7     2111 1    1    -1   0           [ 0    0    0    0    ]
16. RecentView             0         1546    9     2115 1    1    -1   0           [ 0    0    0    0    ]
17. imeWindow              0         1530    10    2105 1    1    -1   0           [ 0    0    0    0    ]
18. Focus window: 2
19. total window num: 10
```

常见windowName与内置应用窗口的对应关系：

| windowName | 内置应用窗口 |
| --- | --- |
| EntryView | 桌面 |
| RecentView | 最近任务 |
| SystemUi\_NavigationBar | 三键导航 |
| SystemUi\_StatusBar | 状态栏 |
| ScreenLockWindow | 锁屏 |

### 获取期望应用组件树

如果需要查看应用中所有组件的信息，可以通过下列命令实现。

```
1. hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -element'"
```

windowId是期望应用的窗口ID。

**使用样例：**

```
1. hdc shell "hidumper -s WindowManagerService -a '-w 5 -element'"

3. -------------------------------[ability]-------------------------------
4. ----------------------------------WindowManagerService---------------------------------
5. WindowName: SystemUi_NavigationBar
6. DisplayId: 0
7. WinId: 5
8. Pid: 1274
9. Type: 2112
10. Mode: 102
11. Flag: 1
12. Orientation: 0
13. IsStartingWindow: false
14. FirstFrameCallbackCalled: 0
15. IsVisible: false
16. WindowRect: [ 0, 1208, 720, 72 ]
17. TouchHotAreas: [ 0, 1208, 720, 72 ]
18. |-> RootElement childSize:1
19. | ID: 0
20. | elmtId: -1
21. | retakeID: 16
22. | Active: Y
23. |-> StackElement childSize:2
24. | ID: 1
25. | elmtId: -1
26. | retakeID: 14
27. | Active: Y
28. |-> StageElement childSize:1
29. | ID: 2
30. | elmtId: -1
31. | retakeID: 13
32. | Active: Y
33. |-> PageElement childSize:1
34. | ID: 3
35. | elmtId: -1
36. | retakeID: 569
37. | Active: Y
38. ......
```

### 获取应用中指定Node的组件信息

如果只需要查看组件中某一节点的组件信息，可以通过下列命令实现。

```
1. hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -element -lastpage %nodeID%'"
```

windowId是应用的窗口ID，nodeID是指定Node的ID。可以通过获取期望应用组件树的操作获取nodeID。

**使用样例：**

```
1. hdc shell "hidumper -s WindowManagerService -a '-w 5 -element -lastpage 3'"

3. -------------------------------[ability]-------------------------------
4. ----------------------------------WindowManagerService---------------------------------
5. WindowName: SystemUi_NavigationBar
6. DisplayId: 0
7. WinId: 5
8. Pid: 1274
9. Type: 2112
10. Mode: 102
11. Flag: 1
12. Orientation: 0
13. IsStartingWindow: false
14. FirstFrameCallbackCalled: 0
15. IsVisible: false
16. WindowRect: [ 0, 1208, 720, 72 ]
17. TouchHotAreas: [ 0, 1208, 720, 72 ]
18. |-> PageElement childSize:1
19. | ID: 3
20. | elmtId: -1
21. | retakeID: 569
22. | Active: Y
23. ......
```

### 获取期望应用的Inspector树

上述示例中的element/render树主要包含多项内部实现，与应用代码中的组件无法一一对应。可以通过打印Inspector树来获取与应用中组件对应的树结构及组件基本信息。Inspector树与DevEco Testing及DevEco中的ArkUI Inspector完全匹配。

使用此功能需要先打开ArkUI debug调试开关。

```
1. hdc shell param set persist.ace.testmode.enabled 1
```

set: 设置命令；persist.ace.testmode.enabled：ArkUI debug调试开关名称；1：开关设置为true，打开调试功能。

命令如下：

```
1. hdc shell "hidumper -s WindowManagerService -a '-w %windowId% -inspector'"
```

**使用样例：**

```
1. hdc shell "hidumper -s WindowManagerService -a '-w 5 -inspector'"

3. |-> rootstacktag childSize:1
4. | ID: 2100001
5. | compid:
6. | text:
7. | top: 72.000000
8. | left: 0.000000
9. | width: 0.000000
10. | height: 0.000000
11. | visible: 1
12. | clickable: 0
13. | checkable: 0
14. |-> Column childSize:1
15. | ID: 128
16. | compid:
17. | text:
18. | top: 72.000000
19. | left: 0.000000
20. | width: 720.000000
21. | height: 1136.000000
22. | visible: 1
23. | clickable: 0
24. | checkable: 0
25. |-> GridContainer childSize:1
26. | ID: 129
27. | compid:
28. | text:
29. | top: 72.000000
30. | left: 0.000000
31. | width: 720.000000
32. | height: 1136.000000
33. | visible: 1
34. | clickable: 0
35. | checkable: 0
36. |-> Column childSize:2
37. | ID: 130
38. | compid:
39. | text:
40. | top: 72.000000
41. | left: 0.000000
42. | width: 720.000000
43. | height: 180.000000
44. | visible: 1
45. | clickable: 0
46. | checkable: 0

48. ......
```

### 获取期望应用路由栈信息

该命令将输出应用页面路由栈的信息，依据栈的创建顺序及其父子关系排列。

说明

仅支持通过[Navigation](arkts-navigation-architecture.md)组件实现页面路由的应用。

命令：

```
1. hidumper -s WindowManagerService -a '-w %windowId% -navigation -c'
```

**使用样例：**

```
1. hidumper -s WindowManagerService -a '-w 15 -navigation -c'

3. -------------------------------[ability]-------------------------------

6. ----------------------------------WindowManagerService--------------------------------
7. WindowName: myapplication0
8. DisplayId: 0
9. WinId: 12
10. Pid: 5908
11. Type: 1
12. Mode: 1
13. Flag: 0
14. Orientation: 0
15. IsStartingWindow: false
16. FirstFrameCallbackCalled: 1
17. VisibilityState: 0
18. Focusable: true
19. DecoStatus: true
20. IsPrivacyMode: false
21. isSnapshotSkip: 0
22. WindowRect: [ 0, 0, 720, 1280 ]
23. TouchHotAreas: [ 0, 0, 720, 1280 ]
24. bundleName:com.example.myapplication
25. moduleName:entry
26. LastRequestVsyncTime: 2351504075334
27. transactionFlags: [ 5908, 0 ]
28. last vsyncId: 527
29. Navigation number: 4
30. |-> Navigation ID: 7, Depth: 7, Mode: "SPLIT", NavDestinations:
31. | [0]{ ID: 0, Name: "pageOne", Mode: "STANDARD", IsOnShow: "FALSE" }
32. | [1]{ ID: 1, Name: "pageTwo", Mode: "STANDARD", IsOnShow: "TRUE" }
33. |-> Navigation ID: 19, Depth: 7, Mode: "AUTO (STACK)", NavDestinations:
34. |-> Navigation ID: 28, Depth: 11, Mode: "STACK", NavDestinations:
35. | [0]{ ID: 2, Name: "pageOne", Mode: "STANDARD", IsOnShow: "FALSE" }
36. | [1]{ ID: 3, Name: "pageTwo", Mode: "DIALOG", IsOnShow: "FALSE" }
37. |-> Navigation ID: 123, Depth: 11, Mode: "AUTO (SPLIT)", NavDestinations:
38. | [0]{ ID: 4, Name: "pageFive", Mode: "STANDARD", IsOnShow: "FALSE" }
39. | [1]{ ID: 5, Name: "pageSix", Mode: "STANDARD", IsOnShow: "FALSE" }
40. | [2]{ ID: 6, Name: "pageThree", Mode: "STANDARD", IsOnShow: "TRUE" }
```

说明

同一级别的节点，显示在最下方的节点为栈顶节点。

## 常见问题

### hidumper 查询到的内存使用情况与Hidebug接口获取到的内存使用情况之间的关系

**现象描述**

hidumper --mem 系列命令与[HiDebug](../harmonyos-references/js-apis-hidebug.md)接口获取到的内存信息存在差异。

**可能原因&解决方法**

hidumper --mem命令与HiDebug接口内存获取功能详细对比参考下表。

**表1**

| 命令或接口 | 使用场景 | 数据来源 | 是否导出图形内存 |
| --- | --- | --- | --- |
| hidumper --mem | 命令行获取**所有进程**的内存使用情况 | 系统节点：/proc/pid/smaps\_rollup | 是 |
| hidumper --mem [pid] | 命令行获取**单个进程**的内存使用情况 | 系统节点：/proc/pid/smaps | 是 |
| hidumper --mem-smaps [pid] | 命令行获取**单个进程**的详细内存使用情况 | 系统节点：/proc/pid/smaps\_rollup | 否 |
| [hidebug.getAppNativeMemInfo](../harmonyos-references/js-apis-hidebug.md#hidebuggetappnativememinfo12) | 获取**应用自身**的内存使用情况 | 系统节点：/proc/pid/smaps\_rollup | 否 |

若想通过Hidebug获取图形内存，请参考[HiDebug能力概述](hidebug-guidelines.md)中的相关说明。

### hidumper获取进程虚拟机内存和泄露对象信息为空

**现象描述**

通过hidumper --mem-jsheap [pid] --leakobj命令获取指定进程的虚拟机堆内存和泄露对象信息，该命令没有正常生成文件。

**可能原因&解决方法**

hidumper --mem-jsheap [pid] --leakobj 命令依赖[JsLeakWatcher](../harmonyos-references/js-apis-jsleakwatcher.md)。应用需通过JsLeakWatcher接口开启泄漏检测功能。具体步骤参考：[查询虚拟机堆内存](hidumper.md#查询虚拟机堆内存)。
