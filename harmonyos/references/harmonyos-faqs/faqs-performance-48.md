---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-48
title: 应用在横竖屏切换旋转过程中丢帧
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用在横竖屏切换旋转过程中丢帧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e59c8df41ba019f277e0ac2f437634593a8f96cf4f2b7fa426b7871b6907a509
---

## 问题现象

应用切换横竖屏模式，在旋转为横屏或竖屏显示模式的过程中出现丢帧的现象。

## 背景知识

* **屏幕刷新率：**

  屏幕刷新率的意思是每秒钟屏幕会刷新的次数，即120Hz是一秒内刷新120次，平均一次耗时8.33ms。由此可得：

  | 刷新频率 | 平均单次耗时 |
  | --- | --- |
  | 120Hz | 8.33ms |
  | 90Hz | 11.11ms |
  | 60Hz | 16.67ms |
* **DevEco Profiler**：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，具体可参考[调优工具简介](../harmonyos-guides/ide-profiler.md)。

## 问题定位

1. 使用DevEco Profiler的Frame模板抓取横竖屏切换旋转过程的Trace。在Frame泳道应用包名子泳道搜索H:WindowSessionImpl::UpdateRectForRotation作为横竖屏切换的起点，可以明显看到在此后有标红Trace点，出现丢帧现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/XhAkChmtR4e6YacVebKUMA/zh-cn_image_0000002628555202.png "点击放大")
2. 点击编号为133的Trace点，在下方的Details中点击Corresponding Slice左侧的箭头按钮，可跳转至应用包名主泳道应用包名主线。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/CGrVlBYIQFCZhPBT39xr0g/zh-cn_image_0000002658914523.png "点击放大")
3. 跳转至应用包名主线程查看对应帧绘制的Trace信息，观察到泳道中存在大量Measure和Layout相关的Trace点，这是应用在测量组件宽高并进行布局。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/_BA_CmsjRyuCEXPQTTE68A/zh-cn_image_0000002628395292.png "点击放大")
4. 根据这一帧的起始时间和结束时间框选出分析范围，在下方Slice List中过滤出测量任务（H:Measure）和布局（H:Layout）任务。可以看到这一帧进行了254次测量、布局任务，单帧耗时达到23ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/hFnlBPNJStueqrXq1q5Tug/zh-cn_image_0000002658794571.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/V-VuNrtTTG2a7i_WW3-2bA/zh-cn_image_0000002628555204.png "点击放大")
5. 重复以上步骤查看后续帧的绘制情况，发现在长达640ms的旋转过程中单帧绘制耗时均在23ms左右，远超过屏幕刷新率120Hz所要求的8.33ms。综上所述是应用页面结构复杂导致在横竖屏切换时大量组件需要重新测量宽高并布局，造成单帧绘制超时，因而出现丢帧现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Tj0i0AbTTqG1dQCAeNrAbQ/zh-cn_image_0000002658914525.png "点击放大")

## 分析结论

页面结构复杂导致在横竖屏切换时大量组件需要重新测量宽高并布局，造成单帧绘制超时，因而出现丢帧现象。

## 修改建议

针对结构复杂的页面，可进行[组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，减少节点数，降低整体性能消耗。
