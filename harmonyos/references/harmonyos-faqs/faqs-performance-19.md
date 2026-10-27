---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-19
title: 点击评论框进入评论页面时，软键盘弹出慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击评论框进入评论页面时，软键盘弹出慢
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:53d077f3fb9d8ab4aa6153184a6250987d15417b1c9ff39dc82b8b3038f7be54
---

## 问题现象

点击评论框进入评论页面时，软键盘弹出慢，延迟一段时间后才显示。

## 背景知识

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能。更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。
* 在RN框架中，RNOH\_JS线程负责构造节点树并提交到应用主线程完成渲染。
* Trace关键字说明：

  | 关键字 | 说明 |
  | --- | --- |
  | H:DispatchTouchEvent id:X, pointX=XXX, pointY=XXX type=1 | 应用收到手指离开屏幕事件 |
  | H:[TextField:组件ID] on focus | 输入框获取焦点 |
  | H:RequestKeyboard | 请求显示软键盘 |
  | H:ShadowTree::commit | RNOH\_JS线程提交节点树到应用主线程 |

## 问题定位

1. 使用DevEco Profiler Frame分析工具抓取点击评论框到软键盘显示过程的Trace信息，在搜索框中搜索应用收到手指离开屏幕事件以及输入框获取焦点的Trace关键字，可以看到输入框获取焦点之后应用请求显示软键盘。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Q0ywXWtVRJKIr3oS8WtS_Q/zh-cn_image_0000002628395146.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ImHb1xEPSe2p4x_RP2PBdw/zh-cn_image_0000002658914371.png "点击放大")
2. 查看应用收到手指离开屏幕事件的Trace关键字以及输入框获取焦点的Trace关键字间的时间间隔，可知应用在收到手指离开屏幕事件后过了829.5ms，输入框才获取到焦点，输入框获取焦点较慢导致了软键盘弹出慢。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/qCC9zag7SX6P-cGHd7ZNPA/zh-cn_image_0000002658794415.png "点击放大")
3. 查看该过程线程的运行状态可以看到线程大部分时间处于休眠态（Sleeping）以及运行态（Running），并没有出现长时间持续处于运行态，因此可知并不是主线程执行耗时任务导致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/C8ci_RjxS7makSP-dUJOWg/zh-cn_image_0000002628555052.png "点击放大")
4. 使用ArkUI Inspector工具抓取应用页面布局，发现该应用页面为RN页面，需要分析RNOH\_JS线程上的Trace信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5f9oNculRUabSL3FglWD7Q/zh-cn_image_0000002628395148.png "点击放大")
5. 查看RNOH\_JS线程，发现线程有多次提交组件树到主线程绘制，耗时主要集中在节点树构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/0vcaecaQR72OgbpSk66zGw/zh-cn_image_0000002658914373.png "点击放大")
6. 通过ArkUI Inspector查看应用页布局发现，应用页面组件较多，布局复杂，文本框组件的层级达到21。页面绘制整体耗时较多导致文本框获取焦点较慢，软键盘显示时延较长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Suf2kFh5RCG4vYzV7D0fLA/zh-cn_image_0000002658794417.png "点击放大")

## 分析结论

应用页面布局复杂，绘制耗时较多，文本框绘制、获取焦点慢，导致点击评论框时，软键盘弹出慢。

## 修改建议

[组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，减少嵌套层级或采用扁平化布局。
