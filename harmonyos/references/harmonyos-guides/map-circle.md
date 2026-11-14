---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-circle
title: 圆形
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 圆形
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:24+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:724c1be5920182dad0b08ffdf641b25fed2079fa352596bfe6ddab42792beb7a
---

## 场景介绍

本章节将向您介绍如何在地图上绘制圆形。

圆形通常用于表示特定区域的服务覆盖范围、地理围栏或兴趣点的影响区域。通过设置中心点和半径，可以直观地展示某一地点周边一定距离内的范围。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/MmvixYgEQbq3BkYHSpdQ9g/zh-cn_image_0000002817507607.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=7323D65D606C243957909723C75B40E73565A85F791E59D75463291BD660A609 "点击放大")

## 接口说明

添加圆形功能主要由[MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions)、[addCircle](../harmonyos-references/map-map-mapcomponentcontroller.md#addcircle)和[MapCircle](../harmonyos-references/map-map-mapcircle.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcircle.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions) | 圆形参数。 |
| [addCircle](../harmonyos-references/map-map-mapcomponentcontroller.md#addcircle)(options: [mapCommon.MapCircleOptions](../harmonyos-references/map-common.md#mapcircleoptions)): Promise<[MapCircle](../harmonyos-references/map-map-mapcircle.md)> | 在地图上添加一个圆，指定圆心经纬度和圆的半径，用于表示某个位置的周边范围。 |
| [MapCircle](../harmonyos-references/map-map-mapcircle.md) | 圆形，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加圆，在callback方法中创建初始化参数并新建Circle。

   ```typescript
   @Entry
   @Component
   struct MapCircleDemo {
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapCircle?: map.MapCircle;

     aboutToAppear(): void {
       // 地图初始化参数
       this.mapOptions = {
         position: {
           target: {
             latitude: 39.918,
             longitude: 116.397
           },
           zoom: 14
         }
       };

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           // Circle初始化参数
           let mapCircleOptions: mapCommon.MapCircleOptions = {
             center: {
               latitude: 39.918,
               longitude: 116.397
             },
             radius: 500,
             clickable: true,
             fillColor: 0xFFFFC100,
             strokeColor: 0xFFFF0000,
             strokeWidth: 10,
             visible: true,
             zIndex: 15
           }
           // 创建Circle
           try {
             this.mapCircle = await this.mapController.addCircle(mapCircleOptions);
           } catch (e) {
             console.error(`Failed to create the mapCircle, code is：${e.code}, message is ${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       Stack() {
         Column() {
           MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
         }.width('100%')
       }.height('100%')
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/YNxDTEinQSaIrIJUJ-0hvQ/zh-cn_image_0000002788308176.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004640Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6586C9B3F8A77559B16EC065DEBE07E154E761F15EEB40DC21D64292D3B86AD "点击放大")
