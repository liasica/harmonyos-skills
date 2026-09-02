---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-53
title: ArkUI页面滑动卡顿丢帧问题分析
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面滑动卡顿丢帧问题分析
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:1715ca431ea4149e38ac0923c63f9ad6713ccbd30ceba73ed45df41fa76417f8
---

## 问题现象

页面滑动过程卡顿，不流畅。

## 背景知识

* [渲染流程](../best-practices/bpta-optimization-overview.md#section1625893416218)：在HarmonyOS中，图形系统采用统一渲染模式，遵循典型流水线模式。下图为90Hz刷新率的渲染流程，Vsync信号周期为90Hz为11.1ms，每个Vsync信号到来时，应用侧会处理消费者的屏幕点击等输入事件，生成界面描述数据结构，提交给Render Service，Render Service协调GPU等资源处理，最终将图像送到屏幕上显示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/gaA79a9qRqWr20IQ9NQBOQ/zh-cn_image_0000002658794573.png "点击放大")

  在上述渲染流程中，如果本次Vsync信号到来时，应用侧或者Render Service侧相关流程的执行时间超过11.1ms，未在下一次Vsync信号到来时执行完本次的渲染流程，会造成两次Vsync信号到来时仅执行一次渲染流程，出现丢帧。如果存在多次丢帧的情况，用户会感知到卡顿的现象。
* [Frame分析](../harmonyos-guides/ide-insight-session-frame.md)：DevEco Profiler提供的Frame场景分析能力，可以录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因。

  常见Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:FlushDirtyNodeUpdate | 刷新标脏的组件，当状态变量变化时，比如宽度和高度，组件需要重新布局刷新 |
  | H:CustomNodeUpdate 组件名 | 组件刷新，当状态变量变化时触发 |
  | H:CreateTaskMeasure[组件名][self:组件ID][parent:父组件ID] | 创建组件的测量任务，确定组件的宽、高 |
  | H:CreateTaskLayout[组件名][self:组件ID][parent:父组件ID] | 创建组件的布局任务，确定组件的位置 |
  | H:Create[组件名][self:组件id] | 组件创建 |
  | H:SendCommands | 发送指令，通知图形侧进行渲染。下方H:MarshRSTransactionData表示提交渲染数据给渲染服务 |
  | H:HandleOnAreaChangeEvent | 处理组件区域变化事件，组件的大小、位置发生时触发。 |
  | H:HandleVisibleAreaChangeEvent | 处理可见区域变化事件，组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值与设置的阈值接近时触发。 |
  | H:LazyForEach predict | LazyForEach预处理 |
  | H:List predict | List预处理 |
  | H:Builder:BuildLazyItem | 构建LazyItem |
  | H:CustomNode:BuildItem[组件名][self:组件ID][parent:父组件ID] | 构建自定义组件 |
  | H:ExecuteJS | 运行ArkTS业务逻辑 |
  | H:ViewPU.viewPropertyHasChanged 组件名 状态变量名 N | 状态变量更新，N表示该状态变量更新后影响的组件数量。该Trace关键字需要运行hdc shell param set persist.ace.debug.enabled 1命令然后重启应用才能生效 |
  | H:JSAnimation | 执行显示动画 |
  | H:Napi complete | 执行Napi接口函数的回调函数 |
  | binder transaction | 同步binder调用 |
  | H:DispatchDisplaySync | 帧回调函数执行 |
  | H:aboutToBeDeleted | 组件析构时执行，在未使用复用机制时，FlushDirtyNodeUpdate和LazyForEach predict下会析构组件，导致刷新时组件重复创建 |
* 应用在进行图片解码操作时，需要申请对应内存，当PixelMap较大且使用共享内存时，RS主线程将经历较长的纹理上传时间，导致卡顿现象。图形侧提供了DMA内存零拷贝功能，可在绘制图片时避免纹理上传时间消耗。在hilog日志中搜索CreatePixelMapExtended，通过memoryType的值可以确认PixelMap创建时使用的内存类型，值为2表示共享内存，值为4表示DMA内存。

## 问题定位

ArkUI页面滑动卡顿丢帧问题的定位思路如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/fMqTsOXFSWCkq8wZQA-z9w/zh-cn_image_0000002628555206.png "点击放大")

