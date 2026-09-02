---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-3
title: 平板相机拍照预览画面拉伸
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板相机拍照预览画面拉伸
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:48a31a1d2b04b27cc9baa64321427a66fdb7b98b9ce8bad3c1e63194a78358fc
---

## 问题现象

应用在手机上拍照正常，在平板上拍照时，预览画面被拉伸。

## 背景知识

* [相机预览](../harmonyos-guides/camera-preview.md)：预览是启动相机后看见的画面，通常在拍照和录像前执行。
* [Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)：相机配置信息项。包含预览输出流的分辨率宽度和高度。
* [CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)：相机输出能力项。包含支持的预览配置信息集合。

## 问题定位

1. 检查代码是否通过CameraOutputCapability类中的previewProfiles属性获取当前设备支持的预览分辨率，并选取跟设备宽高接近的分辨率作为预览输出流。
2. 检查代码中预览输出流的宽高分辨率和XComponent组件的宽高分辨率是否保持一致。

## 分析结论

应用未获取当前设备支持的预览分辨率，并设置预览输出流的宽高分辨率和XComponent组件的宽高分辨率保持一致。

## 修改建议

获取设备支持的预览分辨率，然后根据手机屏幕的宽高设置最合适的预览流分辨率，并使Surface和XComponent的宽高一致。具体可参考[自定义相机预览](../harmonyos-guides/camera-preview.md)。
