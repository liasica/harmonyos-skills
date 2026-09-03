---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch
title: Launch模板基本操作
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > Launch模板基本操作
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:aba985156322b292378bc7e91818db073fe1e99667e9b7c21b99444106234b94
---

## 功能介绍

开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。

Launch模板支持的泳道包括：Launch、Frame、ArkTS Callstack、Callstack、Network Traffic、Network Request、CPU Core、Process。本文介绍Launch泳道，其他泳道的详细信息请参考对应模板内容。

* Frame泳道的介绍请参考[Frame分析](ide-insight-session-frame.md)。
* ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* Network Traffic、Network Request泳道的介绍请参考[网络诊断：Network分析](ide-profiler-network.md)。
* CPU Core、Process泳道的介绍请参考[CPU活动分析](ide-insight-session-cpu.md)。

**说明** 

* 任务分析前，需创建Launch分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)；或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。
* 不支持命令拉起的Release应用，不能进行Launch分析。
* 锁屏状态下可进行Launch录制。

## 启动模式介绍

录制前应用的启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/jyZ_ht1SQy6dSdyU-xfibA/zh-cn_image_0000002731542043.png "点击放大")自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/LjFgr-y4SLmrm0zsLqrR7A/zh-cn_image_0000002731542049.png "点击放大")手动启动，可点击图标切换两种不同模式：

* 若选择自动启动模式，当用户使用Launch模板并开始录制时，将自动重启所选应用。
* 若选择手动启动模式，在开始录制时，只会自动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

## 查看启动过程中各阶段的耗时情况

1. 框选**Launch**泳道图区域的一个阶段或多个阶段，在下方的**Details**区域中，可查看到所选阶段的耗时统计情况。

   展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息，单击跳转按钮，可直接跳转至相关线程打点任务中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/KS5cY81EQhuSgi548jl0Lw/zh-cn_image_0000002701662840.png "点击放大")
2. DevEco Studio 6.0.0 Beta1版本新增**Load ETS Files**区域，支持查看冷启动过程中ets文件的加载情况。各字段含义如下：
   * Category：该ets文件在应用启动过程中是否被使用。
   * Weight**：**该ets文件加载子节点文件（不包括自身）的总耗时。
   * Self：该ets文件自身加载的耗时。
   * Import Count：该ets文件被其他文件导入的次数。
   * File Name：该ets文件的名称。
   * Path：该ets文件构建产物的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/gMd6AgwjStComkV3Ts7HdA/zh-cn_image_0000002701822764.png "点击放大")
3. 切换到**TOP Redundant**区域，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5NNW6uOZSCKrBVZHGGcWLA/zh-cn_image_0000002701662846.png "点击放大")

**说明** 

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中ETS文件的加载情况。

## 分析静态资源库加载耗时

1. 展开**Launch**泳道，其中的**Static Initialization**子泳道展示启动过程中各静态资源库的加载耗时。
2. 单击单个静态资源库色块，或框选多个静态资源库**色块**，下方的**Details**区域展示所选对象的耗时统计信息。

   针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/WMZyPM7XTHSCVuLepUmN8w/zh-cn_image_0000002701822772.png "点击放大")

## 查看核心线程在CPU Core的运行情况

1. 展开**Launch**泳道，其中的**Running CPU Cores**子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2. 单击单个进程色块或框选多个进程色块，下方的**Details**区域展示所选对象的运行情况统计信息，单击CPU的跳转按钮，可跳转到CPU Core泳道查看详细的调度信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/dzHZ8sw2SviBr_i15jxcqg/zh-cn_image_0000002731382075.png "点击放大")

## 查看启动过程相关的线程Trace数据

1. 展开**Launch**泳道，除Static Initialization和Running CPU Cores子泳道外，还包含启动过程的关键线程的状态和Trace数据。
2. 单击单个切片色块或框选多个切片色块，可查看所选对象的详情。
   * **Details**区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
   * **Thread States**区域展示线程的状态统计信息。
   * **Thread Usage**区域展示线程的使用情况。
   * **Slice List**区域展示所选对象的切片统计信息。
   * **Load Statistics**区域展示所选对象的中载和重载信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/LObp4vPRRpWEyHLb8gaFBg/zh-cn_image_0000002701662844.png "点击放大")
