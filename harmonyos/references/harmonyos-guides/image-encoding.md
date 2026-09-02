---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding
title: 使用ImagePacker完成图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编码 > 使用ImagePacker完成图片编码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4d05363a0d3c3aa5c26eb19ccc40711f3f1713957efb6ca7450e912cfdb484f7
---

图片编码指将PixelMap压缩成不同格式的图片文件，用于保存和传输。

支持使用[PackToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13-1)和[PackToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-2)将[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)编码为JPEG、WebP、PNG、HEIC和TIFF格式。

从API version 18开始，支持使用[PackToDataFromPixelmapSequence](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodatafrompixelmapsequence18)和[PackToFileFromPixelmapSequence](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofilefrompixelmapsequence18)将多个PixelMap编码为GIF格式。

从API版本26.0.0开始，支持使用[PackBinaryImageToTiffFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packbinaryimagetotifffile)和[PackBinaryImageToTiffData](../harmonyos-references/arkts-apis-image-imagepacker.md#packbinaryimagetotiffdata)将二值图像数据编码为TIFF格式。

## 开发步骤

图片编码相关API的详细介绍请参见[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)。

### 图片编码进文件流

1. 导入相关模块包。

   ```typescript
   // 导入相关模块。
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { resourceManager } from '@kit.LocalizationKit';
   ```
2. 设置编码选项[PackingOption](../harmonyos-references/arkts-apis-image-i.md#packingoption)。

   2.1 这里以编码成jpeg图片为例。编码的目标格式format遵循MIME标准定义，因此PackingOption.format应设置为image/jpeg，编码后的文件扩展名可设为.jpg或.jpeg。

   ```typescript
   // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
   let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 90 };
   ```

   2.2 当图片源是HDR，且希望编码为HDR图片文件时，需要额外配置desiredDynamicRange。

   ```typescript
   // 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
   packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
   ```
3. 封装函数，传入imageSource或pixelMap，使用[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)接口编码到ArrayBuffer，或使用[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)接口编码到文件。

   **说明** 

   在进行编码前，需要先获取imageSource或pixelMap，可参考[使用ImageSource完成图片解码](image-decoding.md)。

   * 定义copyData，获取编码后的文件流，方便后续保存为图片或者用于解码显示。

     ```typescript
     let copyData: ArrayBuffer = new ArrayBuffer(0);
     ```
   * pixelMap编码到ArrayBuffer。

     ```typescript
     async function packToDataFromPixelMap(pixelMap : image.PixelMap) {
       const imagePackerApi = image.createImagePacker();
       // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 90 };
       // 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
       packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
       try{
         let data = await imagePackerApi.packToData(pixelMap, packOpts);
         // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
         copyData = new ArrayBuffer(0);
         copyData = data;
       } catch (error) {
         console.error('Failed to pack the pixelMap to data. And the error is: ' + error);
       }
     }
     ```
   * imageSource编码到ArrayBuffer。

     ```typescript
     async function packToDataFromImageSource(imageSource : image.ImageSource) {
       const imagePackerApi = image.createImagePacker();
       // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 90 };
       try {
         let data = await imagePackerApi.packToData(imageSource, packOpts);
         // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
         copyData = new ArrayBuffer(0);
         copyData = data;
       } catch (error) {
         console.error('Failed to pack the imageSource to data. And the error is: ' + error);
       }
     }
     ```
   * pixelMap编码到文件。

     ```typescript
     async function packToFileFromPixelMap(context : Context, pixelMap : image.PixelMap) {
       const imagePackerApi = image.createImagePacker();
       // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 90 };
       const path : string = context.cacheDir + '/pixel_map.jpg';
       let file: fileIo.File | undefined = undefined;
       try {
         file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         await imagePackerApi.packToFile(pixelMap, file.fd, packOpts);
       } catch (error) {
         console.error('Failed to pack the pixelMap to file. And the error is: ' + error);
       } finally {
         if (file) {
           fileIo.closeSync(file.fd);
         }
       }
     }
     ```
   * imageSource编码到文件。

     ```typescript
     async function packToFileFromImageSource(context : Context, imageSource : image.ImageSource) {
       const imagePackerApi = image.createImagePacker();
       // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 90 };
       const filePath : string = context.cacheDir + '/image_source.jpg';
       let file: fileIo.File | undefined = undefined;
       try {
         file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         await imagePackerApi.packToFile(imageSource, file.fd, packOpts);
       } catch (error) {
         console.error('Failed to pack the imageSource to file. And the error is: ' + error);
       } finally {
         if (file) {
           fileIo.closeSync(file.fd);
         }
       }
     }
     ```
4. 将图片保存进图库。

将图片编码到ArrayBuffer或文件后，可使用[Media Library Kit](photoaccesshelper-overview.md)的相关接口[保存媒体库资源](photoaccesshelper-savebutton.md)保存进图库。

## 示例代码

* [图片压缩](https://gitcode.com/HarmonyOS_Samples/image-compression)
