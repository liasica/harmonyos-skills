---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:29223090cbef75f7fa757038b8c58b36658c3f4231247662c132f222d434ae0c
---

本案例介绍如何判断应用存在Native内存泄漏。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/YW-6TUloSyONTSel81h8Rg/zh-cn_image_0000002701662668.png "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/D8UULxKISvOFU_LNlJUxUg/zh-cn_image_0000002701662662.png)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/0a-D_4B9TOC50bqANJ68tA/zh-cn_image_0000002701662664.png "点击放大")即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4imMfxBNQHSSvtOxOt3zvg/zh-cn_image_0000002731541859.png "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/FRR2sQJzQvWaH_8Ku7JEtQ/zh-cn_image_0000002731381887.png "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/nD_dot2WR2WJucpklsHkfQ/zh-cn_image_0000002731541847.png "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/WUKP2ai7QI2S9Q-vhdV9tQ/zh-cn_image_0000002731381875.png "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Va5Y3dRaQVyMYbldVAccrA/zh-cn_image_0000002701662658.png "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/NzE1EXczQ9mYbOLA7TneqA/zh-cn_image_0000002701822576.png "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/TDz-t48_TFuPgFdn4Lr0ew/zh-cn_image_0000002731381883.png "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/wxawtidSTcig5oTfuI7nIA/zh-cn_image_0000002731381877.png "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/jMrjqeXNRduchf4y8RjITg/zh-cn_image_0000002701822572.png "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ZCq5J39_TxSIeuhVgr8vqA/zh-cn_image_0000002731381881.png "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/2bevbH3rQBibc54pEkkStQ/zh-cn_image_0000002701822580.png "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/joxJ8kx0TwqZIxl2JQO0tg/zh-cn_image_0000002731541855.png "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。
