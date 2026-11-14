---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory
title: UI组件内存：ComMemory分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > UI组件内存：ComMemory分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e926c2b3fc9b2080bc94e4505b8a3aa1e22610e4fbbaffac39c0339c37915089
---

## 功能介绍

从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

ComMemory模板支持的泳道包括：Memory、ArkUI Snapshot、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory。本文介绍ArkUI Snapshot泳道，其他泳道的详细信息请参考对应模板内容。

* Memory、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory泳道的介绍请参考[基础内存：Allocation分析](ide-insight-session-allocations.md)。
* ArkTS Snapshot泳道的介绍请参考[内存泄漏：Snapshot分析](ide-insight-session-snapshot.md)。

**说明** 

任务分析前，需创建ComMemory分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看组件树和组件信息

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/pFGb5M9eT-Suvilf85Ng0w/zh-cn_image_0000002808766181.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=515084330898334A69D9DF00E8B32FD11A21D19BA77409E2ECB71B3ADA70BAC7 "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/8mGyRt8mSU-rLdoorRfa7w/zh-cn_image_0000002808766175.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=BED6B24453142D191C5840D1A2726D7E89CA3214CE5EDD0870CB54BD2D107DD2 "点击放大")
2. 在ArkUI Inspector中查看组件树。26.0.0版本新增Show Free-Node Components。

   默认勾选**Show Component Size**和**Show Free-Node Components**，Show Component Size显示各组件的内存占用情况，Show Free-Node Components显示游离组件（未在组件树上的组件）。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/1jFBoSSxR2uHc5l8xxtSlw/zh-cn_image_0000002779406606.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AB2F89F9D30E991EC39190022D536A216B064332F044F4AB458BF3E407B0DAE "点击放大")，勾选**Show Recursive Size**，显示各组件为根的子树的内存占用情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/pMUQ8hc4QS2AOLGrtzP_Qg/zh-cn_image_0000002779566590.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7FE1360A9A642CC9555E3ED21FB63A6B782A6A6A33D314C9DD2AE27BC4671FF)
3. 在ArkUI Inspector中查看组件的信息。
   * 在ArkUI Inspector的**Memory** >**Statistics**中，查看组件的内存统计信息。
     + Current：当前组件ArkTS内存和Native内存的占用情况。
     + ArkTS：当前组件对应的ArkTS堆快照对象的[Retained Size](ide-snapshot-basic-operations.md#li1323381634912)。
     + Native：当前组件新增占用的Native内存。
     + Subtree：当前组件及其子组件的Current内存之和。
     + nativeCount：当前组件存活的Native分配内存个数。
     + arktsCount：当前组件的ArkTS堆快照对象个数。
     + recursive：递归统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/UN5egmgpTzizeSl1asUx_g/zh-cn_image_0000002779406610.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=25E2049BE693464080709D330D5D70C087DED885288ED6B73B2F178B500B4FF3 "点击放大")
   * 在ArkUI Inspector的**Memory** > **Details**中，点击Details中任一项后，打开DevEco Profiler查看显示组件的详情。
     + ShowAllocationDetail：显示当前组件的Allocation详情。
     + ShowSnapshotDetail：显示当前组件的Snapshot详情，系统组件不显示该项。
     + ShowRecursiveAllocationDetail：显示当前组件及其子组件的Allocation详情。
     + ShowRecursiveSnapshotDetail：显示当前组件及其子组件的Snapshot详情。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/p7xMHHXMSz2DbPNCZVCaYQ/zh-cn_image_0000002808886259.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4F1243044B388F2FE4E9FA82FF753677612E5FDBFD405EE57B7224D9BE363DC "点击放大")
   * 在ArkUI Inspector的**Memory** > **State****s**中，查看UI组件的状态变量内存。

     memory字段表示该状态变量在对应组件的ArkTS堆快照中的Retained Size，更多请参考[查看UI组件的状态变量](ide-arkui-inspector.md#section19923158103412)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/HPluu9nLS2axT5mdetd4vA/zh-cn_image_0000002779406614.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1010C643302EC564FD7F16DA0F0E4F494AAD046FB944950B4874FD4AC384B1F)
4. 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/5vGatyOXSxqFkCtCZdgrgg/zh-cn_image_0000002779566586.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F3D4846697FCC3F7BC0323A927EC3F27EA8CAF8CD91A59A8C808E27575D048B)可以将包含内存信息的组件树快照导出到本地。

## .arkli文件对比

从26.0.0版本开始，支持对比.arkli文件，通过对比快速定位异常增多的组件。

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/w1NhYDB5RWK0m-5H8zRFkA/zh-cn_image_0000002779406620.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=0229F0F82DB3E6422124790EBF641119D260F427B12D9AFAB68C15C23F30FDB2 "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Ye9KUfmxRleIZx-NTsc4yA/zh-cn_image_0000002808886243.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=726523CAB27FD68EBCA9E26BE2EB3DC65E439C8B1BD81F6BAB64A0C449B22C6D "点击放大")
2. 当前打开的.arkli文件作为base文件，在Component Tree下拉框选择的.arkli文件作为Target文件，查看两个.arkli文件的比较结果，从比较结果可查看：新增组件（绿色，如Column）、删除组件（红色，如NavBar）、游离组件（灰色，如JsView），及其子组件新增（绿色，如+1576）和删除个数（红色，如-8）。点击异常增多的组件，在右侧属性面板展示组件所在代码文件，点击可跳转至具体代码。

   **说明** 

   Target文件需要先点击**Open**按钮在ArkUI Inspector中打开，否则在下拉框中选不到。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/8EJXDEb1TsC9HVpXNaQZCg/zh-cn_image_0000002779566594.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE5DC7F30DC6FB70EB628F726361909B51F2147D1E1B2DE8FBB8A75110D2C011)
