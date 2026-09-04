---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-aggregate
title: 点聚合
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 点聚合
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c56d00d849f8b0e1334b27a8ab4025bab8dd2b251373afb2fcbed7e50d832da2
---

## 场景介绍

本章节将详细介绍如何基于地图数据实现点聚合功能。

您可以通过比例尺缩放自适应聚合效果，聚合图标可点击。聚合支持功能：

* 支持按距离聚合[ClusterItem](../harmonyos-references/map-common.md#clusteritem)。
* 支持绘制聚合覆盖物的默认图标。
* 支持绘制聚合覆盖物的[自定义图标](../harmonyos-references/map-common.md#getcustomicon)。
* 支持监听聚合覆盖物的点击事件。
* 支持添加单个[ClusterItem](../harmonyos-references/map-common.md#clusteritem)到聚合覆盖物中。
* 支持删除聚合覆盖物。
* 支持移动地图时重绘聚合覆盖物。

5.0.3(15)开始，支持聚合标记点击事件监听功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/YdjuoCwHRsS2tAyF7R0dJA/zh-cn_image_0000002712245308.jpg "点击放大")

## 接口说明

聚合功能主要由[ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams)、[addClusterOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addclusteroverlay)、[ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-clusteroverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams) | 点聚合参数。 |
| [addClusterOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addclusteroverlay)(params: [mapCommon.ClusterOverlayParams](../harmonyos-references/map-common.md#clusteroverlayparams)): Promise<[ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md)> | 聚合接口，支持节点聚合能力。 |
| [ClusterOverlay](../harmonyos-references/map-map-clusteroverlay.md) | 点聚合，支持更新和查询相关属性。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { map, mapCommon, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 新增聚合图层。

   ```typescript
   @Entry
   @Component
   struct ClusterOverlayDemo {
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;

     aboutToAppear(): void {
       this.mapOptions = {
         position: {
           target: {
             latitude: 31.98,
             longitude: 118.7
           },
           zoom: 7
         }
       }

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           // 生成待聚合点
           let clusterItem1: mapCommon.ClusterItem = {
             position: {
               latitude: 31.98,
               longitude: 118.7
             }
           };
           let clusterItem2: mapCommon.ClusterItem = {
             position: {
               latitude: 32.99,
               longitude: 118.9
             }
           };
           let clusterItem3: mapCommon.ClusterItem = {
             position: {
               latitude: 31.5,
               longitude: 118.7
             }
           };
           let clusterItem4: mapCommon.ClusterItem = {
             position: {
               latitude: 30,
               longitude: 118.7
             }
           };
           let clusterItem5: mapCommon.ClusterItem = {
             position: {
               latitude: 29.98,
               longitude: 117.7
             }
           };
           let clusterItem6: mapCommon.ClusterItem = {
             position: {
               latitude: 31.98,
               longitude: 120.7
             }
           };
           let clusterItem7: mapCommon.ClusterItem = {
             position: {
               latitude: 25.98,
               longitude: 119.7
             }
           };
           let clusterItem8: mapCommon.ClusterItem = {
             position: {
               latitude: 30.98,
               longitude: 110.7
             }
           };
           let clusterItem9: mapCommon.ClusterItem = {
             position: {
               latitude: 30.98,
               longitude: 115.7
             }
           };
           let clusterItem10: mapCommon.ClusterItem = {
             position: {
               latitude: 28.98,
               longitude: 122.7
             }
           };
           let array: Array<mapCommon.ClusterItem> = [
             clusterItem1,
             clusterItem2,
             clusterItem3,
             clusterItem4,
             clusterItem5,
             clusterItem6,
             clusterItem7,
             clusterItem8,
             clusterItem9,
             clusterItem10
           ]
           // 为了演示大量点聚合的效果，添加了100个clusterItem1和10个clusterItem2
           for(let index = 0; index < 100; index++){
             array.push(clusterItem1)
           }
           for(let index = 0; index < 10; index++){
             array.push(clusterItem2)
           }
           // 生成聚合图层的入参 聚合distance设置为100vp
           let clusterOverlayParams: mapCommon.ClusterOverlayParams = {
             distance: 100,
             clusterItems: array
           };
           try {
             // 调用addClusterOverlay生成聚合图层
             let clusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
           } catch (e) {
             console.error(`code:${e.code}, message:${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       }
     }

     build() {
       Stack() {
         Column() {
           MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
             .width('100%')
             .height('100%');
         }.width('100%')
       }.height('100%')
     }
   }
   ```
3. 聚合标记点击事件监听。

   ```typescript
   let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
     console.info("markerClusterClick", `callback1 markerClusterInfo`);
   };
   // 添加监听
   clusterOverlay.on("markerClusterClick", callback1);
   // 取消监听
   clusterOverlay.off("markerClusterClick", callback1);
   ```
