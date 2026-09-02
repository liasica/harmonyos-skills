---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-5
title: ArkUI页面点击图片查看时加载缓慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面点击图片查看时加载缓慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b23a79f101ed09d21326e31c27ea4555175b91eb5184d47399c4762360a926d3
---

## 问题现象

图片是应用页面中常见的内容，会在应用页面中占用适当的空间。为了避免图片占用空间过大导致屏幕无法显示文字内容，同时能够查看到图片的细节，应用提供了点击图片放大查看图片细节的功能。

在点击图片查看时，通常期望能够更快地查看到图片细节，但在一些应用中，需要等待一段时间才能够看到放大后的图片，存在图片加载慢的问题。

## 背景知识

* [Image](../harmonyos-guides/arkts-graphics-display.md)：ArkUI提供的图片显示接口，常用于在应用中显示图片。其主要的参数为：

  | 参数名 | 说明 |
  | --- | --- |
  | src | 图片的数据源，支持本地图片和网络图片。 |
  | alt | 设置图片加载时显示的占位图。 |
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* 图片下载相关日志：
  1. 通过搜索NETSTACK日志关键字可以查看到应用通过http请求下载资源的耗时情况，其中的参数含义为：

     size：上传或者下载的数据大小（byte）。

     dns：域名解析耗时，单位：ms。

     connect：TCP握手耗时，单位：ms。

     tls：TLS握手（加密鉴权）耗时，单位：ms。

     firstSend：从加密鉴权结束到传输即将开始的耗时，单位：ms。

     firstRecv：从传输开始到第一个字节被接收的耗时，单位：ms。

     total：总耗时，单位：ms。
  2. 通过搜索Download image日志关键字可以查看图片下载的相关日志，其中ImageData length表示图片大小，单位为字节。
* DevEco Profiler [ArkUI分析](../harmonyos-guides/ide-arkui-analysis.md)：DevEco Profiler提供用于定位与页面布局相关的卡顿问题的分析工具，可用来查看组件测量绘制、状态变量更新的耗时情况。

  Trace关键字说明：

  | 关键字 | 说明 |
  | --- | --- |
  | H:DispatchTouchEvent id:X, pointX=XXX pointY=XXX type=1 | 应用收到手指离开屏幕的事件。 |
  | H:OnImageLoadSuccess[self:组件Id][src:图片来源] | 图片加载完成。 |
  | H:HttpRequestInner | http请求。 |
  | H:DownloadImageSuccess[src:图片来源] | 图片下载完成。 |
  | H:ABILITY\_OR\_PAGE\_SWITCH | 页面切换过程。 |
* 网络环境质量日志：

  可在日志中搜索关键字SignalPoll或chload|noise|rssi来判断网络环境质量。

  chload：通道占用比，能够体现WiFi信道的繁忙情况。chload值越高表示网络状态越差，chload值大于500时网络质量差，大于800时网络基本不可用。

  rssi：信号强度，-30表示信号很强，-80表示信号很弱。

  noise：-80为干扰环境，到-60以上就是强干扰。

  具体如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/kK9eP0TWQRWfzYMOyjsHrA/zh-cn_image_0000002658914273.png)

## 问题定位

1. 在日志中搜索SignalPoll查看chload、noise、rssi参数值判断网络环境质量，如chload值大于500或rssi值在-80左右或noise值大于-80，则网络环境质量较差，会导致图片加载慢。

   ```txt
   04-22 15:40:34.628  2443 32558 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-89,chload:841, ...
   04-22 15:40:35.647  2443 32558 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-89,chload:841, ...
   04-22 15:40:36.666  2443 31712 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-91,chload:880, ...
   04-22 15:40:37.688  2443 13198 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-91,chload:842, ...
   04-22 15:40:38.704  2443 32558 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-90,chload:830, ...
   04-22 15:40:39.722  2443 13198 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-57,noise:-88,chload:879, ...
   04-22 15:40:40.742  2443 32255 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-56,noise:-89,chload:882, ...
   04-22 15:40:41.757  2443 32558 I C01560/wifi_manager_service/StaStateMachine: SignalPoll,bssid:48:b2:**:**:**:22,ssid:Hua******est,networkId:44,band:2,freq:5805,rssi:-56,noise:-88,chload:866, ...
   ```
2. 如网络环境正常，使用DevEco Profiler ArkUI分析工具抓取点击图片到图片全屏显示完成的Trace信息，点击应用主线程泳道，在下方弹框中的Slice List页使用H:OnImageLoadSuccess来过滤图片加载完成的Trace信息，发现一共有7个Image组件加载图片资源完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/wxGNVwuCQgyn7dqI38GEJg/zh-cn_image_0000002658794319.png "点击放大")

   由于无法确认何时图片全屏显示完成，使用Ark Inspector查看全屏显示完成后的Image组件，发现该组件Id为5505，在右侧Attributes中的输入框输入src确认图片数据源为网络图片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/zSuuHLjETye5ic-e7agPpA/zh-cn_image_0000002628554954.png "点击放大")

   在Profiler上方搜索框中分别输入type=1和H:OnImageLoadSuccess[self:5505]找到点击图片、图片全屏显示完成的位置，如下图所示，两者时间间隔3.6s，页面切换过程400ms左右，可知点击图片后400ms切换到新页面，过了3.2s后图片才全屏显示完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/rq5uVMx7RTWzZoR32ofX0w/zh-cn_image_0000002628395054.png "点击放大")
3. 查看图片资源下载完成Trace点（H:DownloadImage）左侧的Runnable状态信息，可知应用主线程是由OS\_NET\_HttpWork线程唤醒，即该图片资源是应用通过http请求访问服务器下载的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/g1dQmjNgS-yRRmyjnxQJxg/zh-cn_image_0000002658914275.png "点击放大")

   查看http请求Trace点信息，可知该图片下载耗时达到3.2s。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/N_L0_C6kTQiYu66zqzI-rg/zh-cn_image_0000002658794321.png "点击放大")

   排查日志中NETSTACK、Download image关键日志，发现该图片大小为6.95M，图片资源较大导致查看图片时图片加载慢的问题。

   ```txt
   02-28 09:49:45.136   14651-15038  C015B0/com.exam...ion/NETSTACK com.examp...lication     I     taskid=68, size:7292359, dns:0.130, connect:0.000, tls:0.000, firstSend:0.197, firstRecv:128.160, total:3029.077, redirect:0.000, errCode:0, RespCode:200, httpVer:2, method:GET, osErr:0
   02-28 09:49:45.136   14651-14651  C0391F/com.exam...ion/AceImage com.examp...lication     I     [(100000:100000:scope)] Download image successfully, nodeId = 4216, accessId = 4217, srcInfo = <private>, ImageData length=7292359
   ```

## 分析结论

图片放大查看时出现加载慢问题的原因有：

* 网络环境质量差。
* 放大后的图片包含更多细节信息、像素较高，加载时间较长。

## 修改建议

* 使用[LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)，增加加载动效过渡。
* [通过预下载的方式](../best-practices/bpta-image-white-lump-solution.md#section66762818562)可以将网络图片通过应用沙箱的方式进行提前缓存，将图片下载解码提前到组件创建之前执行，当Image组件加载时从应用沙箱中获取缓存数据。非首次请求时会判断应用沙箱里是否存在资源，如存在直接从缓存里获取，不再重复下载，减少Image加载大的网络图片时图片放大查看加载慢的问题，提升用户体验。
