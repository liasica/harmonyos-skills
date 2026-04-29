---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation
title: 使用PixelMap完成位图操作
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成位图操作
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:13+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:811dbb4ced164a01dce627922bccb679794abf01f1b6993651f9b69d03bd666c
---

当需要对目标图片中的部分区域进行处理时，可以使用位图操作功能。此功能常用于图片美化等操作。

如下图所示，一张图片中，将指定的矩形区域像素数据读取出来，进行修改后，再写回原图片对应区域。

**图1** 位图操作示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/_PCj_r4dTfmAMFUoH86AlQ/zh-cn_image_0000002589244895.png?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=B223274281D243CC668ADEBDF9B8E2E5E9C361CC1B8EAF4AF4F59DE1BC88171F)

## 开发步骤

位图操作相关API的详细介绍请参见[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

1. 完成[图片解码](image-decoding.md)，获取PixelMap位图对象。
2. 从PixelMap位图对象中获取信息。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // 获取图像像素的总字节数。
   4. let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
   5. // 获取图像像素每行字节数。
   6. let rowBytes: number = pixelMap.getBytesNumberPerRow();
   7. // 获取当前图像像素密度。像素密度是指每英寸图片所拥有的像素数量。像素密度越大，图片越精细。
   8. let density: number = pixelMap.getDensity();
   ```
3. 读取并修改目标区域像素数据，写回原图。

   说明

   建议readPixelsToBuffer和writeBufferToPixels成对使用，readPixels和writePixels成对使用，避免因图像像素格式不一致，造成PixelMap图像出现异常。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // 场景一：读取并修改整张图片数据。
   4. // 按照PixelMap的像素格式，读取PixelMap的图像像素数据，并写入缓冲区中。
   5. const buffer = new ArrayBuffer(pixelBytesNumber);
   6. pixelMap.readPixelsToBuffer(buffer).then(() => {
   7. console.info('Succeeded in reading image pixel data.');
   8. }).catch((error : BusinessError) => {
   9. console.error('Failed to read image pixel data. The error is: ' + error);
   10. })
   11. // 按照PixelMap的像素格式，读取缓冲区中的图像像素数据，并写入PixelMap。
   12. pixelMap.writeBufferToPixels(buffer).then(() => {
   13. console.info('Succeeded in writing image pixel data.');
   14. }).catch((error : BusinessError) => {
   15. console.error('Failed to write image pixel data. The error is: ' + error);
   16. })

   18. // 场景二：读取并修改指定区域内的图片数据。
   19. // 固定按照BGRA_8888格式，读取PixelMap指定区域内的图像像素数据，并写入PositionArea.pixels缓冲区中，该区域由PositionArea.region指定。
   20. const area : image.PositionArea = {
   21. pixels: new ArrayBuffer(8),
   22. offset: 0,
   23. stride: 8,
   24. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
   25. }
   26. pixelMap.readPixels(area).then(() => {
   27. console.info('Succeeded in reading the image data in the area.');
   28. }).catch((error : BusinessError) => {
   29. console.error('Failed to read the image data in the area. The error is: ' + error);
   30. })
   31. // 固定按照BGRA_8888格式，读取PositionArea.pixels缓冲区中的图像像素数据，并写入PixelMap指定区域内，该区域由PositionArea.region指定。
   32. pixelMap.writePixels(area).then(() => {
   33. console.info('Succeeded in writing the image data in the area.');
   34. }).catch((error : BusinessError) => {
   35. console.error('Failed to write the image data in the area. The error is: ' + error);
   36. })
   ```

## 开发示例

### 复制（深拷贝）位图并改变像素格式

说明

* 该方法仅可实现PixelMap基本内容的复制，不支持复制色域和HDR元数据。如果不需要改变新PixelMap的像素格式，请使用[clone](../harmonyos-references/arkts-apis-image-pixelmap.md#clone18)或[cloneSync](../harmonyos-references/arkts-apis-image-pixelmap.md#clonesync18)。
* 该方法不支持将新PixelMap转换为下列像素格式：RGBA\_1010102、YCBCR\_P010、YCRCB\_P010、ASTC\_4x4。

1. 完成[图片解码](image-decoding.md)，获取PixelMap位图对象。
2. 参考以下代码对PixelMap进行深拷贝。

   ```
   1. /**
   2. * 复制（深拷贝）PixelMap并改变像素格式。
   3. *
   4. * @param pixelMap - 被复制的原PixelMap。
   5. * @param desiredPixelFormat - 新PixelMap的像素格式。如果不指定，则仍使用原PixelMap的像素格式。
   6. * @returns 新PixelMap的Promise。
   7. */
   8. async function clonePixelMap(pixelMap: PixelMap, desiredPixelFormat?: image.PixelMapFormat): Promise<PixelMap> {
   9. // 获取原PixelMap的图片信息。
   10. const imageInfo = pixelMap.getImageInfoSync();
   11. // 读取原PixelMap的像素数据，并按照原PixelMap的像素格式写入缓冲区。
   12. const buffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
   13. await pixelMap.readPixelsToBuffer(buffer);

   15. // 根据原PixelMap的图片信息，生成初始化选项。
   16. const options: image.InitializationOptions = {
   17. // 数据源的像素格式：必须匹配原PixelMap的像素格式，否则新PixelMap的图像会出现异常。
   18. srcPixelFormat: imageInfo.pixelFormat,
   19. // 新PixelMap的像素格式。
   20. pixelFormat: desiredPixelFormat || imageInfo.pixelFormat,
   21. // 新PixelMap的透明度类型。
   22. alphaType: imageInfo.alphaType,
   23. // 新PixelMap的尺寸：必须匹配原PixelMap的尺寸，不支持传入其他尺寸以进行缩放。
   24. size: imageInfo.size
   25. };

   27. // 根据像素数据和初始化选项，创建新PixelMap。
   28. return await image.createPixelMap(buffer, options);
   29. }
   ```

### 将两张宽度相同的位图纵向拼接成一张长图

说明

该方法仅支持以下像素格式的PixelMap：RGBA\_8888、BGRA\_8888、RGBA\_F16。

1. 完成[图片解码](image-decoding.md)，获取两张宽度相同且像素格式相同的PixelMap位图对象。
2. 参考以下代码对两张PixelMap进行拼接。

   ```
   1. async function concatPixelMap(pixelMap1: PixelMap, pixelMap2: PixelMap): Promise<PixelMap> {
   2. // 将pixelMap1的像素数据读取至area1.pixels中。
   3. const imageInfo1 = pixelMap1.getImageInfoSync();
   4. const area1: image.PositionArea = {
   5. pixels: new ArrayBuffer(pixelMap1.getPixelBytesNumber()),
   6. offset: 0,
   7. stride: pixelMap1.getBytesNumberPerRow(),
   8. region: {
   9. size: imageInfo1.size,
   10. x: 0,
   11. y: 0
   12. }
   13. };
   14. await pixelMap1.readPixels(area1);

   16. // 将pixelMap2的像素数据读取至area2.pixels中。
   17. const imageInfo2 = pixelMap2.getImageInfoSync();
   18. const area2: image.PositionArea = {
   19. pixels: new ArrayBuffer(pixelMap2.getPixelBytesNumber()),
   20. offset: 0,
   21. stride: pixelMap2.getBytesNumberPerRow(),
   22. region: {
   23. size: imageInfo2.size,
   24. x: 0,
   25. y: 0
   26. }
   27. };
   28. await pixelMap2.readPixels(area2);

   30. // 创建一个新的空白PixelMap，其宽度与pixelMap1和pixelMap2相等，高度为pixelMap1和pixelMap2相加。
   31. const options: image.InitializationOptions = {
   32. srcPixelFormat: imageInfo1.pixelFormat,
   33. pixelFormat: imageInfo1.pixelFormat,
   34. size: {
   35. width: imageInfo1.size.width,
   36. height: imageInfo1.size.height + imageInfo2.size.height
   37. }
   38. };
   39. const newPixelMap = image.createPixelMapSync(options);

   41. // 将之前获取的pixelMap1和pixelMap2的像素数据按顺序写入新PixelMap。
   42. await newPixelMap.writePixels(area1);
   43. area2.region.y = imageInfo1.size.height; // pixelMap2像素的写入位置应该从pixelMap1末行像素的下一行开始。
   44. await newPixelMap.writePixels(area2);

   46. return newPixelMap;
   47. }
   ```

## 示例代码

* [PixelMap深拷贝案例](https://gitcode.com/HarmonyOS_Samples/image-depth-copy)
