---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-6
title: ArkUI页面动画卡顿掉帧
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面动画卡顿掉帧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f9543cd9db1f90700efee45bb1cac5120c5420bc1665b8435318bb487edc532e
---

## 问题现象

动画运行时存在不流畅、掉帧的现象。

## 背景知识

* 屏幕刷新率：显示设备每秒钟更新屏幕内容的次数，其决定了Vsync信号周期，120Hz对应8.33ms，90Hz对应11.11ms，60Hz对应16.67ms。
* Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
* 下图为90Hz刷新率的渲染流程，首先应用侧在收到Vsync信号后会响应用户的屏幕点击等输入事件，确定UI元素的位置、大小、资源、动效属性等，提交绘制指令给渲染服务(Render Service)，渲染服务会根据绘制指令进行相应的图形计算和渲染操作，将渲染结果写入到帧缓冲区（存储用于显示器输出的图像数据）中，将数据送到屏幕上显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/yLN87ThmQYeRm07Yx_5KzA/zh-cn_image_0000002628554956.png "点击放大")

  按上述流程中，应用侧和Render Service侧都可能因为处理时间较长，超过了Vsync信号周期，导致界面送显的频率低于屏幕刷新率，出现卡顿丢帧的情况。前者可能是应用业务逻辑、组件复杂，执行耗时逻辑等导致，后者可能是界面结构过于复杂、GPU负载过大等导致。
  1. 应用卡顿导致丢帧的故障模型：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ZZ1gYGNLQFCZcF3PEiDY3Q/zh-cn_image_0000002628395056.png "点击放大")
  2. Render Service卡顿导致丢帧的故障模型：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/eHOJwLXESbmaFoQxl3mdFw/zh-cn_image_0000002658914277.png "点击放大")
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件可以用于绘制静态图形，还可以通过不断更新图形来创建动画效果。通常可以通过以下步骤实现动画效果：
  1. 设置定时器：使用定时器（如setTimeout或setInterval）来定期更新画布的内容。
  2. 更新图像：在定时器的回调函数中，更改画布上的图像或图形元素的位置或其他属性，以反映动画的变化。
  3. 重新绘制：每次更新属性后，重新绘制整个场景或仅更新部分图像，显示新的状态。
* [XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)组件是一种渲染组件，可用于EGL/OpenGLES和媒体数据写入，其在独立线程中完成绘制，避免影响应用主线程性能，通常用于在开发中满足较为复杂的自定义渲染需求，例如地图、相机预览流的显示和游戏画面的渲染。
* Trace文件是一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况，查看Trace文件可使用[Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host/tree/master/smartperf_host)。

  动画、绘制相关的Trace关键字如下：

  | Trace关键字 | 说明 |
  | --- | --- |
  | H:ReceiveVsync | 接收Vsync信号。 |
  | H:RSModifierManager Draw num | 组件属性变更产生的绘制，如果num不变，持续绘制可能和动画组件的属性变更有关。 |
  | H:RSModifier::Draw | 单个组件由于属性变更产生的绘制。 |
  | H:SendCommands | 发送指令，通知图形侧进行渲染，该Trace信息下方存在H:MarshRSTransactionData表示应用有推送绘制指令相关的数据给图形侧。 |
  | H:FlushDirtyNodeUpdate | 刷新标脏的组件，当状态变量变化时，比如宽度和高度，组件需要重新布局刷新。 |
  | H:HandleOnAreaChangeEvent | 处理组件区域变化事件，组件的大小、位置发生时触发。 |
  | H:JSAnimateTo | 应用调用[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)触发ArkUI动效。 |
  | H:FrameNode[组件名][id:组件Id号]::RenderTask | 执行组件的渲染任务。 |

  在Trace中可以通过框选渲染服务（render\_service）主线程Trace信息查看被框选的这段时间内的平均帧率，如下图所示，平均帧率为120fps。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/O60IlsoxTBGUydxJeH48YA/zh-cn_image_0000002658794323.png "点击放大")
* DevEco Profiler目前是集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码，更多详细内容可查看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  [Time分析](../harmonyos-guides/ide-insight-session-time.md)是DevEco Profiler提供的应用基础耗时分析工具，可以查看应用执行的ArkTS代码以及相应耗时。

* ArkUI Inspector是DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。

## 问题定位

