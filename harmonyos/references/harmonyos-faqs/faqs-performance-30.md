---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-30
title: 应用内点击邀请好友生成分享图慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用内点击邀请好友生成分享图慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f24db44f43f9e6ce23a8531c86b479ea75ba66da1d77d5342938944c98656032
---

## 问题现象

应用内点击分享等功能，生成分享图片慢，需要等待较长时间。

## 背景知识

* [ArkUI Inspector](../harmonyos-guides/ide-arkui-inspector.md)：DevEco Studio中提供用于检查UI的工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* [DevEco Profiler](../harmonyos-guides/ide-profiler.md)：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能。使用DevEco Profiler提供的[Frame](../harmonyos-guides/ide-insight-session-frame.md)场景分析能力可分析卡顿丢帧问题。

## 问题定位

1. 使用Profiler的Frame模板抓取该过程的Trace信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/KINBN1mDSAOH3ZHZvMQliQ/zh-cn_image_0000002628555076.png "点击放大")

   * 以应用收到手指离开屏幕事件的Trace关键字**DispatchTouchEvent xxx type=1**作为问题分析的起点，时间点为4.864s。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/4-nrBiEeRL2VCNMpiM4nLQ/zh-cn_image_0000002628395170.png "点击放大")
   * 找到创建Stack组件的Trace关键字**H:Create[Stack]**，时间点为7.959s，此时距离应用收到手指离开屏幕事件过去3.095s。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/ac9GDTBFTu-r8rpDD3Djsw/zh-cn_image_0000002658914399.png "点击放大")
   * 观察应用包名泳道Trace，在生成分享图后会生成一个页面切换的Trace点：**H:ABILITY\_OR\_PAGE\_SWITCH**，标志已生成分享图，可以将此时间点7.973s作为问题分析的终点，此时距离创建Stack组件过去14ms，几乎不会影响分享图生成总时间。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/j0VFhrItQ7ex0UevqmHHxQ/zh-cn_image_0000002658794441.png "点击放大")
2. 依据以上分析，问题分析重点范围为应用收到手指离开屏幕事件到创建Stack组件。可以看到过程中应用调用C库的GetImageInfo方法后处理获取的图像信息耗时接近1s，导致生成分享图片慢。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/uVa-9KQ1SpabA9rl99EIvg/zh-cn_image_0000002628555078.png "点击放大")

## 分析结论

应用处理获取的图像信息耗时过久导致生成分享图片慢。

## 修改建议

1. 优化获取到的图像信息处理逻辑，降低图像信息处理耗时。
2. 增加“图片生成中”等友好提示。
