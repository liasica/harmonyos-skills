---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-2
title: ArkUI页面侧滑返回响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面侧滑返回响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:469eb9c24a765c5fa217e903f89e7bb947a2655530e22a20d4cd61dc4b658af1
---

## 问题现象

在使用ArkUI框架开发的应用中，用户通过侧滑手势返回上一页时，页面响应速度慢，存在明显延迟。这导致用户需要多次尝试才能成功返回，并且有时完成滑动后页面仍未及时响应，影响了用户体验。

## 背景知识

* 页面侧滑返回响应时延：

  响应时延是用户使用移动设备时，从手指触摸屏幕（如点击按钮）到屏幕上有反应（如按钮呈现被按下的效果）的时间间隔。

  页面侧滑返回响应时延指用户滑动屏幕左或右侧，从当前页面返回到上一页面中，滑动完成、手指离开屏幕到当前页面开始退出的时间间隔。时间间隔越短，响应越快，用户体验上就越流畅。
* 整体处理流程：

  对于当前页面侧滑返回上一页面场景，设备上整体处理流程大致如下：

  1. 多模输入服务mmi\_service线程收到用户触摸屏幕的相关事件（比如按下、滑动、离开屏幕），根据窗口的触摸热区判定分发给返回手势窗口。
  2. 返回手势窗口识别用户滑动松手操作，下发返回事件给应用模块，应用模块收到返回事件后进行自身业务处理，启动页面返回，提交绘制指令给渲染服务render\_service。
  3. 渲染服务进行图形计算和渲染操作，将渲染结果写入到帧缓冲区（存储用于显示器输出的图像数据）中，将数据送到屏幕上显示。
* Trace：

  Trace文件是一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况。查看Trace文件可使用[SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host/tree/master/smartperf_host)工具。

  侧滑返回响应时延问题Trace关键字如下：

  | 关键字 | 线程/泳道 | 说明 |
  | --- | --- | --- |
  | H:originEventHandle code:501 | mmi\_service | 点击应用页面内容离手点。 |
  | H:DispatchTouchEvent 位置 type=1 | ohos.sceneboard | sceneboard应用收到点击离手的事件，返回手势窗口在该应用中。 |
  | H:[Gesture]backGesture | H:[Gesture]backGesture | 返回手势消费事件阶段。 |
  | H:ABILITY\_OR\_PAGE\_SWITCH | H:ABILITY\_OR\_PAGE\_SWITCH | 页面切换过程。 |
  | H:SendCommands | 应用包名 | 应用发送绘制请求，下方H:MarshRSTransactionData表示提交绘制相关数据给渲染服务。 |
  | H:RSMainThread::ProcessCommandUni[应用进程号，序号] | render\_service | 渲染服务处理渲染请求，在接收Vsync信号时执行，应用进程号、序号与应用发送渲染请求的transactionFlag相同。 |
  | H:RSHardwareThread::CommitAndReleaseLayers rate: 帧率，now：时间 | RSHardwareThread | 将GPU处理的渲染结果提交到显示硬件，now与H:RSMainThread::ProcessCommandUni上方的H:ReceiveVsync中的now字段一一对应。 |
  | H:JSAnimateTo | 应用包名 | 执行动画。 |

## 问题定位

以某应用侧滑返回首页响应时延267ms问题为例，按整体流程拆分总耗时，确定各模块耗时。

1. 多模输入模块耗时，为检测到手指离开屏幕的事件，与事件分发到SceneBoard应用（返回手势窗口所属的应用）的时间间隔。用SmartPerf打开Trace文件，在上方搜索框中输入H:originEventHandle code:501找到手指离开屏幕的地方。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/CTAc-tHxSM2RDJPYX5t_yg/zh-cn_image_0000002628395038.png "点击放大")

   接着以该点为起始点在ohos.sceneboard泳道中找到ohos.sceneboard应用收到该事件的地方（Trace点H:DispatchTouchEvent xxx type=1），根据两者之间的时间间隔得到多模输入模块耗时为3.3ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/x1VEtLe0RCOOIumdfZSknA/zh-cn_image_0000002658914257.png "点击放大")
