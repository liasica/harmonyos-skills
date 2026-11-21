---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polygon
title: 多边形
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 多边形
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:31+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:767f3abfd294a1802212db98291bdd0cf7dda1a9a2151188cbe2015ecf27ef74
---

## 场景介绍

本章节将向您介绍如何在地图上绘制多边形。

多边形主要用于标识小区、学校、商圈等封闭区域范围，同时可呈现省、市、区县等行政区域边界。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/9-vL0PfgSoWoQDFF6gjZVQ/zh-cn_image_0000002821838063.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=331DA60095ED49D95CFD738DF8321444B38B5A2513A9179DDD642D655C534F0C "点击放大")

## 接口说明

添加多边形功能主要由[MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions)、[addPolygon](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolygon)和[MapPolygon](../harmonyos-references/map-map-mappolygon.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mappolygon.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions) | 多边形参数。 |
| [addPolygon](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolygon)(options: [mapCommon.MapPolygonOptions](../harmonyos-references/map-common.md#mappolygonoptions)): Promise<[MapPolygon](../harmonyos-references/map-map-mappolygon.md)> | 在地图上添加一个多边形。 |
| [MapPolygon](../harmonyos-references/map-map-mappolygon.md) | 多边形，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加多边形，在callback方法中创建初始化参数并新建polygon。

   ```typescript
   @Entry
   @Component
   struct MapPolygonDemo {
     // ...
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapPolygon?: map.MapPolygon;

     aboutToAppear(): void {
       // 地图初始化参数
       this.mapOptions = {
         position: {
           target: {
             latitude: 31.98,
             longitude: 118.78
           },
           zoom: 14
         }
       };
       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           // 多边形初始化参数
           let polygonOptions: mapCommon.MapPolygonOptions = {
             points: [
               { longitude: 118.78, latitude: 31.975 },
               { longitude: 118.78, latitude: 31.985 },
               { longitude: 118.79, latitude: 31.985 },
               { longitude: 118.79, latitude: 31.975 }
             ],
             clickable: true,
             fillColor: 0xff00DE00,
             geodesic: false,
             strokeColor: 0xff000000,
             jointType: mapCommon.JointType.DEFAULT,
             strokeWidth: 10,
             visible: true,
             zIndex: 10
           }
           // 创建多边形
           try {
             this.mapPolygon = await this.mapController.addPolygon(polygonOptions);
           } catch (e) {
             console.error(`Failed to create the mapPolygon, code is：${e.code}, message is ${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       // ...
         Stack() {
           Column() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
           }.width('100%')
         }.height('100%')

         // ...
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/lbz_KMYASEq-A8ruPd-u2A/zh-cn_image_0000002821758065.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=938191A47727EC379F233631D466D29442DD807385E87E63CA7346C27F0AD3E6 "点击放大")
