---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:c1be58bac50b360b7d7475e39109731b23f72b6998bc9722811f1689b0f19f1c
---

本案例介绍如何判断应用存在Native内存泄漏。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

[6.1.0(23) Beta1](../harmonyos-releases/overview-610.md#section174491130173414)及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Ybni8TH9Swi4hfKOmrLsSA/zh-cn_image_0000002779406502.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF3F78AA22B7C1D4EB4F9B051FD7F28024F419A4A575D7934BDE058996FF51CC "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/TaE-5QDgTCGtX2wgx-PlZw/zh-cn_image_0000002808766053.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=7497AA15534BA0AB4031BA1617A3C673E79085582D0E699EF8BF34BC23E4724B)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/H8wV52QjTJ-x_KIFrF9MmA/zh-cn_image_0000002779406492.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=90B17F1179D55A37840A01C521A495F97BCA75E6B418206BB2EF4D0E6547C3C0 "点击放大")即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/0kOdoEr6T6WsawWBHgP0_Q/zh-cn_image_0000002779566482.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=52A8832F5B8011D140FA5807908FCA78B9CF932F965A3617203E5A26511D2E60 "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/KJYbLYwBSVSlo3MolLF9Og/zh-cn_image_0000002808766069.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB71A65C2654DCCC682A93BF123F4F0E8F00A6AD228093D6B7D0D4BCC4BA2498 "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/m7WkSS4MTRisjpY2HGkmFg/zh-cn_image_0000002808886147.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=39C0A0EC04A6F44FB32E5CB0A36CB63A1F905D0F291DB4A3502A0099DBE311AB "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/yzCfg8XoTdi8Qh1mJ54NaQ/zh-cn_image_0000002808766059.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=81F5903356D9B92871EF29EDD86E33BB3F15D0005485565BEA90CCF5510022C4 "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/tOU8op3xTBqMcMxjXcW5CQ/zh-cn_image_0000002808886143.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA93A2A41ED6A0DA95AC9663355B621CB26782B24A0323CD2D96369BBB1557DA "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/MnX-shIhTnONtmSz7Z7apg/zh-cn_image_0000002779566476.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5555D4D118BEC1CF1D2985BB37EE6C40363AB8ABE1AA6E68656B4E548B157A6 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/07CxD21wQZaUkJzwJXA3dQ/zh-cn_image_0000002808886137.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A9EB2B38BDF8DA34187FC4CF85740CAE4D7A068E4A4C278EF180D695C0A6E47 "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   **说明** 

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/IMinRI-5RjO0flulzRx47Q/zh-cn_image_0000002779406486.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DD5616F36458FA670216E00F0203E7845D0B002BEC01ACDB0FE01B3E397A532 "点击放大")按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OE8zeGVBQrOEHL8n15KCVA/zh-cn_image_0000002808886127.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D787CC3E521770727D2B287B6C9B08FBE7A0A8C00910A64C30BD1CB881869C0D "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   **说明** 

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/1aAPLk8TTgKjzDzpRS1zdQ/zh-cn_image_0000002808886133.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=78FE7D3E11A0B00513C683C52E85DA8411FDCDD4FCB16CAA9306A7177CB29CF2 "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2Ty8dFrmTxi_4lYYPLZC2w/zh-cn_image_0000002779406488.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6CDCB16B3052E2E3295128F8B0B626C051F6893DC5C98EF169A71967BF7AF3 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/el4H281OQsiA8Hq7FhE2rw/zh-cn_image_0000002808766065.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3DA209FEC174DEA8126A327F129DC559D0657DDFCC8AA1995E61EA4D57F4FFC "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   **说明** 

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

更多高频泄漏场景和Native内存泄漏分析案例请参考[开发态快速定位Native泄漏](../doccenter-app-quality/bpta-native-leak-in-develop.md)。
