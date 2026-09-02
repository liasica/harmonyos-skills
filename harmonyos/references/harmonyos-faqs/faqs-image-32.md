---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-32
title: 使用PixelMap完成图像变换及常见问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 使用PixelMap完成图像变换及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b733dea56e7f2b569dad0e9734374cf41c4ead5f03c7154fada1fb4898cf4da
---

## 问题现象

如何对图片进行裁剪、缩放、偏移、旋转、翻转、透明度修改等图像变换操作。

## 背景知识

[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)是图像解码后的一种无压缩位图格式，图片解码是指将所支持格式的图片文件解码成统一的PixelMap格式，目前支持的图片格式有JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。PixelMap主要用于图像显示或进一步处理。这种格式可以有效地存储图像的原始数据，使其可以方便地进行[图像变换](../harmonyos-guides/image-transformation.md)，如裁剪、缩放、偏移、旋转、翻转、设置透明度等。

## 解决方案

使用HarmonyOS的PixelMap进行图像变换主要涉及以下几个步骤：

1. [图片解码](../harmonyos-guides/image-decoding.md)：首先，需要加载并解码图片文件，这将返回一个PixelMap对象，该对象用于后续的图像操作。
2. 获取图片信息：在进行变换之前，若需要获取图片的一些基本信息如宽度和高度，可以通过调用异步方法[getImageInfo()](../harmonyos-references/js-apis-sendableimage.md#getimageinfo)或同步方法[getImageInfoSync()](../harmonyos-references/js-apis-sendableimage.md#getimageinfosync)来进行获取。
3. 执行图像变换：包括裁剪、缩放、旋转、翻转、透明度修改等操作，以图片缩放的具体示例代码如下：

   ```ts
   import { image } from '@kit.ImageKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State imagePixelMap: PixelMap | undefined = undefined;
     @State scaleCount: number = 1;

     async aboutToAppear() {
       let pixelMap = this.getPixelMap();
       this.imagePixelMap = pixelMap;
     }

     // 获取pixelMap
     getPixelMap() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取resourceManager资源管理
       const resourceManager = context.resourceManager; // 获取图片数据
       const fileData = resourceManager.getMediaContentSync($r('app.media.startIcon').id); // startIcon为测试图片，开发者需要替换为实际图片
       const buffer = fileData.buffer;
       const imageSource = image.createImageSource(buffer);
       const pixelMap = imageSource.createPixelMapSync({
         editable: true,
         desiredDynamicRange: image.DecodingDynamicRange.AUTO
       });
       return pixelMap;
     }

     // 对pixelMap进行缩放
     scalePixelMap(pixelMap: PixelMap, scaleCount: number) {
       pixelMap.scaleSync(scaleCount, scaleCount);
       return pixelMap;
     }

     build() {
       Column() {
         Image(this.imagePixelMap ? this.imagePixelMap : '')
           .width('80%')
           .height('60%')
           .objectFit(ImageFit.None)
         Row() {
           Button('缩小')
             .onClick(() => {
               if (this.imagePixelMap) {
                 this.scaleCount = this.scaleCount - 0.1;
                 // 获取图片基本信息，如果宽高大于300，继续缩小
                 let imageInfo = this.imagePixelMap.getImageInfoSync();
                 if (imageInfo.size.width > 300 || imageInfo.size.width > 300) {
                   this.imagePixelMap = this.scalePixelMap(this.imagePixelMap, this.scaleCount);
                 }
               }
             })
         }
       }
       .width("100%")
       .height("100%")
     }
   }
   ```

更多[图像变换示例效果](../harmonyos-guides/image-transformation.md#示例代码)。

## 常见FAQ

Q：获取网络图片的PixelMap，如何进行居中剪裁（center crop）？

A：获取到PixelMap后，可调用[crop(region: Region)](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9-1)方法，设置剪裁目标区域[region](../harmonyos-references/arkts-apis-image-i.md#region8)参数为居中，对图片进行裁剪。

Q：HarmonyOS系统上，有时候竖屏图片加载时会显示成横屏。

A：有些设备会给图片加一个旋转属性，HarmonyOS相册组件是Image的API无法读取此属性，想要规避这个问题可以通过[getImageProperty()](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperty11)获取旋转信息，判断图片是否要旋转，如果需要旋转可以通过[rotate(90)](../harmonyos-references/js-apis-sendableimage.md#rotate)进行调整。

Q：图片缩放算法函数[scaleSync(x:number,y:number)](../harmonyos-references/js-apis-sendableimage.md#scalesync)，x和y大概0.2左右（图片长宽尺寸缩小0.046），最终图片byte值为原始图的0.0558倍，这个结果不符合预期，预期也是0.046倍。

A：scaleSync影响的是PixelMap的比例大小，缩放后编码的数据会变小，但是不一定成比例。

Q：使用PixelMap.rotate旋转图片没有改变。

A：这个问题涉及PixelMap的深拷贝，可以参考[深拷贝demo](https://gitee.com/harmonyos_samples/image-depth-copy)。

Q：相同代码真机中无法正常旋转图片。

A：需要把图片解码设置选项[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)中设置editable：true。

Q：使用pixelMap.scale缩放图片没有效果。

A：[pixelMap.scale](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9-1)是异步函数，需要在执行成功后再进行别的操作，否则图片没有缩放效果，需要使用同步接口[pixelMap.scaleSync](../harmonyos-references/arkts-apis-image-pixelmap.md#scalesync12)，或者在接口pixelMap.scale前增加异步await。

Q：如何对拍照后获取的JPEG图像进行裁剪，再写回文件？

A：先将JPEG图像[解码](../harmonyos-guides/image-decoding.md)获取PixelMap对象，对PixelMap使用[crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)接口进行裁剪，再将裁剪后的PixelMap[编码](../harmonyos-guides/image-encoding.md)成JPEG图像重新写入文件即可。

Q：为什么通过resourceManager.getMediaContent方法获取媒体文件内容后，通过createPixelMap方法转换失败？

A：[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)方法的入参为图像像素数据，而resourceManager.[getMediaContent](../harmonyos-references/js-apis-resource-manager.md#getmediacontent9)方法回调函数中返回的是媒体文件内容数据，媒体文件数据可以直接用于播放，但是不能作为image.createPixelMap方法的入参，需要通过解码转换为可用图片像素数据才可以用于图片处理或渲染。
