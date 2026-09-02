---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-52
title: 自定义相机双路预览通过Image组件显示ImageReceiver接收的预览流图像异常
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 自定义相机双路预览通过Image组件显示ImageReceiver接收的预览流图像异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9dcc7f3c238c747b4a382bda6f11af05829042c11ea5cd0cb931f858287f7a81
---

## 问题现象

自定义相机双路预览，将ImageReceiver接收到的预览图像流通过Image组件显示，Image组件的objectFit属性设置为ImageFit.Contain，但是Image组件不能完整显示预览图像流，显示的画面不完整。用于显示预览图像数据的Image组件的UI描述如下：

```screen
Column() {
  // this.imagePixelMap为ImageReceiver接收的预览流数据
  Image(this.imagePixelMap)
    .width('100%')
    .height('100%')
    .rotate({ angle: -90 })       // 组件逆时针旋转90度，用于适应相机预览流的旋转角度
    .objectFit(ImageFit.Contain)  // 设置图片的填充，使得预览流画面在Image组件中完整显示
    .backgroundColor(Color.Black)
}
.clip(true)
.width(this.floatWindowWidth)     // 组件宽
.height(this.floatWindowHeight)   // 组件高
```

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，用于在应用中显示图片，支持加载PixelMap类型的图片数据。[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)用于设置图片的填充效果，设置为[ImageFit.Contain](../harmonyos-references/ts-appendix-enums.md#imagefit)后，将保持宽高比进行缩小或者放大，使得图片或视频完全显示在显示边界内。
* 双路预览即应用可同时使用两路预览流，一路通过XComponent的surface获取预览流数据，一路通过ImageReceiver的surface获取拍照流的数据，具体可参考：[双路预览](../harmonyos-guides/camera-dual-channel-preview.md)。
* [clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)属性表示是否对子组件超出当前组件范围外的区域进行裁剪。[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)属性用于设置组件旋转。

## 问题定位

为了适应相机预览流图像的旋转角度，将Image组件逆时针旋转了90度，若组件宽高不一致时，旋转后会导致Image组件的一部分超出父容器组件的范围，同时因为父容器Column组件设置了clip属性为true，这将导致Image组件旋转后超出Column组件的部分将被裁剪，若被裁剪的部分包含图像，则会导致图像显示不完整。

## 分析结论

Image组件旋转后超出了父容器Column组件的范围，同时Column组件设置了clip属性为true，将Image组件超出Column组件的部分裁剪，被裁剪的部分包括了显示的相机预览流画面，导致相机预览流图像不能完整显示。

## 修改建议

不通过旋转Image组件来适应相机预览流图像的旋转。调用[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)的[getPreviewRotation](../harmonyos-references/arkts-apis-camera-previewoutput.md#getpreviewrotation12)接口，获取预览流的旋转角度。在[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)的[imageArrival](../harmonyos-references/arkts-apis-image-imagereceiver.md#on9)回调中接收到预览流图像后，通过获取的预览流旋转角度调用[PixelMap.rotate](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9)来旋转预览流图像将图像调正。
