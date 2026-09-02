---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-8
title: H5页面加载缓慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > H5页面加载缓慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:80d9a92bdac26d42fac4a14e2ea2a9a221f0c9ff5be6691d3acdd83ab5b4af7c
---

## 问题现象

在应用内浏览或切换内部页面时，页面整体加载缓慢，需要等待较长时间才能完全显示。

## 背景知识

* DevEco Profiler提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率，相关内容可看[性能优化概述](../harmonyos-guides/ide-insight-description.md)。
* 应用开发过程中，会通过在APP中嵌入WebView以提高开发效率，可能面临ArkWeb加载和丢帧等问题。DevEco Profiler提供ArkWeb分析模板，可以结合ArkWeb执行流程的关键Trace点来定位问题发生的阶段。更多详细内容可以看[加载丢帧：ArkWeb分析](../harmonyos-guides/ide-profiler-arkweb.md)。

  Web加载相关的Trace关键字如下：

  | 描述 | 线程 | Trace关键字 |
  | --- | --- | --- |
  | 组件销毁 | 应用主线程 | H:CustomNodeBase:Destroy [组件名] |
  | 应用收到手指离开屏幕的事件 | 应用主线程 | H:DispatchTouchEvent xxx type=1 |
  | web组件创建 | 应用主线程 | H:NWebImpl |
  | 加载url | 应用主线程 | H:NavigationControllerImpl::LoadURLWithParams | url= |
  | 开始加载网页 | 应用包名:render | H:NavigationBodyLoader::StartLoadingBody |
  | 网页加载完成 | 应用包名:render | H:RenderFrameImpl::didStopLoading |
  | 渲染输出 | CompositorGpuTh | SkiaOutputSurfaceImplOnGpu::SwapBuffers |
* Web组件支持使用DevTools工具调试前端页面。DevTools是一个Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力。开发者通过setWebDebuggingAccess()接口开启Web组件前端页面调试能力，利用DevTools工具可以在电脑上调试移动设备上的前端网页，设备需为4.1.0及以上版本。更多详细内容可以看[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。
* 网络环境质量的日志搜索关键字为SignalPoll或chload|noise|rssi，关键参数如下：

  **chload**：通道占用比，能够体现WiFi信道的繁忙情况。chload值越高表示网络状态越差，chload值大于500时网络质量差，大于800时网络基本不可用。

  **rssi**：信号强度，-30表示信号很强，-80表示信号很弱。

  **noise**：-80为干扰环境，到-60以上就是强干扰。

  具体如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Znl3VF5wTMWLGRJKfD8Srg/zh-cn_image_0000002628554968.png)
* 搜索NETSTACK\_RCP日志关键字可以看到应用进行rcp网络请求的耗时情况，其中的参数含义为：

  size：上传或者下载的数据大小（byte）

  dnsDur：域名解析耗时，单位：ms。

  tcpDur：TCP握手耗时，单位：ms。

  tlsDur：TLS握手（加密鉴权）耗时，单位：ms。

  sndDur：从加密鉴权结束到传输即将开始的耗时，单位：ms。

  rcvDur：从传输开始到第一个字节被接收的耗时，单位：ms。

  totDur：总耗时，单位：ms。

  statusCode：状态码。

## 问题定位

1. 在日志中搜索SignalPoll或chload|noise|rssi判断网络环境质量，如chload值大于500或rssi值在-80左右或noise值大于-80，则网络环境质量较差，导致页面加载慢。存在如下日志信息可判断为网络环境质量差。

   ```txt
   07-30 19:52:29.427   1005-1759     P015B5/netmanager/BoosterNet    netmanager            I     [nodict][app_general.cpp] AdaBoostPredict# Ada_app,index:2,NisPsSlow:0,NProba:312,rssi:-82,noise:-93,chload:653,uldelay:1,rtt:1
   ```
2. 搜索NETSTACK\_RCP日志关键字确认rcp请求耗时是否有异常，如下日志可看到网络请求总耗时10s，状态码为504，网关超时异常，未能从服务器中接收到正确响应，导致加载慢。

   ```txt
   11:13:13.175 19203 19286 I C015C5/com.hw.example/NETSTACK_RCP:  id=134, httpVer:2, method:POST, size:1624, statusCode: 504. httpPhase:000111, dnsDur:0.06, tcpDur:0.00, tlsDur:0.00, sndDur:0.34, rcvDur:10118.74, totDur:10119.52 ...
   ```

