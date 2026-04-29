---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ff766118a474be59d8e30934076aa7bd867c23e612e4976b7dd225bd045babf
---

## 创建深度分析任务并进行录制

开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景：

* Frame：主要用于深度分析应用/元服务的卡顿丢帧原因。
* Launch：主要用于分析应用/元服务的启动耗时，分析启动周期各阶段的耗时情况、核心线程的运行情况等，协助开发者识别启动瓶颈。
* Snapshot：支持多次拍摄ArkTS堆内存快照，分析单个内存快照或多个内存快照之间的差异，定位ArkTS的内存问题。
* Allocation：主要用于应用/元服务内存资源占用情况的分析，可深度采集内存相关数据，直观呈现不同分类的内存趋势，提供内存实例分配的调用栈记录，深入分析内存问题。
* ArkUI：主要用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。
* Energy：主要用于应用/元服务的能耗异常分析。
* ArkWeb：主要用于定位web应用加载和丢帧问题。
* Network: 主要用于定位http协议栈网络信息诊断，用于网络请求分段耗时分析。
* Concurrency：主要用于显示并行并发应用的实际运行情况，用于帮助优化并行并发代码。
* GPU：主要识别GPU利用率低以及执行图形和计算工作负载性能瓶颈的根本原因。
* Time：主要用于改进函数执行效率的分析，深度录制函数调用栈及每帧耗时等相关运行数据，并完整展现ArkTS到Native的跨语言调用栈，支撑Native API典型问题分析。
* CPU：通过深度采集CPU内核相关数据，直观地呈现出当前选择调优应用/元服务进程的CPU使用率、CPU各核心时间片调度信息、CPU各核心频率信息、CPU各核心使用率信息、系统各进程的CPU使用情况、线程状态及Trace信息等。

1. 选择场景模板，创建会话：

   新建任务的入口，DevEco Profiler提供Frame、Launch、Snapshot、Allocation、ArkUI、Energy、ArkWeb、Network、Concurrency、GPU、Time、CPU场景化分析任务类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Iij1Bs_hSHSayFoJ3XTyug/zh-cn_image_0000002561832891.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=D55D10BF5651B91F7934E34FD1A72D098EF757ACBC614F97B8B12541ED6981D1)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/RNHH70mDTmeUKQQcTRSkkQ/zh-cn_image_0000002561752887.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=82B4317B80C2B07EF30CFA0B450F40367F5AFB947BC3BFF299E0E2F5B5764A81)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/cRgvJGWbSUSQEEdvNepwAg/zh-cn_image_0000002530752948.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=DC4C6D0E556BCF6BA3161C1B5012929743F664DA81DEC5BB67289F6DF410641E)：在DevEco Profiler主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。创建后的分析任务，将显示在界面左侧的任务列表中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/N6jaE9aiTB68G0Rm1LVumg/zh-cn_image_0000002561752893.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=3DEB2DAE3E8FB3456853BC161B91AD060DB7BC126F6E87BEF7D934A4E23C691D)：调优详情，显示具体的调优内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/eN0WIWYWScim2e4tW7dbew/zh-cn_image_0000002530752954.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=E396E9F203B5DE6347A3F4972167B5ED6BD97D56B6104E2FB44A94EADEB61EAC "点击放大")
2. 配置并确认会话环境：

   在右边录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/EuBRbp_CTNqKcJxgAGmhEg/zh-cn_image_0000002530912966.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=5A489054F5090653137B962B2324880FF9FC163DB12591951061FA9A1B77AA7D)
3. 启动录制，复现性能劣化场景：

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ppftK55oR8CJrxw1AOeavQ/zh-cn_image_0000002561752897.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=ABFB3D71FC97F522AC690E60967EE013D2766F734558521D9E361A58CAA0C55F)，启动录制，也可以选择左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/nctKCubfQd6zSB5iVr3zCA/zh-cn_image_0000002561752903.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=558760B848E9F764404B803D96D8CA3FCD0FD6B7ACAAFF89EA1DC1EA9C7D0F32)，启动录制后，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Q2glmgXQT_uH7g5p9eV_xw/zh-cn_image_0000002530912946.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=FCDFDC762B4D1781CC0B1568C9DDAFECD105D3BCF611CD14AA721FC099E1C2BD "点击放大")
4. 录制场景结束，停止录制：

   在调优设备侧操作APP，执行要验证的操作，复现应用性能问题。单击该任务的停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Xw5Kz2J4QjKMiDp3mZzwsg/zh-cn_image_0000002530752968.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=FE896EE0F2629E23C1130996BFB2C3F3E80289565A941205EC2AF2D500AB05B4)，进入数据解析阶段，所有泳道任务状态由“analyzing”变为“rendering”，解析结束，右侧调优详情区域显示具体调优内容，解析过程可能包含大量的数据，需要等待一段时间，请耐心等待解析完成。

   说明

   若录制结束后，ArkTS Callstack/Callstack/Native Allocation/ArkTS Allocation泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/dE0MF9xuQLCjmVBygE3-Qw/zh-cn_image_0000002530912958.png?HW-CC-KV=V1&HW-CC-Date=20260429T054729Z&HW-CC-Expire=86400&HW-CC-Sign=8A82EBC45F9ACE5CA7985CD49342F1BF2942FD24DBAFAB64B58BA19436794449)
