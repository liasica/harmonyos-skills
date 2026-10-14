---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-troubleshootin-0004
title: H5页面加载缓慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 故障排查 > H5页面加载缓慢
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:33+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:ca0dff8b79209a877da550f4c8c3058fee1a65b77915ee10d842d6851343169a
---

## 问题现象

在应用内浏览或切换内部页面时，页面整体加载缓慢，需要等待较长时间才能完全显示。

## 定位过程

1. 在日志中搜索SignalPoll或chload|noise|rssi判断网络环境质量，如chload值大于500或rssi值在-80左右或noise值大于-80，则网络环境质量较差，导致页面加载慢。存在如下日志信息可判断为网络环境质量差。

   ```txt
   07-30 19:52:29.427   1005-1759     P015B5/netmanager/BoosterNet    netmanager            I     [nodict][app_general.cpp] AdaBoostPredict# Ada_app,index:2,NisPsSlow:0,NProba:312,rssi:-82,noise:-93,chload:653,uldelay:1,rtt:1
   ```
2. 搜索NETSTACK\_RCP日志关键字确认rcp请求耗时是否有异常，如下日志可看到网络请求总耗时10s，状态码为504，网关超时异常，未能从服务器中接收到正确响应，导致加载慢。

   ```txt
   11:13:13.175 19203 19286 I C015C5/com.hw.example/NETSTACK_RCP:  id=134, httpVer:2, method:POST, size:1624, statusCode: 504. httpPhase:000111, dnsDur:0.06, tcpDur:0.00, tlsDur:0.00, sndDur:0.34, rcvDur:10118.74, totDur:10119.52 ...
   ```
3. 如问题场景下网络环境正常，可使用DevEco Profiler ArkWeb模板抓取加载过程Trace。结合ArkWeb泳道划分的各阶段耗时和Trace点、网页加载完成Trace点H:RenderFrameImpl::didStopLoading、加载完成后的第一帧渲染Trace点SkiaOutputSurfaceImplOnGpu::SwapBuffers，可得到整体以及各阶段耗时，分析其中耗时较多的阶段。
   * 耗时集中在路由导航：

     以下表和图为例，耗时主要集中在路由导航，该部分表示通过url找到网页过程耗时较多，可通过预连接优化。

     | 阶段 | 相关Trace关键字 | 耗时 |
     | --- | --- | --- |
     | 点击事件处理 | H:DispatchTouchEvent xxx type=1到H:NWebImpl|CreateNWeb | 10ms |
     | Web组件初始化 | H:NWebImpl | CreateNWeb到H:NavigationControllerImpl::LoadURLWithParams | url= | 674ms |
     | 导航流程 | H:NavigationControllerImpl::LoadURLWithParams到H:NavigationBodyLoader::StartLoadingBody | 4.4s |
     | html解析以及重要子资源下载，页面加载完成 | H:NavigationBodyLoader::StartLoadingBody到H:RenderFrameImpl::didStopLoading | 572ms |
     | 页面加载完成到开始显示网页 | H:RenderFrameImpl::didStopLoading到之后的第一个SkiaOutputSurfaceImplOnGpu::SwapBuffers | 5.5ms |
     | 总耗时 | - | 5661.5 |

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/-h0sSkCPS46S8H89nyIBeQ/zh-cn_image_0000002792210187.png "点击放大")
   * 耗时集中在html解析、子资源下载到页面加载完成：
     + 以下表和图为例，耗时主要集中在html解析、子资源下载到页面加载完成部分（1.7s）。

       | 阶段 | 相关Trace关键字 | 耗时 |
       | --- | --- | --- |
       | 点击事件处理 | H:DispatchTouchEvent xxx type=1到H:NWebImpl | CreateNWeb | 26ms |
       | Web组件初始化 | H:NWebImpl | CreateNWeb到H:NavigationControllerImpl::LoadURLWithParams | url= | 65ms |
       | 导航流程 | H:NavigationControllerImpl::LoadURLWithParams到H:NavigationBodyLoader::StartLoadingBody | 644ms |
       | html解析以及重要子资源下载，页面加载完成 | H:NavigationBodyLoader::StartLoadingBody到H:RenderFrameImpl::didStopLoading | 1712ms |
       | 页面加载完成到开始显示网页 | H:RenderFrameImpl::didStopLoading到之后第一个SkiaOutputSurfaceImplOnGpu::SwapBuffers | 88.4ms |
       | 总耗时 | - | 2535.4 |

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/a5_srN_mTtq1LJv5T0iixA/zh-cn_image_0000002762691394.png "点击放大")
     + 通过查看应用包名:render线程的Trace点，html解析、子资源下载到页面加载完成部分耗时主要是在解析过程中脚本运行耗时，与网页本身有关，可使用DevTools分析网页侧性能。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/fQ92DkzHTASKuDqXpYStRw/zh-cn_image_0000002762689282.png "点击放大")
     + 使用DevTools录制页面加载情况，分析"性能"页中"网络"和"主要"项的耗时情况。
       1. 查看"网络"项是否有耗时较长的网页资源请求，网络请求是否正常。

          如下图所示可以发现加载慢主要是网页资源加载造成的，耗时集中在发送请求、等待处理以及资源下载部分。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ISaDZh-ISIatODP7Lr82LA/zh-cn_image_0000002792087867.png "点击放大")

          如发现有耗时超长的网络请求，耗时集中在排队和连接部分（如下图index.css），则可能是网络请求出现异常，可通过查看"网页"项的资源请求状态确认，如下图中请求index.css资源出现403状态码（服务器拒绝客户端授权访问）。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KLD7WcMUToOdNYF6FYzEKw/zh-cn_image_0000002762849204.png "点击放大")

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/wfyZMhp_SoCecaJwp5c_pQ/zh-cn_image_0000002762849208.png "点击放大")

          如未发现有耗时较长的网络请求（如下图所示），可排查网络页和控制台是否有错误信息。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/h2Z-Ie6jRxayM1GnPn2h0g/zh-cn_image_0000002792208089.png "点击放大")

          下图中可看到网页加载时访问js脚本的地址出现ERR\_NAME\_NOT\_RESOLVED错误（域名无法解析），IP地址不正确，资源请求超时导致页面加载慢。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/f_N9_lg1Reyf9L7svGQDGg/zh-cn_image_0000002792208095.png "点击放大")
       2. 查看"主要"项中是否存在耗时任务。

          可查看"主要"项是否有标红的部分来确认网页是否存在耗时任务，如下图可看到网页存在472.92ms的长任务，其中耗时主要集中在脚本执行，脚本代码flushJobs函数执行耗时最长。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/KwvAAElSS_qt5gAvq15mmA/zh-cn_image_0000002792087877.png "点击放大")

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
