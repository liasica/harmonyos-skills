---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-23
title: 双指缩放时抖动卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 双指缩放时抖动卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:144f22c6a64a6d01550934fb8a25dc9bbaef05db1df8fc3ae730e77b30400324
---

## 问题现象

在双指缩放应用内页面或图片时，缩放的动效卡顿不流畅。

## 背景知识

* **ArkUI Inspector**：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* **DevEco Profiler**：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析等问题，帮助应用开发者定位到问题代码，具体可参考[调优工具简介](../harmonyos-guides/ide-profiler.md)。
* **屏幕刷新率**：每秒钟屏幕会刷新的次数，120Hz是一秒内刷新120次，平均一次耗时8.33ms。

## 问题定位

1. 使用DevEco Profiler中的Frame模板抓取双指缩放过程中的Trace，在UserEvents泳道可以看到手指操作事件的开始和结束时间，以此框定分析问题的范围。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NnQlsxIbSImY_hX9VsuU5A/zh-cn_image_0000002628555060.png "点击放大")
2. 在render\_service线程中根据H:PreferredFrameRate获取当前屏幕刷新率为90Hz，根据背景知识中【屏幕刷新率】换算得平均单次刷新耗时11.11ms。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Kk1G4Ek4SJqTSyRhrZ5UwA/zh-cn_image_0000002628395156.png)
3. 查看Frame泳道应用包名线程是否有标红的掉帧点。
   * **有标红掉帧点**，查看对应时间范围应用包名泳道的应用包名子线程Trace，可以看到单次ReceiveVsync（接收Vsync信号）耗时70ms左右，远超步骤1中换算得出的11.11ms，说明此时在多次屏幕刷新时页面信息没有更新，在视觉上体现为卡顿丢帧。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/_4m8XxwaSYG_WRqqEvjwjA/zh-cn_image_0000002658914383.png "点击放大")

     根据H:ViewPU.viewPropertyHasChanged xxx isValidate 0耗时53.8ms可以判断具体原因为状态变量更新时执行耗时操作导致此次ReceiveVsync（接收Vsync信号）耗时过长。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/On9pvezCQYyIvJadUxaNZw/zh-cn_image_0000002658794425.png "点击放大")
   * **没有标红掉帧点**，需要对相关组件绘制渲染的频率进行分析。通过ArkUI Inspector抓取对应页面布局，得知使用的是Canvas组件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/kp4gRKs8TceGCF0jHht4MQ/zh-cn_image_0000002628555062.png "点击放大")

     在Frame模板分析结果的上方搜索框中根据关键字H:FrameNode[Canvas][id:组件ID]::RenderTask搜索Canvas组件渲染的频率，可以看到每次渲染间隔在25ms左右，通过计算可得出应用侧渲染该组件的频率为40Hz左右，不到当前屏幕刷新率90Hz的一半，因此在双指缩放过程中有明显抖动卡顿现象。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/fgOoJXSdRLWlG38MxOGvfg/zh-cn_image_0000002628395158.png "点击放大")

## 分析结论

* 状态变量更新时执行耗时操作导致单次接收Vsync信号耗时超过一帧绘制时间，因此双指缩放时卡顿丢帧。
* 应用组件渲染的频率远低于屏幕刷新率导致双指缩放时抖动卡顿。

## 修改建议

* 优化状态变量更新逻辑，避免在更新时执行耗时操作。
* 参考[GPU后端Canvas的创建与显示](../harmonyos-guides/canvas-get-result-draw-c.md#gpu后端canvas的创建与显示)，创建GPU后端Canvas，提高绘制性能，减少卡顿。
