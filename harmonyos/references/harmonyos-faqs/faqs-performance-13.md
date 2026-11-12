---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-13
title: 滑动浏览长图时有卡顿的情况
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 滑动浏览长图时有卡顿的情况
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-22
content_hash: sha256:e025264ddd74e7da4ab0dc49dddb6638ddacb1cc7804cf3179b982dd6c4e12ff
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/4R2JNmclTFS1hjt88gwN0A/zh-cn_image_0000002658914329.png?HW-CC-KV=V1&HW-CC-Date=20261112T233216Z&HW-CC-Expire=31536000000&HW-CC-Sign=E227F216C30FC601EB5DAAE4875D5F232FB6F87DAA70C79B07D87EF31D47D5BB "点击放大")

   然后查看应用主线程请求绘制渲染的周期，Trace中找到应用包名的泳道，通过H:SendCommands关键字查看应用发送的渲染请求，其中相邻的两个transactionFlag的时间间距，就是主线程请求绘制渲染的周期。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/WDDN9CWYRAKVNevs6vC3fQ/zh-cn_image_0000002658794375.png?HW-CC-KV=V1&HW-CC-Date=20261112T233216Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AEDB6020160E04E0B5B3D770946180C6D2C25044276940327DA31B02226167C "点击放大")

   正常情况下主线程请求绘制渲染周期（如8.3ms）会与屏幕刷新率（如120Hz）对应，但如果主线程在执行耗时操作时，会导致两次请求绘制渲染的时间间隔变长，在120Hz屏幕刷新率下应用绘制的帧率少于120，出现卡顿、丢帧的情况。
2. 查看滑动手势事件是否使用animateTo。

   抓取日志发现使用了PanGesture滑动手势事件：

   ```screen
   I C03951/com.example.myapplication/InputKeyFlow: [(100002:100002:scope)] Pan accepted, tag = Stack
   ```

   通过Trace发现只能看到多次状态变量刷新，在应用收到手指离开屏幕的事件处，仅更新页面偏移状态，没有调用animateTo启动动画：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/N8UW6OWuQSWlfUyy60Z-zA/zh-cn_image_0000002628555010.png?HW-CC-KV=V1&HW-CC-Date=20261112T233216Z&HW-CC-Expire=31536000000&HW-CC-Sign=D92CAD53DACE559292E1EA2D4E06A11053B7F31F96651B081197CC11B4260C42 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/M7ISiAlBTOWs_z_gx5m61Q/zh-cn_image_0000002628395110.png?HW-CC-KV=V1&HW-CC-Date=20261112T233216Z&HW-CC-Expire=31536000000&HW-CC-Sign=25D93C40CF2F1D3114F7C1221EEEB4C4D82EF34671FC6C00BA331401B6E66779 "点击放大")

## 分析结论

使用PanGesture滑动手势事件时没有设置惯性动画，致使滑动手势停止时长图的滑动效果立刻停止，即表现为滑动卡顿。

## 修改建议

在滑动离手后增加滑动动效。
