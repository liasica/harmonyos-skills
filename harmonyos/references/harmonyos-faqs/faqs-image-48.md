---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-48
title: 如何获取PixelMap图像的文件大小
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何获取PixelMap图像的文件大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7acd86961edd81f3033cf9189e7e2c2393405017d13bdac5a31e8b7faed4ebb9
---

## 问题现象

在编辑PixelMap时，由于PixelMap在动态的修改，有什么方法可以获取到PixelMap图像的大小。

## 背景知识

* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：是一种用于管理和操作像素数据的数据结构。它通常用于图像处理和渲染，能够动态地存储和修改像素信息，主要特点：
  + 动态修改：PixelMap，可以实时更新和修改像素数据，支持高效的像素操作。
  + 像素访问：可以通过索引直接访问和修改单个像素值。
  + 图像渲染：可以将PixelMap转换为图像文件或直接在屏幕上进行渲染。
* [ImagePacker](../harmonyos-guides/image-encoding.md)：图片编码指将PixelMap编码成不同格式的图片文件，当前支持编码为JPEG、WebP、PNG和HEIF格式，用于后续处理，如保存、传输等。
* [getPixelBytesNumber](../harmonyos-references/arkts-apis-image-pixelmap.md#getpixelbytesnumber7)：获取图像像素的总字节数。
* [packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)：图片编码获取到的文件流，写入文件保存即可得到一张图片。
* [packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)：图片编码进文件，通过传入对应的文件路径，编码后的PixelMap数据将直接写入文件。

## 解决方案

获取PixelMap的文件大小可以通过以下两种方案：

* 使用[getPixelBytesNumber](../harmonyos-references/arkts-apis-image-pixelmap.md#getpixelbytesnumber7)方法获取图像像素的总字节数，需要注意的是该方法得到的是位图占的字节数。在对PixelMap进行处理前，需要使用createImageSource获取图片的ArrayBuffer，并创建新的PixelMap实例。
* 可使用ImagePacker的[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)方法，将PixelMap图片进行编码，从而获取到图片文件的大小。使用方式和效果图如下：

完整示例参考如下：

```ts
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Page {
  @State pixelMap: PixelMap | undefined = undefined;

  saveToData() {
    let packOpts: image.PackingOption = { format: 'image/png', quality: 100 };
    const imagePackerApi: image.ImagePacker = image.createImagePacker();
    imagePackerApi.packToData(this.pixelMap, packOpts)
      .then((data: ArrayBuffer) => {
        console.info(`packToData后的文件大小：${data.byteLength.toString()}`);
      });
  }

  CreatePixelMap() {
    this.getUIContext().getHostContext()?.resourceManager.getMediaContent($r('app.media.startIcon').id).then((data) => {
      // 提取图片数据的缓冲区
      let arrayBuffer = data.buffer.slice(data.byteOffset, data.byteLength + data.byteOffset);
      // 创建ImageSource对象
      let imageSource = image.createImageSource(arrayBuffer);
      // 设置初始化选项
      let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 6, width: 6 } };
      // 创建PixelMap
      imageSource.createPixelMap(opts, (err, pixelMap) => {
        if (err) {
          console.error(`Failed to create pixelmap. code is ${err.code}, message is ${err.message}`);
        }
        this.pixelMap = pixelMap;
      });
    });
  }

  aboutToAppear(): void {
    this.CreatePixelMap();
  }

  build() {
    Column() {
      Image(this.pixelMap)
        .width(200)
        .height(200)
        .borderWidth(1);
      Button('点击').onClick(() => {
        if (this.pixelMap) {
          // 获取PixelMap的像素字节数
          let pixelBytesNumber: number = this.pixelMap.getPixelBytesNumber();
          console.info(`PixelMap像素的总字节数：${pixelBytesNumber.toString()}`);
        }
      });
      Button('点击').onClick(() => {
        this.saveToData();
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/4eQqQw0yTJiR59U46Tg0Jg/zh-cn_image_0000002658911821.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Bz9enBOQQrOTsMF3EG2Slw/zh-cn_image_0000002628392612.png "点击放大")

## 常见FAQ

Q：通过getPixelBytesNumber方法获取到的图片大小和实际图片大小相差较大。

A：图片解码内存占用是宽 \* 高 \* 像素字节数，默认是rgba格式即一个像素占用四字节，所以通过getPixelBytesNumber方法获取到的图片大小为宽 \* 高 \* 4。

Q：ImageInfo中的stride表示什么含义？getPixelBytesNumber获取到的字节数和通过height乘以stride得到的数值为什么不同？

A：[ImageInfo](../harmonyos-references/arkts-apis-image-i.md#imageinfo)中的stride表示图片跨距，内存中每行像素所占的空间。stride通常满足：stride≥图像宽度×每像素字节数。[getPixelBytesNumber](../harmonyos-references/arkts-apis-image-pixelmap.md#getpixelbytesnumber7)是获取图像像素的总字节数。图像像素总字节数=图像高度x图像宽度x每像素字节数。所以图像像素总字节数小于等于height\*stride。

Q：packToData方法执行时提示未定义。

A：[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)方法在API13以上才提供，需要系统升级到对应版本以上才能使用该方法。

Q：[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-1)方法执行时提示[62980115](../harmonyos-references/errorcode-image.md#section62980115-图片无效参数)。

A：packToFile接口使用Promise形式时，无返回结果，需按接口规范使用。
