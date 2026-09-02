---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-coverings
title: 覆盖物
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 覆盖物
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:28+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:219c4a2198d9ad298f5d6de85e97899940061e9a64417633f724e0a38b74d4eb
---

## 场景介绍

地图覆盖物是固定在地图上的图片，本章节将向您介绍如何为地图增加覆盖物。

覆盖物是一种显示在地图表面的图像图层，它不会遮挡地图上的文字和图标标注，这种图层类型允许图片随地图操作自动调整位置和大小。通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类来设置，开发者可以通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类设置一张图片，该图片可随地图的平移、缩放、旋转等操作做相应的变换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Lqobiry4QseIYhVx9qg_4Q/zh-cn_image_0000002736314171.jpg "点击放大")

## 接口说明

增加覆盖物功能主要由[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)、[addImageOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addimageoverlay)、[ImageOverlay](../harmonyos-references/map-map-imageoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-imageoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams) | 覆盖物参数。 |
| [addImageOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addimageoverlay)(params: [mapCommon.ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)): Promise<[ImageOverlay](../harmonyos-references/map-map-imageoverlay.md)> | 为地图增加覆盖物。 |
| [ImageOverlay](../harmonyos-references/map-map-imageoverlay.md) | 覆盖物，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { map, mapCommon, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 增加覆盖物。

   ```typescript
   @Entry
   @Component
   struct ImageOverlayDemo {
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapEventManager?: map.MapEventManager;

     aboutToAppear(): void {
       this.mapOptions = {
         position: {
           target: {
             latitude: 32.2,
             longitude: 118.2
           },
           zoom: 10
         }
       }

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           this.mapEventManager = this.mapController.getEventManager();
           let imageOverlayParams: mapCommon.ImageOverlayParams = {
             // 覆盖物范围
             bounds: {
               southwest: {
                 latitude: 32,
                 longitude: 118
               },
               northeast: {
                 latitude: 32.4,
                 longitude: 118.4
               }
             },
             // 覆盖物图片，图标需存放在resources/rawfile目录下
             image: 'icon/icon.png',
             transparency: 0.3,
             zIndex: 101,
             anchorU: 0.5,
             anchorV: 0.5,
             clickable: true,
             visible: true,
             bearing: 0
           };
           // 添加覆盖物
           try {
             let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
           } catch (e) {
             console.error(`Failed to create the imageOverlay, code is：${e.code}, message is ${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       }
     }
     build() {
       Stack() {
         Column() {
           MapComponent({
             mapOptions: this.mapOptions,
             mapCallback: this.callback,
           })
             .width('100%')
             .height('100%');
         }.width('100%')
       }.height('100%')
     }
   }
   ```
3. 设置覆盖物点击监听事件。

   ```typescript
   let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay: map.ImageOverlay) => {
     console.info("imageOverlay callback");
   }
   // 打开覆盖物的点击监听
   this.mapEventManager.on("imageOverlayClick", imageOverlayCallback);
   // 关闭覆盖物的点击监听
   this.mapEventManager.off("imageOverlayClick", imageOverlayCallback);
   ```
