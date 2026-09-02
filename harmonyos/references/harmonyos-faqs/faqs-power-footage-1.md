---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-power-footage-1
title: 应用前台CPU高负载
breadcrumb: FAQ > 应用质量 > 技术质量 > 功耗 > 应用前台CPU高负载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:10753f94677c9635ee6e1eeb64f4955e945948779b49d59b0d5b2d6a9c9d4501
---

## 问题现象

一些应用程序会在前台长时间工作运行，比如视频直播类应用长时间播放视频，金融理财类应用不断更新显示的数据，会使设备CPU持续在高频下工作，存在CPU高负载问题。

## 背景知识

* DevEco Profiler目前是集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码，更多详细介绍可查看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  DevEco Profiler提供[实时监控](../harmonyos-guides/realtime-monitor.md)（Realtime Monitor）能力，该能力提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、温度、电流、能耗以及网络流量消耗等多个维度的数据，可以帮助识别性能瓶颈，定界问题所在。
* Trace文件是一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况，查看Trace文件可使用[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/README_zh.md)。
* 火焰图是一种用于可视化程序性能分析的工具，其以直观的图形界面，将复杂的函数调用关系和执行时间分布清晰地展示出来。在分析功耗问题中常常借助火焰图来找到应用运行中比重较大的部分，确定问题分析的方向。

  Smartperf的[Hiperf](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/ide/src/doc/md/quickstart_hiperf.md)工具包含了火焰图功能。

## 问题定位

1. 使用DevEco Profiler实时检测工具(Realtime Monitor)查看运行应用一段时间后的在CPU上的运行占比以及设备温度，如果手机温度在持续上升达到发热、应用进程运行在CPU运行占比较高，如下图所示，则存在功耗问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/xPo877t2QbOHVUSNooTg9w/zh-cn_image_0000002628316224.png "点击放大")
2. 使用Smartperf的Hiperf工具抓取该过程的火焰图数据，通过Hiperf的火焰图功能查看运行占比较高的线程是应用子线程还是渲染相关的线程，展开Hiperf泳道，框选前面两个泳道，下方会以运行频率从高到低来显示各个进程的情况。
   * 如果运行占比较高的线程为应用的子线程，则会看到如下图所示的情况，在运行占比最高的应用进程7139中，子线程7394运行占比最多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/9Cy_czRwTsmwmZRO8xEbZw/zh-cn_image_0000002658675461.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/xK47jesWRfSG1QqkZ7cKfA/zh-cn_image_0000002658555519.png "点击放大")

     a.在应用线程中该子线程的泳道，框选运行状态，查看该线程主要运行在什么CPU上，如果在CPU10和CPU11（大核）上，则确定是由于该线程长时间运行导致功耗问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/qzR-nMQ9QHKKtBNGbf_kmw/zh-cn_image_0000002628476140.png "点击放大")

     b.通过Perf Profile来查看该线程的调用栈，耗时集中在执行什么函数上。从下图中可以看到uv\_run运行时间最长，堆栈中涉及到了libuv.so库，该库基于事件驱动来实现异步I/O，适用于网络编程和文件系统操作。应用通常使用该库访问云侧查询数据，因此需要排查应用侧业务处理逻辑是否合理，是否存在死循环，任务是否过多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/V6mYDRvjR2SIbC6Yj4_dXg/zh-cn_image_0000002628316228.png "点击放大")
   * 如果运行占比较高的线程为绘制、渲染相关的线程，如下图所示，渲染服务进程render\_service和应用进程29187运行占比最高。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/6rcDG8L9SdO12MdSdWj8GQ/zh-cn_image_0000002658675465.png "点击放大")

     a.点击/system/bin/render\_service(1466)查看render\_service的子线程运行占比，可看到RSUniRenderThread线程和主线程占比最高。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7aDX2hT6SaK6vz1mRd0izw/zh-cn_image_0000002658555523.png "点击放大")

     b.点击应用进程29187查看应用的子线程运行占比，可看到主线程运行占比最高。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Id4gWkhzR5SiNBhTwzFsJA/zh-cn_image_0000002628476142.png "点击放大")

     c.在Trace中框选应用主线程泳道，在下方搜索框输入anima、FrameNode来确认是否有动画、组件绘制的情况，如果存在动画、组件多次绘制的情况，使用ArkUI Inspector工具查看执行动画、进行多次绘制的组件是什么，是否显示在屏幕上，如果不存在屏幕上则存在动画空跑、冗余绘制的情况，会导致功耗问题。

     如在下图中可以看到应用主线程有执行动画，同时组件Canvas（id为1441）、Image（id为338、284、516）有多次绘制。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/RdNlRpCNTQ22e-HBI02x8A/zh-cn_image_0000002628316230.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Qx9E_lCDTyK8tQq4LFCc-Q/zh-cn_image_0000002658675467.png "点击放大")

     d.使用ArkUI Inspector工具来查看绘制的组件，可以看到组件Canvas未显示在屏幕上，而Image组件显示在屏幕上。Image显示组件在屏幕上，有执行动画，属于正常的业务流程，而Canvas组件未显示在屏幕上，存在冗余绘制的问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6g71uCh4TTSnSAFVMe_LXA/zh-cn_image_0000002658555525.png "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/41dSuf7pSLSrl5YudiS_ZQ/zh-cn_image_0000002628476144.png "点击放大")

## 分析结论

1. 应用子线程处理任务较多，长时间在大核CPU上运行，导致功耗问题。
2. 应用组件冗余绘制、动画空跑，使主线程长时间在大核CPU上运行，导致功耗问题。

## 修改建议

1. 优化应用子线程处理逻辑，减少处理任务。
2. 应用组件存在冗余绘制问题时，可优化成不显示时停止绘制，避免冗余绘制。