使用DevEco Profiler Frame工具录制滑动卡顿丢帧过程，相关步骤可以参考[创建深度分析任务并进行录制](../harmonyos-guides/deep-recording.md)。如果已有待分析的Trace文件，可以参考[会话区](../harmonyos-guides/ide-profiler-session.md)中数据导入的步骤，将文件导入DevEco Profiler中查看分析。

1. 识别滑动过程：在DevEco Profiler上方的搜索框中输入H:APP\_LIST\_FLING搜索。

   如下图为搜索Trace关键字H:APP\_LIST\_FLING的示例，其中H:APP\_LIST\_FLING为示例应用（包名为com.example.myapplication，Trace中简写为e.myapplication）的滑动泳道，泳道中有颜色部分（图中为紫色）为页面滑动过程。点击H:APP\_LIST\_FLING泳道右侧星型按钮将泳道置顶，方便问题分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/SxhR5mfYTZqg0OR-jkA6lQ/zh-cn_image_0000002658914527.png "点击放大")
2. 识别卡顿丢帧位置。

   找到Frame泳道后点击左侧箭头展开，查看子泳道是否存在数据。

   * Frame泳道中的子泳道存在数据：

     根据H:APP\_LIST\_FLING泳道中的Trace点框选滑动过程的数据，点击Display泳道确认滑动过程的屏幕刷新率，如下图中可看到屏幕刷新率为120Hz左右（Avg Hz为119），则Vsync信号周期为8.3ms，如果应用侧或Render Service侧未在8.3ms内执行完渲染流程，会引起丢帧。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/oGPfiRCkQSeWjM21xC7Gaw/zh-cn_image_0000002628395302.png "点击放大")

     通过App Frame(如e.myapplication的下方)和RS Frame（render\_service下方）标签的泳道中可分别确认应用、Render Service卡顿丢帧的位置，出现卡顿丢帧（未在8.3ms执行完渲染流程）的地方显示为红色，正常完成渲染（在8.3ms内执行完渲染流程）的帧显示为绿色。

     如下图可看到应用（e.myapplication）存在几处卡顿丢帧，点击红色部分，然后点击"Details"区域"Corresponding Slice"下方左侧的箭头跳转到应用主线程泳道，结合App Frame卡顿丢帧处（红色部分）以及应用主线程的Trace信息，可以分析应用卡顿丢帧的原因。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/hhcQOrflSsqNQErUClGPPw/zh-cn_image_0000002658794577.png "点击放大")
   * Frame泳道中的子泳道无数据（比如打开.sys文件时会出现）时，可以找到render\_service泳道展开，通过其子泳道H:PreferredFrameRate确认屏幕刷新率，框选滑动过程Present Fence（图形上屏信号）泳道来确认滑动帧率，如下图可看到屏幕刷新率为120Hz，滑动过程FPS为88.9，远少于120，存在滑动卡顿丢帧的现象。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/x8RJEQtWRDKPuY2vhAgx2g/zh-cn_image_0000002628555210.png "点击放大")

     在滑动范围中，Present Fence泳道上缺少Trace点H:Waiting for Present Fence的部分（下图方框中空白的部分），很可能是存在丢帧问题，需要结合应用侧、Render Service侧主线程的Trace信息确认。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/BbX5lqkCRmCexmcXd7ag8g/zh-cn_image_0000002658914531.png "点击放大")
