---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis
title: CPU高负载分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > CPU高负载分析
category: best-practices
scraped_at: 2026-11-24T12:47:53+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:3a562d1ca357c11e37ec9f99bbaa22a9faf72604681c2c4144d4140ba2fe88b5
---

## 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1. 点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2. 观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/D3fpgJ_HT3mxllwHnhXLHA/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=780F226DE60F10A49CF0A399DF87E1B109568B1FE82153E0B2F8927114B566DC "点击放大")

   **说明** 

   CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
3. 点击下方中的三角形，可展开后直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/1w61LXb-SIul4WKXVtlBPQ/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=619930F7C5788563CA9EFB03F8DA009DD2985672B8B88A03FA9048E87CF33F57 "点击放大")

## 分析思路

CPU高负载问题通常涉及以下三种情况：

1. GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2. UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3. 应用侧其他线程负载高。需要借助callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/f1l-M27lQSyyEub3n5vMDg/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=837B4F1D7BFFFD2EF01BB34DC9295B5548C0681D0F148C9A30725F5079A1ACE6)

## 分析步骤

### 案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/OwIjj0iBRIC-GAVCTdPhyw/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D19B308583226DB48F8297D7EE4FBBE30F57EA24DAFCE960CBC831CB94F08D2 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。

   Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/fuSU-3HuRn2-Ux5RS-IajQ/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=16B0472A5D59C1D30689B95AEA1743F0B5EB206A98E9F8C37CE17630503E2D44 "点击放大")

   当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/DFX4veVFRLqXEfUNPm_oog/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A7F59C1B24D952ED8CD65759B2BABA5A160B955BC529BB20935B9041D164AEF "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](bpta-click-to-complete-delay-analysis.md)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

### 案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/hP1zI9JfSNez8sh3hiMmBw/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=08A58904EBC06284F6AAF12BF64F4282CFD4DDFE8BCA105CD8C53239CA35D23B "点击放大")

   查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Y-IAwghCSxyEU6_kMx42tg/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AB6A954B1C972E60678AB3E902BAD7E03B4C2B9F03080A3A8DD7308A31DDDB2 "点击放大")

   当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/juscuQwlTnmLmDyGZ9n2Jw/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB66260E68C410649509B59490D213EC47C2335D27FC69F099CA3762255FAF4D "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/DdNzMIoVT7er24vb9fUpvg/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE5416C102BFA5C809261E4A8340E041A78B13595C1BECB0B5BD69419EBE78DC "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)和[内存泄漏：Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)。

### 案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/0BDBndg8RFGNIKiruTXk7w/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE7B1CA0AF9CE79694A93FB66ECCA3A8C052540BE59A594DB961BAA38DA09331 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/3i0fYuJ-TIiZ5L4U7r3EpQ/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA5D6CFD10B2C48E1F38050FC3750D04F069D01B6BCE1596200DD9D18DB19173 "点击放大")

   选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/52SOlvk5RW2LUr0iWQQx1g/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=49A734BA6DF046CFF029F07BBC1337C3168ACC1905E7087F3BDCA5E68C832A11 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。

   找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/b8CNbnyTTISbnF2nUV9nyw/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B4B536A43D46716682ADE8BAB2A8E8463B11C57707A3FC134A94270EC2BC4AC "点击放大")

   查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](../harmonyos-guides/ide-arkui-inspector.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Maqirj_pRzGf_YMivtXNHA/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9307A04A09AB86F34F5DCEA637163A9AAE85671A3C3C30F91260FB0DE6F0DDF "点击放大")
