---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-specification
title: 模拟器与真机的差异
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 概述 > 模拟器与真机的差异
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:89ff79286347556b342836c4c553899fc704b6416d15e8874af1e61fa78c77d1
---

模拟器是开发和调试HarmonyOS应用/元服务的便捷工具，例如不需要配置服务器域名即可开发和调试元服务，在大多数情况下，模拟器上推包调试不需要签名，但部分Kit仍需签名后才能正常运行，具体要求请参考Kit的开发指南。

由于模拟器和真机在硬件和能力上存在差异，部分功能场景仍需在真机上进行开发。您可以通过阅读本文档来决定哪些功能在模拟器中测试，哪些功能在真机上测试。

## 性能差异

模拟器是运行在Mac或Windows电脑上的虚拟机应用，会使用电脑的硬件资源，包括CPU、内存和网络连接等。这些资源在容量和速度上可能与真机存在显著差异。因此，模拟器不适合用于测试应用/元服务的性能（如数据处理、图形渲染、网络速度）、资源占用（如内存、CPU、功耗），模拟器的性能测试结果仅能用于评估应用功能的相对差异。如需获取真实场景下的用户体验数据，建议在真机上进行测试。

## 显示效果差异

* 模拟器使用电脑的显示器，与真机屏幕不同，可能会导致文本和图像在模拟器上出现边缘锯齿。放大模拟器窗口比例可以使文字和图像更清晰。
* 电脑屏幕的色域范围可能与移动设备不同，从而导致颜色显示不准确。
* 模拟器不支持屏幕亮度调节。

## 图形接口差异

* Mac模拟器不支持OpenGL ES 3.1、3.2接口。
* DevEco Studio 6.1.0 Beta2之前的版本，不支持Vulkan接口，从DevEco Studio 6.1.0 Beta2版本开始，支持除vkGetSwapchainGrallocUsageOHOS、vkAcquireImageOHOS、vkQueueSignalReleaseImageOHOS之外的接口。

## 多媒体差异

* 模拟器不支持heif格式的图片。
* 视频播放：模拟器仅支持h264文件格式，并且是RGBA像素格式的视频文件。
* 模拟器不支持视频录制/转码/处理、屏幕录像。

## Kit能力差异

当前部分Kit在模拟器上使用时，和真机存在差异，具体请参考对应Kit简介。

如遇到因Kit能力不支持导致的应用闪退问题，可以尝试使用[动态引入Kit](arkts-dynamic-import.md#动态import实现方案介绍)的方式规避此异常问题。

Kit不支持导致的报错信息如：

```
1. LastFatalMessage:[default] [LoadJSPandaFile:00] resolveBufferCallback get hsp buffer failed，hsp path:/data/storage/el1/bundle/com.huawei.hmos.{KitName}.kit
```

## 其他差异

**表1**

| 模拟器和真机的其他重要差异 | 影响场景 |
| --- | --- |
| SIM卡 | 不支持拨打电话、发送短信 |
| USB | 不支持连接、数据传输 |
| 蓝牙 | 不支持蓝牙设备扫描、连接、数据传输 |
| 星闪 | 不支持星闪设备扫描、连接、数据传输、分布式能力 |
| NFC | 不支持NFC卡片读写、刷卡 |
| TEE（Trusted Execution Environment，可信执行环境） | 不支持安全GPS、设备证书等，部分安全相关Kit暂不支持，详情参考[安全Kit简介](system-security.md) |
| NPU | 部分AI相关Kit暂不支持，详情参考[AI Kit简介](hmaf-introduction.md) |
| 生物识别 | 不支持指纹、人脸认证等 |
| 摄像头/麦克风 | 依赖电脑设备，不支持多摄像头切换（广角/长焦）、闪光灯、降噪算法等 |
| 电源 | 模拟电源，不支持温控、快充等场景 |
