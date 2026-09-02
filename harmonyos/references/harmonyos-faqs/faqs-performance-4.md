---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-4
title: ArkUI页面滑动卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面滑动卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cca6c8da45bb8ade5e448a11a070b8f10542cb0dc02347080dba72cc207e5060
---

## 问题现象

用户通常会滑动应用页面来查看当前不可见的内容，比如视频类、新闻类应用。为了保证有良好的用户体验，在滑动页面时期望看到页面流畅滑动，然而实际会存在滑动卡顿的现象，导致用户对应用程序的整体评价下降。

## 背景知识

* 屏幕刷新率：显示设备每秒钟更新屏幕内容的次数，其决定了Vsync信号周期，120Hz对应8.33ms，90Hz对应11.11ms，60Hz对应16.67ms。
* Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
* 在HarmonyOS中，图形系统采用统一渲染模式，遵循典型流水线模式。在渲染流程中，应用侧首先响应消费者的屏幕点击等输入事件，处理完成后提交给Render Service。Render Service协调GPU等资源处理，最终将图像送到屏幕上显示，整个流程应用侧和Render Service侧都可能出现卡顿，导致最终用户观察到丢帧，具体可看[渲染流程](../best-practices/bpta-optimization-overview.md#section1625893416218)。
* Trace：一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况，查看Trace文件可使用[Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host/tree/master/smartperf_host)。

  页面滑动相关Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:APP\_LIST\_FLING | 手指按下开始拖动到抬手后的惯性滚动及最后尾动效的抛滑全过程，用于标记应用页面滑动。 |
  | H:PreferredFrameRate | 屏幕刷新率，在render\_service泳道中。 |
  | H:ReceiveVsync | 接收Vsync信号。 |
  | H:FlushDirtyNodeUpdate | 刷新标脏的组件，当状态变量变化时，比如宽度和高度，组件需要重新布局刷新。 |
  | H:CustomNodeUpdate 组件名 | 组件刷新，当状态变量变化时触发。 |
  | H:CreateTaskMeasure[组件名][self:组件ID][parent:父组件ID] | 创建组件的测量任务，确定组件的宽、高。 |
  | H:CreateTaskLayout[组件名][self:组件ID][parent:父组件ID] | 创建组件的布局任务，确定组件的位置。 |
  | H:SendCommands | 发送指令，通知图形侧进行渲染。下方H:MarshRSTransactionData表示提交渲染数据给渲染服务。 |
  | H:HandleOnAreaChangeEvent | 处理组件区域变化事件，组件的大小、位置发生时触发。 |
  | H:HandleVisibleAreaChangeEvent | 处理可见区域变化事件，组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值与设置的阈值接近时触发。 |
  | H:LazyForEach predict | LazyForEach预处理。 |
  | H:List predict | List预处理。 |
  | H:Builder:BuildLazyItem | 构建LazyItem。 |
  | H:CustomNode:BuildItem[组件名][self:组件ID][parent:父组件ID] | 构建自定义组件。 |
  | H:ExecuteJS | 运行ArkTS业务逻辑 |
  | H:ViewPU.viewPropertyHasChanged 组件名 状态变量名 N | 状态变量更新，N表示该状态变量更新后影响的组件数量。该Trace关键字需要运行hdc shell param set persist.ace.debug.enabled 1命令然后重启应用才能生效。 |
* DevEco Profiler提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率，相关内容可看[性能调优工具简介](../harmonyos-guides/ide-insight-description.md)。

## 问题定位

1. 使用SmartPerf抓取或打开问题场景Trace文件，通过滑动Trace点H:APP\_LIST\_FLING确定应用滑动操作区间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/8u4tg7cFRROv4EGnQsSfjQ/zh-cn_image_0000002658914265.png "点击放大")
2. 确定滑动区域内卡顿点。

   针对不同屏幕刷新率，Vsync信号的周期不同，120Hz对应8.33ms，90Hz对应11.11ms，60Hz对应16.67ms，滑动卡顿问题需要先确定Vsync信号的周期。

   查看滑动操作区间内的屏幕刷新率（找到render\_service泳道中H:PreferredFrameRate对应的位置），如下图为120Hz，则在滑动区间内应用主线程接收Vsync信号周期（两个Vsync信号的起始点之间的间隔时间）为8.3ms，超出8.3ms的地方为卡顿点，需要分析排查其中耗时部分。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/0QKhbkA1QcmHH9obcoF0FA/zh-cn_image_0000002658794313.png "点击放大")
