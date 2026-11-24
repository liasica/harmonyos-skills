---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9a5109566fb794ccf3817f1c2e58ecdf7895ed8ff70fc61e68e0b58ff574314f
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/UMo1p-3lR-qBQgGSUSgZkg/zh-cn_image_0000002808766391.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=64E304887C3087783B85D0364D73BB12D41527E3EFBA8EFD585114C9D3D18DD4)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Zqw8Ax3TTRya5V-je6Cy3A/zh-cn_image_0000002808886471.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3FC51AAAA7C66433AC2901187F587609F65BE66586CE45621500095A1B4BC07)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。从26.0.0版本开始，支持将前台应用展示在进程列表中Running Applications的最上方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/HNsnEa8ESteDf4OQ1m4soA/zh-cn_image_0000002808766397.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FF7975E8FC01F399FE3C4603926277C7C02B0ED02F33B6F9FC3D33F9A93C248)：在主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/QF_Y2X4GSuOZlH8HF8vslQ/zh-cn_image_0000002808766395.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D5CA3D4F0F2A4F715595FC5FB28E37C8389941F60E4C4678BA8300B245893C1 "点击放大")
2. 配置并确认会话环境。在录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/lf_S48MzTy-FdMhyumjyAg/zh-cn_image_0000002808766399.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5845BA26FE2EA74DB9AA1214B7ABB191D51E6DE3BFA9B17ED2485F938A80F2C8 "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/KSmmGA7QS3G27N5s1h70Kw/zh-cn_image_0000002808886475.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD7A88CD47ECCA65A36E9D3AA5F8FBE960A8FC7B251DEF40867B568DC5663FE4)
3. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/3LSzfex5TPWWPF8SBs1fsQ/zh-cn_image_0000002779566810.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5B58318A85AC8FD5E8048CAC2EA6E37912FEA0774098261A0379FAC3B537BCB)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ZgE1xVeXQ1u2fMEguRjU5A/zh-cn_image_0000002808886479.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=65B374F57326DAA3EF5D41408ED3CB0BEB7797A0D647A5CAD1E171306AB07956)，启动录制。在调优设备操作APP，执行要验证的操作，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/eL2eyErnTkKGf-qg0W99Ew/zh-cn_image_0000002779406838.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEFECCF130D0AFC614D7CCC7F8589AB900B969B6AD95F30A89CF8D339E92875E "点击放大")
4. 性能劣化场景完成，停止录制。

   单击停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/bCivdY4wQuKxbCM3pd_A3A/zh-cn_image_0000002779566814.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BDB505C68CE29FF053B7A28797A14066EBDA90F070AB81AE1C6383419201355)，进入数据解析阶段，泳道任务状态由“analyzing”变为“rendering”时解析结束，右侧调优详情区域显示具体调优内容。解析过程可能包含大量的数据，请耐心等待解析完成。

   **说明** 

   若录制结束后，ArkTS Callstack、Callstack、All Heap & Anonymous VM、All Heap、All Anonymous VM、ArkTS Allocation等泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/o0gqv0rSTim0Plwla7110A/zh-cn_image_0000002808886477.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A9C3BF2185B91A05BFF1B01704A0C584679A2ECB5D27B768329D651DF604BA6 "点击放大")
