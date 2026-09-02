---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-screenshots
title: 地图截图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 地图截图
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:28+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:4d79b66d9aff46d662bb9d41507598d7061a708f63c4c37514f0f829feceb946
---

本章节将向您介绍如何实现地图截图功能。

地图截图指对当前屏幕显示区域进行截屏，支持对地图、覆盖物、Logo进行屏幕截图。地图截图功能适用于需要将当前地图状态保存为图片的场景，如分享当前位置、生成导航路线图、记录特定视角的地图内容等。该功能可以帮助开发者快速实现地图内容的可视化输出，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/0CNZyjGHStaaznncjtHnkA/zh-cn_image_0000002706675108.jpg "点击放大")

## 接口说明

以下是地图截图相关接口，以下功能主要由[snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)。

| 接口名 | 描述 |
| --- | --- |
| [snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)(): Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 地图截图。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   import { image } from '@kit.ImageKit';
   ```
2. 调用[snapshot](../harmonyos-references/map-map-mapcomponentcontroller.md#snapshot)方法对当前屏幕进行截图。

   ```typescript
   @Entry
   @Component
   struct MapScreenshotsDemo {
     // ...
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     @State image?: image.PixelMap = undefined;

     aboutToAppear(): void {
       // 地图初始化参数，设置地图中心点坐标及层级
       this.mapOptions = {
         position: {
           target: {
             latitude: 39.9,
             longitude: 116.4
           },
           zoom: 10
         }
       };

       // 地图初始化的回调
       this.callback = async (err, mapController) => {
         if (!err) {
           // 获取地图的控制器类，用来操作地图
           this.mapController = mapController;
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       // ...
         Stack() {
           Column() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
               .width('100%')
               .height('50%');

             Scroll(new Scroller()) {
               Column() {
                 Image(this.image)
                   .objectFit(ImageFit.Auto)
                   .border({ width: 1, color: Color.Red }).width('100%')
                 Button('获取截图')
                   .margin({ left: 10 })
                   .fontSize(12)
                   .onClick(async () => {
                     if (this.mapController) {
                       // 获取截图
                       let pixelMap = await this.mapController.snapshot();
                       this.image = pixelMap;
                     }
                   });
               }
             }.width('70%').height('50%')
           }.width('100%')
         }.height('100%')

         // ...
     }
   }
   ```