2. 返回手势窗口模块耗时，起始点为ohos.sceneboard应用收到手指离开屏幕的事件（Trace关键字为H:DispatchTouchEvent位置type=1），终点为该事件处理完成的结束点，在返回手势结束点（Trace关键字为H:[Gesture]backGesture）的附近。从下图中可以得到该部分耗时为5.1ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/a8NPl2oPQvCVL__--jApBQ/zh-cn_image_0000002658794303.png "点击放大")
3. 应用模块耗时，为返回手势结束点（Trace关键字为H:[Gesture]backGesture）到页面切换（Trace关键字为H:ABILITY\_OR\_PAGE\_SWITCH）的起始点之间的时间间隔，从下图中可看到该部分耗时为12.9ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/seppBYc3TDKt1PevVQHQWQ/zh-cn_image_0000002628554940.png "点击放大")
4. 渲染服务模块耗时，为渲染服务处理应用发送的绘制请求到将GPU处理的渲染结果提交到显示硬件的时间。

   找到应用页面切换起始点、接收Vsync信号处，点击上方的Actual Timeline，在下方显示框中点击render\_service右侧的跳转箭头可以找到渲染服务处理该绘制请求相应的Vsync信号接收点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/9ECkASXdReqCBsOQfVbDfQ/zh-cn_image_0000002628395040.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/7_7w5388TACkuIpHxP1IAw/zh-cn_image_0000002658914259.png "点击放大")

   然后以render\_service此处Vsync信号接收点为起点，根据now时间值，在RSHardwareThread泳道中找到render\_service将该帧GPU处理的渲染结果提交到显示硬件的地方，最终得到渲染服务模块耗时14.6ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/HZo1o0pPRTG_Q4zHaBiNSg/zh-cn_image_0000002658794305.png "点击放大")

最终得到如下耗时拆分结果：

| 多模输入模块 | 返回手势窗口模块 | 应用 | 应用->渲染服务（应用结束点到渲染服务起始点） | 渲染服务 | 总和 |
| --- | --- | --- | --- | --- | --- |
| 3.3ms | 5.1ms | 12.9ms | 11.0ms | 14.6ms | 46.9ms |

按上述步骤分析得到总耗时为46.9ms，与问题反馈的总耗时267ms相差甚远。需要对各模块逐个分析、排查异常点。

1. 多模输入模块仅接收用户触发事件进行分发，并无其他逻辑处理。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zAFjSwPjRcOskId3-ZWgFw/zh-cn_image_0000002628554942.png "点击放大")
2. 返回手势窗口模块仅执行ArkTS业务逻辑，并将返回事件分发给应用，无异常点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/YMetIGqdQMGpjPiUf2KLcA/zh-cn_image_0000002628395042.png "点击放大")
3. 应用收到返回事件后执行自身业务逻辑，然后启动页面返回，提交绘制指令。排查应用在提交绘制指令前有启动动画，动画延时了210ms执行，如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/5Puq_6SEQWyOMR5T-xMphw/zh-cn_image_0000002658914261.png "点击放大")

   框选animateTo中的Trace关键字，在下方Slices中搜索viewPropertyHasChanged查看有状态变量刷新的组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/KFQLDuxaSlW3OSqxqOV_wA/zh-cn_image_0000002658794309.png "点击放大")

   使用Ark Inspector查看该组件，该组件为侧滑退出的页面，可知在侧滑退出时应用对当前页面执行了延时210ms的X轴位移动画，该延时动画导致侧滑返回的响应时延增加。

## 分析结论

在侧滑返回退出时，对当前页面执行了延时位移动效，导致侧滑返回响应慢问题。

## 修改建议

去除延时动效。