3. 卡顿点可能存在以下情况：
   * 应用执行耗时操作：

     应用在两侧接收Vsync信号处理存在长时间的Running，如下图所示，此处应用在执行耗时操作，会导致卡顿。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/7HiLNkG5T5KJgG2HTXCtQw/zh-cn_image_0000002628554948.png "点击放大")
   * 应用执行耗时的ArkTS业务逻辑：

     如下图所示，应用在接收Vsync信号处理时耗时20.1ms，远远超出了8.3ms，耗时主要在H:ExecuteJS，运行ArkTS业务逻辑。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ysp-UoxXR1modKfhL22pNQ/zh-cn_image_0000002628395048.png "点击放大")
   * 应用组件复杂，测量、布局耗时：

     如下图所示，应用在接收Vsync信号处理时耗时10ms，超出了预期时间8.3ms，耗时主要集中在组件ListItem测量部分。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/fUB99yUJTd2sGub3kqZQEg/zh-cn_image_0000002658914267.png "点击放大")

     使用ArkUI Inspector工具查看该组件的层级，可看到该组件层级达到了10+，组件层级较多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/eJJlwn5cRRO57neX-PjlVA/zh-cn_image_0000002658794315.png "点击放大")
   * 应用以独立的帧率绘制更新UI页面：

     如下图所示，应用在接收Vsync信号处理时耗时14.3ms，超出了预期时间8.3ms，耗时主要集中在H:DispatchDisplaySync，推测应用进行了降帧率。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/UHKVi_TYTsqdBg2-QZSmuA/zh-cn_image_0000002628554950.png "点击放大")

     可以使用DevEco Profiler [Frame分析](../harmonyos-guides/ide-insight-session-frame.md)工具抓取该过程Trace信息，查看DispatchDisplaySync部分应用的调用栈，如下图可看到耗时集中在应用so文件的帧回调函数，应用有[请求自绘制内容绘制频率](../harmonyos-guides/displaysync-xcomponent.md)，该频率较低导致滑动卡顿问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/CHFeUGQ7Tl2VMyghnsjbAQ/zh-cn_image_0000002628395050.png "点击放大")
   * 滑动期间binder调用过多：

     如下图所示，应用接收Vsync信号的周期超过90ms，远大于预期的11.11ms，耗时主要集中在大量binder调用。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Wsv26OVuTGu5dkPr7pLZIA/zh-cn_image_0000002658914269.png "点击放大")
   * 状态变量变化，组件更新耗时多：

     如下图所示，应用在接收Vsync信号处理时耗时10.1ms，超出了预期时间8.3ms，耗时主要集中在H:FlushDirtyNodeUpdate，状态变量变化，组件更新耗时多。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Xn4h0RVbQm6RLByfQeyUKA/zh-cn_image_0000002658794317.png "点击放大")

     查看滑动过程中Trace信息，发现有大量状态变量更新、节点刷新，同时在日志中可以看到有大量State variable 'xxx' has changed during render日志打印，这是由于组件渲染绘制时有更新状态变量，一直触发节点刷新，导致滑动卡顿丢帧问题。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/9b31WHrJSzaGCunKmrIk6A/zh-cn_image_0000002628554952.png "点击放大")

     ```txt
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
     ```
   * List组件多次测量布局：

     如下图所示，在滑动过程List组件有多次进行测量布局，测量布局耗时较多导致滑动卡顿。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/tIUVPkiCQnWPnTCmteCcxQ/zh-cn_image_0000002628395052.png "点击放大")

## 分析结论

ArkUI页面滑动卡顿的原因有：

* 应用执行耗时操作。
* 应用接收Vsync信号处理时执行耗时的ArkTS业务逻辑。
* 应用组件复杂，在测量、布局时耗时较多。
* 应用请求自绘制内容绘制频率，该频率远低于120Hz。
* 应用滑动期间binder调用过多导致长时间sleeping。
* 应用在组件渲染绘制时更新状态变量，一直触发节点刷新。
* List组件有多次进行测量布局，测量布局耗时较多。

## 修改建议

* 优化处理逻辑，减少不必要的流程，或者[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)将该耗时操作迁移到子线程中。
* 在接收Vsync信号处理时减少其中耗时逻辑或移到其他流程中处理。
* [组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，避免冗余的嵌套或者使用扁平化布局来优化嵌套层次。
* 提高自绘制内容绘制频率。
* 减少binder调用或将相关调用迁移到子线程中。
* 在组件渲染绘制时不更新状态变量。
* 在滑动过程尽量避免多次更新List组件的数据，采用[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)，定义合理的键值生成函数，数据更新时才刷新页面，使用[自定义组件复用](../harmonyos-guides/arkts-component-reusable.md)避免重复创建和销毁。
