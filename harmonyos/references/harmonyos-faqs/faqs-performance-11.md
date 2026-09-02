---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-11
title: 应用冷启动慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用冷启动慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b055759f5ca6b1280886412912863e760763dfd8e9461ad2c3fa90bbfa265ba4
---

## 问题现象

首次打开应用或长时间未使用后重新打开应用时，从点击图标到应用主页面完全加载出来的时间过长，期间可能显示空白屏幕或加载动画。

## 背景知识

* 冷启动：当应用启动时，设备后台没有该应用的进程，需要重新创建应用的进程。
* 应用冷启动流程大致可分为以下部分：

1. 应用进程创建、初始化：该阶段主要是系统完成应用进程的创建以及初始化的过程，解码启动页图标。
2. 启动应用、Ability：该阶段主要是加载资源，创建和初始化Application和Ability对象，加载依赖模块。
3. Ability和AbilityStage生命周期：该阶段主要执行Ability和AbilityStage启动生命周期的回调。
4. 加载绘制首页：该阶段主要是加载首页内容、测量布局、刷新组件并绘制显示。

* 可在日志中搜索关键字SignalPoll或chload|noise|rssi来判断网络环境质量。

  chload：通道占用比，能够体现WiFi信道的繁忙情况。chload值越高表示网络状态越差，chload值大于500时网络质量差，大于800时网络基本不可用。

  rssi：信号强度，-30表示信号很强，-80表示信号很弱。

  noise：-80为干扰环境，到-60以上就是强干扰。

  具体如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/low87v3cQIKKbVuZ2QDfLw/zh-cn_image_0000002658794363.png)
* [Launch分析](../harmonyos-guides/ide-launch-overview.md)是DevEco Profiler工具提供的冷启动场景性能分析能力，可以拆解应用冷启动过程，抓取不同阶段的耗时数据，帮助开发者快速分析启动过程的耗时瓶颈，识别出导致启动缓慢的原因。

  Launch分析将应用的冷启动过程拆解为以下几个阶段：

  | 阶段 | 说明 |
  | --- | --- |
  | Process Creating | 应用进程创建 |
  | Application Launching | 应用启动阶段 |
  | UI Ability Launching | UIAbility启动阶段 |
  | UI Ability OnForeground | 应用进入前台阶段 |
  | First Frame - App Phase | 应用提交首帧渲染阶段 |
  | First Frame - Render Phase | 渲染服务提交首帧渲染阶段 |
* 路由导航过程[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)生命周期变化日志关键字如下：

  | 日志关键字 | 描述 |
  | --- | --- |
  | 页面名 lifecycle change to onWillShow state | 页面显示之前 |
  | 页面名 lifecycle change to onShown state | 页面显示时 |
  | 页面名 lifecycle change to onWillHide state | 页面隐藏之前 |
  | 页面名 lifecycle change to onHidden state | 页面隐藏时 |

## 问题定位

1. 根据背景知识中网络环境质量相关信息排查问题发生前后的网络情况，若无异常则可排除网络质量差导致的应用启动慢。
2. 在日志中搜索SetAsanEnabledEnv cold start app关键字，查看应用是否有设置[ASan](../best-practices/bpta-stability-asan-detection.md)或[HWASan](../best-practices/bpta-stability-hwasan-detection.md)，使用ASan或HWASan会有性能开销，适用于开发态调试压测场景，当进行性能测试或者应用上线时，需要把该功能关闭。

   ```txt
   05-10 11:07:09.086   5643-5643  C02C11/com.exa...tion/APPSPAWN  pid-5643  I   [asan_detector.c:176]SetAsanEnabledEnv cold start app com.example.myapplication
   ```
3. 在日志中搜索onWillShow state|onShown state|onWillHide state|onHidden state关键字，如发现应用有长时间处于引导页（如下图所示中处于引导页长达15s），则推测在启动过程中主线程执行耗时操作或者应用业务逻辑设计导致启动时间长，可使用DevEco Profiler抓取该过程Trace进行分析。

   ```txt
   05-10 11:14:54.636   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] splash lifecycle change to onWillShow state.
   05-10 11:14:54.638   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] splash lifecycle change to onShown state.
   05-10 11:15:09.777   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] splash lifecycle change to onWillHide state.
   05-10 11:15:09.777   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] main lifecycle change to onWillShow state.
   05-10 11:15:09.777   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] splash lifecycle change to onHidden state.
   05-10 11:15:09.794   1356  1356 I C03922/com.example.myapplication/AceNavigation:  [(100000:100000:scope)] main lifecycle change to onShown state.
   ```

   在DevEco Profiler工具的分析结果中输入navDestinationName关键字找到进入引导页和进入主页时的Trace信息，分析该过程线程的运行状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/GC5J4oO6S8m3ieL6iPhmIw/zh-cn_image_0000002628554998.png "点击放大")

   如该过程应用大部分时间处于休眠态（Sleeping），并且问题场景引导页停留时长相对固定（比如15s），则推测属于应用业务逻辑异常场景下设计相关问题（比如启动过程需要访问服务器获取数据，等待一段时间未有返回结果则停止等待，进入主页），需要排查应用业务逻辑。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/n_h2S9FtQ9iOwkNaOL2Hkg/zh-cn_image_0000002628395098.png "点击放大")