3. 如问题场景下网络环境正常，可使用DevEco Profiler ArkWeb模板抓取加载过程Trace。

   结合ArkWeb泳道划分的各阶段耗时和Trace点、网页加载完成Trace点H:RenderFrameImpl::didStopLoading、加载完成后的第一帧渲染Trace点SkiaOutputSurfaceImplOnGpu::SwapBuffers，可得到整体以及各阶段耗时，分析其中耗时较多的阶段。

   * 耗时集中在路由导航：

     以下表和图为例，耗时主要集中在路由导航，该部分表示通过url找到网页过程耗时较多，可通过预连接优化。

     | 阶段 | 相关Trace关键字 | 耗时 |
     | --- | --- | --- |
     | 点击事件处理 | H:DispatchTouchEvent xxx type=1到H:NWebImpl|CreateNWeb | 10ms |
     | Web组件初始化 | H:NWebImpl | CreateNWeb到H:NavigationControllerImpl::LoadURLWithParams | url= | 674ms |
     | 导航流程 | H:NavigationControllerImpl::LoadURLWithParams到H:NavigationBodyLoader::StartLoadingBody | 4.4s |
     | html解析以及重要子资源下载，页面加载完成 | H:NavigationBodyLoader::StartLoadingBody到H:RenderFrameImpl::didStopLoading | 572ms |
     | 页面加载完成到开始显示网页 | H:RenderFrameImpl::didStopLoading到之后的第一个SkiaOutputSurfaceImplOnGpu::SwapBuffers | 5.5ms |
     | 总耗时 |  | 5661.5 |

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2hYltBfwQUqqFnqAck1rvQ/zh-cn_image_0000002628395068.png "点击放大")
   * 耗时集中在html解析、子资源下载到页面加载完成：
     + 以下表和图为例，耗时主要集中在html解析、子资源下载到页面加载完成部分（1.7s）。

       | 阶段 | 相关Trace关键字 | 耗时 |
       | --- | --- | --- |
       | 点击事件处理 | H:DispatchTouchEvent xxx type=1到H:NWebImpl | CreateNWeb | 26ms |
       | Web组件初始化 | H:NWebImpl | CreateNWeb到H:NavigationControllerImpl::LoadURLWithParams | url= | 65ms |
       | 导航流程 | H:NavigationControllerImpl::LoadURLWithParams到H:NavigationBodyLoader::StartLoadingBody | 644ms |
       | html解析以及重要子资源下载，页面加载完成 | H:NavigationBodyLoader::StartLoadingBody到H:RenderFrameImpl::didStopLoading | 1712ms |
       | 页面加载完成到开始显示网页 | H:RenderFrameImpl::didStopLoading到之后第一个SkiaOutputSurfaceImplOnGpu::SwapBuffers | 88.4ms |
       | 总耗时 |  | 2535.4 |

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Rxc2mYz_TUmcbHw6d3MDlA/zh-cn_image_0000002658914289.png "点击放大")
     + 通过查看应用包名:render线程的Trace点，html解析、子资源下载到页面加载完成部分耗时主要是在解析过程中脚本运行耗时，与网页本身有关，可使用DevTools分析网页侧性能。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/cBLZfA6CTzm6VnWq1s0Oaw/zh-cn_image_0000002658794337.png "点击放大")
     + 使用DevTools录制页面加载情况，分析"性能"页中"网络"和"主要"项的耗时情况。
       1. 查看"网络"项是否有耗时较长的网页资源请求，网络请求是否正常。

          如下图所示可以发现加载慢主要是网页资源加载造成的，耗时集中在发送请求、等待处理以及资源下载部分。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/np76qG_ARv6-fYhPkHgOGg/zh-cn_image_0000002628554970.png "点击放大")

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/mxqzUuF6RQiP5xfpV2JffA/zh-cn_image_0000002628395070.png "点击放大")

          如发现有耗时超长的网络请求，耗时集中在排队和连接部分（如下图index.css），则可能是网络请求出现异常，可通过查看"网页"项的资源请求状态确认，如下图中请求index.css资源出现403状态码（服务器拒绝客户端授权访问）。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/xGGKzf_DQkS0BJ-BgFlCbw/zh-cn_image_0000002658914291.png "点击放大")

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ZPBrDg1xSoWX_gzKCU1xBA/zh-cn_image_0000002658794339.png "点击放大")

          如未发现有耗时较长的网络请求（如下图所示），可排查网络页和控制台是否有错误信息。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BN4yKIvLSG2CNzYk1JmOag/zh-cn_image_0000002628554972.png)

          下图中可看到网页加载时访问js脚本的地址出现ERR\_NAME\_NOT\_RESOLVED错误（域名无法解析），IP地址不正确，资源请求超时导致页面加载慢。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/wLsoI0wrQBWBbvexIoqjYQ/zh-cn_image_0000002628395074.png "点击放大")
       2. 查看"主要"项中是否存在耗时任务。

          可查看"主要"项是否有标红的部分来确认网页是否存在耗时任务，如下图可看到网页存在472.92ms的长任务，其中耗时主要集中在脚本执行，脚本代码flushJobs函数执行耗时最长。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/2xsh0tH0R4mkcqhaVoXarg/zh-cn_image_0000002658914295.png)

## 分析结论

导致H5页面加载慢的原因有：

* 网络环境质量差。
* 网关超时异常，未能从服务器中接收到正确响应。
* 页面路由导航时间较长。
* 页面加载慢是因为应用的网页导航、子资源加载、脚本运行耗时较多。
* 请求资源时连接服务器超时，出现403状态码（服务器拒绝客户端授权访问）。
* 请求资源时出现ERR\_NAME\_NOT\_RESOLVED错误（域名无法解析），IP地址不正确，资源请求超时。
* 脚本代码函数执行耗时较多。

## 修改建议

* 增加加载中提示。
* 排查、确认后端服务器是否正常运行中，后端服务是否响应过慢，优化服务性能。
* [预解析和预连接优化](../best-practices/bpta-web-develop-optimization.md#section29621418112311)。
* 通过[预下载优化](../best-practices/bpta-web-develop-optimization.md#section11708113212514)提前下载页面所需的资源。
* 检查服务器侧的权限设置，确认是否有权限限制。
* 修改成正确的资源IP地址。
* 优化脚本代码函数逻辑。
