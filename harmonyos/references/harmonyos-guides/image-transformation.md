---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f615de844d911d22227f8d7df4697bf5961aebed1c0dd0f1df2d93119bd6e90c
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/U_XLXaLxSgCKCHt4q37KgQ/zh-cn_image_0000002815399437.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7CDC595E10112D99D9E492C0F1DD63C6A8AD200A24BB412839A54661CA2FF61)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/l-voHbYURNiia4GQ0Fnjjg/zh-cn_image_0000002786519862.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=92C7441650E27FEB2E0E5D2E7391ECAB4BB6569289DCDD04E117EF56BF8B74DF)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/5TssumNYSFWB6HIxDQhHqw/zh-cn_image_0000002786359934.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BEC9D5BBE6D1B18216C295088C69026F67AE5B6D9CDF3D0886469A5EEBC01A8)
   * 平移

     ```typescript
     // 向右平移100像素并向下平移100像素。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/n6aPECk6SOW8CmQDweI9hQ/zh-cn_image_0000002815559355.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D473CF1DEB0201ADF2799910805076A6ACE7F7AF078E1AE1D9727A2574EECF0B)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/zwgx20DKQa-rnoX01VRFAg/zh-cn_image_0000002815399439.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C4D96A3D16413FC999B812BB435265DC7703E7D31075E926789B7FCFFEDE9DD)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/WZpRp5gqS0qTNvNZ-3WqGA/zh-cn_image_0000002786519864.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=209737C964C8138ACA22566F4675A9756E8419F344B0BEFF5A6919963178FACF)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/LdQCL5DNTJGgUx4V6Uoebg/zh-cn_image_0000002786359936.jpeg?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D76E3776CE4AADC0A358176919776F110F30ADA9780BCE4EE0A637B0CE164B6A)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/3IqFihUMS6CewJC5tzQoUw/zh-cn_image_0000002815559357.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3894A713BB6DD1DAF3AE07254A317741665B91AF30D91AFCE3C3F873619C1992)
