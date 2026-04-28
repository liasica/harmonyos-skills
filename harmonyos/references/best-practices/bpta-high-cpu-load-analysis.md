---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis
title: CPU 高负载分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > CPU 高负载分析
category: best-practices
scraped_at: 2026-04-28T08:22:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:ca058c7f2d7b899f2d7c3237d593760c9cf314965cfd1efec513596cf3e45e99
---

## 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1. 点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2. 观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/exW-ZB9PT_-fPDJzZuy2GQ/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=425DC55B84D5AE6B30B731A3C38284F2F5084A8139FA8570A3BA4F616329FFD1 "点击放大")

   说明

   CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
3. 点击More中的箭头，可直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/LSKYF1uXQ1eQeXZHz3M-Rg/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=5272B6AF63D3A45CEA5A06477881C5495D235C17B60E0FC61D7CEE4FD22192FB "点击放大")

## 分析思路

CPU高负载问题通常涉及以下三种情况：

1. GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2. UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3. 应用侧其他线程负载高。需要借助Callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/y0Oa7Z6nRu2LeI-_xJ67BQ/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=BCC6FF9A05771EB1AFF7376C1D288737386827341473420466A2D940C81870D5)

## 分析步骤

### 案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/g-Gf5xAzTpmUYSop7Dmunw/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=29A11462C3EEB9426E56D4FE0769F9EA7636899E71193B42DD86929A1CBB7D06 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。

   Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/pNamSyJsRuqiwMaL2TQYWg/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=0299AFD2F81CB5C1550B1ABDB2D4E2D2C154E08636031071109A5F73C8DB05BE "点击放大")

   当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/2Vt7GzNUQ1uWMbIIbHgzLQ/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=0A74A7BF276430207AB8EDFAD9AEAE08BE3BF18104E0847B5EC3E0145B86A5CC "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](bpta-click-to-complete-delay-analysis.md)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

### 案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KGClUwgiQmmgw1psesKjbw/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=C151DA8F053B86D87AE8BCCCD83023402D73C75551518DDCF3957AD2964ACE38 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3Cl_TmUoTpWyq9E4Rw6zJQ/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=EB0632EBD131EAF5099A478AD2BFE78261592BEE20CD25F3DDE22036E2E4ED17 "点击放大")

   当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vY3dLvMLSPKzQf06BRD6xA/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=7F00E98B90AAED2D410378DE957AB6C5A5A056299A6444932DE3FCFB96E46BC4 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/QhU5D5PhSQGShmfiWjL8yQ/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=F204B744BD7A02204E4A92C5DEDC9D1BD458C6184BEDEF4789898EDB01681DA4 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)和[Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)。

### 案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fry0Z5wcS66nMUJ7j5d_Ag/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=B9334B6AD2B9EE19C5B37E09E7131A65667B6D824BC3115EE87412CEF5CB714B "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/sAjYBSzVSLKBABNyGUY57w/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=35AF0926AA499A094634579FD7C4686FD77BCC46D1A6AE8824A675C42A4FB0B8 "点击放大")

   选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/e8X8eRrHQuGn-wd7QCWBsA/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=26418E4670255DBE9EE998483471C17D7E4C8E200BDCB18B568140D9D9E544DF "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。

   找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/AXRjgUT5TW-SwJf9lXowSA/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=7EB8CA91093C6C44E357E019E50430B030CBBA43580C7E4E37F69C2E9F0E6788 "点击放大")

   查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](../harmonyos-guides/ide-arkui-inspector.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/yzGFy8cySxOk8Gb3l-_NkQ/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20260428T002237Z&HW-CC-Expire=86400&HW-CC-Sign=55E851FB3F18E26AE823CBCB2F8FA9783AA9455A46EC082DC2E33F88123E1D4E "点击放大")
