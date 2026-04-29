---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2cf1d5ca8cb089b905de6c280169d3c2841b0a5a920957c8079f0a2bcfc2b6e0
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/gT2g_DqWRTC0bCvXO1Dxbg/zh-cn_image_0000002589244891.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=ACB6AD3E1F50F6DAF1DA190FE1ADD4470E9CD445D689C1334D003180E7994DBA)

   * 裁剪

     ```
     1. // x：裁剪起始点横坐标0。
     2. // y：裁剪起始点纵坐标0。
     3. // height：裁剪高度400，方向为从上往下（裁剪后的图片高度为400）。
     4. // width：裁剪宽度400，方向为从左到右（裁剪后的图片宽度为400）。
     5. pixelMap.crop({x: 0, y: 0, size: { height: 400, width: 400 } });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/2iueoL0QTMmJ5aSEt-FQeg/zh-cn_image_0000002558765086.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=F8BA204137254025531405DB93B0E3CF0BA2230F8EC3EB4C972DC264F3704F1C)
   * 缩放

     ```
     1. // 宽为原来的0.5。
     2. // 高为原来的0.5。
     3. pixelMap.scale(0.5, 0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/w37-sA7ZSS2vJXS4HnZz4A/zh-cn_image_0000002558605430.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=9B3EC614754FB0151EB4FD97CAC883A5AF9E9063C2B8882F0364EB73F72BE5F5)
   * 偏移

     ```
     1. // 向下偏移100。
     2. // 向右偏移100。
     3. pixelMap.translate(100, 100);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/QnsD0pl0TwSoHUycbZck6w/zh-cn_image_0000002589324957.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=4A1EE3BBBDE56AA0EA4D04B001B3D5CD1B78172F8D6928E884B54059F7C540CE)
   * 旋转

     ```
     1. // 顺时针旋转90°。
     2. pixelMap.rotate(90);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/37TtcpGXRciurlwQP__raw/zh-cn_image_0000002589244893.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=7D68C5D05A4A54FAD496130642E9A200A604DF97E07C13E52789737E257BB57C)
   * 翻转

     ```
     1. // 垂直翻转。
     2. pixelMap.flip(false, true);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/2ZC9HCmVThOg3mrtmYdq7Q/zh-cn_image_0000002558765088.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=B303C5E6A79F3D13D8A7EB74857E4E8C6B590B51C385833BD2C56FD7AC86B982)

     ```
     1. // 水平翻转。
     2. pixelMap.flip(true, false);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/-tZjfIWaTtygCGCoo93LjQ/zh-cn_image_0000002558605432.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=ECF277A7D28C940A1D2C2562B3C3FB9A23D57C9C0852E8C493A79248D0914516)
   * 透明度

     ```
     1. // 透明度0.5。
     2. pixelMap.opacity(0.5);
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/kcLGUa1CTsar7b5dA1lQdA/zh-cn_image_0000002589324959.png?HW-CC-KV=V1&HW-CC-Date=20260429T053512Z&HW-CC-Expire=86400&HW-CC-Sign=4307E44DEC4C2E8D8A0C7EF65DFF449C6FA399E6A31808F53DC335AA5D2BA0BF)

## 示例代码

* [拼图](https://gitcode.com/HarmonyOS_Samples/game-puzzle)
