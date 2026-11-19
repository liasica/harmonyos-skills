---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:39+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dd20da5bfcc5d0d723350e91e2b63ae717cb2d5435a2b266b94b08e997c0d431
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/9PA0usv8RaCNdwnEwPQhRQ/zh-cn_image_0000002820525947.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6F2E6564E059736EA63A8191C2C66C905963D68DF9AFB4A7BBFDD0D68677FB3)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Qv3-5DF0QmCIAW8OrDtjDg/zh-cn_image_0000002820405947.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=397AD08083AF57431EF3FCFD5D79F2D4B6031EBFAC528B19E17C68B0A5829044)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/8BjMK5u6QHq1Yt9pRbu5Kw/zh-cn_image_0000002791725968.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6EDC6DD62B8EE2675677B9829B8AC43E13C2B28D792A5E38C61F812E0E955E5)
   * 平移

     ```typescript
     // 向右平移100像素并向下平移100像素。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/eAFnqHIgTt6GAAHZutSdeA/zh-cn_image_0000002791565996.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=5061917FDB371E570B39D51C74718A359B1C24CAAAF841BF797959C9F8177C81)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/tVHunOrYR1KRsIMtdcWC5w/zh-cn_image_0000002820525949.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=031BABDECF63C0F9E65BF9535148BC035AC04A88DD40D997ACF4FE37638F660A)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/wAWIer4nRA6EKUZHiTvPHQ/zh-cn_image_0000002820405949.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=97C9A9645EAEA08BD81F5D76B06A693FC60801B85D5C2E1215AF5681B92B2A3B)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/BLvkbHBfRH2XMcdXSQ5yHA/zh-cn_image_0000002791725970.jpeg?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1B7C3AD5D9DE4555CA544FA6B75635094E9736B815185A7CD12B6ACE84C8F8C)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Zos5TNSHQZGptl-tQVBbFg/zh-cn_image_0000002791565998.png?HW-CC-KV=V1&HW-CC-Date=20261119T014838Z&HW-CC-Expire=31536000000&HW-CC-Sign=645EADBB47D121A72CE7BF27CBB06A68CF99618DBA5734F73ABE9CD9231115A4)
