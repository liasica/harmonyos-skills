---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-21
title: 视频录制完成后的加载时间过长
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 视频录制完成后的加载时间过长
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0dbc89dfadd6c43696e86b0b5e3779d70920521bcbfab65cd5153ffef0a3091d
---

## 问题现象

用户在使用应用录制完视频后，会显示正在加载中，且需要等待一段时间后才完成加载。

## 背景知识

* [LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)：用于显示加载动效的组件，常用于加载时间较长的业务场景，比如页面加载、视频录制和图片处理等。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多详细内容可查看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

## 问题定位

1. 使用ArkUI Inspector抓取加载过程页面，发现加载动效的组件为LoadingProgress。
2. 使用DevEco Profiler Frame模板抓取加载动效从显示到消失过程的Trace信息，在Profiler页面上方搜索框中搜索H:FrameNode[LoadingProgress]找到加载动效首次渲染和最后一次渲染的Trace点。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/n0DHhiYhSm-BO00oV39x1A/zh-cn_image_0000002658914375.png "点击放大")
3. 视频录屏完成后加载过程通常是在处理视频数据，但无法确认数据处理线程是什么线程，可以通过查看CPU Core泳道中应用线程在CPU上的运行占比来确定，从下图中可看到运行占比最多的两个线程为应用主线程和OS\_FFRT\_2\_13线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/0vkGuF_3REW7sdJLqLbyJQ/zh-cn_image_0000002658794419.png "点击放大")
4. 处理视频数据耗时通常较多，如果在主线程中处理视频会导致主线程卡顿，而在该过程中加载动效流畅运行，因此推测视频数据处理是由OS\_FFRT\_2\_13线程完成。分析OS\_FFRT\_2\_13线程的Trace信息，发现该线程调用napi接口ffmpeg时耗时较多。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/FAHBQleqS6udfYFpKVAB8A/zh-cn_image_0000002628555056.png "点击放大")
5. 查看Callstack泳道中OS\_FFRT\_2\_13子泳道的调用堆栈，可看到视频数据处理逻辑在libffmpeg.so文件中。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/OYT-CS1sRA6YT3bm1z5KjA/zh-cn_image_0000002628395152.png "点击放大")

## 分析结论

应用处理视频数据由单线程完成，业务逻辑复杂，耗时较多，导致视频录制完成后加载时间长。

## 修改建议

采用多线程处理视频数据，可参考[CPU密集型任务开发指导 (TaskPool和Worker)](../harmonyos-guides/cpu-intensive-task-development.md)。
