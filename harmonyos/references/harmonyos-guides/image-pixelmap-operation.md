---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation
title: 使用PixelMap完成位图操作
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成位图操作
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:47024a676c54a70ea86c5c434e0c36f3b2e4857cd8cf9d0f4132d82a9d6faa48
---

当需要对目标图片中的部分区域进行处理时，可以使用位图操作功能。此功能常用于图片美化等操作。

如下图所示，一张图片中，将指定的矩形区域像素数据读取出来，进行修改后，再写回原图片对应区域。

**图1** 位图操作示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/I4GCWWWsRAiVTAKMna7kzA/zh-cn_image_0000002736313673.png)

## 开发步骤

位图操作相关API的详细介绍请参见[Interface (PixelMap)](../harmonyos-references/arkts-apis-image-pixelmap.md)。

1. 完成[图片解码](image-decoding.md)，获取PixelMap位图对象。
2. 从PixelMap位图对象中获取信息。

   ```typescript
   // 获取图像像素的总字节数。
   const totalPixelBytes: number = this.pixelMap.getPixelBytesNumber();
   Logger.info('Total bytes: ', totalPixelBytes.toString());
   // 获取图像像素的每行字节数。
   const rowBytes: number = this.pixelMap.getBytesNumberPerRow();
   Logger.info('Row bytes: ', rowBytes.toString());
   // 获取当前图像的像素密度。像素密度是指每英寸图片所拥有的像素数量，像素密度越大，图片越精细。
   const density: number = this.pixelMap.getDensity();
   Logger.info('Density: ', density.toString());
   ```
3. 读取并修改目标区域像素数据，写回原图。

   **说明** 

   建议readPixelsToBuffer和writeBufferToPixels成对使用，readPixels和writePixels成对使用，避免因图像像素格式不一致，造成PixelMap图像出现异常。

   ```typescript
   // 场景一：读取并修改整张图像数据。
   // 读取整个PixelMap的像素数据，并按照PixelMap的像素格式写入缓冲区。
   const buffer = new ArrayBuffer(totalPixelBytes);
   await this.pixelMap.readPixelsToBuffer(buffer).then(() => {
     Logger.info('Succeeded in reading image pixel data.');
   }).catch((error: BusinessError) => {
     Logger.error('Failed to read image pixel data. The error is: ' + String(error));
   });
   // ...
   // 按照PixelMap的像素格式，读取缓冲区内的图像像素数据，并将其写入整个PixelMap。
   this.pixelMap!.writeBufferToPixels(buffer).then(() => {
     Logger.info('Succeeded in writing image pixel data.');
     this.updateImageInfo();
   }).catch((error: BusinessError) => {
     Logger.error('Failed to write image pixel data. The error is: ' + String(error));
   });
   ```

   ```typescript
   // 场景二：读取并修改指定区域内的图像数据。
   // 读取PixelMap指定区域内的像素数据，并按照RGBA_8888像素格式写入PositionArea.pixels缓冲区，该区域由PositionArea.region指定。
   const regionWidth: number = 200;
   const regionHeight: number = 100;
   const area: image.PositionArea = {
     pixels: new ArrayBuffer(regionWidth * regionHeight * 4), // BGRA_8888格式的每个像素占4字节。
     offset: 0,
     stride: regionWidth * 4, // 指定区域的行跨距。
     region: {
       x: 0,
       y: 0,
       size: { width: regionWidth, height: regionHeight }
     }
   };

   await this.pixelMap.readPixels(area).then(() => {
     Logger.info('Succeeded in reading the image data in the area.');
     // ...
   }).catch((error: BusinessError) => {
     Logger.error('Failed to read the image data in the area. The error is: ' + String(error));
   });
   // 读取PositionArea.pixels缓冲区内的图像像素数据，并按照BGRA_8888像素格式将其写入PixelMap的指定区域，该区域由PositionArea.region指定。
   await this.pixelMap.writePixels(area).then(() => {
     this.updateImageInfo();
     Logger.info('Succeeded in writing pixelMap into the specified area.');
   }).catch((error: BusinessError) => {
     Logger.error('Failed to write pixelMap into the specified area. The error is: ' + String(error));
   });
   ```

## 开发示例

### 复制（深拷贝）位图并改变像素格式

**说明** 

