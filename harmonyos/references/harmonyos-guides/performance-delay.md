---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-delay
title: 时延
breadcrumb: 指南 > 应用体验建议 > 应用性能体验建议 > 时延
category: harmonyos-guides
scraped_at: 2026-09-02T14:51:00+08:00
doc_updated_at: 2026-06-17
content_hash: sha256:d85c3b130762a056a482f83f116fa1cf368b539afac449df32103802c05fd143
---

## 应用或元服务启动加载完成快

|  |  |  |
| --- | --- | --- |
| **描述** | | 应用启动加载完成时延应≤1100ms；  元服务启动加载完成时延应≤340ms。 |
| **类型** | | 规则 |
| **适用设备** | | 手机，平板，PC/2in1，智慧屏，车机，手表 |
| **应用形态适用性** | | 鸿蒙应用，鸿蒙元服务 |
| **说明** | | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 应用或元服务冷启动过程动画/视频时延

|  |  |  |
| --- | --- | --- |
| **描述** | | 如果应用或元服务冷启动过程动画/视频时延大于3s，建议增加进度提示。 |
| **类型** | | 建议 |
| **适用设备** | | 手机，平板，PC/2in1，智慧屏，车机，手表 |
| **应用形态适用性** | | 鸿蒙应用，鸿蒙元服务 |
| **说明** | | 无 |

## 应用或元服务应用内点击操作响应快

|  |  |  |
| --- | --- | --- |
| **描述** | | 应用或元服务内点击操作响应时延应≤100ms。 |
| **类型** | | 规则 |
| **适用设备** | | 手机，平板，PC/2in1，智慧屏，车机，手表 |
| **应用形态适用性** | | 鸿蒙应用，鸿蒙元服务 |
| **说明** | | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 应用或元服务应用内点击操作完成快

|  |  |  |
| --- | --- | --- |
| **描述** | | 应用内点击操作完成时延应≤900ms；  元服务内点击操作完成时延应≤1400ms；  小程序内点击操作完成时延应≤1400ms。 |
| **类型** | | 规则 |
| **适用设备** | | 手机，平板，PC/2in1，智慧屏，车机，手表 |
| **应用形态适用性** | | 鸿蒙应用，鸿蒙元服务 |
| **说明** | | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 应用或元服务内滑动操作响应快

|  |  |  |
| --- | --- | --- |
| **描述** | | 抛滑（速度大于300mm/s ）场景：触屏响应时延应≤80ms；  拖滑（速度小于100mm/s）场景： 触屏响应时延应≤60ms。 |
| **类型** | | 规则 |
| **适用设备** | | 手机，平板，PC/2in1，智慧屏，车机，手表 |
| **应用形态适用性** | | 鸿蒙应用，鸿蒙元服务 |
| **说明** | | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 在线长视频类应用播放起播快

|  |  |
| --- | --- |
| **描述** | 应用在线视频播放起播时延应≤800ms。 |
| **类型** | 规则 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机 |
| **应用形态适用性** | 鸿蒙应用 |
| **说明** | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 在线长视频类应用Seek操作播放快

|  |  |
| --- | --- |
| **描述** | 拖动进度条40%~60%位置后，应用在线视频播放起播时延应≤800ms。 |
| **类型** | 规则 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机 |
| **应用形态适用性** | 鸿蒙应用 |
| **说明** | [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 在线短视频类应用快速切换播放起播快

|  |  |
| --- | --- |
| **描述** | 应用内滑动视频，新视频起播时延应≤230ms。 |
| **类型** | 规则 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机 |
| **应用形态适用性** | 鸿蒙应用 |
| **说明** | [开发自测试：DevEco Studio AppAnalyzer 性能分析诊断](../best-practices/bpta-performance-detection.md#section135451444171)  [本地自测试：DevEco Testing 性能测试](performance-testing.md)  [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |

## 在线短视频类应用Seek操作播放快

|  |  |
| --- | --- |
| **描述** | 拖动进度条40%~60%位置后，应用在线短视频起播时延应≤100ms。 |
| **类型** | 规则 |
| **适用设备** | 手机，平板，PC/2in1，智慧屏，车机 |
| **应用形态适用性** | 鸿蒙应用 |
| **说明** | [云端自测试：AppGallery Connect 云测试性能检测](../app/agc-help-cloudtest-performancetest-0000002289647209.md) |
