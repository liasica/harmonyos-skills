---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d59526b0b8f3be071b9213fdc8b46d5b4c1a4b0878624d2362342c942d797b93
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/VkxelyEyRTCl1ScMTD2g3A/zh-cn_image_0000002817507097.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCB112A0ADB4C46FCAF15423B1F88CC372F38F9ED81A4BA31736C275C4FA9F96)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/t6YqZOtTTRe5lasYi1tPFA/zh-cn_image_0000002788307666.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E94EE0D08EBB535C88AEC3F6B223812264306E783D4B266616838D08F07774F)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/cqWszfsKSDS6HWXFoXBn5w/zh-cn_image_0000002817427029.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D0F35A7C7880D6E4FA9D33892DCC62A35928DFCDADB3FFC09CED99A97C3281B)
   * 平移

     ```typescript
     // 向右平移100像素并向下平移100像素。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/l3r5RKK7RzOBQ-gLr8vRJw/zh-cn_image_0000002788467610.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C015C402B82D9932EFF62AA4C3B9084E44203000045167E145AC60A030C99F6)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/CbQqH507RqSDz4OlAXvC7Q/zh-cn_image_0000002817507099.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEF86CA19B54A54787A315755F54893962B7303CC5CB094ECB599806CDA0421C)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Iq6ACcKDQ1WK93h1DXDBXA/zh-cn_image_0000002788307668.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=25AC4C0CE2C1297F1C5DCB93A61A96249C57303DA99AA2CA9991E11942604D04)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/HGE4oPYZT0m_OpK65nfCBQ/zh-cn_image_0000002817427031.jpeg?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1088318927EC490934BA6E234495B230B813B23997659C6F2451E52E6369D7CA)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/f5-q8sz9Rj6es8LHgDhjyw/zh-cn_image_0000002788467612.png?HW-CC-KV=V1&HW-CC-Date=20261114T004758Z&HW-CC-Expire=31536000000&HW-CC-Sign=924FE98C612E95A189DC444EFD9D7CE22CB4C1AA317E84D32D01270BC50558B8)
