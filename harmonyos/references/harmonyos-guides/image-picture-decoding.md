---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-picture-decoding
title: 使用ImageSource完成多图对象解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource完成多图对象解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf3e6d3dce96ff99583ba73f95e5651f5a60ac5636c0bbe7c5e071886e805cf7
---

将所支持格式的图片文件解码成[Picture](image-overview.md#基础概念)多图对象，以便在应用或系统中进行HDR图片显示、辅助图处理等操作。当前支持的图片文件格式包括JPEG、HEIF。

Picture是包含主图、辅助图和元数据的多图对象。主图包含主要图像信息，辅助图用于存储与主图相关的附加信息（如HDR增益图GAINMAP），元数据用于存储与图片相关的其他信息。Picture适用于HDR图片处理、HEIF专业格式解码等场景。

## Picture与PixelMap的区别

Picture和PixelMap是两种不同的图片解码对象，适用于不同的场景：

| 对象类型 | 适用场景 | 特性 |
| --- | --- | --- |
| [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md) | 单图显示、基础图片处理 | 单一像素数据，支持图像变换（裁剪、缩放、旋转等）、位图操作，可直接传给Image组件显示。 |
| [Picture](../harmonyos-references/arkts-apis-image-picture.md) | HDR图片、HEIF专业格式、辅助图处理 | 包含主图+辅助图+元数据，可提取主图/增益图/合成HDR图为PixelMap后显示或处理，支持辅助图和元数据操作。 |

**选择建议：**

* 需要直接显示单张图片或进行裁剪、缩放、旋转等图像处理时，使用PixelMap。
* 需要处理HDR图片、获取辅助图（如GAINMAP）、操作图片元数据时，使用Picture。如需对Picture的内容进行裁剪缩放，可通过[getMainPixelmap](../harmonyos-references/arkts-apis-image-picture.md#getmainpixelmap13)等方法提取PixelMap后再处理。

## 开发步骤

图片解码相关API的详细介绍请参见[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)。

1. 全局导入Image模块。

   ```typescript
   // 导入相关模块。
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { resourceManager } from '@kit.LocalizationKit';
   ```
2. 获取图片。

   * 方法一：通过沙箱路径直接获取。该方法仅适用于应用沙箱中的图片。更多细节请参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。

     ```typescript
     function getFilePath(context: Context, fileName: string): string {
       const filePath: string = context.cacheDir + '/' + fileName;
       return filePath;
     }
     ```
   * 方法二：通过沙箱路径获取图片的文件描述符。具体请参考文档[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)。该方法需要导入@kit.CoreFileKit模块。

     ```typescript
     function getFileFd(context: Context, fileName: string): number | undefined {
       try {
         const filePath: string = context.cacheDir + '/' + fileName;
         const file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
         const fd: number = file?.fd;
         return fd;
       } catch (err) {
         console.error(`Failed to get the fileFd with error: ${err}.`);
         return undefined;
       }
     }
     ```
   * 方法三：通过资源管理器获取资源文件的ArrayBuffer。具体请参考[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9-1)。该方法需要导入@kit.LocalizationKit模块。

     ```typescript
     async function getFileBuffer(context: Context, fileName: string): Promise<ArrayBuffer | undefined> {
       try {
         const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
         // 获取资源文件内容，返回Uint8Array。
         const fileData: Uint8Array = await resourceMgr.getRawFileContent(fileName);
         console.info('Successfully get the RawFileContent.');
         // 转为ArrayBuffer并返回。
         const buffer: ArrayBuffer = fileData.buffer.slice(0);
         return buffer;
       } catch (error) {
         console.error(`Failed to get the RawFileContent with error: ${error}.`);
         return undefined;
       }
     }
     ```
   * 方法四：通过资源管理器获取资源文件的RawFileDescriptor。具体请参考[getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9-1)。该方法需要导入@kit.LocalizationKit模块。

     ```typescript
     async function getRawFd(context: Context, fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
       try {
         const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
         const rawFileDescriptor: resourceManager.RawFileDescriptor = await resourceMgr.getRawFd(fileName);
         console.info('Successfully get the RawFileDescriptor.');
         return rawFileDescriptor;
       } catch (error) {
         console.error(`Failed to get the RawFileDescriptor with error: ${error}.`);
         return undefined;
       }
     }
     ```
3. 创建ImageSource实例。

   * 方法一：通过沙箱路径创建ImageSource。沙箱路径可以通过步骤2的方法一获取。

     ```typescript
     // path为已获得的沙箱路径。
     const imageSource : image.ImageSource = image.createImageSource(filePath);
     ```
   * 方法二：通过文件描述符fd创建ImageSource。文件描述符可以通过步骤2的方法二获取。

     ```typescript
     // fd为已获得的文件描述符。
     const imageSource: image.ImageSource = image.createImageSource(fd);
     ```
   * 方法三：通过缓冲区数组创建ImageSource。缓冲区数组可以通过步骤2的方法三获取。

     ```typescript
     const imageSource: image.ImageSource = image.createImageSource(buffer);
     ```
   * 方法四：通过资源文件的RawFileDescriptor创建ImageSource。RawFileDescriptor可以通过步骤2的方法四获取。

     ```typescript
     const imageSource: image.ImageSource = image.createImageSource(rawFileDescriptor);
     ```
4. 设置解码参数DecodingOptionsForPicture，解码获取picture多图对象。

   解码时可指定需要解码的辅助图类型。辅助图本身不作为独立图像直接显示，而是作为辅助数据参与图像处理（如HDR合成、深度信息提取等）。常见的辅助图类型包括：

   | 辅助图类型 | 说明 |
   | --- | --- |
   | GAINMAP | 增益图，用于HDR图像的高动态范围渲染。 |
   | DEPTH\_MAP | 深度图，存储像素距离信息，用于3D重建、背景分离等场景。 |
   | UNREFOCUS\_MAP | 未重对焦原图，用于人像虚化后期处理。 |
   | LINEAR\_MAP | 线性图，用于视觉效果增强与色彩后期处理。 |
   | FRAGMENT\_MAP | 水印裁剪图，用于水印移除、原图恢复等场景。 |

   **说明** 

   并非所有图片都包含辅助图。在获取辅助图前，应先调用Picture的[getAuxiliaryPicture](../harmonyos-references/arkts-apis-image-picture.md#getauxiliarypicture13)方法尝试获取。其他辅助图类型请参考[AuxiliaryPictureType](../harmonyos-references/arkts-apis-image-e.md#auxiliarypicturetype13)。

   ```typescript
   async createPicture(imageSource : image.ImageSource | undefined, isReturnAux: Boolean)
     : Promise<image.PixelMap | undefined | image.Picture> {
     // 配置解码选项参数。
     let options: image.DecodingOptionsForPicture = {
       desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP] // GAINMAP为需要解码的辅助图类型。
     };
     let returnPixelMap: image.PixelMap | undefined = undefined;
     // 创建picture。
     try {
       let picture = await imageSource?.createPicture(options);
       if (picture) {
         // 返回解码后获取到的辅助图
         if (isReturnAux) {
           // type为解码参数中包含的辅助图类型
           let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
           let auxPicture: image.AuxiliaryPicture | null = picture.getAuxiliaryPicture(type);
           // 获取辅助图信息。
           if (auxPicture != null) {
             let auxInfo: image.AuxiliaryPictureInfo = auxPicture.getAuxiliaryPictureInfo();
             console.info('GetAuxiliaryPictureInfo type: ' + auxInfo.auxiliaryPictureType +
               ' height: ' + auxInfo.size.height + ' width: ' + auxInfo.size.width +
               ' rowStride: ' + auxInfo.rowStride + ' pixelFormat: ' + auxInfo.pixelFormat +
               ' colorSpace: ' + auxInfo.colorSpace);
             // 将辅助图数据读到ArrayBuffer。
             try {
               let pixelsBuffer = await auxPicture.readPixelsToBuffer();
               let opts: image.InitializationOptions = { size: auxInfo.size };
               try {
                 returnPixelMap = image.createPixelMapSync(pixelsBuffer, opts) as image.PixelMap;
                 console.info(`Create PixelMap with buffer successfully.`);
               } catch (error) {
                 console.error(`Create PixelMap failed with ${error}.`);
               }
             } catch (error) {
               console.error(`Read pixels to buffer failed, error.code: ${error.code},
                 error.message: ${error.message}`);
             }
             auxPicture.release();
           }
           return returnPixelMap;
         } else {
           return picture; // 返回解码后获取到的picture
         }
       }
       return returnPixelMap;
     } catch (error) {
       console.error(`Create picture failed: ${error}.`);
     }
     return returnPixelMap;
   }
   ```
5. 释放picture。

   确认picture的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```typescript
   async release(picture: image.Picture) {
     picture?.release();
   }
   ```
