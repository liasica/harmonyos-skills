---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1594
title: 图片尺寸约束
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 图片尺寸约束
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:892f50e63be3038e51d95db3ba643dd6a6fcb5ffdfdd73d65641d3adf22c2855
---

## 问题现象

在使用Image组件时，如何实现以下场景：

1. 图片不进行任何缩放、裁剪或拉伸，直接按图源宽度和高度渲染。
2. 如何自定义图片的显示尺寸，使其按相应比例进行缩放。

## 背景知识

* [objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)：设置图片的填充效果，使图片按照对应宽高比进行缩小或者放大。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，用于读取或写入图像数据以及获取图像信息。
* [fitOriginalSize](../harmonyos-references/ts-basic-components-image.md#fitoriginalsize)：设置图片的显示尺寸是否跟随图源尺寸，当图片组件已设置width、height属性时，该属性不生效。

## 解决方案

* **场景一**：通过将Image的fitoriginalsize属性设为true，可以在Image组件未设置宽高的情况下适应图源尺寸。具体参考[Column宽高自适应背景图片大小](faqs-arkui-1275.md)。
* **场景二**：定义[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)，通过[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)构建PixelMap对象，并基于目标尺寸计算缩放比例后调用scaleSync方法实现动态图片缩放。
  1. 获取原始尺寸，通过pixelMap.getImageInfo获取图片的原始宽度和高度。
  2. 计算缩放比例，分别计算宽度和高度需要缩放的比例。
  3. 调用scaleSync方法，按照计算出的比例进行缩放。缩放操作会直接修改PixelMap对象本身。

  具体代码如下：

  ```ts
  import image from '@ohos.multimedia.image';
  import fs from '@ohos.file.fs';

  @Entry
  @Component
  struct Index {
    @State pixelMap: PixelMap | undefined = undefined;
    context: Context = this.getUIContext().getHostContext() as Context;
    path: string = this.context.filesDir + '/hehe.jpg';
    decodingOptions: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: 3,
    };

    async aboutToAppear(): Promise<void> {
      let resourceManager = this.context.resourceManager;
      let imageArray =
        await resourceManager.getMediaContent($r('app.media.BigImage').id); // 需开发者自行更换图片
      let file = fs.openSync(this.path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      try {
        fs.writeSync(file.fd, imageArray.buffer);
      } catch (err) {
      } finally {
        fs.closeSync(file);
      }
    }

    async packingDetail(targetWidth: number, targetHeight: number) {
      if (this.pixelMap) {
        let imageInfo = await this.pixelMap.getImageInfo();
        // 计算压缩比
        let scaleX: number = targetWidth / imageInfo.size.width;
        let scaleY: number = targetHeight / imageInfo.size.height;
        this.pixelMap.scaleSync(scaleX, scaleY);
      }
    }

    build() {
      Row() {
        Column() {
          Image(this.pixelMap)
            .width(200)
            .height(200)
            .backgroundColor(Color.Gray)
            .margin({ bottom: 40 })
            .objectFit(ImageFit.Contain)

          Button('1:3').onClick(async () => {
            const imageSource: image.ImageSource = image.createImageSource(this.path);
            // 创建pixelMap
            this.pixelMap = await imageSource.createPixelMap(this.decodingOptions);
            // 指定压缩宽、高
            this.packingDetail(100, 300);
          }).margin({ bottom: 20 })

          Button('1:2').onClick(async () => {
            // path为已获得的沙箱路径
            const imageSource: image.ImageSource = image.createImageSource(this.path);
            // 创建pixelMap
            this.pixelMap = await imageSource.createPixelMap(this.decodingOptions);
            // 指定压缩宽、高
            this.packingDetail(100, 200);
          })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

## 常见FAQ

Q：[ImageAnimator](../harmonyos-references/ts-basic-components-imageanimator.md)在设置了[fixedSize](../harmonyos-references/ts-basic-components-imageanimator.md#fixedsize)之后，图片不会跟随组件宽高做拉伸。

A：设置fixedSize属性后，ImageAnimator将维持图片的原始宽高比。当图片原始尺寸与组件尺寸不一致时，图片会适配至ImageAnimator的宽高范围内显示，而不会被拉伸变形。
