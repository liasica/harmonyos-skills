---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bcb8881a4c0efb5734770ed17303623894ff9365d77ca3c571c61feec756b82
---

开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景：

* Frame：主要用于深度分析应用/元服务的卡顿丢帧原因。
* Launch：主要用于分析应用/元服务的启动耗时，分析启动周期各阶段的耗时情况、核心线程的运行情况等，协助开发者识别启动瓶颈。
* Snapshot：支持多次拍摄ArkTS堆内存快照，分析单个内存快照或多个内存快照之间的差异，定位ArkTS的内存问题。
* Allocation：主要用于应用/元服务内存资源占用情况的分析，可深度采集内存相关数据，直观呈现不同分类的内存趋势，提供内存实例分配的调用栈记录，深入分析内存问题。
* ArkUI：主要用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。
* ComMemory：主要用于定位UI组件内存占用情况。
* Energy：主要用于应用/元服务的能耗异常分析。
* ArkWeb：主要用于定位web应用加载和丢帧问题。
* Network: 主要用于定位http协议栈网络信息诊断，用于网络请求分段耗时分析。
* Concurrency：主要用于显示并行并发应用的实际运行情况，用于帮助优化并行并发代码。
* GPU：主要识别GPU利用率低以及执行图形和计算工作负载性能瓶颈的根本原因。
* Time：主要用于改进函数执行效率的分析，深度录制函数调用栈及每帧耗时等相关运行数据，并完整展现ArkTS到Native的跨语言调用栈，支撑Native API典型问题分析。
* CPU：通过深度采集CPU内核相关数据，直观地呈现出当前选择调优应用/元服务进程的CPU使用率、CPU各核心时间片调度信息、CPU各核心频率信息、CPU各核心使用率信息、系统各进程的CPU使用情况、线程状态及Trace信息等。
* FileSystem：可以结合应用逻辑IO和物理IO的读写耗时、整机（设备上所有应用）逻辑IO和物理IO的读写耗时等情况，定位IO耗时问题。

## 操作步骤

1. 打开DevEco Profiler，选择场景模板，创建会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/yF132upQSrS-Yr8a8LKieg/zh-cn_image_0000002701822716.png)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/pIiMocvNTFOyhHZYM5ntdA/zh-cn_image_0000002701662792.png)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。从26.0.0版本开始，支持将前台应用展示在进程列表中Running Applications的最上方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/4wlDjbsdTyWWWHSR2NBsJg/zh-cn_image_0000002701822718.png)：在主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/hGtp49EAQrOOd6PMieAVsQ/zh-cn_image_0000002701662800.png "点击放大")
2. 配置并确认会话环境。在录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/EvIW_zIWTgSg8KjuOioxOg/zh-cn_image_0000002731382021.png "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/s3RBVb87T4yXXFE_DjNWvA/zh-cn_image_0000002731541999.png)
3. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Lw0nJa7nSOyomGkomY-kTA/zh-cn_image_0000002701662796.png)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/1xQ39hVUQs-b3rFca7wi7w/zh-cn_image_0000002731382019.png)，启动录制。在调优设备操作APP，执行要验证的操作，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/IYPvINv9REKbZlE6xNCHSA/zh-cn_image_0000002731541993.png "点击放大")
4. 性能劣化场景完成，停止录制。

   单击停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/C7trDp52RqiAzH-2U1nwMQ/zh-cn_image_0000002731382025.png)，进入数据解析阶段，泳道任务状态由“analyzing”变为“rendering”时解析结束，右侧调优详情区域显示具体调优内容。解析过程可能包含大量的数据，请耐心等待解析完成。

   **说明** 

   若录制结束后，ArkTS Callstack、Callstack、All Heap & Anonymous VM、All Heap、All Anonymous VM、ArkTS Allocation等泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Aji8koo8TUaizqSqNgkrcA/zh-cn_image_0000002731541997.png "点击放大")
