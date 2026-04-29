---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis
title: CPU 高负载分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > CPU 高负载分析
category: best-practices
scraped_at: 2026-04-29T14:13:47+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:bd0673cfb74528efd6c2f2bb7efe70a82506e4631f4e7c18a95f7ec59b225ef5
---

## 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1. 点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2. 观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/exW-ZB9PT_-fPDJzZuy2GQ/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=E8701CF3B44B4F0DC2BD678EA888541152508E56B8E96AE6F23BDC068676A8A8 "点击放大")

   说明

   CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
3. 点击More中的箭头，可直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/LSKYF1uXQ1eQeXZHz3M-Rg/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=9BC78AE7818D2433181B47D3F48F587AFDEBBCB85729572B8156FBA15D03C47E "点击放大")

## 分析思路

CPU高负载问题通常涉及以下三种情况：

1. GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2. UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3. 应用侧其他线程负载高。需要借助Callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/y0Oa7Z6nRu2LeI-_xJ67BQ/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=ED7A183B8BC4867E3CE5C781D2968E346797123FC845B4FD0FC7BDB0F272325D)

## 分析步骤

### 案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/g-Gf5xAzTpmUYSop7Dmunw/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=622220E6B4702201683A64E699A3F0D72B1DA3B2515DDC83B50FED5F2851A15A "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。

   Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/pNamSyJsRuqiwMaL2TQYWg/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=9FB840F92C39CDBCC9CE9B0190BE8792ADFDE0EFEE9616EB672ABF4A267164B9 "点击放大")

   当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/2Vt7GzNUQ1uWMbIIbHgzLQ/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=174C2CE99DAD8B49217C4C27B3996EF2FF14405F322065B2C278B8518A634E1A "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](bpta-click-to-complete-delay-analysis.md)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

### 案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KGClUwgiQmmgw1psesKjbw/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=747A7884B19F089F3CF42783A92685B3C80635EDC32E32274476141B699DA9FA "点击放大")

   查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3Cl_TmUoTpWyq9E4Rw6zJQ/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=39544F00112F06F542104A571EC20C6EC772F69C19B322A1E319AC3240C8097A "点击放大")

   当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vY3dLvMLSPKzQf06BRD6xA/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=02A321C6EE3BF10C45C3C53BE9CA7C8309D842D40869591601DFE4BFDB168869 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/QhU5D5PhSQGShmfiWjL8yQ/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=B52297A966E1FFBADDB5A8279D5CF3C7DD10A1C55549FD1495CEC276EC4CF3EC "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)和[Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)。

### 案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fry0Z5wcS66nMUJ7j5d_Ag/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=C845F1BD13CB3E9D80D45D551CDBD7F57F7E3E5A4C615CF340CB137E946C2AD4 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/sAjYBSzVSLKBABNyGUY57w/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=5A59D21A4D69A1EDD629AF0D23AA65A614A14DC2A2362B571D4FB6F6B4D6B9E9 "点击放大")

   选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/e8X8eRrHQuGn-wd7QCWBsA/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=D30B63E30E549DF1AFDACA294B08D795C1ED85D7B8FDC6789192A1A4F26836FE "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。

   找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/AXRjgUT5TW-SwJf9lXowSA/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=96E981A98ADE93DE75746BAA5F2051D9ACBD1A7F5F088BC3527BCB314521FE04 "点击放大")

   查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](../harmonyos-guides/ide-arkui-inspector.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/yzGFy8cySxOk8Gb3l-_NkQ/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20260429T061346Z&HW-CC-Expire=86400&HW-CC-Sign=CE005E90F7ADF52F569CABC336FA63C9E409B5D407A09D5D22A6139729D99B88 "点击放大")
