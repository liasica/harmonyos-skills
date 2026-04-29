---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aeba191669f6557416cc150164fb76d2b1c663fbb824966766cee587b3ac04d
---

本案例介绍如何判断应用存在Native内存泄漏。

DevEco Studio 6.1.0 Beta1以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

DevEco Studio 6.1.0 Beta1及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。

   监控Memory用到变化。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/yfTEiVKZTzaXQzqNpIA4tQ/zh-cn_image_0000002530752708.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=B39C7C81A065A0878D65A7A047744D61CF5984786CF687F48690E5E555755DC5 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   说明

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/r4M9VmmtTuu-lGqJZEsazQ/zh-cn_image_0000002530912718.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=B6DB64E63887E7F4623D299A694335727434E752E399BFB6A199F36F837F6588)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Sr0Z_3sMTGGCqO-jVUEnfA/zh-cn_image_0000002561752653.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=62430CBBD99363C11DF7BFC3EAEE7504B66B911E29D231AB01D6ED031EDE085F)即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/BlPJlC6PQ9mS8tjdCStJoQ/zh-cn_image_0000002530752718.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=1ACC1D8B1CE6F25CE24F6A246CF908C06B4D52AD5DEE2E720A17C4A021B5AF5B "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/cA7wFxioTt6-VmWf875ykA/zh-cn_image_0000002530912732.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=0F92622849001772D7009B956A2FB6B7A779DA2FE5FF5E8B22117ACB2E65141C "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/kfiu7EOpTNq0eGQ0xBYJhA/zh-cn_image_0000002530912730.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=06BB90B49C73024E18F1AD0DAA04A78B621FA69AB89FAF65FF4225EF889F8C81)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/R6K3f0-dSoSG_b1Wr6hGzw/zh-cn_image_0000002530912720.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=EF80CCC18F2A72A8CB6D3E3D055C23F992081862B21528A4DEC75F4E52E0D0F3 "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ok_k88-sQQqrfa5-XlNW-g/zh-cn_image_0000002530912726.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=2DF780FA02570114253B4CD103F0CBFD430CEED7082656B4E67F046E5FE75C57 "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2djgNVS0SvqRq6RZicbL3A/zh-cn_image_0000002530912724.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=6021D7818B5612EAAE598AA8581D0CA8A84978B9A75F606FA88FD563375C74A9 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/UZwz3IOVR8CKB9bJpALDFQ/zh-cn_image_0000002561752663.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=AA7B87DADFF271F5E5F6299A05C994FE6985B65B52184CF06AA319F6EDF3F27D "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/pbanXBdaSYyz4Xp5y0J3DQ/zh-cn_image_0000002561832631.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=F6C6E867BA5A50852719323183D9C8C49232152DF8F073DF3BEDE15A2B988C1E)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/1ZVfvZevTZ-6DYwxvwliCg/zh-cn_image_0000002561832633.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=2B5DF60A8ECDCFE4168EE5DF867066EA7D278BF1A517DFF2D732EED8AF1DA42A "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/gNBPJaQDQYiGTOkW7t3kbQ/zh-cn_image_0000002530752722.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=D3CB59D2CE3A4C79A47D910057709375A322F943A2984AC87ABF91BD776AF9EA "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/A597oCmeTj6L4cEpKhKOig/zh-cn_image_0000002530912712.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=5AB3A256CAE18238DC1BA9AE65C8ED67C5C472338833014BA3096D6087A76A1E "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/w2bzINC_Rju3K52XKTozDA/zh-cn_image_0000002561832641.png?HW-CC-KV=V1&HW-CC-Date=20260429T054734Z&HW-CC-Expire=86400&HW-CC-Sign=091D26BFA87E187568F8A1F4FB48C718CDC405B23CDAF453A0B7C5A2D7E0763A "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。
