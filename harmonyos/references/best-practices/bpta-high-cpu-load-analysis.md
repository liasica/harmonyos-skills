---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis
title: CPU高负载分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > CPU高负载分析
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:c189a528f4e1f322ff487130e9f248a44459f016fd83c2c9a994c1ce6290ba94
---

## 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1. 点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2. 观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/rFbjc5qpRUmI9pwCiX1sQw/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C886B9F25AF224255282D295DCB168472F3526BB4B3257F2F407AF298518159 "点击放大")

   **说明** 

   CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
3. 点击下方中的三角形，可展开后直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/fS7fay9DTeGVv4mMdbmnXw/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=20057AA1E17AC345274BADF2CD6335DF182B742F27FE35D0C89D75CFC29EE12F "点击放大")

## 分析思路

CPU高负载问题通常涉及以下三种情况：

1. GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2. UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3. 应用侧其他线程负载高。需要借助callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/XW7fz3XLRRqqs_cOfYiscA/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5651DF03A74DE0C0C9562EA4896A8F28AF807F9002B9B3A2B342CFA8C803324)

## 分析步骤

### 案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/wjA_LtdBSM-y6MTzXtkjgA/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=4028963A455ED4AC93C5019453CB901D7AA76CC1458EE47517815688088B8056 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。

   Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/xFSB-iQCTECaxGRzkVBrbg/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=50B6A6913359770F91127538FAB38C00D661776C9F3246C81AA424D897C764E2 "点击放大")

   当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/i6H_jitwQyumXrCAeJY2Tg/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=F31AE91659B2B7EBF83BE4A119CB4FB4C6296424CA90E3E171A62E7B2A9BC496 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](bpta-click-to-complete-delay-analysis.md)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

### 案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/e4l2pGKlT_mytr0ieorVew/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=885CD335533EE84294035031530F12D5F5E927A0C0E2E291E9C89208BC6AB7E0 "点击放大")

   查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/8cx_fiCcSM2KKL6xTYrXPA/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=49FE78816CC1914029086BBFF965389BBDFDD48106CAED03F049CF5F14452971 "点击放大")

   当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/dW9KRR7rQaK6FgS7WRHQmQ/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=661CF706CC7B47263106D8FA1E4A1C4B7CD4C89F1B57A1681FE0CFA3978439AE "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/yzFK8MmESHiMX-LWWh9-cg/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=C094CC5F472C92753509DAF9BC5F52E3BD06622A56FFFF4FA73882FD76AC8BEE "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[基础内存：Allocation分析](../harmonyos-guides/ide-insight-session-allocations.md)和[内存泄漏：Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)。

### 案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1. 在Profiler工具中开启Energy模板分析任务并复现问题场景。
2. 观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](../harmonyos-guides/ide-insight-session-cpu.md)。

   选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/IWpK2TkjRgKpDvDTlm6NWA/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BF740827F6D0C04BA0EC96E63279F984691C13A69E0DC903A6AE4320D0C421D "点击放大")

   查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/DR2iOKjLTUSbtBLU2KJUjQ/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1436CA8E98028E1B2C25F8634837CE3FB5BB2ED962FEE9C2D18E4CB7421504D "点击放大")

   选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/1x6jwbalQQu_yUA6fDdO7A/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9D042A39EE0DC8E24A80308F63E065E1B2C4541820C33B4A37CBD8605D01984 "点击放大")
3. 根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。

   找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/cYCZpwzDTqeoOA4qdebVnw/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=A086E924A5BD6998C382F1DCE71FDAA833B52C2EA2A8B8D12DA3B5257097FB33 "点击放大")

   查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](../harmonyos-guides/ide-arkui-inspector.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ksZc5JboS7anLiuRT5iLOA/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC8A7C0A7D2B791BE07CCDFBA5C9779E45947A173C93A9583E2028A9B35F2861 "点击放大")
