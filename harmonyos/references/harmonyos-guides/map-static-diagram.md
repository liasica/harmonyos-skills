---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-static-diagram
title: 静态图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 静态图
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:31+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:e3b8724b3030cf534d3dacf92c566a47816bfc673ee49fbc91c0c9b5f02f2ffa
---

## 场景介绍

本章节将向您介绍如何使用静态图功能。静态图功能会返回一张地图图片，您可以将地图以图片形式嵌入自己的应用/元服务中。在使用时，您可以指定请求的地图位置、图片大小。

**图1** 静态图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/OuzLzCMYSGmdZ_eMAqG7Kw/zh-cn_image_0000002821838073.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A55DC2D6C88CC2C0BC76715C1DC4D5EA3D463A12501FF09956DEF806FFA9A6E2 "点击放大")

## 接口说明

以下是地图静态图相关接口，获取静态图功能主要由[staticMap](../harmonyos-references/map-staticmap.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-staticmap.md)。

| 接口名 | 描述 |
| --- | --- |
| [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions) | 用于描述静态图属性。 |
| [getMapImage](../harmonyos-references/map-staticmap.md#getmapimage)(options: [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions)): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 根据提供的参数创建静态图。 |
| [getMapImage](../harmonyos-references/map-staticmap.md#getmapimage-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), options: [StaticMapOptions](../harmonyos-references/map-staticmap.md#staticmapoptions)): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 根据提供的参数创建静态图。支持上传Context上下文。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { staticMap } from '@kit.MapKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建静态图初始化参数，调用[getMapImage](../harmonyos-references/map-staticmap.md#getmapimage)方法获取静态图，效果如下图。

   ```typescript
   @Entry
   @Component
   struct MapStaticDiagramDemo {
     // ...
     @State image?: PixelMap = undefined;

     build() {
       // ...
         Column() {
           this.buildDemoUI();
         }.width('100%')
         .margin({ bottom: 48 })
         .backgroundColor(0xf2f2f2)
         .height('100%')

         // ...
     }

     @Builder
     buildDemoUI() {
       // 展示获取的静态图
       Image(this.image)
         .width('100%')
         .fitOriginalSize(false)
         .border({ width: 1 })
         .borderStyle(BorderStyle.Dashed)
         .objectFit(ImageFit.Contain)
         .height('90%')

       Row() {
         Button('getStaticMap')
           .fontSize(12)
           .onClick(async () => {
             // 设置静态图标记参数
             let markers: staticMap.StaticMapMarker[] = [{
               location: {
                 latitude: 50,
                 longitude: 126.3
               },
               font: 'statics',
               defaultIconSize: staticMap.IconSize.TINY
             }];

             // 设置静态图绘制路径参数
             let path: staticMap.StaticMapPath = {
               locations: [
                 {
                   latitude: 50,
                   longitude: 126
                 },
                 {
                   latitude: 50.3,
                   longitude: 126
                 },
                 {
                   latitude: 50.3,
                   longitude: 126.3
                 },
                 {
                   latitude: 49.7,
                   longitude: 126
                 },
                 {
                   latitude: 50,
                   longitude: 126
                 }
               ],
               width: 3
             };

             // 拼装静态图参数
             let option: staticMap.StaticMapOptions = {
               location: {
                 latitude: 50,
                 longitude: 126
               },
               zoom: 10,
               imageWidth: 1024,
               imageHeight: 1024,
               scale: 1,
               markers: markers,
               path: path
             };

             try {
               // 获取静态图
               this.image = await staticMap.getMapImage(option);
               console.info('Succeeded in getting image.');
             } catch (error) {
               const err: BusinessError = error as BusinessError;
               console.error(`Failed in getting image, code: ${err.code}, message: ${err.message}`);
             }
           })
       }.margin({ top: 12 })
     }
   }
   ```

   **图2** 调用getMapImage方法获取静态图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/ZNgA7X9BQtqTnpHTD9Ur2w/zh-cn_image_0000002821758075.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011231Z&HW-CC-Expire=31536000000&HW-CC-Sign=55B42255D467628C80860FA898B5B56636994C3E1A0B90902AF2F875FE6BB391 "点击放大")
