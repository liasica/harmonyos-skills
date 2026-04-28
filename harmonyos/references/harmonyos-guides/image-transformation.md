---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9fe96540b96c2ce4c83c665d8bd69e1a2d38aa6692b55b400310042be181a794
---

图片处理指对PixelMap进行相关的操作，如获取图片信息、裁剪、缩放、偏移、旋转、翻转、设置透明度、读写像素数据等。图片处理主要包括图像变换、[位图操作](image-pixelmap-operation.md)，本文介绍图像变换。

## 开发步骤

图像变换相关API的详细介绍请参见[API参考](../harmonyos-references/arkts-apis-image-pixelmap.md)。

1. 完成[图片解码](image-decoding.md)，获取PixelMap对象。
2. 获取图片信息。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. // 获取图片大小。
   3. pixelMap.getImageInfo().then( (info : image.ImageInfo) => {
   4. console.info('info.width = ' + info.size.width);
   5. console.info('info.height = ' + info.size.height);
   6. }).catch((err : BusinessError) => {
   7. console.error("Failed to obtain the image pixel map information.And the error is: " + err);
   8. });
   ```
3. 进行图像变换操作。

   原图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/CdgITebqQEKO5_IAUyVIPA/zh-cn_image_0000002583438631.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=9E127F64BDDA6D236ECD9A913092B6EF110618DB0BEDA18EC1C63C622595F08C)

   * 裁剪

     ```
     1. // x：裁剪起始点横坐标0。
     2. // y：裁剪起始点纵坐标0。
     3. // height：裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。
     4. // width：裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。
     5. pixelMap.crop({x: 0, y: 0, size: { height: 400, width: 400 } });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/lnhGBHBAQ_OkUo4CLzUF5w/zh-cn_image_0000002552958586.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=76762D533DC292195E45EDA4B1303BCDA45349644014E6610A52548195092A19)
   * 缩放

     ```
     1. // 宽为原来的0.5。
     2. // 高为原来的0.5。
     3. pixelMap.scale(0.5, 0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/2XdhYsHgQUCUyBn0Uj7Fhw/zh-cn_image_0000002583478587.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=F5E5E65E1E9339F2163CB668C49012A0018597FF18362C768B477A1135027776)
   * 偏移

     ```
     1. // 向下偏移100。
     2. // 向右偏移100。
     3. pixelMap.translate(100, 100);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/hVqD_0hMSfqDeyvTbeWN8w/zh-cn_image_0000002552798938.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=B301AC4EBE5A253746700BE00A354166B491C0A2F55D3C10420DF9557EC4F020)
   * 旋转

     ```
     1. // 顺时针旋转90°。
     2. pixelMap.rotate(90);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/BNJLoz1eQDGeUNPeHId6-g/zh-cn_image_0000002583438633.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=54112D56FC12A1035E74B2618ED66E593CED0229960336CB4E2B7F79ABB59A77)
   * 翻转

     ```
     1. // 垂直翻转。
     2. pixelMap.flip(false, true);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/4Zp7UEdZQ4KoBXUUoX8A6w/zh-cn_image_0000002552958588.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=4BBFF199E44CEB1199DC23EF544F1F72398D5ED3AE32A1CFE00DD877EEDC5F74)

     ```
     1. // 水平翻转。
     2. pixelMap.flip(true, false);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/nrBaSMS1RpWgVq70JpWF8w/zh-cn_image_0000002583478589.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=0CFB4654530DB54B40ECAB86025BA8179AD9DB38B6DD4914476216097CDE477E)
   * 透明度

     ```
     1. // 透明度0.5。
     2. pixelMap.opacity(0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/LeAK0KTFQpm2Khd-3FHTVA/zh-cn_image_0000002552798940.png?HW-CC-KV=V1&HW-CC-Date=20260427T234614Z&HW-CC-Expire=86400&HW-CC-Sign=54115DEC5DEB8C606AF7ADAE19E04F89457A222BF1F509B5BCBEEDDD3593C37D)

## 示例代码

* [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
