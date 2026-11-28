---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch
title: Launch模板基本操作
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 冷启动：Launch分析 > Launch模板基本操作
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f2e55f5f7a43228b539345134260ef98fd699efe65413957cdbf0e6a9b159ce7
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
* 不支持[应用预加载](preload-application.md)和[应用快启](hyperstartup-application.md)机制。
  + 上述机制会由系统提前完成应用进程创建与基础资源初始化，跳过冷启动完整流程，导致Launch泳道无法采集从进程创建到首帧渲染的全链路启动节点，无法输出完整的启动生命周期分析数据。
  + 可以通过重启系统或者重新安装应用之后清理系统缓存，确保录制应用是冷启动过程。

## 启动模式介绍

录制前应用的启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/CpFdz5pmT0KU2Qdjl2RmLQ/zh-cn_image_0000002808766361.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=612F419194D5E65E24C4D20AB518023A04FDCC4C11EB4583FCB5F1B22C1E686A "点击放大")自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ar2P7QFDQiuysdrRQjGUmw/zh-cn_image_0000002808886445.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=C57627FFA88570CA42731FA94659673063E795A444F4E5A701F5D405FF9FF291 "点击放大")手动启动，可点击图标切换两种不同模式：

* 若选择自动启动模式，当用户使用Launch模板并开始录制时，将自动重启所选应用。
* 若选择手动启动模式，在开始录制时，只会自动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

## 查看启动过程中各阶段的耗时情况

1. 框选**Launch**泳道图区域的一个阶段或多个阶段，在下方的**Details**区域中，可查看到所选阶段的耗时统计情况。

   展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息，单击跳转按钮，可直接跳转至相关线程打点任务中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/juNpXdfPSfatjXhzdWySmw/zh-cn_image_0000002779566784.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E0B7B27662CE41209BF54DC27F57BCBDF7304DCAC88310840BF526097EB5AA5 "点击放大")
2. DevEco Studio 6.0.0 Beta1版本新增**Load ETS Files**区域，支持查看冷启动过程中.ets文件的加载情况。各字段含义如下：
   * Category：该.ets文件在应用启动过程中是否被使用。
   * Weight**：**该.ets文件加载子节点文件（不包括自身）的总耗时。
   * Self：该.ets文件自身加载的耗时。
   * Import Count：该.ets文件被其他文件导入的次数。
   * File Name：该.ets文件的名称。
   * Path：该.ets文件构建产物的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/hl2QzeKRRW-bMw6JJBgosw/zh-cn_image_0000002808766367.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A3E47B4523B5C17C100BB6C0005534BAF3CEFFB598A2D397F582C24769620B6 "点击放大")
3. 切换到**TOP Redundant**区域，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Juh-9woGQ9KqLXEWpDhN8A/zh-cn_image_0000002808766363.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=93A073557068061A77FF0346EACE81C3C4D530227D0337BA3F99259ADDA5FDF1 "点击放大")

**说明** 

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中.ets文件的加载情况。

## 分析静态资源库加载耗时

1. 展开**Launch**泳道，其中的**Static Initialization**子泳道展示启动过程中各静态资源库的加载耗时。
2. 单击单个静态资源库色块，或框选多个静态资源库**色块**，下方的**Details**区域展示所选对象的耗时统计信息。

   针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/SYd2D0-GSZmsj6rb0HvalA/zh-cn_image_0000002808886449.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B974BFFE235D0AEAB8B9079CF9E7F23E70BC9EA66C9C5FD55A626951C00AA53 "点击放大")

## 查看核心线程在CPU Core的运行情况

1. 展开**Launch**泳道，其中的**Running CPU Cores**子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2. 单击单个进程色块或框选多个进程色块，下方的**Details**区域展示所选对象的运行情况统计信息，单击CPU的跳转按钮，可跳转到CPU Core泳道查看详细的调度信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/JzyFS6dVTyuS5i1MaSF1Xg/zh-cn_image_0000002779566780.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FE478393B8D73A76CAD51639EC4365151D4794806D8821B90BC0574FF112ED0 "点击放大")

## 查看启动过程相关的线程Trace数据

1. 展开**Launch**泳道，除Static Initialization和Running CPU Cores子泳道外，还包含启动过程的关键线程的状态和Trace数据。
2. 单击单个切片色块或框选多个切片色块，可查看所选对象的详情。
   * **Details**区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
   * **Thread States**区域展示线程的状态统计信息。
   * **Thread Usage**区域展示线程的使用情况。
   * **Slice List**区域展示所选对象的切片统计信息。
   * **Load Statistics**区域展示所选对象的中载和重载信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/69RsG9zyRxiJKa0Hvataqg/zh-cn_image_0000002779566782.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=879E3EADDF758B9CA93D014C6FD4C0E319329C5249375F1A6D584BAA85FF83EA "点击放大")
