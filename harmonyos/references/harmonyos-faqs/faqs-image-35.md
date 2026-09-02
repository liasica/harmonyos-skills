---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-35
title: 如何将一张图片写入到另一张图片中
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将一张图片写入到另一张图片中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:78abbef00e69c71921f327e3fe0da6d656de7938772a24f799752ab0d6cbee1a
---

## 问题现象

在图片开发过程中，如何将图片写入另一张背景图片中，且背景图片需要大于原图片大小？

需要写入的图片：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yDhxwNyGS2Ol6K_XM9BxnA/zh-cn_image_0000002658791871.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)：Image为图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。
* [@ohos.multimedia.image (图片处理)](../harmonyos-references/js-apis-image.md)：提供图片解码、图片编码、图片编辑和处理、图片接收等能力，包括创建PixelMap、读取图像像素数据、读取区域内的图片数据等。
* [readPixelsSync](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelssync12)：固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入PositionArea.pixels缓冲区中，该区域由PositionArea.region指定，同步返回结果。
* [readPixelsToBufferSync](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffersync12)：按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中，同步返回结果。
* [writePixelsSync](../harmonyos-references/arkts-apis-image-pixelmap.md#writepixelssync12)：固定按照BGRA\_8888格式，读取PositionArea.pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由PositionArea.region指定，同步返回结果。

## 解决方案

创建指定格式的PixelMap。用readPixelsSync方法，固定按照BGRA\_8888格式，读取PixelMap指定区域内的图像像素数据，并写入PositionArea.pixels缓冲区中。再用writePixelsSync方法，固定按照BGRA\_8888格式，读取PositionArea.pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内。

```ts
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PassImage {
  @State imagePix: image.PixelMap | null = null;
  arr: ArrayBuffer | null = null;

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 获取resourceManager资源管理器
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    let fd = resourceMgr.getRawFdSync('picture.jpg');
    let source = image.createImageSource(fd);
    let imPix = source.createPixelMapSync();
    let imInfo = imPix.getImageInfoSync();
    this.imagePix = imPix;
    // 创建像素数据
    // 下述width、height加1k创建比原图更大的像素区域模拟写入另一张图片中，实际情况请以需要写入的图片宽高为准
    const width = imInfo.size.width + 1000;
    const height = imInfo.size.height + 1000;
    const bytesPerPixel = 4;
    const bufferSize = width * height * bytesPerPixel;
    const colorBuffer = new ArrayBuffer(bufferSize);
    // 创建PixelMap
    const bufferArr = new Uint8Array(colorBuffer);
    // 填充背景色
    for (let i = 0; i < bufferArr.length; i += bytesPerPixel) {
      bufferArr[i] = 0xF5; // B通道（原R通道）
      bufferArr[i+1] = 0xF3; // G通道
      bufferArr[i+2] = 0xF1; // R通道（原B通道）
      bufferArr[i+3] = 0xFF; // Alpha通道
    }
    const opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.BGRA_8888,
      size: { width, height }
    };
    this.imagePix = image.createPixelMapSync(colorBuffer, opts);
    let pixelBytesNumber: number = imPix.getPixelBytesNumber();
    const readBuffer = new ArrayBuffer(pixelBytesNumber);
    const area: image.PositionArea = {
      pixels: readBuffer, // 源图片的像素数据
      offset: 0, // 数据起始偏移量
      stride: imInfo.size.width * 4, // 每行字节数（源图片宽度*4）
      region: {
        size: { width: imInfo.size.width, height: imInfo.size.height }, // 写入区域尺寸（源图片尺寸）
        x: 0, // 目标位置x坐标
        y: 0 // 目标位置y坐标
      }
    };
    // 写入缓存区使用下列方法，固定按照BGRA_8888格式，读取PixelMap指定区域内的图像像素数据，并写入PositionArea.pixels缓冲区中
    imPix.readPixelsSync(area);
    // 固定按照BGRA_8888格式，读取PositionArea.pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内
    this.imagePix.writePixelsSync(area);
    resourceMgr.closeRawFd('picture.jpg');
  }

  build() {
    Column() {
      Image(this.imagePix).width('100%').objectFit(ImageFit.Auto)
    }.width('100%').height('100%')
  }
}
```

## 常见FAQ

Q：其他平台中bitmap.setPixels对应HarmonyOS是什么实现方式？

A：其他平台中bitmap.setPixels方法可以使用[writePixels](../harmonyos-references/arkts-apis-image-pixelmap.md#writepixels7)方法实现。
