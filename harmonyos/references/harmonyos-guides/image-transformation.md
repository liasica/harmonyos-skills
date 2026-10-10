---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-10-11T07:21:57+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:4e078fa6ccd7edd2c0f0dca0be9c6e2808f50554a38021cab11fbe0b592a8777
---

图片处理指对PixelMap进行相关的操作，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。图片处理主要包括图像变换、[位图操作](image-pixelmap-operation.md)，本文介绍图像变换。

## 开发步骤

图像变换相关API的详细介绍请参见[Interface (PixelMap)](../harmonyos-references/arkts-apis-image-pixelmap.md)。

1. 完成[图片解码](image-decoding.md)，获取PixelMap对象。
2. 获取图片信息。

   ```typescript
   // 获取图片大小。
   await this.pixelMap.getImageInfo().then((info: image.ImageInfo) => {
     this.imageInfo = info;
     Logger.info('Image width: ', info.size.width.toString());
     Logger.info('Image height: ', info.size.height.toString());
   }).catch((err: BusinessError) => {
     Logger.error('Failed to obtain the image pixel map information. The error is: ', String(err));
   });
   ```
3. 进行图像变换操作。

   原图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Xz1j9565TqeYlIWD5oxcwA/zh-cn_image_0000002784663305.jpeg)

   * 裁剪

     ```typescript
     const imageInfo = this.pixelMap.getImageInfoSync();
     const cropWidth = Math.min(400, imageInfo.size.width); // 原图宽度小于400时防止裁剪区域超出范围。
     const cropHeight = Math.min(400, imageInfo.size.height); // 原图高度小于400时防止裁剪区域超出范围。
     // x：裁剪起始点横坐标0。
     // y：裁剪起始点纵坐标0。
     // width：原图宽度不小于400时，裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。
     // height：原图高度不小于400时，裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。
     this.pixelMap.crop({ x: 0, y: 0, size: { width: cropWidth, height: cropHeight } }).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/nY9f1s4iSJOfWz8fFIFwkw/zh-cn_image_0000002755024372.jpeg)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/2aRHkCLLR9arEa84LB5lsw/zh-cn_image_0000002755184260.jpeg)
   * 平移

     ```typescript
     // 向下平移100。
     // 向右平移100。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/7fufE8_9TIO9HG3Am8oVug/zh-cn_image_0000002784583127.jpeg)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/-Pe44sWjTqi2qmruMzcuRQ/zh-cn_image_0000002784663307.jpeg)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/qlXBo5bOQC6gK_YdmQE4tQ/zh-cn_image_0000002755024374.jpeg)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7moORnDTTzK4oaJFmXXbjQ/zh-cn_image_0000002755184262.jpeg)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/8VYZq49FQq-Zw2wRbQla5w/zh-cn_image_0000002784583129.png)

## 示例代码

* [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