3. 确认卡顿丢帧模块。
   * Frame泳道中的子泳道存在数据：可根据滑动范围框选Frame泳道，查看应用和render\_service泳道相应的FPS值以及颜色来确认卡顿丢帧模块。
     + 应用进程卡顿丢帧：

       如下图为应用侧卡顿丢帧的示例（屏幕刷新率为120Hz），可看到应用泳道（e.myapplication）存在卡顿帧（红色），而render\_service泳道无卡顿帧（绿色）。应用泳道的FPS值为87.6，远少于120，应用侧存在卡顿丢帧，而render\_service泳道的FPS值少于120是应用侧发生丢帧，提交绘制相关数据较晚导致。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/QKGp4zbgSQ6QkyoDv5FOnw/zh-cn_image_0000002628395306.png "点击放大")
     + Render Service进程卡顿丢帧：

       如下图为Render Service卡顿丢帧的示例（屏幕刷新率为120Hz），可看到应用泳道无卡顿帧（绿色），而render\_service泳道存在卡顿帧（红色）。应用泳道的FPS值为122.0，而render\_service泳道的FPS值为11.9，远少于120，Render Service进程存在卡顿丢帧。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dRvzbjw6TZmRjVBrDIdLng/zh-cn_image_0000002658794581.png "点击放大")
   * Frame泳道中的子泳道无数据：可根据应用主线程和render\_service线程的Trace信息的宽度、密集特征来大致判断发生卡顿丢帧的模块。
     + 应用进程卡顿丢帧：

       如下图为应用侧卡顿丢帧的示例，可看到应用泳道中卡顿丢帧区域（方框部分）的Trace信息较宽且相连到一块，而右侧未丢帧处的Trace点较短且均匀分布。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/qauEpue4QaudAcCTfPxlSw/zh-cn_image_0000002628555214.png "点击放大")
     + Render Service进程卡顿丢帧：

       如下图为Render Service卡顿丢帧的示例，可看到应用泳道中的Trace信息较短且均匀分布，而render\_service泳道的Trace信息较宽且相连到一块。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/nzXcuGCrS9uo1RaELUoY4w/zh-cn_image_0000002658914535.png "点击放大")
4. 分析卡顿丢帧原因。

