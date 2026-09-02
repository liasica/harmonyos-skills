---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-700
title: 相机预览画面拉伸
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 相机预览画面拉伸
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:ca54a974aa2b3aa20a5179afa54be1355511f1e53b2d9090c6b7ba0abdc58ed4
---

## 问题现象

在使用手机相机进行拍照时，预览画面出现拉伸变形，影响用户体验。

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。
* [自定义渲染 (XComponent)](../harmonyos-guides/napi-xcomponent-guidelines.md)：XComponent持有一个Surface，开发者能通过调用NativeWindow等接口，申请并提交Buffer至图形队列，以此方式将自绘制内容传送至该Surface。XComponent负责将此Surface整合进UI界面，其中展示的内容正是开发者传送的自绘制内容。Surface的默认位置与大小与XComponent组件一致，开发者可利用setXComponentSurfaceRect接口自定义调整Surface的位置和大小。

## 问题定位

在日志中可以搜索关键字ValidateOutputProfile，检查预览流与输出流的分辨率的宽高比是否一致。如下所示，outputType:0代表预览流，分辨率为800×480，宽高比为5:3，outputType:1代表输出流，分辨率为1280×720，宽高比为16:9，由此可知预览流和输出流分辨率宽高比不一致。

```shell
07-22 14:55:11.637   23295-23295   C02B01/应用包名/CAMERA    应用包名     I     {ValidateOutputProfile():4817} CaptureSession::ValidateOutputProfile profile:w(800),h(480),f(1003) outputType:0
07-22 14:55:50.463   23295-23295   C02B01/应用包名/CAMERA    应用包名     I     {ValidateOutputProfile():4817} CaptureSession::ValidateOutputProfile profile:w(1280),h(720),f(2000) outputType:1
```

## 分析结论

由于预览流与输出流的宽高比不一致，导致系统在渲染预览画面时进行非等比缩放，从而造成画面拉伸。

## 修改建议

获取设备支持的预览分辨率，然后根据手机屏幕的宽高设置最合适的预览流分辨率，并使Surface和XComponent的宽高一致。参考[自定义相机预览](../harmonyos-guides/camera-preview.md)。