1. 使用Smartperf抓取动画卡顿场景的Trace信息，找到查看render\_service泳道中的H:PreferredFrameRate子泳道确认问题场景屏幕刷新率，如下图中屏幕刷新率为120Hz，则Vsync信号周期为8.3ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/LBah6NqEQNaAFzUxOYkmQQ/zh-cn_image_0000002628554958.png "点击放大")
2. 找到render\_service泳道中的render\_service子泳道，框选问题场景中的Trace信息确认该过程绘制帧率，如下图为25.6fps，绘制帧率远小于屏幕刷新率。根据H:ReceiveVsync关键字在Slices页中查看相关Trace信息，发现render\_service线程在接收Vsync信号处理时耗时最多为7.6ms，未超出8.3ms，因此render\_service未出现卡顿，推测是应用进程问题导致卡顿丢帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/l9bHXKXcTkyOuX7fiTqZPA/zh-cn_image_0000002628395058.png "点击放大")
3. 找到应用主线程泳道，根据H:MarshRSTransactionData关键字查看应用发送绘制相关数据给图形服务进程的频率，如果发送绘制指令相关数据的周期大于Vsync信号周期，则是应用进程发送绘制指令较慢导致动画卡顿。如下图中发送绘制指令相关数据周期为42.9ms左右，远大于8.3ms，需要排查应用进程发送绘制指令较慢的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/HmBvodGtSMO30Z08GErN8w/zh-cn_image_0000002658914279.png "点击放大")
4. 分析H:MarshRSTransactionData关键字间应用进程Trace信息和运行状态确定应用进程发送绘制指令较慢的原因，具体如下：
   * 情况一：
     1. 如果在应用主线程两次发送绘制指令间，主线程大多数时间处于sleeping状态、应用接收Vsync信号处理耗时未大于8.3ms，如下图所示，该情况下可能是应用进程中执行动画的组件渲染周期较长，应用送帧较少导致动画卡顿丢帧。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/lNEvkr4vTu6zP3DXFABrjw/zh-cn_image_0000002658794325.png "点击放大")
     2. 使用ArkUI Inspector确认执行动画的组件的id为317，在Trace中搜索执行该组件渲染任务的Trace关键字H:FrameNode[Canvas][id:317]::RenderTask，可看到执行该组件渲染任务的周期为42.9ms左右，远大于8.3ms，可知应用动画本身帧率较低，送帧较少导致卡顿丢帧现象。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/amy79v6bSNWh5gGqQX-oDA/zh-cn_image_0000002628554960.png "点击放大")
   * 情况二：
     1. 如果在应用主线程两次发送绘制指令间，应用有执行耗时操作，如下图所示中在Napi complete部分耗时长（达到44ms），该部分是由于complete回调函数或await之后业务逻辑耗时较多导致，需要排查JsGetComponent执行后的业务代码。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/rFc3dk_WTNavtrlnp_sjBw/zh-cn_image_0000002628395060.png "点击放大")
     2. 使用DevEco Profiler Time分析Napi complete耗时原因，从Callstack泳道中的应用主线程泳道中可看到该部分耗时主要集中在应用so文件业务代码部分。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/0dfkfT3_SCimWJ2jVqj-Yg/zh-cn_image_0000002658914281.png "点击放大")
   * 情况三：
     1. 如果在应用主线程两次发送绘制指令间，主线程大多数时间处于running状态、应用接收Vsync信号处理耗时大于8.3ms，如下图所示，该情况下是应用进程执行耗时操作导致动画卡顿丢帧。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/M779CXIEQ0iARG61sZM35Q/zh-cn_image_0000002658794327.png "点击放大")
     2. 排查上图中Trace点H:ReceiveVsync下Trace信息，发现耗时较长为H:RSModifier::Draw，推测该应用是通过不断修改组件的属性值，触发绘制来实现动画效果，但没有看到组件相关的Trace关键字，因此使用Ark Inspector查看应用当前页面的组件树，发现该页面通过XComponent组件渲染显示。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/lTib5ToESnWrutWNGnVmsg/zh-cn_image_0000002628554962.png "点击放大")
     3. 使用DevEco Profiler Time分析应用绘制时的大致流程，得知其在动画启动时首先执行了onDrawChild函数，在Canvas上绘制显示的内容，然后调用flush2Surface函数，从Canvas中读取数据传递到XComponent组件渲染，之后则不断在Canvas上绘制当前页面，从Canvas中读取数据传递给XComponent组件更新当前页面的翻页过程状态。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/krCrX2r8RQGM2P79Nnywgw/zh-cn_image_0000002628395062.png "点击放大")

        从上图中可看到在动画执行过程中，耗时主要在从Canvas中读取数据（12ms），超出了Vsync信号周期（8.3ms），导致动画卡顿丢帧。

## 分析结论

ArkUI页面动画卡顿丢帧的原因有：

* 应用动画本身帧率较低，送帧较少，导致动画卡顿丢帧。
* 应用在动画期间有调用Napi接口，同时在Napi complete回调函数或await之后有耗时操作，阻塞绘制，导致动画卡顿丢帧。
* 应用在接收Vsync信号处理时执行耗时操作，发送参与动画的组件的相关渲染指令和数据给render\_service较慢，导致动画卡顿丢帧。

## 修改建议

* 提高动画帧率，增加组件的绘制频率。
* 优化Napi接口调用之后的耗时操作，可以[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)将耗时任务移到子线程执行。
* 优化耗时处理逻辑，可参考[主线程耗时操作优化](../best-practices/bpta-time-optimization-of-the-main-thread.md)。对于应用使用Canvas实现动画效果，从显存中读取Canvas数据耗时较多导致无法达到动画流畅性要求的问题，在API16中提供了接口[OH\_Drawing\_SurfaceCreateOnScreen()](../harmonyos-references/capi-drawing-surface-h.md#oh_drawing_surfacecreateonscreen)，能够将surface对象上的画布绘制内容直接提交给GPU处理，完成绘制内容上屏显示。
