---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-mass-point
title: 海量点图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 海量点图层
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:1094a1e5ebb3d7c5d788afcc285f24c4a1273fa435d0ef4b487a54f2ce9ee6a2
---

## 场景介绍

新增海量点图层，用于批量展示坐标点数据。海量点图层支持处理的点数量级跨度较大，从几十个点至十万个点都可以应用海量点图层进行处理，本章节将向您介绍如何在地图上绘制海量点图层。

6.0.0(20)开始，支持海量点图层功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/VBWw0sHZSl-DLX_CcBzkMA/zh-cn_image_0000002742004261.jpg "点击放大")

## 接口说明

海量点图层功能主要由[MassPointOverlayParams](../harmonyos-references/map-common.md#masspointoverlayparams)、[addMassPointOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addmasspointoverlay)、[MassPointOverlay](../harmonyos-references/map-map-masspointoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-masspointoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [MassPointOverlayParams](../harmonyos-references/map-common.md#masspointoverlayparams) | 海量点参数。 |
| [addMassPointOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addmasspointoverlay)(params: mapCommon.[MassPointOverlayParams](../harmonyos-references/map-common.md#masspointoverlayparams)): Promise<[MassPointOverlay](../harmonyos-references/map-map-masspointoverlay.md)> | 新增海量点。 |
| [MassPointOverlay](../harmonyos-references/map-map-masspointoverlay.md) | 海量点管理对象。 |

## 开发步骤

### 添加海量点图层

1. 导入相关模块。

   ```typescript
   import { mapCommon, map, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制海量点图层。

   ```typescript
   @Entry
   @Component
   struct MapMassPointDemo {
     // ...
     private TAG = 'OHMapSDK_MassPointOverlayDemo';
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private massPointOverlay?: map.MassPointOverlay;
     @State currentTimestamp: number = 0;
     @State mapHeight: string = '65%'
     @State mapWidth: string = '100%'

     aboutToAppear(): void {
       this.mapOptions = {
         position: {
           target: {
             latitude: 32.11111,
             longitude: 118.11111
           },
           zoom: 9
         },
         scaleControlsEnabled: true
       }
       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           let items: mapCommon.MassPointItem[] = [];
           for (let i = 0; i < 1000; i++) {
             // 将海量点存入items
             items.push({
               itemId: 'test' + i,
               position: {
                 longitude: 118.11111 + Math.random() * 1 - 0.5,
                 latitude: 32.11111 + Math.random() * 1 - 0.5
               },
               snippet: 'test' + i,
               title: 'test' + i
             })
           }
           let params: mapCommon.MassPointOverlayParams = {
             id: 'test',
             items: items,
             // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
             icon: 'icon/maps_blue_dot.png'
           }
           try {
             this.massPointOverlay = await this.mapController?.addMassPointOverlay(params);
           } catch (e) {
             console.error(this.TAG, `code:${e.code}, message:${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       }
     }

     build() {
       // ...
         Stack() {
           Column() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
               .width(this.mapWidth)
               .height(this.mapHeight);
           }.width('100%')
         }.height('100%')

         // ...
     }
   }
   ```

### 海量点点击事件

```typescript
// 初始化地图组件的监听事件管理接口
let mapEventManager = this.mapController?.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(`overlayId:${overlay.getId()},item :${JSON.stringify(item)}`);
}
// 启动海量点点击事件监听
mapEventManager?.on('massPointOverlayClick', massCallback);
// 停止海量点点击事件监听,传入指定callback
mapEventManager?.off('massPointOverlayClick', massCallback);
// 停止所有海量点点击事件监听，无需传入callback
mapEventManager?.off('massPointOverlayClick');
```
