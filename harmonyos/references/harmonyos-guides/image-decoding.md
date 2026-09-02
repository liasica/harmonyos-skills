---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding
title: 使用ImageSource完成图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource完成图片解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c7eaff58f6afdb726502cb7bfdcb21be8949161da62893f6591f59e77bf84c5c
---

当应用需要读取图片内容、显示图片，或对图片进行缩放、裁剪等处理时，可使用[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)完成图片解码。应用可通过图片在应用沙箱中的路径、文件描述符或缓冲区创建ImageSource，并将图片解码为PixelMap。

解码后的PixelMap可用于图片显示、图像处理和编辑等场景。开发者还可在解码时设置图片尺寸、解码区域和输出像素格式，以适配不同的业务需求。

## 解码支持的图片格式

当前支持的图片文件格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIC、TIFF23+、HEIFS23+、WBMP23+。

从API版本26.0.0开始，增加支持AVIF、AVIS格式。

部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats](../harmonyos-references/arkts-apis-image-f.md#imagegetimagesourcesupportedformats20)接口，动态查询当前设备上的解码能力。

从API version 22开始，支持对专业相机拍摄的CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW格式图片内嵌的预览图（通常为JPEG格式）进行解码。该解码能力不受运行设备类型限制。

## 设置解码输出像素格式

图片解码像素格式是指将图片解码为PixelMap后采用的数据存储格式。使用[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)和[createPixelMapUsingAllocator](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmapusingallocator15)解码图片时，通过设置[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)中的desiredPixelFormat可指定期望的输出像素格式[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)。

不同像素格式在内存占用、透明度支持以及后续显示和图像处理场景中存在差异。当应用需要控制解码后的图像数据格式时，可设置desiredPixelFormat。

实际支持的格式组合与输入图片格式、图片特征、动态范围和设备能力有关。解码完成后，可调用[getImageInfoSync](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfosync12) 获取ImageInfo.pixelFormat，确认实际输出像素格式。

下表为不同图片格式支持的目标像素格式（desiredPixelFormat）：

| 输入图片格式 | 支持的目标像素格式 |
| --- | --- |
| JPEG、BMP、DNG、HEIC、WBMP、HEIFS、AVIF、AVIS | RGB\_565、RGBA\_8888、BGRA\_8888、NV21、NV12、ASTC\_4x4 |
| PNG、GIF、WebP、ICO | RGB\_565（图片不带透明通道）、RGBA\_8888、BGRA\_8888、NV21、NV12、ASTC\_4x4 |
| TIFF、SVG | RGBA\_8888、BGRA\_8888、ASTC\_4x4 |

**注意** 

* 将desiredPixelFormat设置为UNKNOWN时，输出像素格式默认为RGBA\_8888。
* 对于PNG、GIF、ICO和WebP图片，将desiredPixelFormat设置为RGB\_565时，仅支持解码不带透明通道的图片，带透明通道的图片解码失败。
* 当前解码不支持ARGB\_8888和RGBA\_F16像素格式。对于JPEG、BMP、DNG、HEIC、WBMP、HEIFS、AVIF、AVIS、PNG、GIF、WebP和ICO图片，如果将desiredPixelFormat设置为ARGB\_8888和RGBA\_F16，则解码输出的像素格式为RGBA\_8888。
* 当同时设置desiredPixelFormat和desiredDynamicRange时，前者用于指定期望的输出像素格式，后者用于指定解码后的动态范围。为满足SDR或HDR的解码要求，实际输出的PixelMap像素格式可能与desiredPixelFormat不同。建议调用[getImageInfoSync](../harmonyos-references/arkts-apis-image-pixelmap.md#getimageinfosync12)获取ImageInfo.pixelFormat，确认实际输出像素格式。

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
2. （可选）查询设备解码能力。

   部分图片格式的解码能力依赖于设备硬件，解码前可先查询设备支持的解码格式列表：

   ```typescript
   // 获取当前设备支持的解码格式列表。
   export function getSupportedFormats(): string[] {
     let formats = image.getImageSourceSupportedFormats();
     console.info('Supported formats: ' + formats);
     return formats;
   }

   // 检查指定格式是否支持解码。
   export function isFormatSupported(format: string): boolean {
     let formats = image.getImageSourceSupportedFormats();
     return formats.includes(format);
   }
   ```
3. 获取图片。

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
4. 创建ImageSource实例。

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
5. 设置解码参数DecodingOptions，解码获取pixelMap图片对象。

   配置解码选项参数进行解码：

   ```typescript
   async createPixelMap(imageSource: image.ImageSource | undefined): Promise<image.PixelMap | undefined> {
     if (!imageSource) {
       console.error('imageSource is undefined.');
       return undefined;
     }
     // 配置解码选项参数。
     let decodingOptions: image.DecodingOptions = {
       editable: true,
       desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
       // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelMap。
       desiredDynamicRange: image.DecodingDynamicRange.AUTO,
     };

     try {
       // 生成 pixelMap 并返回
       const pixelMap = await imageSource.createPixelMap(decodingOptions);
       if (pixelMap) {
         console.info('Create PixelMap successfully.');
         // 判断pixelMap是否为hdr内容。
         let imageInfo = await pixelMap.getImageInfo();
         console.info(`Create PixelMap successfully with imageInfo.isHdr: ${imageInfo.isHdr}.`);
         return pixelMap;
       } else {
         console.info('Create PixelMap failed.');
         return undefined;
       }
     } catch (error) {
       console.error(`Failed to create PixelMap: ${error}.`);
       return undefined;
     }
   }
   ```

   解码完成，获取到pixelMap对象后，可以进行后续[图片处理](image-transformation.md)。
6. 释放pixelMap和imageSource。

   确认pixelMap和imageSource的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

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

   **说明** 

   1. 释放imageSource的合适时机：createPixelMap执行完成，成功获取pixelMap后，如果确定不再使用imageSource的其他方法，可以手动释放imageSource。由于解码得到的pixelMap是一个独立的实例，imageSource的释放不会导致pixelMap不可用。
   2. 释放pixelMap的合适时机：如果使用系统的[Image组件](../harmonyos-references/ts-basic-components-image.md)进行图片显示，无需手动释放，Image组件会自动管理传递给它的pixelMap；如果应用自行处理pixelMap，则推荐在页面切换、应用退后台等场景下手动释放老页面pixelMap；在内存资源紧张的场景，推荐释放除当前页面外其他不可见页面的PixelMap。

## 进阶主题

* **内存优化解码**：使用DMA内存和YUV像素格式降低内存占用、提升解码性能，参见[图片解码内存优化](image-allocator-type.md)。
* **区域解码**：解码图片指定区域，适用于大图局部查看和裁剪预览场景，参见[图片区域解码与下采样](image-region-and-downsampling.md)。
* **下采样解码**：解码时直接缩放目标尺寸，避免解码后缩放的性能开销，适用于缩略图生成场景，参见[图片区域解码与下采样](image-region-and-downsampling.md)。
* **多图对象解码**：解码包含主图和辅助图的Picture对象，适用于HDR图片和HEIF专业格式处理，参见[使用ImageSource完成多图对象解码](image-picture-decoding.md)。

## 示例代码

* [实现图片获取与保存功能](https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave)
* [水印添加能力](https://gitcode.com/HarmonyOS_Samples/watermark)
