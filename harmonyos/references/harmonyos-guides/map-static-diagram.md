---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-static-diagram
title: 静态图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 静态图
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:24+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:55ac3be667b5ab6fddc3dac4473556124ed08aaaceb3ffd912cc90b53ce88168
---

## 场景介绍

本章节将向您介绍如何使用静态图功能。静态图功能会返回一张地图图片，您可以将地图以图片形式嵌入自己的应用/元服务中。在使用时，您可以指定请求的地图位置、图片大小。

**图1** 静态图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/_V1lHf3GSVetgBeTj-KSIg/zh-cn_image_0000002817427547.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A0C61A259341669848855CB719649D927E103B559D39CD868D2D6679E4B1077 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/xoAO8WavROuysTMAx4-YbQ/zh-cn_image_0000002788468128.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8EA12755C4B5693A05A5C5D5E68D14D838F3F40C5A2AD647CCC9AF0C53E0A25 "点击放大")
