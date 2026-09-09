---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-09-10T06:22:58+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:ff595eb14f14e53b80d08f48fed1eb5ae5b1e66d659da1e2962bfa24e51fb190
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GYKyQjurT66N6biXD6sIyQ/zh-cn_image_0000002717611418.jpeg)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/jgeBHdPUQkCoiSxsmP3amg/zh-cn_image_0000002747291371.jpeg)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/ISYXgE_RTIS_6Np10OX1ng/zh-cn_image_0000002747211289.jpeg)
   * 平移

     ```typescript
     // 向下平移100。
     // 向右平移100。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/eaH91gOSSkeLIVh5MwDVww/zh-cn_image_0000002717771354.jpeg)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Z5vSE7BURVq6U0EUCX3Tfw/zh-cn_image_0000002717611420.jpeg)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Bx34mtj_Tbe0w-KJvtkSvA/zh-cn_image_0000002747291373.jpeg)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Qu_kihVsRdGy7MsljdGpMQ/zh-cn_image_0000002747211291.jpeg)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/gC9iFldjRH-mOvlgXxsOkQ/zh-cn_image_0000002717771356.png)

## 示例代码

* [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
