---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-picture-decoding
title: 使用ImageSource完成多图对象解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 使用ImageSource完成多图对象解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a887ed45940c427399374502503eaa808a6d574ff3c935cf908b6a795e4d46f
---

将所支持格式的图片文件解码成[Picture](image-overview.md#基础概念)。当前支持的图片文件格式包括JPEG、HEIF。

## 开发步骤

图片解码相关API的详细介绍请参见[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)。

1. 全局导入Image模块。

   ```
   1. // 导入相关模块包。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   5. import { fileIo as fs } from '@kit.CoreFileKit';
   6. import { resourceManager } from '@kit.LocalizationKit';
   ```

   [DecodingPicture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/pages/DecodingPicture.ets#L16-L23)
2. 获取图片。

   * 方法一：通过沙箱路径直接获取。该方法仅适用于应用沙箱中的图片。更多细节请参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。

     ```
     1. function getFilePath(context: Context, fileName: string): string {
     2. const filePath: string = context.cacheDir + '/' + fileName;
     3. return filePath;
     4. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L31-L36)
   * 方法二：通过沙箱路径获取图片的文件描述符。具体请参考文档[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)。该方法需要导入@kit.CoreFileKit模块。

     ```
     1. function getFileFd(context: Context, fileName: string): number | undefined {
     2. try {
     3. const filePath: string = context.cacheDir + '/' + fileName;
     4. const file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
     5. const fd: number = file?.fd;
     6. return fd;
     7. } catch (err) {
     8. console.error(`Failed to get the fileFd with error: ${err}.`);
     9. return undefined;
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L38-L45)
   * 方法三：通过资源管理器获取资源文件的ArrayBuffer。具体请参考[资源管理器API参考文档](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9-1)。该方法需要导入@kit.LocalizationKit模块。

     ```
     1. async function getFileBuffer(context: Context, fileName: string): Promise<ArrayBuffer | undefined> {
     2. try {
     3. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     4. // 获取资源文件内容，返回Uint8Array。
     5. const fileData: Uint8Array = await resourceMgr.getRawFileContent(fileName);
     6. console.info('Successfully get the RawFileContent.');
     7. // 转为ArrayBuffer并返回。
     8. const buffer: ArrayBuffer = fileData.buffer.slice(0);
     9. return buffer;
     10. } catch (error) {
     11. console.error(`Failed to get the RawFileContent with error: ${error}.`);
     12. return undefined;
     13. }
     14. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L47-L62)
   * 方法四：通过资源管理器获取资源文件的RawFileDescriptor。具体请参考[资源管理器API参考文档](../harmonyos-references/js-apis-resource-manager.md#getrawfd9-1)。该方法需要导入@kit.LocalizationKit模块。

     ```
     1. async function getRawFd(context: Context, fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
     2. try {
     3. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     4. const rawFileDescriptor: resourceManager.RawFileDescriptor = await resourceMgr.getRawFd(fileName);
     5. console.info('Successfully get the RawFileDescriptor.');
     6. return rawFileDescriptor;
     7. } catch (error) {
     8. console.error(`Failed to get the RawFileDescriptor with error: ${error}.`);
     9. return undefined;
     10. }
     11. }
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L64-L76)
3. 创建ImageSource实例。

   * 方法一：通过沙箱路径创建ImageSource。沙箱路径可以通过步骤2的方法一获取。

     ```
     1. // path为已获得的沙箱路径。
     2. const imageSource : image.ImageSource = image.createImageSource(filePath);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L182-L185)
   * 方法二：通过文件描述符fd创建ImageSource。文件描述符可以通过步骤2的方法二获取。

     ```
     1. // fd为已获得的文件描述符。
     2. const imageSource: image.ImageSource = image.createImageSource(fd);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L195-L198)
   * 方法三：通过缓冲区数组创建ImageSource。缓冲区数组可以通过步骤2的方法三获取。

     ```
     1. const imageSource: image.ImageSource = image.createImageSource(buffer);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L209-L211)
   * 方法四：通过资源文件的RawFileDescriptor创建ImageSource。RawFileDescriptor可以通过步骤2的方法四获取。

     ```
     1. const imageSource: image.ImageSource = image.createImageSource(rawFileDescriptor);
     ```

     [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L222-L224)
4. 设置解码参数DecodingOptions，解码获取picture多图对象。并对picture进行操作，如获取辅助图等。对于picture和辅助图的具体操作请参考文档[Picture](../harmonyos-references/arkts-apis-image-picture.md)。

   配置解码选项参数进行解码：

   ```
   1. async createPicture(imageSource : image.ImageSource | undefined, isReturnAux: Boolean)
   2. : Promise<image.PixelMap | undefined | image.Picture> {
   3. // 配置解码选项参数。
   4. let options: image.DecodingOptionsForPicture = {
   5. desiredAuxiliaryPictures: [image.AuxiliaryPictureType.GAINMAP] // GAINMAP为需要解码的辅助图类型。
   6. };
   7. let returnPixelMap: image.PixelMap | undefined = undefined;
   8. // 创建picture。
   9. try {
   10. let picture = await imageSource?.createPicture(options);
   11. if (picture) {
   12. // 返回解码后获取到的辅助图
   13. if (isReturnAux) {
   14. // type为解码参数中包含的辅助图类型
   15. let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
   16. let auxPicture: image.AuxiliaryPicture | null = picture.getAuxiliaryPicture(type);
   17. // 获取辅助图信息。
   18. if (auxPicture != null) {
   19. let auxInfo: image.AuxiliaryPictureInfo = auxPicture.getAuxiliaryPictureInfo();
   20. console.info('GetAuxiliaryPictureInfo type: ' + auxInfo.auxiliaryPictureType +
   21. ' height: ' + auxInfo.size.height + ' width: ' + auxInfo.size.width +
   22. ' rowStride: ' + auxInfo.rowStride + ' pixelFormat: ' + auxInfo.pixelFormat +
   23. ' colorSpace: ' + auxInfo.colorSpace);
   24. // 将辅助图数据读到ArrayBuffer。
   25. try {
   26. let pixelsBuffer = await auxPicture.readPixelsToBuffer();
   27. let opts: image.InitializationOptions = { size: auxInfo.size };
   28. try {
   29. returnPixelMap = image.createPixelMapSync(pixelsBuffer, opts) as image.PixelMap;
   30. console.info(`Create PixelMap with buffer successfully.`);
   31. } catch (error) {
   32. console.error(`Create PixelMap failed with ${error}.`);
   33. }
   34. } catch (error) {
   35. console.error(`Read pixels to buffer failed, error.code: ${error.code},
   36. error.message: ${error.message}`);
   37. }
   38. auxPicture.release();
   39. }
   40. return returnPixelMap;
   41. } else {
   42. return picture; // 返回解码后获取到的picture
   43. }
   44. }
   45. return returnPixelMap;
   46. } catch (error) {
   47. console.error(`Create picture failed: ${error}.`);
   48. }
   49. return returnPixelMap;
   50. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L265-L316)
5. 释放picture。

   确认picture的异步方法已经执行完成，不再使用该变量后，可按需手动调用下面方法释放。

   ```
   1. async release(picture: image.Picture) {
   2. picture?.release();
   3. }
   ```

   [CodecUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/CodecUtility.ets#L334-L338)
