---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory
title: UI组件内存：ComMemory分析
breadcrumb: 指南 > 优化应用性能 > UI组件内存：ComMemory分析
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab1caca257d1fd187fc8c096d5518a65d62c57bddf24a5b1ed8c0df405e1db1a
---

## 功能介绍

从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

ComMemory模板支持的泳道包括：Memory、ArkUI Snapshot、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory。本文介绍ArkUI Snapshot泳道，其他泳道的详细信息请参考对应模板内容。

* Memory、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory泳道的介绍请参考[基础内存：Allocation分析](ide-insight-session-allocations.md)。
* ArkTS Snapshot泳道的介绍请参考[内存泄漏：Snapshot分析](ide-insight-session-snapshot.md)。

**说明** 

任务分析前，需创建ComMemory分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看组件树和组件信息

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/RCjHYM_PSMKBZDDgwVuMoQ/zh-cn_image_0000002731381907.png "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/VjeQ5HWYSySh-ulB7Wih0A/zh-cn_image_0000002701822608.png "点击放大")
2. 在ArkUI Inspector中查看组件树。26.0.0版本新增Show Free-Node Components。

   默认勾选**Show Component Size**和**Show Free-Node Components**，Show Component Size显示各组件的内存占用情况，Show Free-Node Components显示游离组件（未在组件树上的组件）。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/XtoSdUy0S_aRVk48MwcTXw/zh-cn_image_0000002731381913.png "点击放大")，勾选**Show Recursive Size**，显示各组件为根的子树的内存占用情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/TLhKzbnUSsmTKcOyhNzsFA/zh-cn_image_0000002701662696.png)
3. 在ArkUI Inspector中查看组件的信息。
   * 在ArkUI Inspector的**Memory** >**Statistics**中，查看组件的内存统计信息。
     + Current：当前组件ArkTS内存和Native内存的占用情况。
     + ArkTS：当前组件对应的ArkTS堆快照对象的[Retained Size](ide-snapshot-basic-operations.md#li1323381634912)。
     + Native：当前组件新增占用的Native内存。
     + Subtree：当前组件及其子组件的Current内存之和。
     + nativeCount：当前组件存活的Native分配内存个数。
     + arktsCount：当前组件的ArkTS堆快照对象个数。
     + recursive：递归统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/slH9Ma7bS2qzUOpOyt152A/zh-cn_image_0000002701662692.png "点击放大")
   * 在ArkUI Inspector的**Memory** > **Details**中，点击Details中任一项后，打开DevEco Profiler查看显示组件的详情。
     + ShowAllocationDetail：显示当前组件的Allocation详情。
     + ShowSnapshotDetail：显示当前组件的Snapshot详情，系统组件不显示该项。
     + ShowRecursiveAllocationDetail：显示当前组件及其子组件的Allocation详情。
     + ShowRecursiveSnapshotDetail：显示当前组件及其子组件的Snapshot详情。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/J4NvLEWWSMKcS72Sxnt8OQ/zh-cn_image_0000002701822612.png "点击放大")
   * 在ArkUI Inspector的**Memory** > **State****s**中，查看UI组件的状态变量内存。

     memory字段表示该状态变量在对应组件的ArkTS堆快照中的Retained Size，更多请参考[查看UI组件的状态变量](ide-arkui-inspector.md#section19923158103412)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/KJMK2-TfSzKpCuubrISE7Q/zh-cn_image_0000002731541881.png)
4. 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cWHuoOBpRAeTUnRCTLBoLw/zh-cn_image_0000002701662688.png)可以将包含内存信息的组件树快照导出到本地。

## .arkli文件对比

从26.0.0版本开始，支持对比.arkli文件，通过对比快速定位异常增多的组件。

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/csxEb_mhQourjyh5OdRPig/zh-cn_image_0000002701822616.png "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/WLTD8EPiTBmBKTev_u612A/zh-cn_image_0000002731541889.png "点击放大")
2. 当前打开的.arkli文件作为base文件，在Component Tree下拉框选择的.arkli文件作为Target文件，查看两个.arkli文件的比较结果，从比较结果可查看：新增组件（绿色，如Column）、删除组件（红色，如NavBar）、游离组件（灰色，如JsView），及其子组件新增（绿色，如+1576）和删除个数（红色，如-8）。点击异常增多的组件，在右侧属性面板展示组件所在代码文件，点击可跳转至具体代码。

   **说明** 

   Target文件需要先点击**Open**按钮在ArkUI Inspector中打开，否则在下拉框中选不到。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/j71iGhJSTAqY90O6flMxCA/zh-cn_image_0000002731541885.png)
