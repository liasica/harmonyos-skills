---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch
title: Launch模板基本操作
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 冷启动：Launch分析 > Launch模板基本操作
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:703c0153c951e4a7419e2298ca9a27dfd5e67c788244a44c8154fe0b0c5e00f6
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

录制前应用的启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KjbhiGa7SgWpu_6HC9KWhQ/zh-cn_image_0000002808766361.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E217182A751017F735528BA29D3AAC17AC8FCF1E4AD08ACA0947CBD215DB6669 "点击放大")自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/2n0bKtOzTNaU-1PFdWLThQ/zh-cn_image_0000002808886445.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA38E7E3BC623658D78743C8B60B71C9D184C65ABB84CBF1AC4311479BFC9B7A "点击放大")手动启动，可点击图标切换两种不同模式：

* 若选择自动启动模式，当用户使用Launch模板并开始录制时，将自动重启所选应用。
* 若选择手动启动模式，在开始录制时，只会自动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

## 查看启动过程中各阶段的耗时情况

1. 框选**Launch**泳道图区域的一个阶段或多个阶段，在下方的**Details**区域中，可查看到所选阶段的耗时统计情况。

   展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息，单击跳转按钮，可直接跳转至相关线程打点任务中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/PLUmT64RS26YyI7wmDVBiQ/zh-cn_image_0000002779566784.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5A93F8957CD2BE51493A77BAF104A1E9AF4A7D034EC2C88BEAEF67BABF9B927 "点击放大")
2. DevEco Studio 6.0.0 Beta1版本新增**Load ETS Files**区域，支持查看冷启动过程中.ets文件的加载情况。各字段含义如下：
   * Category：该.ets文件在应用启动过程中是否被使用。
   * Weight**：**该.ets文件加载子节点文件（不包括自身）的总耗时。
   * Self：该.ets文件自身加载的耗时。
   * Import Count：该.ets文件被其他文件导入的次数。
   * File Name：该.ets文件的名称。
   * Path：该.ets文件构建产物的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/8VlaFzO5TSCnKft5c5AUcQ/zh-cn_image_0000002808766367.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8EFD0A2481EF0490E1DE84D0B80E6BC643AD4332B3762EC5AC20594189907289 "点击放大")
3. 切换到**TOP Redundant**区域，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-4SWM9K9TXGoLRoDOFu8HQ/zh-cn_image_0000002808766363.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=472B318C84C403C319FB2FAC627E321082C5BF498A4536DC2E54B3BCC1C5D809 "点击放大")

**说明** 

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中.ets文件的加载情况。

## 分析静态资源库加载耗时

1. 展开**Launch**泳道，其中的**Static Initialization**子泳道展示启动过程中各静态资源库的加载耗时。
2. 单击单个静态资源库色块，或框选多个静态资源库**色块**，下方的**Details**区域展示所选对象的耗时统计信息。

   针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/w_wGKXwCR0-9Yn8COOiiqQ/zh-cn_image_0000002808886449.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A426AEB11DB7F7B794ED892E2D0B145B26C3EAFDE152671F6443F22FF367A454 "点击放大")

## 查看核心线程在CPU Core的运行情况

1. 展开**Launch**泳道，其中的**Running CPU Cores**子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2. 单击单个进程色块或框选多个进程色块，下方的**Details**区域展示所选对象的运行情况统计信息，单击CPU的跳转按钮，可跳转到CPU Core泳道查看详细的调度信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/h6ruChXGSzuMFtVDmCBljA/zh-cn_image_0000002779566780.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=90C2826ED0604AB9C62B99AEBE2E4DA08DF8FA5801E1CEED7EAC860020E4D707 "点击放大")

## 查看启动过程相关的线程Trace数据

1. 展开**Launch**泳道，除Static Initialization和Running CPU Cores子泳道外，还包含启动过程的关键线程的状态和Trace数据。
2. 单击单个切片色块或框选多个切片色块，可查看所选对象的详情。
   * **Details**区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
   * **Thread States**区域展示线程的状态统计信息。
   * **Thread Usage**区域展示线程的使用情况。
   * **Slice List**区域展示所选对象的切片统计信息。
   * **Load Statistics**区域展示所选对象的中载和重载信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/PLqJdiamT-OSkpUpO69QVQ/zh-cn_image_0000002779566782.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=87C26537E9038C4A5D7805F98882542DA04B9E35C232173BC321A7CF90BD10C2 "点击放大")
