---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-3dbuilding
title: 3D建筑
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 3D建筑
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:78ad2f54b3feb9635ec8fd6e52611439ba2fbdf553cb3d419f27b6780b47372b
---

## 场景介绍

本章节将向您介绍如何在地图上绘制3D建筑。

3D建筑主要用于展示城市建筑外观，帮助用户直观了解城市面貌，同时还可应用于楼盘、小区等三维模型的呈现，辅助用户全面了解周边环境。此外，在导航定位、旅游导览以及商业选址分析等场景中也有广泛应用，能够为用户提供更加真实、直观的地图体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/2-lghjOvSZ-R1tN1wPMXyw/zh-cn_image_0000002706675128.gif "点击放大")

## 接口说明

添加3D建筑功能主要由[BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams)、[addBuildingOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addbuildingoverlay)和[BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-buildingoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams) | 3D建筑参数。 |
| [addBuildingOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addbuildingoverlay)(params: [mapCommon.BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams)): Promise<[BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md)> | 在地图上添加3D建筑。 |
| [BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md) | 3D建筑，支持更新和查询相关属性。 |

## 开发步骤

### 添加3D建筑

1. 导入相关模块。

   ```typescript
   import { mapCommon, map, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加3D建筑。

   ```typescript
   @Entry
   @Component
   struct BuildingOverlayDemo {
     private TAG = "OHMapSDK_BuildingOverlayDemo";
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private buildingOverlay?: map.BuildingOverlay;

     aboutToAppear(): void {
       // 初始化地图参数
       this.mapOptions = {
         position: {
           target: {
             latitude: 31.984794,
             longitude: 118.765865
           },
           zoom: 18
         },
         scaleControlsEnabled: true
       }

       this.callback = async (err, mapController) => {
         console.info(this.TAG, "addBuildingOverlay");
         if (!err) {
           this.mapController = mapController;
           // 3D建筑底面坐标集合
           let points: Array<mapCommon.LatLng> = [
             {
               latitude: 31.984794,
               longitude: 118.765865
             },
             {
               latitude: 31.98468,
               longitude: 118.766076
             },
             {
               latitude: 31.98472,
               longitude: 118.766116
             },
             {
               latitude: 31.98463,
               longitude: 118.766292
             },
             {
               latitude: 31.984586,
               longitude: 118.766251
             },
             {
               latitude: 31.984536,
               longitude: 118.766344
             },
             {
               latitude: 31.984633,
               longitude: 118.766446
             },
             {
               latitude: 31.9848,
               longitude: 118.766285
             },
             {
               latitude: 31.984925,
               longitude: 118.766312
             },
             {
               latitude: 31.985282,
               longitude: 118.766661
             },
             {
               latitude: 31.985438,
               longitude: 118.766419
             },
             {
               latitude: 31.985801,
               longitude: 118.766755
             },
             {
               latitude: 31.985856,
               longitude: 118.766504
             },
             {
               latitude: 31.985785,
               longitude: 118.766434
             },
             {
               latitude: 31.985821,
               longitude: 118.766278
             },
             {
               latitude: 31.985897,
               longitude: 118.766311
             },
             {
               latitude: 31.985944,
               longitude: 118.766095
             },
             {
               latitude: 31.985909,
               longitude: 118.766069
             },
             {
               latitude: 31.985794,
               longitude: 118.765989
             },
             {
               latitude: 31.9857,
               longitude: 118.766029
             },
             {
               latitude: 31.985658,
               longitude: 118.766164
             },
             {
               latitude: 31.985647,
               longitude: 118.766271
             },
             {
               latitude: 31.985574,
               longitude: 118.766297
             },
             {
               latitude: 31.985458,
               longitude: 118.766285
             },
             {
               latitude: 31.985271,
               longitude: 118.766002
             },
             {
               latitude: 31.985219,
               longitude: 118.766002
             },
             {
               latitude: 31.985135,
               longitude: 118.766029
             },
             {
               latitude: 31.985093,
               longitude: 118.766083
             },
             {
               latitude: 31.985019,
               longitude: 118.766109
             },
             {
               latitude: 31.984978,
               longitude: 118.766083
             },
             {
               latitude: 31.984794,
               longitude: 118.765865
             }
           ];
           points.reverse();
           // 3D建筑参数
           let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
             {
               // 3D建筑的范围参数（点为顺时针绘制）
               points: points,
               // 3D建筑的高度
               totalHeight: 51,
               // 3D建筑的选中楼层高度
               floorBottomHeight: 33,
               // 3D建筑的顶部颜色
               topFaceColor: 0xffa4b8f7,
               // 3D建筑的侧面颜色
               sideFaceColor: 0x44a4b8f7,
               // 3D建筑的选中楼层颜色
               floorColor: 0xff000000,
               // 3D建筑的展示层级
               showLevel: 14,
               // 3D建筑选中楼层从底部升起的动画时长
               animationDuration: 5000,
               // 3D建筑侧面的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
               sideTexture: { image: $r("app.media.side_tex"), height: 3, width: 3 },
               // 3D建筑选中楼层的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
               floorTexture: { image: $r("app.media.floor_tex"), height: 3, width: 3 }
             };
           let cameraUpdate = map.newCameraPosition({
             target: {
               latitude: 31.984794,
               longitude: 118.765865
             },
             zoom: 18,
             tilt: 70
           });
           // 将地图镜头移动到3D建筑区域
           this.mapController?.moveCamera(cameraUpdate);
           // 新建3D建筑
           try {
             this.buildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
           } catch (e) {
             console.error(`Failed to create the buildingOverlay, code is：${e.code}, message is ${e.message}`);
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
           }).width('100%').height('100%');
         }.width('100%')
       }.height('100%')
     }
   }
   ```
