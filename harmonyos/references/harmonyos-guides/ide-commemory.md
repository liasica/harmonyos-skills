---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory
title: UI组件内存：ComMemory分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > UI组件内存：ComMemory分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0505311190346596d49de4321152c722f764f8e7d46770834129acc99d32d08b
---

## 功能介绍

从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

ComMemory模板支持的泳道包括：Memory、ArkUI Snapshot、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory。本文介绍ArkUI Snapshot泳道，其他泳道的详细信息请参考对应模板内容。

* Memory、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory泳道的介绍请参考[基础内存：Allocation分析](ide-insight-session-allocations.md)。
* ArkTS Snapshot泳道的介绍请参考[内存泄漏：Snapshot分析](ide-insight-session-snapshot.md)。

**说明** 

任务分析前，需创建ComMemory分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看组件树和组件信息

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/_uK9hF7jSq-MGoKtBAYhcg/zh-cn_image_0000002808766181.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=15D98ACD2A8FCE540CD406CC9FF57B203B08A17E0F9CD99B6890B9B6C3131E8F "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/xTUNfOWiTzq5fWsG2fOzMw/zh-cn_image_0000002808766175.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE7FB1778FBB538BD8CD5AEA4513F8C99DC8A06DF5280DC9D5AADF59E0103845 "点击放大")
2. 在ArkUI Inspector中查看组件树。26.0.0版本新增Show Free-Node Components。

   默认勾选**Show Component Size**和**Show Free-Node Components**，Show Component Size显示各组件的内存占用情况，Show Free-Node Components显示游离组件（未在组件树上的组件）。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/OulTbsacR8-ut8fWe1Yt7g/zh-cn_image_0000002779406606.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEB4F5503DC8978D1100137CFDE81700261BE87D6730D2BCD94527D446108C13 "点击放大")，勾选**Show Recursive Size**，显示各组件为根的子树的内存占用情况。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/PR4TsNy6Ryu3nF1UXEsb9A/zh-cn_image_0000002779566590.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D25FED73F6E25CE16523B4954E7C736DE2D6802A8C3D1C2420E18F35FCDE6383)
3. 在ArkUI Inspector中查看组件的信息。
   * 在ArkUI Inspector的**Memory** >**Statistics**中，查看组件的内存统计信息。
     + Current：当前组件ArkTS内存和Native内存的占用情况。
     + ArkTS：当前组件对应的ArkTS堆快照对象的[Retained Size](ide-snapshot-basic-operations.md#li1323381634912)。
     + Native：当前组件新增占用的Native内存。
     + Subtree：当前组件及其子组件的Current内存之和。
     + nativeCount：当前组件存活的Native分配内存个数。
     + arktsCount：当前组件的ArkTS堆快照对象个数。
     + recursive：递归统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/bW0svWeFShWk2-s3G5dyxA/zh-cn_image_0000002779406610.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F7ADA659882E8AAD7043EC3DBC4509BF1084798B861E419C6FE32390CF5CFC6 "点击放大")
   * 在ArkUI Inspector的**Memory** > **Details**中，点击Details中任一项后，打开DevEco Profiler查看显示组件的详情。
     + ShowAllocationDetail：显示当前组件的Allocation详情。
     + ShowSnapshotDetail：显示当前组件的Snapshot详情，系统组件不显示该项。
     + ShowRecursiveAllocationDetail：显示当前组件及其子组件的Allocation详情。
     + ShowRecursiveSnapshotDetail：显示当前组件及其子组件的Snapshot详情。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/QTVZblltQAmt-EZZSwJyGA/zh-cn_image_0000002808886259.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D02B206C02E0D3BB2D55556EA3965FE09EA4B04F392A1FE594957A2EA0D52EAE "点击放大")
   * 在ArkUI Inspector的**Memory** > **State****s**中，查看UI组件的状态变量内存。

     memory字段表示该状态变量在对应组件的ArkTS堆快照中的Retained Size，更多请参考[查看UI组件的状态变量](ide-arkui-inspector.md#section19923158103412)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/C8QHYdNDT42AY2jTUY2eOQ/zh-cn_image_0000002779406614.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCBEFC64C672567C7DAA21F1D09B0FE31D3D6BA0F1714AFB96992D9BDBBE826A)
4. 在中间栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/oPjfp_VGRqGtkooMfA640w/zh-cn_image_0000002779566586.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=4326AA2F066ECAE5CBC8610A1AB5A8711AB020E5C8AB639CA4AF01385BBF2A50)可以将包含内存信息的组件树快照导出到本地。

## .arkli文件对比

从26.0.0版本开始，支持对比.arkli文件，通过对比快速定位异常增多的组件。

1. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/frRxf7u2TJW7cOoDFlnuIQ/zh-cn_image_0000002779406620.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=20A1CAE486D3CDB47B9D59840EA8587EE3090F36FF946F127CE5E670ADEB6E8B "点击放大")启动一次快照，一次快照完成后会在**ArkUI Snapshot**泳道出现紫色区块。

   **Details**区域显示当前快照的详细信息，点击**Open**，将在[ArkUI Inspector](ide-arkui-inspector.md)中打开相应的.arkli文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/8M7PxWk5ROObg5sxzMnW2g/zh-cn_image_0000002808886243.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DC9D0E73F568D4E1FE44EBCED65875554F89778B00E0B0463D08E6D74964E4A "点击放大")
2. 当前打开的.arkli文件作为base文件，在Component Tree下拉框选择的.arkli文件作为Target文件，查看两个.arkli文件的比较结果，从比较结果可查看：新增组件（绿色，如Column）、删除组件（红色，如NavBar）、游离组件（灰色，如JsView），及其子组件新增（绿色，如+1576）和删除个数（红色，如-8）。点击异常增多的组件，在右侧属性面板展示组件所在代码文件，点击可跳转至具体代码。

   **说明** 

   Target文件需要先点击**Open**按钮在ArkUI Inspector中打开，否则在下拉框中选不到。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/OJSbnBkNRmqkNSoVMJswLw/zh-cn_image_0000002779566594.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B16D0150C4715F78120629235A0A9DB8A8423FD58FECAE42D3E5A5BF162C8401)
