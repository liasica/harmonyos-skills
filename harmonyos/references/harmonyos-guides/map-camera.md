---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-camera
title: 更改地图位置
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 地图交互 > 更改地图位置
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:83e290c9e3fce51a2d2d3f63f8861619724e6a9f9fd41ad3f34caa92b6c354b8
---

## 场景介绍

华为地图的移动是通过模拟相机移动的方式实现的，该相机可称为地图相机，您可以通过改变地图相机位置，来控制地图的可见区域，效果如图所示。

本章节将向您介绍地图相机的各个属性与含义，并移动相机。

**图1** 相机移动前

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/tvjP9zRTQcKQn34jhW180Q/zh-cn_image_0000002712405246.jpg "点击放大")

**图2** 相机移动后

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/CzBqFuUxSrqgS2c0XpeC7g/zh-cn_image_0000002742124195.jpg "点击放大")

## 接口说明

您可以通过[map](../harmonyos-references/map-module-desc.md)命名空间下的[moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)方法、[animateCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)方法和[animateCameraStatus](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamerastatus)实现移动地图相机。方法入参[CameraUpdate](../harmonyos-references/map-map-cameraupdate.md)可通过以下方法创建。

| 接口名 | 描述 |
| --- | --- |
| [zoomTo](../harmonyos-references/map-map-functions.md#zoomto)(zoom: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图缩放级别。 |
| [zoomOut](../harmonyos-references/map-map-functions.md#zoomout)(): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 缩小地图缩放级别，在当前地图显示的级别基础上减1。 |
| [zoomIn](../harmonyos-references/map-map-functions.md#zoomin)(): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 放大地图缩放级别，在当前地图显示的级别基础上加1。 |
| [zoomBy](../harmonyos-references/map-map-functions.md#zoomby)(amount: number, focus?: [mapCommon.MapPoint](../harmonyos-references/map-common.md#mappoint)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。 |
| [scrollBy](../harmonyos-references/map-map-functions.md#scrollby)(x: number, y: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 按像素移动地图中心点。 |
| [newLatLngBounds](../harmonyos-references/map-map-functions.md#newlatlngbounds)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), padding?: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图经纬度范围、设置地图区域和边界之间的距离。 |
| [newLatLngBounds](../harmonyos-references/map-map-functions.md#newlatlngbounds-1)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), width: number, height: number, padding: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图经纬度范围、设置经纬度矩形范围的高和宽、设置地图区域和边界之间的距离。 |
| [newLatLngBounds](../harmonyos-references/map-map-functions.md#newlatlngbounds-2)(bounds: [mapCommon.LatLngBounds](../harmonyos-references/map-common.md#latlngbounds), padding: [mapCommon.Padding](../harmonyos-references/map-common.md#padding)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 支持设置地图经纬度范围和4个方向与边界之间的距离。 |
| [newLatLng](../harmonyos-references/map-map-functions.md#newlatlng)(latLng: [mapCommon.LatLng](../harmonyos-references/map-common.md#latlng), zoom?: number): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 设置地图的中心点和缩放层级。 |
| [newCameraPosition](../harmonyos-references/map-map-functions.md#newcameraposition)(cameraPosition: [mapCommon.CameraPosition](../harmonyos-references/map-common.md#cameraposition)): [CameraUpdate](../harmonyos-references/map-map-cameraupdate.md) | 更新地图状态。 |

## 开发步骤

### 相机移动

1. 初始化地图并获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)地图操作类对象。[显示地图](map-presenting.md)章节中有详细讲解。
2. 导入模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   ```
3. 通过调用[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)的[moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)方法、[animateCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamera)方法和[animateCameraStatus](../harmonyos-references/map-map-mapcomponentcontroller.md#animatecamerastatus)方法，可实现移动地图相机。

   您可以选择以动画方式或非动画方式移动相机。

   * 动画方式移动相机时，您可以设置动画持续的时间。
   * 非动画方式移动相机是瞬时完成的。

   ```typescript
   // 创建CameraUpdate对象
   let cameraPosition: mapCommon.CameraPosition = {
     target: {
       latitude: 32.0,
       longitude: 118.0
     },
     zoom: 10,
     tilt: 0,
     bearing: 0
   };
   let cameraUpdate = map.newCameraPosition(cameraPosition);
   // 以非动画方式移动地图相机
   this.mapController.moveCamera(cameraUpdate);

   // 以动画方式移动地图相机
   this.mapController.animateCamera(cameraUpdate, 1000);

   // 以动画方式移动地图相机，并返回动画结果
   let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);
   ```

   **图3** 相机移动前

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/JzzZVm9UQVyEQRUSGU20pg/zh-cn_image_0000002712245288.jpg "点击放大")

   **图4** 相机移动后

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/1NKiqEbLTzuYD1jarqr4UA/zh-cn_image_0000002742004237.jpg "点击放大")
4. 您还可以通过以下方式创建[CameraUpdate](../harmonyos-references/map-map-cameraupdate.md)对象。

   ```typescript
   // 方式1：相机放大级数加1，保持其他属性不变
   let cameraUpdate = map.zoomIn();

   // 方式2：相机放大级数减1，保持其他属性不变
   let cameraUpdate1 = map.zoomOut();

   // 方式3：指定相机缩放级数zoom值，其他属性不变
   let zoom1 = 8.0;
   let cameraUpdate2 = map.zoomTo(zoom1);

   // 方式4：
   // a、指定相机缩放级别增量amount，您调用此方法可以在原来相机的缩放级别之上，进行适当的缩放
   // b、指定缩放级别增量和一个中心点，您调用此API可以移动相机至中心点位置，并进行缩放
   // 以屏幕左顶点为（0, 0）点，positionX正值代表可视区域向右移动，负值代表可视区域向左移动
   // positionY正值代表可视区域向下移动，负值代表可视区域向上移动
   let point: mapCommon.MapPoint = {
     positionX: 31,
     positionY: 118
   };
   let amount = 2.0;
   let cameraUpdate3 = map.zoomBy(amount, point);

   // 方式5：设置相机的经纬度和地图层级
   // a、仅指定相机的经纬度，实现中心点的移动
   // b、指定相机的经纬度和地图层级，您调用此API可以移动相机至中心点位置，并进行缩放
   let latLng: mapCommon.LatLng = {
     latitude: 31.5,
     longitude: 118.9
   };
   let zoom2 = 10;
   let cameraUpdate4 = map.newLatLng(latLng, zoom2);

   // 方式6：设置相机的可见区域
   let latLngBounds: mapCommon.LatLngBounds = {
     northeast: {
       latitude: 32.5,
       longitude: 119.9
     },
     southwest: {
       latitude: 31.5,
       longitude: 118.9
     }
   };
   // 设置地图显示经纬度范围，设置地图区域和边界之间的距离为5像素
   let cameraUpdate5 = map.newLatLngBounds(latLngBounds, 5);
   // 方式7：设置相机的可见区域
   // 设置地图显示经纬度范围，设置经纬度矩形范围的宽为1000像素，设置经纬度矩形范围的高为1000像素，设置地图区域和边界之间的距离为100像素
   let cameraUpdate6 = map.newLatLngBounds(latLngBounds, 1000, 1000, 100);
   // 方式8：设置地图显示经纬度范围，设置地图区域和4个方向的边界之间的距离分别为5、6、7、8像素
   let paddings: mapCommon.Padding = {
     left:5,
     top: 6,
     right: 7,
     bottom: 8
   };
   let cameraUpdate7 = map.newLatLngBounds(latLngBounds, paddings);

   // 方式9：滚动相机，将相机按照指定的像素点移动
   let x = 100.0;
   let y = 100.0;
   let cameraUpdate8 = map.scrollBy(x, y);
   ```

### 设置相机最大/最小偏好缩放级别

```typescript
// 设置最小偏好缩放级别，范围为[2, 20]
this.mapController.setMinZoom(6);
// 设置最大偏好缩放级别，范围为[2, 20]
this.mapController.setMaxZoom(14);
```

### 设置地图相机的边界

Map Kit支持设置地图相机的边界。通过[setLatLngBounds](../harmonyos-references/map-map-mapcomponentcontroller.md#setlatlngbounds)接口指定一个[LatLngBounds](../harmonyos-references/map-common.md#latlngbounds)来约束相机目标，使用户移动地图时，相机目标不会移出此边界。当设置参数为空时，地图相机的边界清除。

```typescript
let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30,
    longitude: 113
  }
};
this.mapController.setLatLngBounds(bounds);
```
