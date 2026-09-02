---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-colorspace-faq
title: 色彩空间配置异常问题
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > Camera Kit常见问题 > 色彩空间配置异常问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:46b2fb671f8d338284c5352e39f99a6423351b7ead67937f95916a9419264fca
---

## 问题现象

应用处于后处理或视频编码场景时，处理后的图片或视频出现偏色、亮度过曝等效果异常的现象。

## 问题分析

应用在处理预览流数据或者录像流数据时，需正确处理色彩空间，否则会导致处理后的数据存在偏色、过曝等效果异常问题。具体原因如下：

1. 应用未主动设置色彩空间，默认SDR的色彩空间，配置相机输出流时使用了HDR对应的格式。
2. 应用主动设置色彩空间，配置相机输出流数据时使用了不符合当前色彩空间的格式。

## 解决措施

1. 通过[getActiveColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#getactivecolorspace12)（ArkTS）或者[OH\_CaptureSession\_GetActiveColorSpace](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_getactivecolorspace)（C/C++）查询当前相机会话生效的色彩空间，处理相机输出流数据时配置正确的色彩空间信息。
2. 根据查询的colorSpace色彩空间信息，相机应用可通过setColorSpace相关接口配置对应的色彩空间参数信息。

   * ImageReceiver场景（ArkTS）：若[使用ImageReceiver完成图片接收](image-receiver.md)时，首先需要将imageArrival事件监听获取底层返回的[Image](../harmonyos-references/arkts-apis-image-image.md)数据转成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)做图像数据处理或送显，并在创建[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)后，可通过[setColorSpace](../harmonyos-references/arkts-apis-image-pixelmap.md#setcolorspace10)设置图像的色彩空间属性。
   * NativeWindow场景（C/C++）：若使用[NativeWindow](../harmonyos-references/capi-nativewindow.md)对相机获取的预览流或录像流数据进行拷贝处理，为了避免数据拷贝时丢失色彩空间属性，可先通过[OH\_NativeWindow\_GetColorSpace](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_getcolorspace)获取OHNativeWindow色彩空间属性，再通过[OH\_NativeWindow\_SetColorSpace](../harmonyos-references/capi-external-window-h.md#oh_nativewindow_setcolorspace)设置NativeWindow色彩空间属性。
