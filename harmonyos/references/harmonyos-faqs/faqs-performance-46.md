---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-46
title: 快速滑动列表时数据加载延迟
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 快速滑动列表时数据加载延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d7ac34eec1ac1de6bd3dd70ebdedd70d1f92c9e14d001d53e8712a7c35149467
---

## 问题现象

在快速滑动列表页时，数据需要等待一段时间才会显示。

## 背景知识

* [DevEco Profiler](../harmonyos-guides/ide-profiler.md)：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能。
* [@Reusable装饰器](../harmonyos-guides/arkts-reusable.md)：@Reusable装饰器标记的自定义组件支持视图节点、组件实例和状态上下文的复用，避免重复创建和销毁，提升性能。
* [组件复用](../best-practices/bpta-component-reuse.md)：在应用开发时，组件复用是优化UI性能，确保应用流畅的重要手段。合理使用可复用组件，一方面，可以避免频繁创建和销毁对象的过程，减少内存回收的频率；另一方面，复用缓存中的组件可以直接绑定数据进行显示，与创建新视图相比，降低了计算开销，提升了显示效率。

## 问题定位

1. 使用DevEco Profiler的Frame模板抓取应用列表页快速滑动后加载内容的Trace。在应用包名主泳道的H:APP\_LIST\_FLING泳道找到抛滑过程结束的时间点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/bxKqSJmIQBGo9N16lUOprA/zh-cn_image_0000002658914517.png "点击放大")
2. 查看应用包名主泳道发现在结束抛滑过程后存在耗时Trace点。可以明显看到Stack、Scroll、List组件的测量任务耗时较长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/UmR9rjehTdWu_kw82A3z9A/zh-cn_image_0000002628395286.png "点击放大")
3. 结合ArkUI Inspector中看到的页面组件结构，可以发现列表中的每一项都是由相同类型的元素和布局构成，列表项组件名为XXXView。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/DTKlaYVqQGWuj8dfZM4X2w/zh-cn_image_0000002658794563.png "点击放大")
4. 根据组件名搜索关键字H:CustomNode:BuildRecycle XXXView，可以看到组件复用13次，平均每次复用时耗时7.9ms，耗时较长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/7xoEk8YCTwyiO905iXNyNg/zh-cn_image_0000002628555198.png "点击放大")
5. 框选单次复用的Trace，在下方Slices中过滤关键字H:Create，可以看到在此过程中创建了27个子组件。结合ArkUI Inspector查看页面组件结构，组件嵌套层数为17层，且其中包含大量并未在当前页面中展示的节点。因此是页面整体组件嵌套层级复杂且复用组件中节点过多导致绘制耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/A1jih2X_QOWmAkvq8_PqKQ/zh-cn_image_0000002658914519.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/I7IgZo48S5q5L18E12_9FA/zh-cn_image_0000002628395288.png "点击放大")

## 分析结论

页面整体组件嵌套层级复杂且复用组件中节点过多导致绘制耗时。

## 修改建议

* [组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，避免冗余的嵌套或者使用扁平化布局来优化嵌套层次。
* 参考高负载场景分帧渲染中的[滑动场景](../best-practices/bpta-dispose-highly-loaded-component-render.md#section15195122915243)，在业务需要一次性加载大量数据时采用分帧渲染，减少卡顿。
