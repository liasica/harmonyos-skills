---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-37
title: 如何将图片的ArrayBuffer处理成黑白、灰度、彩色三种颜色
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将图片的ArrayBuffer处理成黑白、灰度、彩色三种颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d7e3c7821108480c8aed78c1ce9e8510590a43b7fae22fc8d06a27eb55dc1194
---

## 问题现象

图片处理过程中，某些场景需要将拍摄的图片进行黑白处理形成艺术性照片，如何将图片进行黑白处理、灰度处理、彩色处理？

## 背景知识

* [image.createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource)：通过缓冲区创建ImageSource实例。
* [createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)：通过图片解码参数创建PixelMap对象。

## 解决方案

1. 获取图片的像素数据（RGBA格式）。
2. 遍历每个像素，根据需求修改RGB值。
3. 将处理后的数据重新渲染为图片。

对于灰度图像效果，也可以使用[图像效果](../harmonyos-references/ts-universal-attributes-image-effect.md)中的[grayscale](../harmonyos-references/ts-universal-attributes-image-effect.md#grayscale18)为组件添加灰度效果，示例如下。

```ts
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

// 获取图片ArrayBuffer（示例函数）
async function getImageArrayBuffer(context: common.Context): Promise<ArrayBuffer> {
  // 这里以资源文件为例，实际可以是网络或沙箱路径
  const resourceManager = context.resourceManager;
  const imageData = await resourceManager.getMediaContent($r('app.media.example').id);
  return imageData.buffer;
}

// 像素处理函数
async function processImageData(context: common.Context, mode: 'gray' | 'bw'): Promise<image.PixelMap> {
  // 1.获取原始ArrayBuffer
  const arrayBuffer = await getImageArrayBuffer(context);

  // 2.创建ImageSource
  const imageSource = image.createImageSource(arrayBuffer);

  // 3.创建解码选项
  const decodingOptions: image.DecodingOptions = {
    desiredSize: { width: 500, height: 500 } // 按需调整尺寸
  };

  // 4.解码获取PixelMap
  const pixelMap = await imageSource.createPixelMap(decodingOptions);
  const imageInfo = await pixelMap.getImageInfo();

  // 5.读取像素数据
  const buffer = new ArrayBuffer(1024000);
  await pixelMap.readPixelsToBuffer(buffer);
  const data = new Uint8Array(buffer);

  // 6.处理像素数据
  const processPixel = (() => {
    switch (mode) {
      case 'gray':
        return (r: number, g: number, b: number) => {
          const gray = 0.299 * r + 0.587 * g + 0.114 * b;
          return [gray, gray, gray];
        };
      case 'bw':
        return (r: number, g: number, b: number) => {
          const gray = 0.299 * r + 0.587 * g + 0.114 * b;
          const bw = gray > 128 ? 255 : 0;
          return [bw, bw, bw];
        };
      default:
        return (r: number, g: number, b: number) => [r, g, b];
    }
  })();

  // 7.遍历并修改像素
  for (let i = 0; i < data.length; i += 4) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];

    const result = processPixel(r, g, b);
    const nr = result[0];
    const ng = result[1];
    const nb = result[2];

    data[i] = nr; // R
    data[i + 1] = ng; // G
    data[i + 2] = nb; // B
    // Alpha通道保持不变(data[i+3])
  }

  // 8.创建新PixelMap
  return image.createPixelMap(data.buffer, {
    size: { width: imageInfo.size.width, height: imageInfo.size.height },
    pixelFormat: image.PixelMapFormat.RGBA_8888,
    alphaType: image.AlphaType.PREMUL
  });
}

// UI组件使用示例
@Entry
@Component
struct ImageToGrayOrBlack {
  @State grayImage: PixelMap | null = null;
  @State bwImage: PixelMap | null = null;

  aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    processImageData(context, 'gray').then((gray) => {
      this.grayImage = gray;
    });

    processImageData(context, 'bw').then((bw) => {
      this.bwImage = bw;
    });
  }

  build() {
    Column() {
      // 彩色图片
      Image($r('app.media.example'))
        .width(200)
        .height(200)
        .margin(10);

      // 灰度图片
      Row() {
        Image(this.grayImage)
          .width(200)
          .height(200)
          .margin(10);
        Image($r('app.media.example'))
          .width(200)
          .height(200)
          .margin(10)
          .grayscale(1);
      };

      // 黑白图片
      Image(this.bwImage)
        .width(200)
        .height(200)
        .margin(10);
    };
  }
}
```

## 总结

* 原始图片数据通常为RGBA格式，即每个像素由4个字节组成（红、绿、蓝、透明度）。
* 灰度效果通常使用加权平均法（心理学公式）将RGB转换为灰度值：

  ```ts
  const gray = 0.299 * r + 0.587 * g + 0.114 * b;
  return [gray, gray, gray];
  ```

* 黑白效果需要将灰度值与一个阈值比较，大于阈值则为白色（RGB值皆为255），小于等于阈值则为黑色（RGB值皆为0）。阈值可以取固定值（如128）或根据图片动态计算：

  ```ts
  const gray = 0.299 * r + 0.587 * g + 0.114 * b;
  const bw = gray > 128 ? 255 : 0;
  return [bw, bw, bw];
  ```
