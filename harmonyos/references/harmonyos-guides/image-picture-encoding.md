---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-picture-encoding
title: 使用ImagePacker完成多图对象编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编码 > 使用ImagePacker完成多图对象编码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bcb66fc083dced6193219f7b135f034b0cc6b3f1412786f7467722ad9a76d692
---

图片编码指将[Picture](../harmonyos-references/arkts-apis-image-picture.md)对象编码成不同格式的图片文件（当前仅支持编码为JPEG 和 HEIF 格式），用于后续处理，如保存、传输等。

## 开发步骤

图片编码相关API的详细介绍请参见[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)。

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

   **说明** 

   这里以编码成jpeg图片为例。编码的目标格式format遵循MIME标准定义，因此PackingOption.format应设置为image/jpeg，编码后的文件扩展名可设为.jpg或.jpeg。

   ```typescript
   let packOpts: image.PackingOption = {
     format: 'image/jpeg',
     // quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
     quality: 90,
     needsPackProperties: true
   };
   ```
3. 封装函数，传入picture，使用[packing](../harmonyos-references/arkts-apis-image-imagepacker.md#packing13)接口编码到ArrayBuffer，或使用[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-2)接口编码到文件。

   **说明** 

   在进行编码前，需要先通过解码获取picture，可参考[使用ImageSource完成多图对象解码](image-picture-decoding.md)。

   * picture编码到ArrayBuffer。

     ```typescript
     async function packing(picture: image.Picture, packOpts: image.PackingOption) {
       const imagePackerApi = image.createImagePacker();
       try {
         let data = await imagePackerApi.packing(picture, packOpts);
         copyData = data;
         console.info('Succeeded in packing the image.');
       } catch (error) {
         console.error('Failed to pack the picture to data. And the error is: ' + error);
       } finally {
         await imagePackerApi.release();
       }
     }
     ```
   * picture编码到文件。

     ```typescript
     async function packToFile(picture: image.Picture, packOpts: image.PackingOption, context: Context) {
       let imagePackerApi: image.ImagePacker | undefined = undefined;
       let file: fileIo.File | undefined = undefined;
       try {
         const path : string = context.cacheDir + '/picture.jpg';
         file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
         imagePackerApi = image.createImagePacker();
         await imagePackerApi.packToFile(picture, file.fd, packOpts);
       } catch (error) {
         console.error('Failed to pack the picture to file. And the error is: ' + error);
       } finally {
         if (file) {
           fileIo.closeSync(file.fd);
         }
         if (imagePackerApi) {
           await imagePackerApi.release();
         }
       }
     }
     ```
