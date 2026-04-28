---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case
title: 案例：Native内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 案例：Native内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0cfeda23d2a4f8a5c8cc344b41dec340d3818834245a2ab704076763295c5aad
---

本案例介绍如何判断应用存在Native内存泄漏。

DevEco Studio 6.1.0 Beta1以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

DevEco Studio 6.1.0 Beta1及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。

   监控Memory用到变化。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/1eN860u4SQGxWKxd1HkCjA/zh-cn_image_0000002530752708.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=492732F222F333BB488AE3E72C17F136267643F7C4EF30E056F979A53518E714 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   说明

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/4CPROJ2HS42g8KyIsq2gag/zh-cn_image_0000002530912718.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=FE0D76B09982E47380C0949B64A25277E5B20F0582958E0C6D53C21DD4B923CD)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/3e8DwCLmTEaNFvCGEX46gg/zh-cn_image_0000002561752653.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=A43E15302014FB0645E49308562D210DEA9EC2C5A53CC905DD7381730A7C9CEF)即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/-LU7KUF4Rai3qN2gfJ2n6g/zh-cn_image_0000002530752718.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=6C2E053867E837BDF01DEE876F3388D3537CB419CEF3CE55D9EAB194AE5DD5D1 "点击放大")
7. 录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

   当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](ide-native-allocation-case.md#section776643810160)进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/0z1DDCY2QiW9dlXNbLAx4w/zh-cn_image_0000002530912732.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=0B7898E18537681698F44A1EF5531FF0DB5F43719653C7B7A79FAB05F34912B8 "点击放大")

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

### 录制模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YS-9Qq8mQYSkl5vV7SOmbQ/zh-cn_image_0000002530912730.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=76BB3162903906E2E289FBBBDEC864A279FDD28246605790316162E1535FBB68)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/bN44U-ViRkqw4cx803X3Xw/zh-cn_image_0000002530912720.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=A308BD596E13B248AFB1349242EBD43D66B6CB53CEE3D86802D1738C092DEACF "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/n0EUkXOwQnG7WHqpVF-EKw/zh-cn_image_0000002530912726.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=41CC88CEE40DAFB54C26833672F459928D15CAD9EB2DC7BE46011674C07F0B8D "点击放大")

### 分析Native数据

1. 框选All Heap中的Native Heap子泳道。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/9yc6-mBrTe6zXGj8vXG9Nw/zh-cn_image_0000002530912724.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=B78E857A29F6D30EA325FA3D3A5022D5C2CE8DA8D59A0E3EE40AAA5FDB59E997 "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/eFl79L2wR_---8fhMQXnrQ/zh-cn_image_0000002561752663.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=E17191B50864E64AADC9B4DB77B8788628E9A68F577E5AE314145A55AFB7B84A "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。

## 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   说明

   如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/m53vPIPBS1-96bxN2gqFrQ/zh-cn_image_0000002561832631.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=388FD277A004B1CD539CEB78780604712EE7090306A5B9CD8DBE1C8081C63F6E)按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/butmNSaiQSe13EuLRUe0tA/zh-cn_image_0000002561832633.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=9B20A06A6F18321D01D843F781A2641739345DBD03B49683AE3EF6BEB86E23AA "点击放大")
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

   说明

   默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/MPMwdPkkTaqzPMRHrX8-iw/zh-cn_image_0000002530752722.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=9A5A564BBEBDE03BAB196A071F2D0E26F1CF59311E9DF2C5A70312266ECD9B8B "点击放大")

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/6aOgjJ8fQEGZED5ASz0BEA/zh-cn_image_0000002530912712.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=4668166EE6F927686C23D44EC66441EB0BF16E641550C8CF1B6EB756A4D9240D "点击放大")
3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/NpeSM7m9Tv2nKuHj-9MO-A/zh-cn_image_0000002561832641.png?HW-CC-KV=V1&HW-CC-Date=20260427T235733Z&HW-CC-Expire=86400&HW-CC-Sign=D0BFAD42C37DC53F629435A6C12FEEAD3C6AB35291AC76FB6055FF1241E84845 "点击放大")
4. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

   说明

   * Category中亮色代表开发者调用栈，灰色代表系统调用栈。
   * 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](ide-profiler-data.md#section11376118192614)）。
