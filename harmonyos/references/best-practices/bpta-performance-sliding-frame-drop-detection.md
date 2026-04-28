---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-sliding-frame-drop-detection
title: 滑动丢帧类问题检测方法
breadcrumb: 最佳实践 > 性能 > 性能检测 > 运行态性能检测 > 滑动丢帧类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:19+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:6903c4fd833b029a87e45df8146c1a8767aed710cda236d0d2f2cef899170600
---

在滑动操作期间，丢帧问题尤为明显：本应流畅的动画会出现间断。这是因为渲染内容所需的时间超过了系统显示相应帧的时间，导致画面在移动时会在一帧或多帧中暂停，从而产生卡顿。

## 丢帧故障原理

图形系统采用了统一渲染模式。在整个渲染流程中，首先由应用侧响应消费者的屏幕点击等输入事件，处理完成后提交给Render Service（渲染服务）。Render Service协调GPU等资源进行处理，再将最终图像统一送到屏幕上显示。在整个处理流程中，应用侧和Render Service侧都可能出现卡顿，导致最终用户观察到丢帧。如果应用主线程或Render Service中的单帧绘制过程长时间阻塞，则会导致绘制无法按时完成，形成丢帧。滑动丢帧检测原理详见：[滑动事件检测](../harmonyos-guides/perf-detection.md#section191899590502)。

## 滑动丢帧检测

滑动丢帧事件用于检测列表滑动过程中出现的卡顿现象，具体详情请参阅[滑动丢帧事件介绍](../harmonyos-guides/hiappevent-watcher-scroll-jank-event.md)。开发者可以通过HiAppEvent接口[订阅滑动丢帧事件](../harmonyos-guides/hiappevent-watcher-scroll-jank-arkts.md)，当列表滑动中出现卡顿时，系统将上报故障事件。利用事件中的维测信息，可以有效定位滑动卡顿问题。
