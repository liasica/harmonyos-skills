---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-9
title: ArkUI页面加载慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面加载慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:774f110745bed94107cdd75f2c8ac87e54cedf7bc18902f77bda67051ea9da5c
---

## 问题现象

用户在点击应用查看详情页面时，有时会遇到较长的等待时间，存在页面加载慢的问题。

## 背景知识

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* [Smartperf-Host](https://gitcode.com/openharmony-sig/smartperf)是一款深入挖掘数据、细粒度地展示数据的性能功耗调优工具，旨在为开发者提供一套性能调优平台，支持对CPU调度、频点、进程线程时间片、堆内存、帧率等数据进行采集和展示，展示方式为泳道图，支持GUI（图形用户界面）操作进行详细数据分析。

  页面加载相关Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:DispatchTouchEvent 位置 type=1 | 应用收到点击离手的事件 |
  | H:ABILITY\_OR\_PAGE\_SWITCH | 页面切换过程 |
  | H:HttpRequestInner | http请求 |
  | H:CustomNode:BuildItem[组件名][self:组件ID][parent:父组件ID] | 构建自定义组件 |
  | H:CustomNodeBase:Destroy[组件名] | 自定义组件销毁 |
  | H:CreateTaskMeasure[组件名][self:组件ID][parent:父组件ID] | 创建组件的测量任务，确定组件的宽高 |
* 在日志中搜索关键字应用包名/NETSTACK可以看到应用发起http网络请求时的耗时情况，其中的参数含义为：

  **size**：上传或者下载的数据大小（byte）。

  **dns**：域名解析耗时，单位：ms。

  **connect**：TCP握手耗时，单位：ms。

  **TLS**：TLS握手（加密鉴权）耗时，单位：ms。

  **firstSend**：从加密鉴权结束到传输即将开始的耗时，单位：ms。

  **firstRecv**：从传输开始到第一个字节被接收的耗时，单位：ms。

  **total**：总耗时，单位：ms。

  分析问题时首先确认total值在问题反馈的总耗时占比是否较多，如总耗时达到秒级，对用户体验就会有较大影响，然后看耗时主要集中在dns、connect、TLS、firstSend、firstRecv哪一部分，size值是否过大（比如图片正常资源大小为KB，几MB的图片下载耗时较多）。

## 问题定位

以打开某新闻类应用的新闻信息过程中，显示加载时间长问题为例，定位过程如下：

1. 点击页面内容开始加载新页面后，长时间显示加载页，使用ArkUI Inspector工具抓取加载过程的布局，发现加载页是一个Loading组件。当该加载页消失后会显示出应用新闻详情页，因此该加载流程的起始点为手指离开屏幕、加载页显示，结束点为加载页消失。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/E5g7d-ZLQfSW0E6E0VZjlQ/zh-cn_image_0000002658794341.png "点击放大")
2. 在Trace中搜索加载页创建、销毁或完成加载的Trace关键字来确定问题分析的范围。

   首先搜索创建Loading组件的Trace关键字H:CustomNode:BuildItem[Loading]，可看到应用在收到手指离开屏幕的事件中加载了DetailPage详情页面，之后创建了Loading组件显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3cIHgHQoTlSfEPqYvpgkhQ/zh-cn_image_0000002628554974.png "点击放大")

   然后搜索销毁Loading组件的Trace关键字H:CustomNodeBase:Destroy[Loading]，最终划定的分析范围如下图所示。可看到应用在加载详情页面时，会触发页面跳转动画，然后发起http请求从云侧获取详情页的相关数据，最后将详情页面内容刷新显示出来，移除加载页，整体耗时1.0s。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/B7B1ZuKETTyUDF0tHz0S5g/zh-cn_image_0000002628395076.png "点击放大")

   或者搜索Loading组件完成加载的Trace关键字H:ViewPU.viewPropertyHasChanged Loading loadingComplete 1。划定的分析范围如下图所示。可看到应用在创建组件后会发起http请求从云侧获取详情页的相关数据，请求完成后loadingComplete状态值改变为1，整体耗时16.3s。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/rgaUJWc0RcewfZ1hx1uB-Q/zh-cn_image_0000002658914297.png "点击放大")
3. 从上述分析中，可看到页面加载完成耗时主要集中在http请求以及页面内容刷新。
   * http请求：在日志中搜索应用包名/NETSTACK关键字去分析http请求耗时，可看到耗时部分主要集中在服务器响应处理部分，服务器处理请求、数据传输耗时较多导致。

     ```shell
     07-08 20:44:39.812   34907-35118   C015B0/应用包名/NETSTACK  应用包名    I     [Http_exec.cpp:418] taskid=-2147483634, size:183, dns:0.170, connect:0.000, tls:0.000, firstSend:0.533, firstRecv:315.032, total:702.878, redirect:0.000, errCode:0, RespCode:200, HttpVer:3, method:GET, osErr:0
     ```
   * 页面内容刷新：通过查看该部分Trace关键字得知耗时集中在页面测量，主要在创建和测量ImageItem组件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/kTSiyVl7R8-K1lQ3983rIg/zh-cn_image_0000002658794343.png "点击放大")

     通过ArkUI Inspector查看发现是推荐阅读列表，数了下该列表一共有80个ImageItem。ImageItem是应用的自定义组件，用于显示一则新闻的概要信息，该组件个数较多导致应用页面测量确认组件宽高耗时较多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/T3RL-SEDRayp6aexXQCiAg/zh-cn_image_0000002628554976.png "点击放大")

## 分析结论

* 服务器响应、处理请求、传输数据耗时较长，导致http请求总耗时长。
* 应用页面布局包含的子组件数量过多，导致页面测量确认组件宽高耗时多。

## 修改建议

* 优化服务器侧处理逻辑来减少耗时。
* 将应用布局修改成[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)方式，提高页面加载的速度。
