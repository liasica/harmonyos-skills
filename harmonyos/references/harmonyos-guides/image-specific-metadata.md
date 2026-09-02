---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-specific-metadata
title: 使用ImageSource获取专有元数据
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片元数据处理 > 使用ImageSource获取专有元数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d14ece7d406209ac1585b46225dfed04be8356fc6b55d51caf0ac914666d72eb
---

从API version 23开始，支持使用ImageSource获取GIF、HEIFS、DNG、WebP、PNG、JFIF、TIFF、AVIS多种图像格式的专有元数据。

## 支持的元数据类别

| 元数据类别 | MetadataType | 返回字段 | 起始API版本 | 典型信息 |
| --- | --- | --- | --- | --- |
| GIF | GIF\_METADATA | [GifMetadata](../harmonyos-references/arkts-apis-image-gifmetadata.md) | 26.0.0 | 帧延迟时长、循环次数、画布尺寸等。 |
| HEIFS | HEIFS\_METADATA | [HeifsMetadata](../harmonyos-references/arkts-apis-image-heifsmetadata.md) | 23 | 画布高度、画布宽度、未钳制延迟时长等。 |
| DNG | DNG\_METADATA | [DngMetadata](../harmonyos-references/arkts-apis-image-i.md#dngmetadata24) | 24 | DNG版本号、相机型号、CFA参数、黑白电平、色彩校正矩阵等。 |
| WebP | WEBP\_METADATA | [WebPMetadata](../harmonyos-references/arkts-apis-image-webpmetadata.md) | 24 | 画布尺寸、帧延迟时长、循环次数等。 |
| PNG | PNG\_METADATA | [PngMetadata](../harmonyos-references/arkts-apis-image-pngmetadata.md) | 26.0.0 | 像素密度、描述、版权等。 |
| JFIF | JFIF\_METADATA | [JfifMetadata](../harmonyos-references/arkts-apis-image-jfifmetadata.md) | 26.0.0 | 像素密度、渐进编码等。 |
| TIFF | TIFF\_METADATA | [TiffMetadata](../harmonyos-references/arkts-apis-image-tiffmetadata.md) | 26.0.0 | 分辨率、色度坐标、压缩方式等。 |
| AVIS | AVIS\_METADATA | [AvisMetadata](../harmonyos-references/arkts-apis-image-avismetadata.md) | 26.0.0 | 帧延迟时长等。 |

**注意** 

HeifsMetadata自API version 23起可用，其中heifsCanvasWidth、heifsCanvasHeight、heifsUnclampedDelayTime三个属性为API版本26.0.0新增。

## 相关接口

| 接口 | 说明 |
| --- | --- |
| [readImageMetadata](../harmonyos-references/arkts-apis-image-imagesource.md#readimagemetadata23) | 读取图像源的元数据，使用propertyKeys指定元数据字段。  从API version 23开始支持。 |
| [readImageMetadataByType](../harmonyos-references/arkts-apis-image-imagesource.md#readimagemetadatabytype24) | 读取图像源的元数据，使用metadataTypes指定元数据类型。  从API version 24开始支持。 |

## 开发步骤

获取图片专有元数据相关API的详细介绍请参见[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)和[Metadata](../harmonyos-references/arkts-apis-image-metadata.md)。

1. 全局导入Image模块，根据实际需求导入对应的Kit模块。

   ```typescript
   // 导入相关模块。
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { resourceManager } from '@kit.LocalizationKit';
   ```
2. 参考[使用ImageSource完成图片解码](image-decoding.md)创建ImageSource实例。
3. 读取专有元数据。

   使用[readImageMetadata](../harmonyos-references/arkts-apis-image-imagesource.md#readimagemetadata23)接口，通过指定属性键（propertyKeys）读取对应格式的专有元数据。以读取GIF元数据中的帧延迟时长为例：

   ```typescript
   async readImageMetadata(imageSource: image.ImageSource | undefined) : Promise<image.ImageMetadata | undefined> {
     if (imageSource == undefined) {
       console.error('imageSource is undefined.');
       return undefined;
     }
     try {
       let properties: string[] = [image.GifPropertyKey.GIF_DELAY_TIME];
       let index: number = 0;
       let imageMetadata: image.ImageMetadata = await imageSource.readImageMetadata(properties, index);
       if (imageMetadata.gifMetadata != undefined) {
         console.info(`GIF_DELAY_TIME: ${JSON.stringify(imageMetadata.gifMetadata?.delayTime)}`);
       }
       return imageMetadata
     } catch (error) {
       console.error(`ReadImageMetadata failed, error.code: ${error.code},
                  error.message: ${error.message}`)
       return undefined;
     }
   }
   ```

   使用[readImageMetadataByType](../harmonyos-references/arkts-apis-image-imagesource.md#readimagemetadatabytype24)接口，通过指定[MetadataType](../harmonyos-references/arkts-apis-image-e.md#metadatatype13)枚举值读取对应格式的专有元数据。以读取GIF元数据为例：

   ```typescript
   async readImageMetadataByType(imageSource: image.ImageSource | undefined) : Promise<image.ImageMetadata | undefined> {
     if (imageSource == undefined) {
       console.error('imageSource is undefined.');
       return undefined;
     }
     try {
       let types: image.MetadataType[] = [image.MetadataType.GIF_METADATA];
       let index: number = 0;
       let imageMetadata: image.ImageMetadata = await imageSource.readImageMetadataByType(types, index);
       if (imageMetadata.gifMetadata != undefined) {
         console.info(`GIF_DELAY_TIME: ${JSON.stringify(imageMetadata.gifMetadata?.delayTime)}`);
       }
       return imageMetadata;
     } catch (error) {
       console.error(`ReadImageMetadataByType failed, error.code: ${error.code},
                  error.message: ${error.message}`)
       return undefined;
     }
   }
   ```
4. 释放imageSource。

   确认imageSource的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```typescript
   async release() {
     try {
       await this.pixelMap?.release();
     } catch (error) {
       console.error(`Failed to release PixelMap: ${error}.`);
     } finally {
       this.pixelMap = undefined;
     }

     try {
       await this.imageSource?.release();
     } catch (error) {
       console.error(`Failed to release ImageSource: ${error}.`);
     } finally {
       this.imageSource = undefined;
     }
   }
   ```

## 注意事项

* 如果图片中不包含目标元数据，返回字段为undefined，使用前请进行空值判断。
* 读取图片文件需要读取权限，请确保应用已声明并获取相应权限。
* 多帧图片（如GIF）读取时，index不能小于0或超过帧数范围，否则会导致读取失败。
