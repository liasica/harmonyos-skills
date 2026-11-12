---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording
title: 性能问题定位：深度录制
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 使用Profiler进行性能调优 > 性能问题定位：深度录制
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:99e630091fcd4770af0ceaeb0c5f8053f06fa8726b4366c59ac03a59ca53ab22
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/MSlFinXjSN6uaQ5k-b-ogA/zh-cn_image_0000002808766391.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=881A643CD37F520BBEA05179760295DF90BED1E1905634AC8C648CE75CA5E21E)：在设备列表中选择设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/vrCdvPS0T7qn1KxTYDGd8g/zh-cn_image_0000002808886471.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=07DA566224A26BCD4C88358C268E6C3C098C43500B56458152DA9BB18272E907)：在进程列表中选择要调测的应用（可以是正在运行的应用，也可以是已安装但未启动的应用）。从26.0.0版本开始，支持将前台应用展示在进程列表中Running Applications的最上方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/kcJ2yAdvTAK-okYnDpvzeg/zh-cn_image_0000002808766397.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7DF4319D370B0FA84F9BEEEEB26DCD2BE33428E748C8F8301D883E34BACB842)：在主界面的新建任务区域，单击要创建的场景调优分析任务类型，并单击“Create Session”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/T2ls1IYiS3uNT-ZeSSNDyg/zh-cn_image_0000002808766395.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=C39BF928F53AAE151F946C776B78CCAF8153948F18E09FB6A6A405C54A98151A "点击放大")
2. 配置并确认会话环境。在录制详情区域，工具控制栏上有很多小图标，鼠标放上去会有一些功能提示，可以添加一些录制选项，各泳道区域也有下拉框选项，下拉选择不同的设置可以调整录制功能。

   支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/t6kWjj2pQTmqojfnp4AfVw/zh-cn_image_0000002808766399.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D27D9929DEFC6982690C86D864DBE653CC2DEA7D33E00F397F106146A7C6A793 "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qNCN47HATiGeDX2kaC_TQQ/zh-cn_image_0000002808886475.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=86DEC725426888E81C90BA8A86DAA3649E641A70021909DDC0BEC79F20C72CD4)
3. 启动录制，复现性能劣化场景。

   单击任务窗口左上角的 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/OWASvrq1TvSboq5940G9hw/zh-cn_image_0000002779566810.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=A686328DB543CD65365B47B67BFA50804B8FFB605A2851D36DFFE59FF1BA95CD)或左侧的任务列表中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Ue1YqQruTpGGuUU0JlKCHQ/zh-cn_image_0000002808886479.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=44EE4653AB8691B713C0F914F460F4F9AD03401AE5511DDB76C417B870D93238)，启动录制。在调优设备操作APP，执行要验证的操作，等待任务状态由“initializing”变为“recording”。录制过程中整个DevEco Profiler不能再点击其他的模板进行操作，如果想录制其他模板可以结束本次录制重新选择其他模板开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/U_4pYOo-RNKZKpROkA4z1w/zh-cn_image_0000002779406838.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=D40B1B95F273B6C465C2239D22F9BE261AD3122157CA36BABE54E8A47B527D2D "点击放大")
4. 性能劣化场景完成，停止录制。

   单击停止按钮 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/gLIQX6rjRH6VKvZemrAFFA/zh-cn_image_0000002779566814.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=21E8953EB4B46925F2A10E99F4EC07F2F43EB8149527BA4829C0C7A05FD482DA)，进入数据解析阶段，泳道任务状态由“analyzing”变为“rendering”时解析结束，右侧调优详情区域显示具体调优内容。解析过程可能包含大量的数据，请耐心等待解析完成。

   **说明** 

   若录制结束后，ArkTS Callstack、Callstack、All Heap & Anonymous VM、All Heap、All Anonymous VM、ArkTS Allocation等泳道显示No Data，在泳道名称处可将光标悬浮于三角告警图标处，查看泳道报错的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ftOYE-sCT0qzK9AkYgZM0A/zh-cn_image_0000002808886477.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=3223307D08C435CC8A96E8B39250216DAB8806D711B106E09224763266AF38E1 "点击放大")
