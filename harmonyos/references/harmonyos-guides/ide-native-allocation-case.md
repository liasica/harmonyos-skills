---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:2fe9f56b483eef273121d075cdd0c513a3563af27c17fa74eebc4ed11db57b2b
---

本案例介绍如何判断应用存在Native内存泄漏。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/7XGCQcqeRm6orcLxOh0QEA/zh-cn_image_0000002779406502.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A1830AB9E4F5628D0C2AEB6915AFF66659E8D0F1008F9AE34D9D82F9F7ED4EE "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/OtoYeOklRJGNqxkldMSkOw/zh-cn_image_0000002808766053.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C5D8B45B2D2BA48B33A576186889AF7FCCCC3E645F4356649A6A600D7DB5140)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/bOI_7WTCQQyQHEOJLH5GVA/zh-cn_image_0000002779406492.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=26501C667942DA6174B54C21DBF1CF21BCE741DC2ACAC918F059B1BB1DD3925D "点击放大")即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/5gncKPgPRgSMm9m9opgkdw/zh-cn_image_0000002779566482.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=E852CC5F840181628C18FE6EE6256DCFB508206C2024CF558E3F42419668739E "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/AEuc4ftPTs6qi-6VfOxT_w/zh-cn_image_0000002808766069.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B96795125C6F85180E9AB11D0353F43DD299C48A25C48967B96FFDF755621725 "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/005aWld5RuKO-UHldn_NHg/zh-cn_image_0000002808886147.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=84B2392E7FFEB01D534E30FAC18BA1AC8E3E31576072108BDE25BAB53B4565C3 "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/GNuAraL7Q2yCHlmPI-PpaA/zh-cn_image_0000002808766059.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6C8C01AE50D73F367878BB9DD1660745A521A385A23A3E0B44A1E6B98AFD13B "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/YuM94R_4SXSgQl0RABiDbA/zh-cn_image_0000002808886143.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAA0192202200F14B15FE70CD7611561DBB709942B338E77FE0618BB6994F964 "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/B8eD72hKQoqFPq-sBAGBxw/zh-cn_image_0000002779566476.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=991B5F88AC420A4A80F87C8FA8947FBF0BF878740B49FD20A939ACD56DC8F5C9 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/iLrCNhn2RkuSuJxqw-4oXg/zh-cn_image_0000002808886137.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=702BEFD7EAA396CA51D3DF379C83C79EF3AA2A962119AAA2AC16CAC15E82D829 "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/a1gXvw2OS1Kgl81Ll88MLA/zh-cn_image_0000002779406486.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4230218911BABC0F5D0FD91A7F9E8430606EBE01A4170AC1C1062DEA023A8CA "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/rKXtBXYhRIaYfJOiVz5C6A/zh-cn_image_0000002808886127.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=1776BF90A533BA4A75568F8F665D2588495F7A4B0F00B2ABBAEC3E4101E767A5 "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/UM-b64FYTVumVaWh39vpRQ/zh-cn_image_0000002808886133.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=099B3E1E66E2358E752A54D1E80DE8F3EFE975ED8CB9CF80A85AE956C715FFFF "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/OXez2H6WSGeqajqKWimsKg/zh-cn_image_0000002779406488.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2B700AC84784F280E2B978B4AD4628BB19676647C6587237582C588EBE9F2DF "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7Cva0-gYSgaedFMSNBehSQ/zh-cn_image_0000002808766065.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=458356B683737C3F57D5C24420948A313D46C15AB20A580F83208C8EDC49155F "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。