4. 如未搜到日志关键字，按以下图示步骤借助DevEco Profiler Launch分析抓取应用冷启动过程的耗时数据，查看Launch泳道中从Process Creating到First Frame - Render Phase过程耗时集中在哪一部分。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/R8ZR-Pd5QmmjVspjzkNf-A/zh-cn_image_0000002658914317.png "点击放大")

   * 如下图所示，如果耗时主要集中在应用进入前台阶段（UI Ability OnForeground），达到了1.2s。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/3GXwrdxuStikm1I31SiiTg/zh-cn_image_0000002658794365.png "点击放大")

     找到应用进程泳道，将应用进入前台阶段（UI Ability OnForeground）阶段框选起来查看该阶段应用线程的运行状态。如发现大多数时间都处于Running状态，可知应用在此处执行耗时操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/-Z99Afc0RXC4-RXbw_i4fw/zh-cn_image_0000002628555000.png "点击放大")

     然后找到ArkTS Callstack泳道并点击，可以看到应用在该阶段的调用栈，查看调用栈中的函数名以及耗时占比情况可得到该部分耗时是由于Manager管理类在初始化间接调用了SDK.so的初始化方法，SDK初始化时间较长导致。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/6nsA9ZITSHeUmO7p8wHEpw/zh-cn_image_0000002628395100.png "点击放大")
   * 如果耗时主要集中在UIAbility启动阶段（UI Ability Launching），如下图所示该阶段达到1.3s。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/TnB2Z3U2TgqNs2MuHCFXag/zh-cn_image_0000002658914319.png "点击放大")

     找到应用主线程泳道，将UIAbility启动阶段框起来查看该阶段线程的运行状态和Trace信息，Trace信息从上到下显示表示上面Trace打点对应的函数直接或间接调用了下面Trace打点对应的函数，因此分析耗时原因主要分析下面的Trace打点。如发现大多数时间处于Running状态，耗时主要集中在H:SourceTextModule::Evaluate部分，则应用在启动过程时加载import的模块时耗时较多，导致应用启动慢。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/NO1WK33CQJSKIOoFzwsEDg/zh-cn_image_0000002658794367.png "点击放大")
   * 如果整体耗时与用户体验上差距较大，如下图所示，Process Creating到First Frame - Render Phase总耗时385ms，但用户体验加载时长达到3秒，该情况下应用可能长时间停留在启动页，一段时间后才跳转到主页，或者页面组件创建加载耗时较多，显示较慢。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0aLkU-E6Seq3meBhbAWNZQ/zh-cn_image_0000002628555002.png "点击放大")

     **场景一：RN应用启动耗时**：可点击主线程泳道，在Slice List中过滤组件创建的Trace关键字，在下图中可看到有RNSurface组件创建，可知该应用属于RN应用。RN应用中RNOH\_JS线程负责构造节点树并提交到应用主线程完成渲染，可排查RNOH\_JS线程。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/BAKDGcI5QUy8UxAb68gR_Q/zh-cn_image_0000002628395102.png "点击放大")

     查看RNOH\_JS线程Trace信息，可看到耗时主要集中在loadBundle部分（加载包含应用程序代码的JS文件，支持应用启动、更新等功能）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/sSbnz5KjRRamyvzAhYtkHQ/zh-cn_image_0000002658914321.png "点击放大")

     **场景二：初始Web页面加载耗时**：根据下表中对应关键字找到Trace点，计算Web加载各阶段耗时。

     | 阶段 | 相关Trace关键字 | 耗时 |
     | --- | --- | --- |
     | Web组件初始化 | H:NWebImpl | CreateNWeb到H:NavigationControllerImpl::LoadURLWithParams | url= | 24ms |
     | 导航流程 | H:NavigationControllerImpl::LoadURLWithParams到H:NavigationBodyLoader::StartLoadingBody | 274ms |
     | html解析以及重要子资源下载，页面加载完成 | H:NavigationBodyLoader::StartLoadingBody到H:RenderFrameImpl::didStopLoading | 466ms |
     | 页面加载完成到开始显示网页 | H:RenderFrameImpl::didStopLoading到之后第一个SkiaOutputSurfaceImplOnGpu::SwapBuffers | 12ms |
     | 总耗时 |  | 776ms |

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/QRYTJ-hHSdODVw9zS_41zQ/zh-cn_image_0000002658794369.png "点击放大")

     使用DevTools工具抓取页面加载过程，在“性能”选项卡下选择“主要”，可以看到有时长246ms的长任务耗时警告，整体耗时主要是在执行脚本，时间为500ms。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/yksdb8fkQeyN4PAvAcliSQ/zh-cn_image_0000002628555004.png "点击放大")

## 分析结论

应用冷启动慢的原因有：

* 应用开启ASan或者HWASan。
* 应用业务逻辑出现异常时，触发超时等待时的退出机制。
* 应用在进入前台阶段执行耗时的初始化操作。
* 应用在启动过程加载import的模块耗时较多。
* 整体耗时与用户体验上差距较大时：
  + RN应用启动时加载JS bundle文件（应用程序代码）耗时长。
  + 应用初始Web页面执行脚本耗时长。

## 修改建议

* 参考[ASan使能](../best-practices/bpta-stability-asan-detection.md#section17956115264213)和[配置HWASan](../best-practices/bpta-stability-hwasan-detection.md#section10791454125320)将相关功能关闭。
* 优化应用业务逻辑，修复业务逻辑异常问题或减少异常场景下超时等待的时间。
* 将初始化操作改为异步执行，[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)避免阻塞主线程。这样用户界面可以先显示出来，而后台继续完成初始化工作。
* 减少import的模块，按需加载或动态加载，参考[缩短Application和Ability初始化阶段耗时](../best-practices/bpta-application-cold-start-optimization.md#section584818173141)。
* 整体耗时与用户体验上差距较大时：
  + 将JavaScript包编译成Hermes字节码二进制文件作为加载文件，参考字节码（HBC），或者在启动时增加加载动效提示。
  + 优化应用初始Web页面脚本执行逻辑，采用异步方法减少主线程耗时。
