---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding
title: 使用ImagePacker完成图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编码 > 使用ImagePacker完成图片编码
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d4f500106dcf9e58a8a150a9af3ca424204f031d53dec1d80c2729c6f584bb5c
---

图片编码指将PixelMap压缩成不同格式的图片文件，用于保存和传输。

支持使用[PackToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13-1)和[PackToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-2)将[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)编码为JPEG、WebP、PNG和HEIC格式。

从API version 18开始，支持使用[PackToDataFromPixelmapSequence](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodatafrompixelmapsequence18)和[PackToFileFromPixelmapSequence](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofilefrompixelmapsequence18)将多个PixelMap编码为GIF格式。

## 开发步骤

图片编码相关API的详细介绍请参见[ImagePacker](../harmonyos-references/arkts-apis-image-imagepacker.md)。

### 图片编码进文件流

1. 导入相关模块包。

   ```
   1. // 导入相关模块。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { fileIo as fs } from '@kit.CoreFileKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   ```

   [EncodingPixelMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/EncodingPixelMap.ets#L16-L23)
2. 设置编码选项[PackingOption](../harmonyos-references/arkts-apis-image-i.md#packingoption)。

   2.1 这里以编码成jpeg图片为例。编码的目标格式format遵循MIME标准定义，因此PackingOption.format应设置为image/jpeg，编码后的文件扩展名可设为.jpg或.jpeg。

   ```
   1. let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L83-L85)

   2.2 当图片源是HDR，且希望编码为HDR图片文件时，需要额外配置desiredDynamicRange。

   ```
   1. // 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
   2. packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L86-L89)
3. 封装函数，传入imageSource或pixelMap，使用[packToData](../harmonyos-references/arkts-apis-image-imagepacker.md#packtodata13)接口编码到ArrayBuffer，或使用[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)接口编码到文件。

   说明

   在进行编码前，需要先获取imageSource或pixelMap，可参考[使用ImageSource完成图片解码](image-decoding.md)。

   * pixelMap编码到ArrayBuffer。

     ```
     1. async function packToDataFromPixelMap(pixelMap : image.PixelMap) {
     2. const imagePackerApi = image.createImagePacker();
     3. let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
     4. // 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
     5. packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
     6. try{
     7. let data = await imagePackerApi.packToData(pixelMap, packOpts);
     8. // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
     9. copyData = new ArrayBuffer(0);
     10. copyData = data;
     11. } catch (error) {
     12. console.error('Failed to pack the pixelMap to data. And the error is: ' + error);
     13. }
     14. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L78-L101)
   * imageSource编码到ArrayBuffer。

     ```
     1. async function packToDataFromImageSource(imageSource : image.ImageSource) {
     2. const imagePackerApi = image.createImagePacker();
     3. let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
     4. try {
     5. let data = await imagePackerApi.packToData(imageSource, packOpts);
     6. // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
     7. copyData = new ArrayBuffer(0);
     8. copyData = data;
     9. } catch (error) {
     10. console.error('Failed to pack the imageSource to data. And the error is: ' + error);
     11. }
     12. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L103-L118)
   * pixelMap编码到文件。

     ```
     1. async function packToFileFromPixelMap(context : Context, pixelMap : image.PixelMap) {
     2. const imagePackerApi = image.createImagePacker();
     3. let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
     4. const path : string = context.cacheDir + '/pixel_map.jpg';
     5. try {
     6. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
     7. await imagePackerApi.packToFile(pixelMap, file.fd, packOpts);
     8. } catch (error) {
     9. console.error('Failed to pack the pixelMap to file. And the error is: ' + error);
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L120-L132)
   * imageSource编码到文件。

     ```
     1. async function packToFileFromImageSource(context : Context, imageSource : image.ImageSource) {
     2. const imagePackerApi = image.createImagePacker();
     3. let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
     4. const filePath : string = context.cacheDir + '/image_source.jpg';
     5. try {
     6. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
     7. await imagePackerApi.packToFile(imageSource, file.fd, packOpts);
     8. } catch (error) {
     9. console.error('Failed to pack the imageSource to file. And the error is: ' + error);
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L134-L146)
4. 将图片保存进图库。

将图片编码到ArrayBuffer或文件后，可使用[Media Library Kit](photoaccesshelper-overview.md)的相关接口[保存媒体库资源](photoaccesshelper-savebutton.md)保存进图库。

## 示例代码

* [图片压缩](https://gitcode.com/HarmonyOS_Samples/image-compression)
