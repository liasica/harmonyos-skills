---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:e5aacb0e9571a26a4f6a81f47f838fe7d5aba07f5ab5890dee89c46343edf2d6
---

本案例介绍如何判断应用存在Native内存泄漏。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/mexbxKVARp2QEp3VOnLjhA/zh-cn_image_0000002779406502.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA11ADCADFDBCD94167FAA2AE4DE1201892949E74DEFE4D89497DEF1A34CF265 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/Dk3h7sYyS2CXj7z-jOdTrg/zh-cn_image_0000002808766053.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA1665BCA5E4F5712EE4E296DA6AF027D4FE76E16CCF736A3FFD0FFEFB1981F1)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/gHl-Jk_XTTCFGNkHtFut9A/zh-cn_image_0000002779406492.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F8E4EA4DB392301F5049B38BCB8BD4928448D8B895407F55565D0BCEFAA128B "点击放大")即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/-IAfebWyS1GsJ_KN08h7Yw/zh-cn_image_0000002779566482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF2112A470868D540A93EA948486451CC6B60C706020BFD15B2EF505F53D5BAD "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/rO5eACYyQCWi3CEjd-c7TA/zh-cn_image_0000002808766069.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E61A66A618E34FB808CBBCDFA661B3D9CEB5CD5901BD066B21A0D3BC789786A8 "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/vpU5l0VVSPeNUHMCCvnmFQ/zh-cn_image_0000002808886147.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=47FF7F7539EB4C449969F188AEAD3E016CB280C1EAB24EF1E8560334AB2CBBC8 "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/PnSufxeYTd6a9kJUXYzYYw/zh-cn_image_0000002808766059.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=69D14E0941AD5210FF035E0764B59D434A2D1100AF2D8D16BF79846A5EF62A38 "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/JkQzRVQjSIGo6_KiX0a1Lw/zh-cn_image_0000002808886143.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B14ED649993E34E4C6ED6A441E0ABFD13F2665B8EACD0629E7BC01CBB8EBD47 "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/-YDel2-jRZG9oAu8-sBoew/zh-cn_image_0000002779566476.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A5AAA7E07ED05824F657CAB7710AC31DC6ABD6A19D79C1233CB9974E09DFBEE "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/lbZT4c51S8uoQPLj1guOdg/zh-cn_image_0000002808886137.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE57B9441C0E571A03E4F5FB1CC59954768AE78DC6E25882FB5F87EEB4B33E16 "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/y0-EaquyTg2bNC9Zoaekgw/zh-cn_image_0000002779406486.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBE1E2776FFC7A90537A55B63DC860271408EA6B6115524001AABEEF7A555E89 "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/RN3c2XSQTbeIqF4r1E8jTw/zh-cn_image_0000002808886127.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C2CEC693541059FBE65EA446942BDC16E4A96DB44E2ED7D618EA003AE53D3CD "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/CHMfZaHBT2mPdAiIiDYTXw/zh-cn_image_0000002808886133.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D40159ACE772AD8D0C172F783C6548512D4E8311952CCC50639D688F3D51DB71 "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/7RYHPENJRMuAmEwPmq1opQ/zh-cn_image_0000002779406488.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=444BD5B173311A6BF307CC640EFA801BE0F35CEBBEF1B209516C5847DA7AAE2D "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/BlvYkc1BSUKXAZhFRWtk9Q/zh-cn_image_0000002808766065.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0A8701E8800DB9925DE0913F5ECB95EEC9F8BDD209BB6B79BB6A6218327CE4D "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。
