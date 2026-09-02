---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-44
title: 拉起相机时，预览界面花屏
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 拉起相机时，预览界面花屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:424e45459c194060f78e69646e1107a4e992625bbbb02754d37879c262807577
---

## 问题现象

相机类应用，打开相机后，查看相机预览界面，出现花屏问题。

## 背景知识

* 图像数据有三要素，分别为width、height、stride。根据[相机预览花屏解决方案](../harmonyos-guides/camera-preview-glitch-solution.md)，当width与stride不一致时，需要对stride进行处理，处理无效像素后解析出正确的像素数据，避免出现预览流花屏。
* stride指在内存中每行像素实际占用的字节数，在不同的平台上的值不同，开发者需根据实际业务获取stride后做处理适配。
* [getComponent](../harmonyos-references/arkts-apis-image-image.md#getcomponent9)可以根据图像的组件类型从图像中获取组件缓存并使用callback返回结果。通过预览流帧数据的返回值image.Component.rowStride可获取stride。

## 问题定位

检查应用中使用的stride，排查应用在处理图像数据时设置的stride是否合理。应用处理图像数据时获取到的stride的值为1088，与width的值不相等，且未对width进行处理。

```screen
onImageArrival(receiver: image.ImageReceiver): void {
  // 注册imageArrival监听
  receiver.on('imageArrival', () => {
    receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
      if (err || nextImage === undefined) {
        // 错误处理
        // ...
        return;
      }
      if (nextImage) {
        nextImage.getComponent(image.ComponentType.JPEG, async (_err, component: image.Component) => {
          let width = 1080;
          let height = 1080;
          let stride = component.rowStride; // 获取到的stride的值为1088
          let pixelMap = await image.createPixelMap(component.byteBuffer, {
            size: {
              height: height,
              width: width
            },
            srcPixelFormat: image.PixelMapFormat.NV21
          })
          AppStorage.setOrCreate('stridePixel', pixelMap);
          nextImage.release();
        })
      }
    });
  })
}
```

## 分析结论

应用在处理图像数据时，未根据图像数据的stride对width进行额外处理。

## 修改建议

根据图像数据的stride对width进行处理，可以参考[处理图像预览流](../harmonyos-guides/camera-dual-channel-preview.md#用于处理图像的第一路预览流)中第4步的代码。完整实例可以参考[双路预览完整示例](../harmonyos-guides/camera-dual-channel-preview.md#完整示例)。