* 该方法仅可实现PixelMap基本内容的复制，不支持复制色域和HDR元数据。如果不需要改变新PixelMap的像素格式，请使用[clone](../harmonyos-references/arkts-apis-image-pixelmap.md#clone18)或[cloneSync](../harmonyos-references/arkts-apis-image-pixelmap.md#clonesync18)。
* 该方法不支持将新PixelMap转换为下列像素格式：RGBA\_1010102、YCBCR\_P010、YCRCB\_P010、ASTC\_4x4。

1. 完成[图片解码](image-decoding.md)，获取PixelMap位图对象。
2. 参考以下代码对PixelMap进行深拷贝。

   ```typescript
   /**
    * 复制（深拷贝）PixelMap并改变像素格式。
    *
    * @param pixelMap - 被复制的原PixelMap。
    * @param desiredPixelFormat - 新PixelMap的像素格式。如果不指定，则仍使用原PixelMap的像素格式。
    * @returns 新PixelMap的Promise。
    */
   async function clonePixelMap(pixelMap: PixelMap, desiredPixelFormat?: image.PixelMapFormat): Promise<PixelMap> {
     // 获取原PixelMap的图片信息。
     const imageInfo = pixelMap.getImageInfoSync();
     // 读取原PixelMap的像素数据，并按照原PixelMap的像素格式写入缓冲区。
     const buffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
     await pixelMap.readPixelsToBuffer(buffer);

     // 根据原PixelMap的图片信息，生成初始化选项。
     const options: image.InitializationOptions = {
       // 数据源的像素格式：必须匹配原PixelMap的像素格式，否则新PixelMap的图像会出现异常。
       srcPixelFormat: imageInfo.pixelFormat,
       // 新PixelMap的像素格式。
       pixelFormat: desiredPixelFormat || imageInfo.pixelFormat,
       // 新PixelMap的透明度类型。
       alphaType: imageInfo.alphaType,
       // 新PixelMap的尺寸：必须匹配原PixelMap的尺寸，不支持传入其他尺寸以进行缩放。
       size: imageInfo.size
     };

     // 根据像素数据和初始化选项，创建新PixelMap。
     return await image.createPixelMap(buffer, options);
   }
   ```

### 将两张宽度相同的位图纵向拼接成一张长图

**说明** 

该方法仅支持以下像素格式的PixelMap：RGBA\_8888、BGRA\_8888、RGBA\_F16。

1. 完成[图片解码](image-decoding.md)，获取两张宽度相同且像素格式相同的PixelMap位图对象。
2. 参考以下代码对两张PixelMap进行拼接。

   ```typescript
   /**
    * 将两张宽度相同的PixelMap纵向拼接成一张长图。
    *
    * @param pixelMap1 - 第一张PixelMap。
    * @param pixelMap2 - 第二张PixelMap。宽度必须与第一张相同，高度可以不同。
    * @returns 拼接后的新PixelMap的Promise。
    */
   async function concatPixelMap(pixelMap1: PixelMap, pixelMap2: PixelMap): Promise<PixelMap> {
     // 将pixelMap1的像素数据读取至area1.pixels中。
     const imageInfo1 = pixelMap1.getImageInfoSync();
     const area1: image.PositionArea = {
       pixels: new ArrayBuffer(pixelMap1.getPixelBytesNumber()),
       offset: 0,
       stride: pixelMap1.getBytesNumberPerRow(),
       region: {
         size: imageInfo1.size,
         x: 0,
         y: 0
       }
     };
     await pixelMap1.readPixels(area1);

     // 将pixelMap2的像素数据读取至area2.pixels中。
     const imageInfo2 = pixelMap2.getImageInfoSync();
     const area2: image.PositionArea = {
       pixels: new ArrayBuffer(pixelMap2.getPixelBytesNumber()),
       offset: 0,
       stride: pixelMap2.getBytesNumberPerRow(),
       region: {
         size: imageInfo2.size,
         x: 0,
         y: 0
       }
     };
     await pixelMap2.readPixels(area2);

     // 创建一个新的空白PixelMap，其宽度与pixelMap1和pixelMap2相等，高度为pixelMap1和pixelMap2相加。
     const options: image.InitializationOptions = {
       srcPixelFormat: imageInfo1.pixelFormat,
       pixelFormat: imageInfo1.pixelFormat,
       size: {
         width: imageInfo1.size.width,
         height: imageInfo1.size.height + imageInfo2.size.height
       }
     };
     const newPixelMap = image.createPixelMapSync(options);

     // 将之前获取的pixelMap1和pixelMap2的像素数据按顺序写入新PixelMap。
     await newPixelMap.writePixels(area1);
     area2.region.y = imageInfo1.size.height; // pixelMap2像素的写入位置应该从pixelMap1末行像素的下一行开始。
     await newPixelMap.writePixels(area2);

     return newPixelMap;
   }
   ```

## 示例代码

* [PixelMap深拷贝案例](https://gitcode.com/HarmonyOS_Samples/image-depth-copy)
