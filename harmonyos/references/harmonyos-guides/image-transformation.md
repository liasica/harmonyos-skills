---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation
title: 使用PixelMap完成图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用PixelMap完成图像变换
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:03+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1f23f837fe5bd899b63b2d632d57e24c599dfff3649c3ed41d6af7d9f6d65abb
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/6vi1EH3DQJu0LTpBBibGiw/zh-cn_image_0000002793037618.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=495B677A4B8299D19EF745442EC5B2600B0CC24A41035B0FC1236D22DBC014B2)

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/1VraI6pCT1-D0td2VswhNQ/zh-cn_image_0000002792877648.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=A23AD0EC676A63510495772A81F2245F67009BB752BE52CB8A3FE40D707732BD)
   * 缩放

     ```typescript
     // 宽为原来的0.5倍。
     // 高为原来的0.5倍。
     this.pixelMap.scale(0.5, 0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/3xsCCE50Tvi5NYBiq01HEg/zh-cn_image_0000002821837555.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B3ACD61322112D1102F0D422893C04F57A6D3019565FF4A6E217DE849417DB6)
   * 平移

     ```typescript
     // 向右平移100像素并向下平移100像素。
     this.pixelMap.translate(100, 100).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/1XmxbDYdRA2C-pco3tknZQ/zh-cn_image_0000002821757557.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=A12533A18A3E6BB06068581A0CEB070F2EAF9214FCD6638AE3DFD1E540FB7E3A)
   * 旋转

     ```typescript
     // 顺时针旋转90°。
     this.pixelMap.rotate(90).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/QX328LG2QAGY-OK26LFw1Q/zh-cn_image_0000002793037620.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E46347BB21AE8793F4366A745935BCCD744B36F2C2BB82E15D98EFE265FD750)
   * 翻转

     ```typescript
     // 垂直翻转。
     this.pixelMap.flip(false, true).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/a-ur-MRYTxa5qtUdryzyJA/zh-cn_image_0000002792877650.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB8226D598DC988C82A1A7EC2BDAE3FFAED5AD5ED657470F99B0789E1BCA96EB)

     ```typescript
     // 水平翻转。
     this.pixelMap.flip(true, false).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/198CsRNrTDKzloqXW7gaxw/zh-cn_image_0000002821837557.jpeg?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=9628D6A0869C438E1BE983681004A8A9BAC2E2E8DE47DAF0539CEA8B79077290)
   * 透明度

     ```typescript
     // 将所有像素的透明度改为0.5。
     this.pixelMap.opacity(0.5).then(() => {
       // ...
     });
     ```

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jTvLNj92SBWQYQ4LDC7UPQ/zh-cn_image_0000002821757559.png?HW-CC-KV=V1&HW-CC-Date=20261121T011203Z&HW-CC-Expire=31536000000&HW-CC-Sign=737ADB69710C560380AAC73E1C9000A3BBC2B2C07E9C1C643B563C4A4197F5DE)
