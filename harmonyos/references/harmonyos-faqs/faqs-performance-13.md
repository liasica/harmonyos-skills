---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-13
title: 滑动浏览长图时有卡顿的情况
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 滑动浏览长图时有卡顿的情况
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e04f39e007d4caf3ce941500ad05cd4a5076e848711fbfabaee84a2984aadae1
---

## 问题现象

滑动操作浏览长图时，滑动过程十分卡顿，有阻塞感。

## 背景知识

* 刷新频率：每秒钟屏幕会刷新的次数，如120Hz是一秒内刷新120次，周期8.33ms。
* [Profiler Frame](../harmonyos-guides/ide-insight-session-frame.md)：DevEco Profiler是DevEco Studio提供的场景化调优工具，其中Frame可以帮助开发者深度分析性能问题，通过录制应用运行过程中的关键数据，从而识别卡顿丢帧、耗时长等问题的原因所在。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)为滑动手势事件接口，应用通过其监听用户在页面内容上的滑动操作，当滑动的最小距离达到设定的最小值时会触发滑动手势事件，应用收到该事件后会执行相应的业务流程。

## 问题定位

1. 查看帧率信息。

   首先查看屏幕刷新率，Frame泳道下的Display Vsync子泳道会显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计，如下图中，屏幕刷新率为119Hz。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/XlZl4Wb8RbucUsleLJWBew/zh-cn_image_0000002658914329.png "点击放大")

   然后查看应用主线程请求绘制渲染的周期，Trace中找到应用包名的泳道，通过H:SendCommands关键字查看应用发送的渲染请求，其中相邻的两个transactionFlag的时间间距，就是主线程请求绘制渲染的周期。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ti8FaSnCTF-Nrr5RRG27Tw/zh-cn_image_0000002658794375.png "点击放大")

   正常情况下主线程请求绘制渲染周期（如8.3ms）会与屏幕刷新率（如120Hz）对应，但如果主线程在执行耗时操作时，会导致两次请求绘制渲染的时间间隔变长，在120Hz屏幕刷新率下应用绘制的帧率少于120，出现卡顿、丢帧的情况。
2. 查看滑动手势事件是否使用animateTo。

   抓取日志发现使用了PanGesture滑动手势事件：

   ```screen
   I C03951/com.example.myapplication/InputKeyFlow: [(100002:100002:scope)] Pan accepted, tag = Stack
   ```

   通过Trace发现只能看到多次状态变量刷新，在应用收到手指离开屏幕的事件处，仅更新页面偏移状态，没有调用animateTo启动动画：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/I0_gwDILQsimFCQKgbt7IQ/zh-cn_image_0000002628555010.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Q93eaPGEQiighxU6cY76fg/zh-cn_image_0000002628395110.png "点击放大")

## 分析结论

使用PanGesture滑动手势事件时没有设置惯性动画，致使滑动手势停止时长图的滑动效果立刻停止，即表现为滑动卡顿。

## 修改建议

在滑动离手后增加滑动动效，可参考[长图滑动的惯性滚动效果](../architecture-guides/inertial_sliding-0000002308946264.md)。
