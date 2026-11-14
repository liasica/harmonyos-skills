---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9b2826fe0b839be3402c3cbf8f58d78af48f32549e67d89afbc92e9ca1a747c5
---

## 功能介绍

开发者可针对不同的性能问题场景选择不同模式的分析任务，对应用/元服务进行深度分析。当前支持以下调优场景：

* Frame：主要用于深度分析应用/元服务的卡顿丢帧原因。
* Launch：主要用于分析应用/元服务的启动耗时，分析启动周期各阶段的耗时情况、核心线程的运行情况等，协助开发者识别启动瓶颈。
* Snapshot：支持多次拍摄ArkTS堆内存快照，分析单个内存快照或多个内存快照之间的差异，定位ArkTS的内存问题。
* Allocation：主要用于应用/元服务内存资源占用情况的分析，可深度采集内存相关数据，直观呈现不同分类的内存趋势，提供内存实例分配的调用栈记录，深入分析内存问题。
* ArkUI：主要用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。
* ComMemory：主要用于定位UI组件内存占用情况。
* Energy：主要用于应用/元服务的能耗异常分析。
* ArkWeb：主要用于定位web应用加载和丢帧问题。
* Network：主要用于定位http协议栈网络信息诊断，用于网络请求分段耗时分析。
* Concurrency：主要用于显示并行并发应用的实际运行情况，用于帮助优化并行并发代码。
* GPU：主要识别GPU利用率低以及执行图形和计算工作负载性能瓶颈的根本原因。
* Time：主要用于改进函数执行效率的分析，深度录制函数调用栈及每帧耗时等相关运行数据，并完整展现ArkTS到Native的跨语言调用栈，支撑Native API典型问题分析。
* CPU：通过深度采集CPU内核相关数据，直观地呈现出当前选择调优应用/元服务进程的CPU使用率、CPU各核心时间片调度信息、CPU各核心频率信息、CPU各核心使用率信息、系统各进程的CPU使用情况、线程状态及Trace信息等。
* FileSystem：可以结合应用逻辑IO和物理IO的读写耗时、整机（设备上所有应用）逻辑IO和物理IO的读写耗时等情况，定位IO耗时问题。

## 启动深度录制

1. [打开DevEco Profiler](ide-profiler.md)，选择场景模板，创建会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/JVbZO8vFT2WdvJOjVy5vKg/zh-cn_image_0000002808766391.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=90764969A2E619FC33DDE08EDAF2343A8B16B36A22ACA4F4D5D16052E8F0B9F0)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/AHdj3j5IQ1OjpfV2FDZXeQ/zh-cn_image_0000002808886471.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=58BB2C2C00276B08FD8A965EBFC9929977A92681BEA516586FD60685218C9AE7)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。从26.0.0版本开始，支持将前台应用展示在进程列表中Running Applications的最上方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/fOgZgj47TeaOPpzOQe8tsA/zh-cn_image_0000002808766397.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC141F38E458CCFB87C0908A315EC758EDE5A72ADA6724B4ADB241CF5F3310F3)：在主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/bwVpFAjARj-d2qtX8aGJJg/zh-cn_image_0000002808766395.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=D02015C7520373F8EFEE6575CC95AC6E2FAD44CB12C2206C012275BEB20BBA2B "点击放大")
2. 配置并确认会话环境。在录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Mnu2sAn6TYGQhC70KRDVBA/zh-cn_image_0000002808766399.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AE49EF84CE13B4322552F4F424C4EDF8D6F4C05455A852284A37A7E58F5C7D7 "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/tVriReqaRhaOZ2Bveka87w/zh-cn_image_0000002808886475.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=62AED35B83DA68AB119146613A0DB1BD6B0DEB4D7B6C2689FF0FAA12956C536C)
3. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/K8THJnctSvWoVMq55OIMqg/zh-cn_image_0000002779566810.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=A709CC2405F33365EA14743ABC8166385E4905CD9229D073A1B3752839625261)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/mYMua3OvTBqyjvu9pN49yw/zh-cn_image_0000002808886479.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BC80A4A5D5DC374E35FF657192202E0A0BEE3C10692C5F809279A25903F94C1)，启动录制。在调优设备操作APP，执行要验证的操作，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/byPBv514S8W4k6mE-h5LJg/zh-cn_image_0000002779406838.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ED0E15B8D3A88A3B7345B31C82B097BEAF6F58D60FB2E6C26798621AC4DB02A "点击放大")
4. 性能劣化场景完成，停止录制。

   单击停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/3EWRK0EJSz2DmyhE-MRkSQ/zh-cn_image_0000002779566814.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=15FB7F3059A02CA9123AFD890E8A639C13C8E432C7E8CCD64E23444049D29748)，进入数据解析阶段，泳道任务状态由“analyzing”变为“rendering”时解析结束，右侧调优详情区域显示具体调优内容。解析过程可能包含大量的数据，请耐心等待解析完成。

   **说明** 

   若录制结束后，ArkTS Callstack、Callstack、All Heap & Anonymous VM、All Heap、All Anonymous VM、ArkTS Allocation等泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/GTporxFiTCynki8z-gPXxA/zh-cn_image_0000002808886477.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=11DB9A7B837EAF35C44F66E59A6BD17A1FCEB3BDBD334AAEECD392F066EF043A "点击放大")
