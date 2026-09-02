---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-27
title: 双击图片放大时异常卡顿，不流畅
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 双击图片放大时异常卡顿，不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e637bd9d6deb8de69dd36452c3b8aa9bb38b5686bba217d13cd29c40297dd51
---

## 问题现象

在浏览图片时，双击图片放大，放大过程中明显感到卡顿不流畅。

## 背景知识

* 屏幕刷新率意思是每秒钟屏幕会刷新的次数，即120Hz是一秒内刷新120次，平均一次耗时8.33ms。由此可得：

  | 刷新频率 | 平均单次耗时 |
  | --- | --- |
  | 120Hz | 8.33ms |
  | 90Hz | 11.11ms |
  | 60Hz | 16.67ms |
* ArkUI Inspector是DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* [DevEco Profiler](../harmonyos-guides/ide-profiler.md)目前是集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码。

## 问题定位

1. 复现问题，找到发生卡顿的问题页面，使用ArkUI Inspector抓取当前页面的组件结构，发现应用使用Canvas组件绘制当前页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/V3mHc8kbTP6OENFODPw2wQ/zh-cn_image_0000002658794433.png "点击放大")
2. 使用DevEco Profiler中的Frame模板抓取整个复现流程的Trace，由于是双击后放大图片，在应用包名泳道搜索关键字H:DispatchTouchEvent找到第二个type=1的Trace点，此时为双击事件识别成功，可作为问题分析的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/35ZIZYS0SriGAh5WvD_iGA/zh-cn_image_0000002628555070.png "点击放大")
3. 查看render\_service进程中的H:PreferredFrameRate，鼠标悬停可查看此时屏幕刷新率为90Hz。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/oYdpNI_ZQ1WavNc3ZwRjpg/zh-cn_image_0000002628395164.png "点击放大")
4. 应用发生卡顿的页面是用[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件绘制的，因此搜索关键字H:FrameNode[Canvas][id:xxx]::RenderTask，发现应用侧渲染Canvas组件周期为100ms，换算成刷新率仅为10Hz，远低于当前屏幕刷新率90Hz，因此使用体验非常卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/D43bqeSXSaaPxkmd09W7Rw/zh-cn_image_0000002658914393.png "点击放大")

## 分析结论

双击放大图片时，应用组件渲染的频率过低，远小于屏幕刷新率，导致放大过程异常卡顿丢帧问题。

## 修改建议

GPU并行计算能力优于CPU，更适用于绘制图片，建议应用侧参考[GPU后端Canvas的创建与显示](../harmonyos-guides/canvas-get-result-draw-c.md#gpu后端canvas的创建与显示)创建GPU后端Canvas，提高绘制性能，减少卡顿。
