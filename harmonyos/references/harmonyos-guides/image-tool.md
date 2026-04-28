---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool
title: 编辑图片Exif信息
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 编辑图片Exif信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a80435235fba505a56f93d18a73be34cedc6ed057adf012bdf177a9296cf1b58
---

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+、DNG23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

系统目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[Exif信息](../harmonyos-references/arkts-apis-image-e.md#propertykey7)。需要注意的是，DNG格式图片仅支持读取Exif信息，不支持修改。

## 开发步骤

Exif信息的读取与编辑相关的API详细介绍请参考[getImageProperty](../harmonyos-references/arkts-apis-image-imagesource.md#getimageproperty11)等接口。

获取图片，创建ImageSource。读取、编辑Exif信息。示例代码如下：

1. 导入相关模块包。

   ```
   1. // 导入相关模块包。
   2. import { image } from '@kit.ImageKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```

   [ExifUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ExifUtility.ets#L16-L20)
2. 获取指定key的Exif信息接口示例。

   ```
   1. // 获取指定key的Exif信息接口示例
   2. async getExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey): Promise<string> {
   3. let info: string = '';
   4. if (imageSourceApi) {
   5. console.info('getExif: The imageSourceApi is not undefined.');
   6. // 根据传入的key获取其Exif信息
   7. let options: image.ImagePropertyOptions = { index: 0, defaultValue: 'This key has no value!' };
   8. try {
   9. let data = await imageSourceApi.getImageProperty(key, options);
   10. info = `Succeeded in getting the ${key}'s value: ${data}.`;
   11. console.info(info);
   12. return info; // 获取key值成功时返回获取到的key值
   13. } catch (error) {
   14. info =
   15. `Failed to get the value of the ${key} with error: ${error}.`;
   16. console.error(info);
   17. return info; // 获取key值失败时返回错误信息
   18. }
   19. } else {
   20. info = 'getExif: The imageSourceApi is undefined.';
   21. console.info(info);
   22. return info; // 如果 imageSourceApi 是 undefined，则直接返回信息
   23. }
   24. }
   ```

   [ExifUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ExifUtility.ets#L23-L48)
3. 修改指定key的Exif信息的接口示例。

   ```
   1. // 修改指定key的Exif信息的接口示例
   2. async modifyExif(imageSourceApi: image.ImageSource | undefined, key: image.PropertyKey, value: string)
   3. : Promise<string> {
   4. let info: string = '';
   5. if (imageSourceApi) {
   6. // 编辑EXIF信息
   7. try {
   8. await imageSourceApi.modifyImageProperty(key, value);
   9. try {
   10. let modifyValue = await imageSourceApi.getImageProperty(key)
   11. info = `The ${key}'s value is modified to ${modifyValue}.`
   12. console.info(info);
   13. return info; // 获取key值成功时返回修改成功信息
   14. } catch (error) {
   15. console.error(`Failed to get the the ${key}'s value with ${error}`);
   16. console.error(info);
   17. return info; // 获取key值失败时返回错误信息
   18. }
   19. } catch (error) {
   20. info = `Failed to modify the ${key}'s value with ${error}`;
   21. console.error(info);
   22. return info; // 修改key值失败时返回错误信息
   23. }
   24. } else {
   25. info = 'modifyExif: The imageSourceApi is undefined.';
   26. console.info(info);
   27. return info; // 如果 imageSourceApi 是 undefined，直接返回信息
   28. }
   29. }
   ```

   [ExifUtility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageArkTSSample/entry/src/main/ets/tools/ExifUtility.ets#L50-L80)
