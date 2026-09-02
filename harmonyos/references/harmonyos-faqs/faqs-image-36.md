---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-36
title: 如何实现PixelMap图片颜色翻转
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现PixelMap图片颜色翻转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a5adc36a914a9f6c6ea0d71fab4d70b1c85d0f980672bbf23af596e8ca2ec819
---

## 问题现象

通过截图获取的图片类型是PixelMap，图片背景是白色，绘制内容是黑色，需要将白色背景图转换成透明色，将原来黑色的内容转换成白色，如何实现。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/G1YqpdYfTzyheW3GtrZhVw/zh-cn_image_0000002628552500.png "点击放大")

## 背景知识

[PixelMap](../harmonyos-references/js-apis-sendableimage.md#pixelmap)是图像解码后的一种无压缩位图格式，图片解码是指将所支持格式的图片文件解码成统一的PixelMap格式，目前支持的图片格式有JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIF。PixelMap主要用于图像显示或进一步处理，这种格式可以有效地存储图像的原始数据，使其可以方便地进行[图像变换](../harmonyos-guides/image-transformation.md)，如裁剪、缩放、偏移、旋转、翻转、设置透明度等。

## 解决方案

1. 使用[getPixelBytesNumber](../harmonyos-references/arkts-apis-image-pixelmap.md#getpixelbytesnumber7)方法获取图像像素的总字节数，通过[readPixelsToBuffer](../harmonyos-references/js-apis-sendableimage.md#readpixelstobuffer)读取图像像素数据，结果写入缓冲区ArrayBuffer里。

   ```ts
   const imageInfo: image.ImageInfo = await pixelMap.getImageInfo();
   const buffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
   // 通过readPixelsToBuffer实现PixelMap的深拷贝，其中readPixelsToBuffer输出为BGRA_8888
   await pixelMap.readPixelsToBuffer(buffer);
   // readPixelsToBuffer输出为BGRA_8888,此处createPixelMap需转为RGBA_8888
   const opts: image.InitializationOptions = {
     editable: true,
     pixelFormat: image.PixelMapFormat.RGBA_8888,
     size: { height: imageInfo.size.height, width: imageInfo.size.width }
   };
   const pixelData = new Uint32Array(buffer);
   ```
2. 遍历像素数组，改变颜色。再通过[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)创建新的PixelMap对象，按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入新PixelMap。

   ```ts
   // 遍历像素数组，将白色变为透明，深色主题下黑色变成白色
   const length = pixelData.length;
   for (let i = 0; i < length; i++) {
     if (pixelData[i] === 0xFFFFFFFF) { // 检查是否为白色
       pixelData[i] = 0xFF000000; // 为了方便展示，背景先改成深色
     } else {
       if (dark) { // 如果是深色
         pixelData[i] = 0xFFffffff; // 改为白色
       }
     }
   }
   // 重新将修改像素写入
   const newPixelMap = await image.createPixelMap(buffer, opts);
   await newPixelMap.writeBufferToPixels(buffer);
   this.changeImgPixelMap = newPixelMap;
   ```

完整代码示例参考：

```ts
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct TurnImageColorDemo {
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State changeImgPixelMap: image.PixelMap | undefined = undefined;

  async handleLightAndDarkPixelMap(pixelMap: image.PixelMap, dark: boolean) {
    const imageInfo: image.ImageInfo = await pixelMap.getImageInfo();
    const buffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
    // 通过readPixelsToBuffer实现PixelMap的深拷贝，其中readPixelsToBuffer输出为BGRA_8888
    await pixelMap.readPixelsToBuffer(buffer);
    // readPixelsToBuffer输出为BGRA_8888,此处createPixelMap需转为RGBA_8888
    const opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: imageInfo.size.height, width: imageInfo.size.width }
    };
    const pixelData = new Uint32Array(buffer);

    // 遍历像素数组，将白色变为透明，深色主题下黑色变成白色
    const length = pixelData.length;
    for (let i = 0; i < length; i++) {
      if (pixelData[i] === 0xFFFFFFFF) { // 检查是否为白色
        pixelData[i] = 0xFF000000; // 为了方便展示，背景先改成深色
      } else {
        if (dark) { // 如果是深色
          pixelData[i] = 0xFFffffff; // 改为白色
        }
      }
    }
    // 重新将修改像素写入
    const newPixelMap = await image.createPixelMap(buffer, opts);
    await newPixelMap.writeBufferToPixels(buffer);
    this.changeImgPixelMap = newPixelMap;
  }

  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 获取resourceManager资源管理
    const resourceManager = context.resourceManager;
    // 获取图片数据，代码中图片仅作示例，实际请按开发环境图片为准
    const fileData = await resourceManager.getMediaContent($r('app.media.turn_color').id);
    // 创建imageSource
    const imageSource = image.createImageSource(fileData.buffer);
    let decodingOptions: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: 3,
    };
    // 创建PixelMap
    this.pixelMap = await imageSource.createPixelMap(decodingOptions);
  }

  build() {
    Column({ space: 10 }) {
      Text('原图')
        .fontSize(10)
      Image(this.pixelMap)
        .width(200)
        .height(200)
      Button('颜色翻转')
        .width(200)
        .height(30)
        .onClick(() => {
          if (this.pixelMap) {
            this.handleLightAndDarkPixelMap(this.pixelMap, true);
          }
        })
      Text('翻转后的图片')
        .fontSize(10)
      Image(this.changeImgPixelMap)
        .width(200)
        .height(200)
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

实现图片颜色翻转可参考以下步骤：

1. 获取需要转换的图片资源数据，并写入缓冲区。
2. 遍历像素数组，通过条件判断将符合条件的像素值转变成指定的颜色值。
3. 使用修改后的像素数据创建新的PixelMap并保存。

根据不同的业务场景，实现将符合条件的像素数据转变成指定颜色（如蓝色转变为红色等）。