* 应用主进程卡顿丢帧分析：

  分析应用主线程卡顿丢帧问题，首先在hilog日志中搜索has changed during render关键字，如果日志中有大量State variable 'xxx' has changed during render日志打印，这是由于组件渲染绘制时有更新状态变量，一直触发节点刷新，该情况会导致滑动卡顿丢帧问题。

  ```txt
  11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
  11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
  11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
  11889-11889  C03947/com.exam...AceStateMgmt com.examp...lication  E     [(100000:100000:scope)] FIX THIS APPLICATION ERROR:  @Component 'XXXXXX'[11248]: State variable 'XXXXXX' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
  ```

  如没有上述大量日志打印，继续分析Frame工具抓取的Trace信息。

  屏幕刷新率为120Hz下，如果应用在8.3ms内未执行完渲染流程，会引起卡顿丢帧。未执行完渲染流程的情况有：
  + 单帧耗时长：Vsync信号到来时，应用处理输入事件、执行渲染流程耗时多。下图为单帧耗时长的示例（屏幕刷新率为120Hz），可看到H:ReceiveVsync（接收Vsync信号处理的Trace点）整体耗时为13.4ms，超过了8.3ms。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ZEvu57OZQbapssaPsjvuqQ/zh-cn_image_0000002628395310.png "点击放大")

    接收Vsync信号处理耗时主要包含渲染流程（Trace点为H:OnVsyncEvent）耗时以及预加载（Trace点为H:OnIdle）耗时，因此针对单帧耗时长问题，含有如下情况：
    - 渲染流程（Trace点为H:OnVsyncEvent）耗时多。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/l2EOSJIYQSCQsN-maFq3Pw/zh-cn_image_0000002658794585.png "点击放大")

      渲染流程耗时多，可分析H:OnVsyncEvent下方哪部分Trace点较宽来确认问题原因，可能的情况如下表所示：

      | Trace关键字 | 含义 | 耗时多的原因 |
      | --- | --- | --- |
      | H:DispatchDisplaySync | 帧回调函数执行 | 帧回调函数执行耗时业务逻辑 |
      | H:DispatchTouchEvent | 点击事件处理 | 点击事件处理时执行耗时逻辑 |
      | H:FlushDirtyNodeUpdate | 标脏组件刷新 | 多个状态变量更新，大量组件刷新 |
      | H:UITaskScheduler::FlushTask | 刷新UI界面 | 页面组件复杂，测量、布局耗时多 |
      | H:HandleOnAreaChangeEvent | 执行OnAreaChange回调函数 | 回调函数中执行耗时业务逻辑 |
      | H:HandleVisibleAreaChangeEvent | 执行OnVisibleChange回调函数 | 回调函数中执行耗时业务逻辑 |
    - 预加载（Trace点为H:OnIdle）耗时多。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nqGBrFurT8eehYnx6S6Zqw/zh-cn_image_0000002628555218.png "点击放大")

      预加载耗时多，可分析H:OnIdle下方哪部分Trace点较宽来确认问题原因，可能的情况如下表所示：

      | Trace关键字 | 含义 | 耗时多的原因 |
      | --- | --- | --- |
      | H:LazyForEach predict | LazyForEach预处理 | 未采用组件复用、懒加载条目构建时间长 |
      | H:List predict | 列表预加载 | 组件复杂，测量、布局耗时多 |
      | H:Preload FlowItem | 瀑布流（WaterFlow）组件的预加载 | 组件复杂，测量、布局耗时多 |
  + 帧间耗时长：应用执行业务逻辑或调用系统接口等耗时多，导致无法在Vsync信号到来时处理输入事件、执行渲染流程。下图帧间耗时长的示例（屏幕刷新率为120Hz），可看到在两个H:ReceiveVsync（接收Vsync信号处理的Trace点）之间存在耗时为25.1ms的Trace点（H:ExecuteJS），超过8.3ms，应用执行业务代码耗时较多，导致丢帧。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/LWvy3lr8TiOZJedo65qNag/zh-cn_image_0000002658914539.png "点击放大")

    除了业务代码耗时多，可能的情况还有执行同步binder调用（Trace点为binder transaction）耗时多、Napi接口函数的回调函数执行耗时多（Trace点为H:Napi complete）等，可以查看ArkTS Callstack和Callstack泳道的调用栈来确认相关代码，定位耗时函数。

  + Render Service渲染进程卡顿丢帧分析：

    Render Service渲染进程卡顿丢帧，可查看render\_service进程的RSUniRenderThread泳道是否存在单帧耗时长的情况。

    如下图可看到RSUniRenderThread泳道存在单帧耗时长（201.3ms）的情况，同时存在Trace点H:onCreateTexture，在绘制时创建8191\*7176大小的纹理。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/sD3Nqh3rQre_tNuP7w8XHA/zh-cn_image_0000002628395314.png "点击放大")

    在hilog日志中搜索CreatePixelMapExtended查看应用是否有创建像素图，如下日志示例中可以看到创建10800\*7176的高分辨率图片，memoryType值为2表示采用共享内存，而不是DMA内存，导致Render Service渲染进程卡顿丢帧。

    ```txt
    3551-27643    C02B61/com.exa...n/ImageSource  com.examp...lication  I     CreatePixelMapExtended success, imageId:1769788704094294, desiredSize: (0, 0), imageSize: (10800, 7176), desiredHdr: 1, hdrType : 1, memoryType : 2, cost 427949 us
    ```

## 分析结论

ArkUI页面滑动卡顿丢帧的原因有：

* 在组件渲染绘制时更新状态变量，一直触发节点刷新。
* 回调函数、点击事件处理函数中执行耗时业务逻辑。
* 多个状态变量更新，大量组件刷新。
* 页面组件复杂，在测量、布局时耗时较多。
* 未采用组件复用，频繁创建和销毁对象。
* binder调用过多、耗时多。
* 创建高分辨率图片时未采用DMA内存，在绘制图片时进行纹理上传。

## 修改建议

* 在组件渲染绘制时避免更新状态变量。
* 优化处理逻辑，减少不必要的流程，或者[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)将该耗时操作迁移到子线程中。
* 参考[状态刷新控制](../best-practices/bpta-state-refresh.md)、[渲染范围控制](../best-practices/bpta-control-rendering-range.md)优化。
* [组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，避免冗余的嵌套或者使用扁平化布局来优化嵌套层次。
* 参考[组件复用](../best-practices/bpta-component-reuse.md)优化。
* 减少binder调用，采用异步binder调用接口，或将binder相关调用迁移到子线程中。
* 参考[图片解码内存优化(ArkTS)](../harmonyos-guides/image-allocator-type.md)。
