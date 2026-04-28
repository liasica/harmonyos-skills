---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9076d81853a0b17ba6001727d9e99fc17e51faa310540cbddcfd6e88d2badd7
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/oRgn1yOgS-OdyTjeBbxlMA/zh-cn_image_0000002561832891.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=B8B9837E730DDDCFEB64ED89EE9862EB6ABE1F32D4FE996AF5092CDF90BE9928)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/iaJyDo6NTHKFH7wbj1SoKw/zh-cn_image_0000002561752887.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=651FF6AC2C1FFA54272FB987E2767A3EA5D6F5563D23E46BE150BDDD2F8607A9)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/0tuXimdjSFO0XNnYqDdA7A/zh-cn_image_0000002530752948.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=688B16B16AAEF44E6B8EB327266AAC5CC4CE8805758CAF9DEF1B336919F17FC6)：在DevEco Profiler主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。创建后的分析任务，将显示在界面左侧的任务列表中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/pR4fgZAZTXu3SH7Z_oSsQQ/zh-cn_image_0000002561752893.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=6D038E8FD94CFBD7FE9A141A3F1B3ED7598200CCA11CD425C8A157A8749E10AB)：调优详情，显示具体的调优内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/KD03YNxbTcyHzKIGbqg7jQ/zh-cn_image_0000002530752954.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=D5F7A9D9D920F49AB5D68C37FBA5AE59A1F0BEA1213AC56A8F444EE2AD6AF5F8 "点击放大")
2. 配置并确认会话环境：

   在右边录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/xGi8_P0zQSCOjv5U0p9yqg/zh-cn_image_0000002530912966.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=0346FB2DC4C8494686B04911889A6754089652E335C6503FFB3B440C0267B918)
3. 启动录制，复现性能劣化场景：

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/A7_FcPsrSyioRMBGAbrqaA/zh-cn_image_0000002561752897.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=373296C7F5BD2AE4BF5C54AA0DC52B299B3DEB1CDEF57621C62D99DE65C054CA)，启动录制，也可以选择左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/wW1uCMqiRXu5UtBwBgy-pQ/zh-cn_image_0000002561752903.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=62538861A9BA167A964F4A956C0E7E80020E5FEB9D55D529602F0DBE62F6361C)，启动录制后，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Kl72qs90T4CiFy-OoV9xgQ/zh-cn_image_0000002530912946.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=DD80BC7F7E33798AE844C8EB469655D0C176208EB4F77546D906483E8FB99F20 "点击放大")
4. 录制场景结束，停止录制：

   在调优设备侧操作APP，执行要验证的操作，复现应用性能问题。单击该任务的停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/7r00y4V-TUCyKryM3tDk6g/zh-cn_image_0000002530752968.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=941BD79CAEE515B1C73DE2099F0061A83975B0C072AFE21EFF2EC64C309251EA)，进入数据解析阶段，所有泳道任务状态由“analyzing”变为“rendering”，解析结束，右侧调优详情区域显示具体调优内容，解析过程可能包含大量的数据，需要等待一段时间，请耐心等待解析完成。

   说明

   若录制结束后，ArkTS Callstack/Callstack/Native Allocation/ArkTS Allocation泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/yApJuwqUQmqqxvmpzdLdTQ/zh-cn_image_0000002530912958.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=A389431F2B5B0D542028B1464A9E840F3D5D21D711C59358F45F5E6178CF3BB7)
