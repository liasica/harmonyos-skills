---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis
title: CPU高负载分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > CPU高负载分析
category: best-practices
scraped_at: 2026-11-14T08:54:15+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:d96c1ac4218b6c997d1df602628cd4fd4b7ac09579799b1c989316fc7eea1b2a
---

## 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1. 点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2. 观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/kQ5rXr2gTTi2IQGxUtvKpw/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD664460EB435BAA9318285156D851FCF6DD2BA71CFD35438DFCD97275F9B6D5 "点击放大")

   **说明** 

   CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
3. 点击下方中的三角形，可展开后直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Lm0IDPfRRGmosZ9BKz-CCw/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=6840C8A570CDE74CDDB50843F20F39E07CA1D8170CB19C2DE63AC9784CBF6894 "点击放大")

## 分析思路

CPU高负载问题通常涉及以下三种情况：

1. GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2. UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3. 应用侧其他线程负载高。需要借助callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/JPGMBC4XRcKkysfU7llagg/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=054154246AD3F37216280F5C783497AC2CF153E4CF20308A68D124D10D3FB709)

## 分析步骤

### 案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/_-BzUgQSQuSnSSf-Flv5cw/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9E10B90CF24479BBB7E3AA3B779A33B4D86F6E5306B7643D95BB84478E6C59B "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。

   Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/CGDznOEmQTa3vXMDkfOLcg/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAE1ACD09297871106C898BC013B6B2822810E27EDF6E751DFD92AAB8F146E74 "点击放大")

   当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/B7Bi-liMRmGviR9L9NWgCQ/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B5ADFF3F07B289A6C67F1AABE9A6D0DF46EF6597424EC59A84427E4F7F13AB4 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](bpta-click-to-complete-delay-analysis.md)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

### 案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/jRmHWHNsTz-cKRGeTZc2QA/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE136249EDDF2F133F71F215C0B37A1B5B3F737FF59F422BD936AFA73534505B "点击放大")

   查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/9G24rZXaSN65KTQNXjLn-g/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=7524D05A4B3A0C77DE641CA16A92B2569C2518FBDE7399E00CF21FFCD77708AA "点击放大")

   当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/5yT3_TIyQ-2L4_riqQmAoA/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=324CE7EA75002891EB9EBAD58BF64A7C49675358273A4A1E405A8A8984D79776 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/nWOvG7OkSQqsNSDZ5KB-jA/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=5509D79D1CDAC3A1913D9663A58E9A8C6159DED2F3F7462DB5161BD61570CF76 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)和[内存泄漏：Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)。

### 案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/abcDGctbRhykaBgJA4-NBQ/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D1D7E86476438EAE82647F0527A6DF0E9E869A819E62416CA3A0A82BC777A45 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Nin51aD7RuSYIAzVpNpNKQ/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DF704E22DBA7FD395365D6AEA4C0FE77408843BB591E39821D42E70D07CA90A "点击放大")

   选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/znnxHqT0TEywfT1r74YBAg/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=143BFE6E6FD134F5E710AE8B55394D42089229A8204680A3D5A0DA0D215F1304 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。

   找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/3kaJ2PowReiHdQKzqNm0tQ/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=5154322D0E8DEC8B578A5CF0265DD4C435F07D4E22D0827C2BF062F5137076AA "点击放大")

   查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](../harmonyos-guides/ide-arkui-inspector.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/KflVGDkpSSGI496a01jMWg/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=83F7F353610C2CBB578D1C67C06DC35CD292639677282D37ED0317E23AF3BD38 "点击放大")
