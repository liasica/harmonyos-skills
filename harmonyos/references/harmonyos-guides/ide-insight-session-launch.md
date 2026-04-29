---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch
title: Launch模板基本操作
breadcrumb: 指南 > 优化应用性能 > 冷启动：Launch分析 > Launch模板基本操作
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:931ff46cec63be45d177f627e7edbbc592b16b0b542d8bf793bb5cc091f81984
---

开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。此外，Launch任务窗口还集成了Time、CPU、Frame、Network场景分析任务的功能，方便开发者在分析启动耗时的过程中同步对比同一时段的其他资源占用情况。

此处仅介绍“Launch”泳道相关内容，集成的Time、CPU、Frame、Network场景分析任务的功能请参考对应任务的章节。

说明

* 不支持命令拉起的Release应用不能进行Launch分析。
* 锁屏状态下可进行Launch录制。

## 启动模式

启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/aCCC58X7R2CAFeVmp2W72w/zh-cn_image_0000002530912822.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=3875B3890037F9A8BFBABC1D39D35FD1A814EE421F7D900DAEF95B1A4241264F)自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/hnOVzGK9Q1iqqPR2CI0EGg/zh-cn_image_0000002561832753.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=80F73F810457E455DE7DF9AAF7EA800411A2C0ED78E0F45B1F0F3D61B176630A)手动启动，可点击图标切换两种不同模式：

* 若选择自动启动模式，当用户使用Launch模板并开始录制时，将主动重启所选应用；
* 手动启动模式在开始录制时，只会主动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

## 查看启动过程中各阶段的耗时情况

1. 创建Launch场景调优分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。

   说明

   * 在任务分析窗口中，可通过[快捷键](ide-shortcut-key.md)缩放时间轴、移动时间轴、添加时间标签等。
   * Launch分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * Launch分析支持动效场景调优，请参见[支持动效场景调优](ide-insight-session-frame.md#section258014238619)。

   Launch分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/y6NMAkImSqudYLIkXRitIQ/zh-cn_image_0000002561832759.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=A772533C66AE61F74597A0BD936534713721628369B5BC4915F97254BA3C4495)指定要录制的泳道。“Launch”泳道显示启动生命周期各阶段的耗时分布情况。
2. 单击“Launch”泳道上的单个阶段，或框选多个阶段，在下方的“Details”页签中，可查看到所选阶段的耗时统计情况。

   展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息。单击跳转按钮，可直接跳转至相关线程打点任务中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/sCdh8HnTRcivgf9jSKuQZg/zh-cn_image_0000002530912832.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=98240DCA46E985A781EE286CC05E31BDCCCC60575440423D2080EDBF1749837A "点击放大")
3. 切换到“Load ETS Files”页签，从DevEco Studio 6.0.0 Beta1版本开始，支持查看冷启动过程中ETS文件的加载情况。各字段含义如下：
   * Category：该ETS文件在应用启动过程中是否被使用。
   * Weight**：**该ETS文件加载子节点文件（不包括自身）的总耗时。
   * Self：该ETS文件自身加载的耗时。
   * Import Count：该ETS文件被其他文件导入的次数。
   * File Name：该ETS文件的名称。
   * Path：该ETS文件构建产物的路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/hsSPA6xOSSOV1-oMH2lHng/zh-cn_image_0000002530912836.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=DE230E4388FA75B9D59EAE88D0E7024A6908E4176925527FC15497EC44E82248 "点击放大")
4. 切换到“TOP Redundant”页签，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/kFy6A7TmT3WpmpAK9CVctA/zh-cn_image_0000002561832751.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=E6823E968F55D5DEC684452FFEDD21FE67AB20D239DF66E2DA1214703EA447E3 "点击放大")

说明

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中ETS文件的加载情况。

## 分析静态资源库加载耗时

1. 展开“Launch”泳道，其中的“Static Initialization”子泳道展示启动过程中各静态资源库的加载耗时。
2. 单击单个静态资源库色块，或框选多个静态资源库，下方的“Details”区域展示所选对象的耗时统计信息。

   针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/a2tYkBOKSZ286n8kY-0XDQ/zh-cn_image_0000002530752842.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=36195732D0414A4DD0B5EF5AEC37F6253C637A6B8AECF37BB16A15403B6D27E0 "点击放大")

## 查看核心线程在CPU Core的运行情况

1. 展开“Launch”泳道，其中的“Running CPU Cores”子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2. 单击单个进程色块，或框选多个进程，下方的“Details”区域展示所选对象的运行情况统计信息。

   单击对应CPU的跳转按钮，可进一步跳转到CPU Core泳道查看详细的调度信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/g94eeDwoQTy2YanNVTjQSA/zh-cn_image_0000002530752828.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=4D43B8DAA01B70E0365588FE6AB52676E4F5E1316E1526121865E243E698577D "点击放大")

## 查看启动过程相关的线程Trace数据

1. 展开“Launch”泳道，除“Static Initialization”、“Running CPU Cores”外，还包含启动过程的关键线程的状态和Trace数据。
2. 单击单个切片色块，或框选多个切片，可查看所选对象的详情。
   * “Details”区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
   * “Thread States”区域展示线程的状态统计信息。
   * “Thread Usage”区域展示线程的使用情况。
   * “Slice List”区域展示所选对象的切片统计信息。
   * “Load Statistics”区域展示所选对象的中载重载信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/L3RyszAUQauHPFMUT0giGQ/zh-cn_image_0000002561832755.png?HW-CC-KV=V1&HW-CC-Date=20260429T054731Z&HW-CC-Expire=86400&HW-CC-Sign=85FDFA9977EB7BC35F73C4FA4E269EA8770476443C321DC6BEE57FC6D32FC43E "点击放大")
