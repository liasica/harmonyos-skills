---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool
title: 读取和编辑图片Exif信息
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片元数据处理 > 读取和编辑图片Exif信息
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3bf85a5390839d05372e53e48281edf2e4cd08c10191ef6a24218942701d102
---

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。需要图片包含Exif信息。

在图库、相机、图片编辑等应用中，开发者可以读取图片的拍摄时间、方向、焦距、地理位置等Exif信息，也可以在需要时修改部分Exif信息。例如，当摄像机的手动镜头参数无法自动写入Exif信息，或者因相机断电导致拍摄时间错误时，可手动修正对应的Exif数据。

系统目前仅支持读取和修改部分Exif信息，具体支持范围请参见[PropertyKey](../harmonyos-references/arkts-apis-image-e.md#propertykey7)。不同图片格式对Exif信息的读写支持情况如下。

| 图片格式 | 读取Exif信息 | 修改Exif信息 |
| --- | --- | --- |
| JPG/JPEG | 支持 | 支持 |
| PNG | 支持 | 支持 |
| HEIF | 支持 | 支持 |
| WebP23+ | 支持 | 支持 |
| DNG23+ | 支持 | 不支持 |

## 接口说明

Exif信息的读取与编辑相关的API如下，详细介绍请参考[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)。

| 接口 | 说明 |
| --- | --- |
| [getImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperty11) | 获取指定属性键的Exif信息。 |
| [modifyImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#modifyimageproperty11) | 修改指定属性键的Exif信息。 |

## 注意事项

* 需要先创建[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)对象，再读取或编辑Exif信息。
* 读取图片Exif信息前，需要确保应用对目标图片具有读取权限；修改图片Exif信息前，需要确保应用对目标图片具有写入权限。
* 在部分图片来源或访问场景下，即使应用具有图片读取权限，系统也可能对GPS等隐私信息进行去隐私化处理，此时无法获取对应的Exif信息。
* 图片文件需要包含Exif信息。对于没有Exif信息或不包含目标属性键的图片，读取结果可能为空或返回默认值。
* 修改Exif信息前，需要确认图片格式和目标属性键支持写入。
* 图片元数据可能包含拍摄位置等隐私信息，应用展示、上传或共享前应结合业务场景做好用户授权和隐私保护。

## 开发步骤

获取图片并创建ImageSource对象后，可读取或编辑Exif信息。示例代码如下：

1. 导入相关模块包。

   ```typescript
   // 导入相关模块。
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取指定属性键的Exif信息。

   ```typescript
   // 获取指定key的Exif信息接口示例
   async getExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey): Promise<string> {
     let info: string = '';
     if (imageSourceApi) {
       console.info('getExif: The imageSourceApi is not undefined.');
       // 根据传入的key获取其Exif信息
       let options: image.ImagePropertyOptions = { index: 0, defaultValue: 'This key has no value!' };
       try {
         let data = await imageSourceApi.getImageProperty(key, options);
         info = `Succeeded in getting the ${key}'s value: ${data}.`;
         console.info(info);
         return info; // 获取key值成功时返回获取到的key值
       } catch (error) {
         info =
           `Failed to get the value of the ${key} with error: ${error}.`;
         console.error(info);
         return info; // 获取key值失败时返回错误信息
       }
     } else {
       info = 'getExif: The imageSourceApi is undefined.';
       console.info(info);
       return info; // 如果 imageSourceApi 是 undefined，则直接返回信息
     }
   }
   ```
3. 修改指定属性键的Exif信息。

   ```typescript
   // 修改指定key的Exif信息的接口示例
   async modifyExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey, value: string)
     : Promise<string> {
     let info: string = '';
     if (imageSourceApi) {
       // 编辑EXIF信息
       try {
         await imageSourceApi.modifyImageProperty(key, value);
         try {
           let modifyValue = await imageSourceApi.getImageProperty(key)
           info = `The ${key}'s value is modified to ${modifyValue}.`
           console.info(info);
           return info; // 获取key值成功时返回修改成功信息
         } catch (error) {
           console.error(`Failed to get the ${key}'s value with ${error}`);
           console.error(info);
           return info; // 获取key值失败时返回错误信息
         }
       } catch (error) {
         info = `Failed to modify the ${key}'s value with ${error}`;
         console.error(info);
         return info; // 修改key值失败时返回错误信息
       }
     } else {
       info = 'modifyExif: The imageSourceApi is undefined.';
       console.info(info);
       return info; // 如果 imageSourceApi 是 undefined，直接返回信息
     }
   }
   ```
